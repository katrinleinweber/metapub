from __future__ import absolute_import, unicode_literals

HOSTNAME_TO_JOURNAL_MAP = {
		'molbiolcell.org': 'Mol Biol Cell',
		'ndt.oxfordjournals.org': 'Nephrol Dial Transplant',
		'biomedgerontology.oxfordjournals.org': 'J Gerontol A Biol Sci Med Sci',
		'jrr.oxfordjournals.org': 'Radiat Res',
		'circgenetics.ahajournals.org': 'Circ Cardiovasc Genet',
		'circep.ahajournals.org': 'Circ Arrhythm Electrophysiol',
		'cancerdiscovery.aacrjournals.org': 'Cancer Discov',
		'jnci.oxfordjournals.org': 'J Natl Cancer Inst',
		'bja.oxfordjournals.org': 'Br J Anaesth',
		'eje-online.org': 'Eur J Endocrinol',
		'ar.iiarjournals.org': 'Anticancer Res',
		'jvi.asm.org': 'J Virol',
		'pediatrics.aappublications.org': 'Pediatrics',
		'cfp.ca': 'Can Fam Physician',
		'atvb.ahajournals.org': 'Arterioscler Thromb Vasc Biol',
		'genomebiology.com': 'Genome Biol',
		'erc.endocrinology-journals.org': 'Endocr Relat Cancer',
		'pcp.oxfordjournals.org': 'Plant Cell Physiol',
		'jimmunol.org': 'J Immunol',
		'qjmed.oxfordjournals.org': 'QJM',
		'ajcp.ascpjournals.org': 'Am J Clin Pathol',
		'jid.oxfordjournals.org': 'J Infect Dis',
		'ee.oxfordjournals.org': 'Environ Entomol',
		'jcs.biologists.org': 'J Cell Sci',
		'ang.sagepub.com': 'Angiology',
		'jcn.sagepub.com': 'J Child Neurol',
		'pnas.org': 'Proc Natl Acad Sci USA',
		'sciencemag.org': 'Science',
		'iovs.org': 'Invest Ophthalmol Vis Sci',
		'jnnp.bmj.com': 'J Neurol Neurosurg Psychiatry',
		'jpet.aspetjournals.org': 'J Pharmacol Exp Ther',
		'iovs.org': 'IOVS',
		'jra.sagepub.com': 'J Renin Angiotensin Aldosterone Syst',
		'breast-cancer-research.com': 'Breast Cancer Res',
		'eurheartj.oxfordjournals.org': 'Eur Heart J',
		'genome.cshlp.org': 'Genome Res',
		'jb.asm.org': 'J Bacteriol',
		'plantcell.org': 'Plant Cell',
		'jcb.rupress.org': 'J Cell Biol',
		'mutage.oxfordjournals.org': 'Mutagenesis',
		'erj.ersjournals.com': 'Eur Respir J',
		'ojrd.com': 'Orphanet J Rare Dis',
		'femsle.oxfordjournals.org': 'FEMS Microbiol Lett',
		'genesdev.cshlp.org': 'Genes Dev',
		'jneurosci.org': 'J Neurosci',
		'jhl.sagepub.com': 'J Hum Lact',
		'ajh.oxfordjournals.org': 'Am J Hypertens',
		'jco.ascopubs.org': 'J Clin Oncol',
		'mct.aacrjournals.org': 'Mol Cancer Ther',
		'hyper.ahajournals.org': 'Hypertension',
		'cat.sagepub.com': 'Clin Appl Thromb Hemost',
		'jme.endocrinology-journals.org': 'J Mol Endocrinol',
		'rheumatology.oxfordjournals.org': 'Rheumatology (Oxford)',
		'jem.rupress.org': 'J Exp Med',
		'jmg.bmj.com': 'J Med Genet',
		'molpharm.aspetjournals.org': 'Mol Pharmacol',
		'jbc.org': 'J Biol Chem',
		'care.diabetesjournals.org': 'Diabetes Care',
		'dmd.aspetjournals.org': 'Drug Metab Dispos',
		'aac.asm.org': 'Antimicrob Agents Chemother',
		'peds.oxfordjournals.org': 'Protein Eng Des Sel',
		'jasn.asnjournals.org': 'J Am Soc Nephrol',
		'clincancerres.aacrjournals.org': 'Clin Cancer Res',
		'thorax.bmj.com': 'Thorax',
		'diabetes.diabetesjournals.org': 'Diabetes',
		'circ.ahajournals.org': 'Circulation',
		'carcin.oxfordjournals.org': 'Carcinogenesis',
		'jlr.org': 'J Lipid Res',
		'jrheum.org': 'J Rheumatol',
		'gut.bmj.com': 'Gut',
		'mct.aacrjournals.org': 'Mol Canc Therapeut',
		'cpj.sagepub.com': 'Clin Pediatr',
		'humrep.oxfordjournals.org': 'Hum Reprod',
		'circres.ahajournals.org': 'Circ Res',
		'fasebj.org': 'FASEB J',
		'peds.oxfordjournals.org': 'Protein Eng',
		'jbjs.org': 'J Bone Joint Surg Am',
		'neurology.org': 'Neurology',
		'nar.oxfordjournals.org': 'Nucleic Acids Res',
		'cancerres.aacrjournals.org': 'Cancer Res',
		'ajplung.physiology.org': 'Am J Physiol Lung Cell Mol Physiol',
		'jdr.sagepub.com': 'J Dent Res',
		'annonc.oxfordjournals.org': 'Ann Oncol',
		'jn.nutrition.org': 'J Nutr',
		'asm.sagepub.com': 'Assessment',
		'jac.oxfordjournals.org': 'J Antimicrob Chemother',
		'clinchem.org': 'Clin Chem',
		'stroke.ahajournals.org': 'Stroke',
		'jah.sagepub.com': 'J Aging Health',
		'cid.oxfordjournals.org': 'Clin Infect Dis',
		'physiolgenomics.physiology.org': 'Physiol Genomics',
		'mcb.asm.org': 'Mol Cell Biol',
		'molehr.oxfordjournals.org': 'Mol Hum Reprod',
		'lup.sagepub.com': 'Lupus',
		'hmg.oxfordjournals.org': 'Hum Mol Genet',
		'haematologica.org': 'Haematologica',
		'cebp.aacrjournals.org': 'Cancer Epidemiol Biomarkers Prev',
		'acb.sagepub.com': 'Ann Clin Biochem',
		'cardiovascres.oxfordjournals.org': 'Cardiovasc Res',
		'brain.oxfordjournals.org': 'Brain',
		'cpj.sagepub.com': 'Clin Pediatr (Phila)',
		'jcem.endojournals.org': 'J Clin Endocrinol Metab',
		'emboj.embopress.org': 'EMBO J',
		'ajpcell.physiology.org': 'Am J Physiol, Cell Physiol',
		'joe.endocrinology-journals.org': 'J Endocrinol',
		'jmd.amjpathol.org': 'J Mol Diagn',
		'heartrhythmjournal.com': 'Heart Rhythm',
		'ajconline.org': 'Am J Cardiol',
		'cancergeneticsjournal.org': 'Cancer Genet Cytogenet',
		'epires-journal.com': 'Epilepsy Res',
		'amjmed.com': 'Am J Med',
		'nmd-journal.com': 'Neuromuscul Disord',
		'arcmedres.com': 'Arch Med Res',
		'jpeds.com': 'J Pediatr',
		'clineu-journal.com': 'Clin Neurol Neurosurg',
		'ijporlonline.com': 'Int J Pediatr Otorhinolaryngol',
		'mgmjournal.com': 'Mol Genet Metab',
		'ahjonline.com': 'Am Heart J',
		'cancerci.com': 'Cancer Cell Int',
		'internationaljournalofcardiology.com': 'Int J Cardiol',
		'akademiai.com': 'Orv Hetil',
		'placentajournal.org': 'Placenta',
		'prd-journal.com': 'Parkinsonism Relat Disord',
		'pedneur.com': 'Pediatr Neurol',
		'cancerletters.info': 'Cancer Lett',
		'neurobiologyofaging.org': 'Neurobiol Aging',
		'metabolismjournal.com': 'Metabolism',
		'thebonejournal.com': 'Bone',
		'thrombosisresearch.com': 'Thromb Res',
		'brainanddevelopment.com': 'Brain Dev',
		'jpurol.com': 'J Pediatr Urol',
		'metabolismjournal.com': 'Metab Clin Exp',
		'worldneurosurgery.org': 'Surg Neurol',
		'jmmc-online.com': 'J Mol Cell Cardiol',
		'gastrojournal.org': 'Gastroenterology',
		'exphem.org': 'Exp Hematol',
		'medical-hypotheses.com': 'Med Hypotheses',
		'atherosclerosis-journal.com': 'Atherosclerosis',
		'gynecologiconcology-online.net': 'Gynecol Oncol',
		'aaojournal.org': 'Ophthalmology',
		'biologicalpsychiatryjournal.com': 'Biol Psychiatry',
		'ejpn-journal.com': 'Eur J Paediatr Neurol',
		'jdsjournal.com': 'J Dermatol',
		'ajo.com': 'Am J Ophthalmol',
		'fertstert.org': 'Fertil Steril',
		'jns-journal.com': 'J Neurol Sci',
		'diabetesresearchclinicalpractice.com': 'Diabetes Res Clin Pract',
		'clinsci.org': 'Clin Sci',
		'biochemj.org': 'Biochem J',
		'sciencemag.org': 'Science',
		'stm.sciencemag.org': 'Sci Transl Med',
		'advances.sciencemag.org': 'Sci Adv',
		'stke.sciencemag.org': 'Sci Signal',
		'joponline.org': 'J Periodontol',
		'medicinabuenosaires.com': 'Medicina (B Aires)',
}
