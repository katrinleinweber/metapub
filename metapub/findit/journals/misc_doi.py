from __future__ import absolute_import

# simple formats are used for URLs that can be deduced from PubMedArticle XML
#
#       !ACHTUNG!  informa has been known to block IPs for the capital offense of
#                  having "More than 25 sessions created in 5 minutes"
#

doi_templates = {
    'acs': 'http://pubs.acs.org/doi/pdf/{a.doi}',
    'akademii': 'http://www.akademiai.com/content/{a.pii}/fulltext.pdf',
    'ats': 'http://www.atsjournals.org/doi/pdf/{a.doi}',
    'futuremed': 'http://www.futuremedicine.com/doi/pdf/{a.doi}',
    'informa': 'http://informahealthcare.com/doi/pdf/{a.doi}',
    'lancet': 'http://www.thelancet.com/pdfs/journals/{ja}/PII{a.pii}.pdf',
    'liebert': 'http://online.liebertpub.com/doi/pdf/{a.doi}',
    'plos': 'http://www.plosbiology.org/article/fetchObjectAttachment.action?url=info:doi/{a.doi}&representation=PDF',
    'taylor_francis': 'http://www.tandfonline.com/doi/pdf/{a.doi}',
    'wiley': 'http://onlinelibrary.wiley.com/doi/{a.doi}/pdf',
    'jci': 'http://www.jci.org/articles/view/{a.pii}/pdf',
}

simple_formats_doi = {
    'Acta Oncol': doi_templates['informa'],
    'Ann Hum Biol': doi_templates['informa'],
    'Hemoglobin': doi_templates['informa'],
    'J Matern Fetal Neonatal Med': doi_templates['informa'],
    'Ophthalmic Genet': doi_templates['informa'],
    'Platelets': doi_templates['informa'],
    'Ren Fail': doi_templates['informa'],
    'Scand J Rheumatol': doi_templates['informa'],
    'Scand J Urol Nephrol': doi_templates['informa'],
    'Xenobiotica': doi_templates['informa'],

    'Am J Public Health': 'http://ajph.aphapublications.org/doi/pdf/{a.doi}',
    'Am J Respir Cell Mol Biol': doi_templates['ats'],
    'Am J Respir Crit Care Med': doi_templates['ats'],

    'Anal Chem': doi_templates['acs'],
    'ACS Appl Mater': doi_templates['acs'],
    'ACS Nano': doi_templates['acs'],
    'Biochemistry': doi_templates['acs'],
    'Chem Res Toxicol': doi_templates['acs'],
    'Inorg Chem': doi_templates['acs'],
    'J Agric Food Chem': doi_templates['acs'],
    'J Am Chem Soc': doi_templates['acs'],
    'J Med Chem': doi_templates['acs'],
    'J Phys Chem A': doi_templates['acs'],
    'Langmuir': doi_templates['acs'],
    'Nano Lett': doi_templates['acs'],

    #http://www.bioone.org/action/showPublications?type=byAlphabet
    #'TODO': 'http://www.bioone.org/doi/pdf/{a.doi}',

    'AIDS Res Hum Retroviruses': doi_templates['liebert'],
    'Antioxid Redox Signal': doi_templates['liebert'],
    'Child Obes': doi_templates['liebert'],
    'Genet Test': doi_templates['liebert'],
    'Genet Test Mol Biomarkers': doi_templates['liebert'],
    'Thyroid': doi_templates['liebert'],
    'Vector Borne Zoonotic Dis': doi_templates['liebert'],

    'Pharmacogenomics': doi_templates['futuremed'],

    'Autophagy': doi_templates['taylor_francis'],
    'Biosci Biotechnol Biochem': doi_templates['taylor_francis'],
    'Cancer Biol Ther': doi_templates['taylor_francis'],
    'Cell Cycle': doi_templates['taylor_francis'],
    'Environ Technol': doi_templates['taylor_francis'],
    'Health Commun': doi_templates['taylor_francis'],
    'J Biomol Struct Dyn': doi_templates['taylor_francis'],
    'J Pers Assess': doi_templates['taylor_francis'],

    'Endocrinology': 'http://press.endocrine.org/doi/pdf/{a.doi}',
    'Endocr Rev': 'http://press.endocrine.org/doi/pdf/{a.doi}',
    'Mol Endocrinol': 'http://press.endocrine.org/doi/pdf/{a.doi}',
    'J Periodontol': 'http://www.joponline.org/doi/pdf/{a.doi}',

    'PLoS Biol': doi_templates['plos'],
    'PLoS Comput Biol': doi_templates['plos'],
    'PLoS Genet': doi_templates['plos'],
    'PLoS Med': doi_templates['plos'],
    'PLoS ONE': doi_templates['plos'],
    'PLoS Pathog': doi_templates['plos'],
    'N Engl J Med':  'http://www.nejm.org/doi/pdf/{a.doi}',
}
