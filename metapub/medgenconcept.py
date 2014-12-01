from __future__ import absolute_import

"""metapub.medgenconcept -- MedGenConcept class instantiated by supplying ESummary XML string."""

import logging
from lxml import etree

from .base import MetaPubObject
from .exceptions import MetaPubError

logger = logging.getLogger()

class MedGenConcept(MetaPubObject):

    def __init__(self, xmlstr, *args, **kwargs):
        super(MedGenConcept, self).__init__(xmlstr, 'DocumentSummarySet/DocumentSummary', args, kwargs)

        if self._get('error'):
            raise MetaPubError('Supplied XML for MedGenConcept contained explicit error: %s' % self._get('error') )

        # ConceptMeta is an XML document embedded within the XML response. Boo-urns. 
        self.meta = etree.fromstring('<ConceptMeta>'+self.content.find('ConceptMeta').text+'</ConceptMeta>')

    def to_dict(self):
        'returns a dictionary composed of all extractable properties of this concept.'
        return { 'CUI': self.CUI, 'title': self.title, 'definition': self.definition,
                 'semantic_id': self.semantic_id, 'semantic_type': self.semantic_type,
                 'modes_of_inheritance': self.modes_of_inheritance, 
                 'associated_genes': self.associated_genes, 'medgen_uid': self.medgen_uid,
                 'names': self.names, 'OMIM': self.OMIM, 'cytogenic': self.cytogenic,
                 'chromosome': self.chromosome }
                  
    @property
    def CUI(self):
        return self._get('ConceptId')
    
    @property
    def title(self):
        return self._get('Title')
        
    @property
    def definition(self):
        return self._get('Definition')
    
    @property
    def semantic_id(self):
        return self._get('SemanticId')
    
    @property
    def semantic_type(self):
        return self._get('SemanticType')
        
    @property
    def medgen_uid(self):
        return self.content.get('uid')
        
    @property
    def modes_of_inheritance(self):
        '''returns a list of all known ModesOfInheritance, in format:
        [ { 'CUI': 'CNxxxx', 'name': 'some name', 'medgen_uid': 'xxxxxx', 'tui': 'A000 }, ...  ]
        '''
        modes = []
        try:
            for item in self.meta.find('ModesOfInheritance').getchildren():
                modes.append({ 'CUI': item.get('CUI'), 
                               'name': item.find('Name').text,
                               'TUI': item.get('TUI'),
                               'uid': item.get('medgen_uid'),
                               'semantic_type': item.find('SemanticType').text,
                               'definition': item.find('Definition').text })
            return modes
        except AttributeError:
            return None
            
    @property
    def associated_genes(self):
        '''returns a list of AssociatedGenes, in format:
        [ { 'gene_id': 'xxx', 'chromosome': 'X', 'cytogen_loc': 'X9234235', 'hgnc': 'GENE' }, ]
        
        if not available, returns None. 
        '''
        genes = []
        try:
            for gene in self.meta.find('AssociatedGenes').getchildren():
                genes.append({ 'gene_id': gene.get('gene_id'), 
                               'hgnc': gene.text,
                               'chromosome': gene.get('chromosome'),
                               'cytogen_loc': gene.get('cytogen_loc') })
            return genes
        except AttributeError:
            return None


    @property
    def names(self):
        '''returns a list of this concept's equivalent Names in various dictionaries,
        in format:
        
        { 'SDUI': '300555', 'SCUI': 'xxx', 'CODE': '300555', 'SAB': 'OMIM' 'TTY': 'PT' 'type': 'syn', 'name': 'DENT DISEASE 2' }
        
        '''
        names = []

        # not every ID is present in each Name (e.g. SCUI only appears sometimes).        
        possible_keys = ['SDUI', 'SCUI', 'CODE', 'SAB', 'TTY', 'PT', 'type']
        
        for name in self.meta.find('Names').getchildren():
            outd = { 'name': name.text }
            for key in possible_keys:
                try:
                    outd[key] = name.get(key)            
                except AttributeError:
                    pass
            names.append(outd)
        return names
        
    @property
    def OMIM(self):
        '''returns this concept's OMIM id (string), when available, else returns None.'''
        try:
            return self.meta.find('OMIM').find('MIM').text
        except AttributeError:
            return None
        
    @property
    def chromosome(self):
        '''returns this concept's affected chromosome, if applicable/available'''
        try:
            return self.meta.find('Chromosome').text
        except AttributeError:
            return None

    @property
    def cytogenic(self):
        '''returns this concept's cytogenic property, if applicable/available'''
        try:
            return self.meta.find('Cytogenic').text
        except AttributeError:
            return None

    # TODO
    # Definitions
    # <Definitions><Definition source="GeneReviews">Dent disease, an X-linked disorder of proximal renal tubular dysfunction, is characterized by low molecular-weight (LMW) proteinuria, hypercalciuria, nephrocalcinosis, nephrolithiasis, and chronic kidney disease (CKD). Males younger than age ten years may manifest only low molecular-weight (LMW) proteinuria and/or hypercalciuria, which are usually asymptomatic. Thirty to 80% of affected males develop end-stage renal disease (ESRD) between ages 30 and 50 years; in some instances ESRD does not develop until the sixth decade of life or later. Rickets or osteomalacia are occasionally observed, and mild short stature, although underappreciated, may be a common occurrence. Disease severity can vary within the same family. Males with Dent disease 2 (caused by mutation of OCRL) are at increased risk for intellectual disability. Due to random X-chromosome inactivation, some female carriers may manifest hypercalciuria and, rarely, renal calculi and moderate LMW proteinuria. Females rarely if ever develop CKD.</Definition></Definitions>
    
    # TODO
    # ClinicalFeatures / ClinicalFeature
    # <ClinicalFeatures><ClinicalFeature uid="9232" CUI="C0019322" TUI="T190" SDUI="HP:0001537"><Name>Umbilical hernia</Name><SemanticType>Anatomical Abnormality</SemanticType></ClinicalFeature><ClinicalFeature uid="87607" CUI="C0349588" TUI="T033" SDUI="HP:0004322"><Name>Short stature</Name><SemanticType>Finding</SemanticType></ClinicalFeature><ClinicalFeature uid="333360" CUI="C1839606" TUI="T033" SDUI="HP:0003126"><Name>Low-molecular-weight proteinuria</Name><SemanticType>Finding</SemanticType></ClinicalFeature><ClinicalFeature uid="383844" CUI="C1856145" TUI="T033" SDUI="HP:0100543"><Name>Cognitive impairment</Name><SemanticType>Finding</SemanticType></ClinicalFeature><ClinicalFeature uid="349145" CUI="C1859342" TUI="T033" SDUI="HP:0000114"><Name>Proximal tubulopathy</Name><SemanticType>Finding</SemanticType></ClinicalFeature><ClinicalFeature uid="504348" CUI="CN000117" TUI="T033" SDUI="HP:0000121"><Name>Nephrocalcinosis</Name><SemanticType>Finding</SemanticType><Definition>Nephrocalcinosis is the deposition of calcium salts in renal parenchyma.</Definition></ClinicalFeature><ClinicalFeature uid="504774" CUI="CN001157" TUI="T033" SDUI="HP:0001263"><Name>Global developmental delay</Name><SemanticType>Finding</SemanticType><Definition>A delay in the achievement of motor or mental milestones in the domains of development of a child, including motor skills, speech and language, cognitive skills, and social and emotional skills. This term should only be used to describe children younger than five years of age.</Definition></ClinicalFeature><ClinicalFeature uid="505127" CUI="CN001948" TUI="T033" SDUI="HP:0002150"><Name>Hypercalciuria</Name><SemanticType>Finding</SemanticType></ClinicalFeature><ClinicalFeature uid="505493" CUI="CN002923" TUI="T033" SDUI="HP:0003236"><Name>Elevated serum creatine phosphokinase</Name><SemanticType>Finding</SemanticType><Definition>An elevation of the level of the enzyme creatine kinase (also known as creatine phosphokinase, CPK; EC 2.7.3.2) in the blood. CPK levels can be elevated in a number of clinical disorders such as myocardial infarction, rhabdomyolysis, and muscular dystrophy.</Definition></ClinicalFeature><ClinicalFeature uid="425142" CUI="CN003029" TUI="T033" SDUI="HP:0003355"><Name>Aminoaciduria</Name><SemanticType>Finding</SemanticType><Definition>An increased concentration of an amino acid in the urine.</Definition></ClinicalFeature><ClinicalFeature uid="776439" CUI="CN183891" TUI="T033" SDUI="HP:0012622"><Name>Chronic kidney disease</Name><SemanticType>Finding</SemanticType><Definition>Functional anomaly of the kidney persisting for at least three months.</Definition></ClinicalFeature></ClinicalFeatures><PhenotypicAbnormalities><Category CUI="CN000115" name="Abnormality of the genitourinary system"><ClinicalFeature uid="504348" CUI="CN000117" TUI="T033" SDUI="HP:0000121"><SemanticType>Finding</SemanticType><Name>Nephrocalcinosis</Name><Definition>Nephrocalcinosis is the deposition of calcium salts in renal parenchyma.</Definition></ClinicalFeature><ClinicalFeature uid="425142" CUI="CN003029" TUI="T033" SDUI="HP:0003355"><SemanticType>Finding</SemanticType><Name>Aminoaciduria</Name><Definition>An increased concentration of an amino acid in the urine.</Definition></ClinicalFeature><ClinicalFeature uid="776439" CUI="CN183891" TUI="T033" SDUI="HP:0012622"><SemanticType>Finding</SemanticType><Name>Chronic kidney disease</Name><Definition>Functional anomaly of the kidney persisting for at least three months.</Definition></ClinicalFeature></Category><Category CUI="CN000664" name="Abnormality of the nervous system"><ClinicalFeature uid="504774" CUI="CN001157" TUI="T033" SDUI="HP:0001263"><SemanticType>Finding</SemanticType><Name>Global developmental delay</Name><Definition>A delay in the achievement of motor or mental milestones in the domains of development of a child, including motor skills, speech and language, cognitive skills, and social and emotional skills. This term should only be used to describe children younger than five years of age.</Definition></ClinicalFeature></Category><Category CUI="CN001754" name="Abnormality of metabolism/homeostasis"><ClinicalFeature uid="505493" CUI="CN002923" TUI="T033" SDUI="HP:0003236"><SemanticType>Finding</SemanticType><Name>Elevated serum creatine phosphokinase</Name><Definition>An elevation of the level of the enzyme creatine kinase (also known as creatine phosphokinase, CPK; EC 2.7.3.2) in the blood. CPK levels can be elevated in a number of clinical disorders such as myocardial infarction, rhabdomyolysis, and muscular dystrophy.</Definition></ClinicalFeature><ClinicalFeature uid="425142" CUI="CN003029" TUI="T033" SDUI="HP:0003355"><SemanticType>Finding</SemanticType><Name>Aminoaciduria</Name><Definition>An increased concentration of an amino acid in the urine.</Definition></ClinicalFeature>
    
    # TODO
    # PhenotypicAbnormalities 
    # <PhenotypicAbnormalities><Category CUI="CN000115" name="Abnormality of the genitourinary system"><ClinicalFeature uid="504348" CUI="CN000117" TUI="T033" SDUI="HP:0000121"><SemanticType>Finding</SemanticType><Name>Nephrocalcinosis</Name><Definition>Nephrocalcinosis is the deposition of calcium salts in renal parenchyma.</Definition></ClinicalFeature><ClinicalFeature uid="425142" CUI="CN003029" TUI="T033" SDUI="HP:0003355"><SemanticType>Finding</SemanticType><Name>Aminoaciduria</Name><Definition>An increased concentration of an amino acid in the urine.</Definition></ClinicalFeature><ClinicalFeature uid="776439" CUI="CN183891" TUI="T033" SDUI="HP:0012622"><SemanticType>Finding</SemanticType><Name>Chronic kidney disease</Name><Definition>Functional anomaly of the kidney persisting for at least three months.</Definition></ClinicalFeature></Category><Category CUI="CN000664" name="Abnormality of the nervous system"><ClinicalFeature uid="504774" CUI="CN001157" TUI="T033" SDUI="HP:0001263"><SemanticType>Finding</SemanticType><Name>Global developmental delay</Name><Definition>A delay in the achievement of motor or mental milestones in the domains of development of a child, including motor skills, speech and language, cognitive skills, and social and emotional skills. This term should only be used to describe children younger than five years of age.</Definition></ClinicalFeature></Category><Category CUI="CN001754" name="Abnormality of metabolism/homeostasis"><ClinicalFeature uid="505493" CUI="CN002923" TUI="T033" SDUI="HP:0003236"><SemanticType>Finding</SemanticType><Name>Elevated serum creatine phosphokinase</Name><Definition>An elevation of the level of the enzyme creatine kinase (also known as creatine phosphokinase, CPK; EC 2.7.3.2) in the blood. CPK levels can be elevated in a number of clinical disorders such as myocardial infarction, rhabdomyolysis, and muscular dystrophy.</Definition></ClinicalFeature><ClinicalFeature uid="425142" CUI="CN003029" TUI="T033" SDUI="HP:0003355"><SemanticType>Finding</SemanticType><Name>Aminoaciduria</Name><Definition>An increased concentration of an amino acid in the urine.</Definition></ClinicalFeature></Category></PhenotypicAbnormalities>
        
    # TODO
    # <RelatedDisorders></RelatedDisorders>
    
    # TODO
    # <SNOMEDCT></SNOMEDCT>
    
    # known others not planned for inclusion:
    # <PharmacologicResponse></PharmacologicResponse>
    
