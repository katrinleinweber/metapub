# TODO
#
#12035837: Can J Neurol Sci -- no URL because No URL format for Journal Can J Neurol Sci
#       ???

#12036192: Clin. Nephrol. -- no URL because No URL format for Journal Clin Nephrol
#       http://www.dustri.com/uploads/repository/21/1239843263_CN83_suppl_01_090.pdf

#12037434: Eur. Neurol. -- no URL because No URL format for Journal Eur Neurol
#12055472: Retina (Philadelphia, Pa.) -- no URL because No URL format for Journal Retina (Philadelphia, Pa)
#12063046: Jpn. J. Ophthalmol. -- no URL because No URL format for Journal Jpn J Ophthalmol
#12063482: J. Am. Acad. Dermatol. -- no URL because No URL format for Journal J Am Acad Dermatol
#12056405: Genes Cells -- no URL because No URL format for Journal Genes Cells
#12065946: Fetal. Diagn. Ther. -- no URL because No URL format for Journal Fetal Diagn Ther
#12066726: Br J Anaesth -- no URL because No URL format for Journal Br J Anaesth
#12071635: J. Neuropathol. Exp. Neurol. -- no URL because No URL format for Journal J Neuropathol Exp Neurol
#12071824: Arch Dermatol -- no URL because No URL format for Journal Arch Dermatol
#12070551: Saudi Med J -- no URL because No URL format for Journal Saudi Med J
#12074273: Circ. J. -- no URL because No URL format for Journal Circ J
#12076704: Oral Oncol. -- no URL because No URL format for Journal Oral Oncol
#12080609: Rinsho Shinkeigaku -- no URL because No URL format for Journal Rinsho Shinkeigaku
#12162770: Arch. Otolaryngol. Head Neck Surg. -- no URL because No URL format for Journal Arch Otolaryngol Head Neck Surg
#12170759: Cancer Biol. Ther. -- no URL because No URL format for Journal Cancer Biol Ther
#12173465: Mol. Biol. (Mosk.) -- no URL because No URL format for Journal Mol Biol (Mosk)
#12173720: Mayo Clin. Proc. -- no URL because No URL format for Journal Mayo Clin Proc
#12202459: Endocr. Rev. -- no URL because No URL format for Journal Endocr Rev
#12087194: Genes Genet. Syst. -- no URL because No URL format for Journal Genes Genet Syst
#12049533: Arch Surg -- no URL because No URL format for Journal Arch Surg
#10458450: J. Urol. -- no URL because No URL format for Journal J Urol
#10458483: Tohoku J. Exp. Med. -- no URL because No URL format for Journal Tohoku J Exp Med
#10458491: Tohoku J. Exp. Med. -- no URL because No URL format for Journal Tohoku J Exp Med
#10470409: Andrologia -- no URL because No URL format for Journal Andrologia
#10474162: Dev. Dyn. -- no URL because No URL format for Journal Dev Dyn
#10520237: Ophthalmic Genet. -- no URL because No URL format for Journal Ophthalmic Genet
#10521250: Ophthalmic Genet. -- no URL because No URL format for Journal Ophthalmic Genet
#21199372: no URL because No URL format for Journal Basic Clin Pharmacol Toxicol
#15533574: no URL because No URL format for Journal Int J Pediatr Otorhinolaryngol
#17100396: no URL because No URL format for Journal J Med Assoc Thai
#17415575: no URL because No URL format for Journal Arch. Dermatol. Res.
#17415800: no URL because No URL format for Journal Mov. Disord.
#17416296: no URL because No URL format for Journal Arch. Med. Res.
#17143317: no URL because No URL format for Journal Nat Clin Pract Endocrinol Metab
#17145028: no URL because No URL format for Journal Med Clin (Barc)
#17145065: no URL because No URL format for Journal Mutat Res
#15452722: no URL because No URL format for Journal Graefes Arch Clin Exp Ophthalmol
#EBioMedicine

# HARDER CASES:
#
#10413889: Medicina (B Aires) -- no URL because No URL format for Journal Medicina (B Aires)
#12027577: Seizure -- no URL because No URL format for Journal Seizure
#10415464: Ophthalmic Genet. -- no URL because No URL format for Journal Ophthalmic Genet
#12015062: Zhonghua Xue Ye Xue Za Zhi -- no URL because No URL format for Journal Zhonghua Xue Ye Xue Za Zhi
#12015065: Zhonghua Xue Ye Xue Za Zhi -- no URL because No URL format for Journal Zhonghua Xue Ye Xue Za Zhi
#12032748: Int. J. Obes. Relat. Metab. Disord. -- no URL because No URL format for Journal Int J Obes Relat Metab Disord


#TODO: journals whose articles can best be accessed by loading up via dx.doi.org
#       and then doing some text replacement on the URL.
doi2step_journals = [ 
                      'J Public Health Policy'  # ex. http://www.palgrave-journals.com/jphp/journal/v36/n2/pdf/jphp201453a.pdf
                    ]


todo_journals = {
    'Pharmacol Rep': { 'example': 'http://www.ncbi.nlm.nih.gov/pubmed/?term=23238479[uid] --> www.if-pan.krakow.pl/pjp/pdf/2012/5_1234.pdf' },
    'Med Sci Monit': { 'example': 'http://www.medscimonit.com/download/index/idArt/869530' },
    'Asian Pac J Cancer Prev': { 'example': 'http://www.apocpcontrol.org/paper_file/issue_abs/Volume12_No7/1771-1776%20c%206.9%20Lei%20Zhong.pdf' },
    'Rev Esp Cardiol': { 'example': 'http://www.revespcardiol.org/en/linkresolver/articulo-resolver/13131646/' },
    'Ann Dermatol Venereol': { 'example': 'http://www.em-consulte.com/article/152959/alertePM' },
    'Mol Cells': { 'example': 'http://www.molcells.org/journal/view.html?year=2004&volume=18&number=2&spage=141 --> http://pdf.medrang.co.kr/KSMCB/2004/018/mac-18-2-141.pdf'},
    'Mol Vis': { 'example': 'http://www.molvis.org/molvis/v10/a45/ --> http://www.molvis.org/bin/pdf.cgi?Zheng,10,45'},
    'Singapore Med J': { 'example': 'http://www.sma.org.sg/smj/4708/4708cr4.pdf' },
    'Rev Port Cardiol': { 'example': '16335287: http://www.spc.pt/DL/RPC/artigos/74.pdf' },
    'World J Gastroenterol': { 'example': 'http://www.wjgnet.com/1007-9327/full/v11/i48/7690.htm --> http://www.wjgnet.com/1007-9327/pdf/v11/i48/7690.pdf' },
    'Genet Mol Res': { 'example': '24668667: http://www.geneticsmr.com/articles/2992 --> http://www.geneticsmr.com//year2014/vol13-1/pdf/gmr2764.pdf' },
    'Arq Bras Cardiol': { 'example': '20944894: http://www.scielo.br/pdf/abc/v95n5/en_aop13210.pdf' },
    'Arq Bras Endocrinol Metabol': { 'example': '15611820: http://www.scielo.br/pdf/abem/v48n1/19521.pdf' },
    'Neoplasma': { 'example': '17319787: http://www.elis.sk/download_file.php?product_id=1006&session_id=skl2f3grcd19ebnie17u15a571' },
    'Clinics (Sao Paulo)': { 'example': '17823699: http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1807-59322007000400003' },
    'Asian J Androl': {'example': '18097502: http://www.asiaandro.com/Abstract.asp?doi=10.1111/j.1745-7262.2008.00376.x' },
    'Anesthesiology': {'example': '18212565: http://dx.doi.org/10.1097/01.anes.0000299431.81267.3e --> html w/ <a id="pdfLink" data-article-url="THE_URL">' },
    'Nat Prod Commun': {'example': '19634325 (no direct link found yet) -- http://www.naturalproduct.us/' },
    'Oncotarget': {'example': '26008984 (pii = 3900) --> http://www.impactjournals.com/oncotarget/index.php?journal=oncotarget&page=article&op=view&path=3900' },
    'Clin Ter': {'example': '25756258 --> dx.doi.org/10.7417/CT.2015.1799 --> parse page to get PDF' },
    'J Pediatr (Rio J)': { 'example': '17102902 --> dx.doi.org/10.2223/JPED.1550 --> http://www.jped.com.br/conteudo/06-82-06-437/port.pdf' },
    'Teach Learn Med': { 'example': '17144842 --> dx.doi.org/10.1207/s15328015tlm1804_13 --> pdf link?' },
    }


format_templates = {
    'acs': 'http://pubs.acs.org/doi/pdf/{a.doi}',
    'akademii': 'http://www.akademiai.com/content/{a.pii}/fulltext.pdf',
    'ats': 'http://www.atsjournals.org/doi/pdf/{a.doi}',
    'informa': 'http://informahealthcare.com/doi/pdf/{a.doi}',
    'lancet': 'http://www.thelancet.com/pdfs/journals/{ja}/PII{a.pii}.pdf',
    'liebert': 'http://online.liebertpub.com/doi/pdf/{a.doi}',
    'plos': 'http://www.plosbiology.org/article/fetchObjectAttachment.action?url=info:doi/{a.doi}&representation=PDF',
    'wiley': 'http://onlinelibrary.wiley.com/doi/{a.doi}/pdf',
    'jci': 'http://www.jci.org/articles/view/{a.pii}/pdf',
    }

# JCI == Journal of Clinical Investigation
jci_journals = [ 'J Clin Invest' ]

# TODO: Dustri Dance
# Dustri: see http://www.dustri.com/journals-in-english.html
dustri_journals = ( 'Clin Nephrol', 'Int J Clin Pharmacol Ther', 'Clin Neuropathol' )

# Portlan Press Biochemical Society journals: mostly VIP.
#TODO: detect and redo urls for "early" releases, e.g.:
#      http://www.clinsci.org/content/ppclinsci/early/2015/06/10/CS20150073.full.pdf
biochemsoc_journals = { 'Biochem J': { 'host': 'www.biochemj.org', 'ja': 'ppbiochemj' },
                        'Clin Sci': { 'host': 'www.clinsci.org', 'ja': 'ppclinsci' },
                      }
biochemsoc_format = 'http://{host}/content/{ja}/{a.volume}/{a.issue}/{a.first_page}.full.pdf'

lancet_journals = {
    'Lancet': { 'ja': 'lancet' },
    'Lancet Diabetes Endocrinol': { 'ja': 'landia' },
    'Lancet Glob Health': { 'ja': 'langlo' },
    'Lancet Haematol': { 'ja': 'lanhae' },
    'Lancet HIV': { 'ja': 'lanhiv' },
    'Lancet Infect Dis': { 'ja': 'laninf' },
    'Lancet Neurol': { 'ja': 'laneur' },
    'Lancet Oncol': { 'ja': 'lanonc' },
    'Lancet Psychiatry': { 'ja': 'lanpsy' },
    'Lancet Respir Med': { 'ja': 'lanres' },
    }


# the SD journals are also represented in simple_formats_pii
# "piit" means pii-translated (i.e. punctuation removed)
sciencedirect_url = 'http://www.sciencedirect.com/science/article/pii/{piit}'
sciencedirect_journals = (
    'Ann Genet',
    'Am J Pathol',
    'Am J Prev Med',
    'Ambul Pediatr',
    'Appetite',
    'Arch Biochem Biophys',
    'Arch Pediatr',
    'Atherosclerosis',
    'Blood Cells Mol Dis',
    'Biochem Biophys Res Commun' ,
    'Biochem Pharmacol',
    'Biochim Biophys Acta',
    'Br J Oral Maxillofac Surg',
    'Child Abuse Negl',
    'Clin Chim Acta',
    'Clin Immunol',
    'Contemp Clin Trials',
    'Crit Care Clin',
    'Fam Pract',
    'FEBS Lett',
    'Eur J Cancer',
    'Eur J Med Genet',
    'Exp Parasitol',
    'Gene',
    'Genomics',
    'Gynecol Obstet Fertil',
    'Hepatol Res',
    'Hum Immunol',
    'Infect Genet Evol',
    'J Acad Nutr Diet',
    'J Am Coll Cardiol',
    'J Am Diet Assoc',
    'J Adolesc Health',
    'J Autoimmun',
    'J Environ Sci (China)',
    'J Health Econ',
    'J Mol Biol',
    'J Neurol Sci',
    'J Pediatr',
    'J Pediatr Health Care',
    'J Reprod Immunol',
    'J Steroid Biochem Mol Biol',
    'J Struct Biol',
    'J Urol',
    'Leuk Res',
    'Life Sci',
    'Mol Cell Endocrinol',
    'Mol Cell Probes',
    'Mol Genet Metab',
    'Mol Immunol',
    'Mutat Res',
    'Neuromuscul Disord',
    'Neurosci Lett',
    'Neurosci Res',
    'Neuroscience',
    'Neurotoxicology',
    'Nitric Oxide',
    'Nutr Metab Cardiovasc Dis',
    'Patient Educ Couns',
    'Pediatr Nurs',
    'Pediatr Pulmonol',
    'Sci Total Environ',
    'Soc Sci Med',
    'Toxicol In Vitro',
    'Trends Biochem Sci',
    'Virology',
    'Virus Res',
    )


jama_journals = (
     'Arch Gen Psychiatry',
     'Arch Neurol',
     'Arch Ophthalmol',
     'JAMA',
     'JAMA Dermatol',
     'JAMA Facial Plast Surg',
     'JAMA Intern Med',
     'JAMA Neurol',
     'JAMA Oncol',
     'JAMA Ophthalmol',
     'JAMA Otolaryngol Head Neck Surg',
     'JAMA Pediatr',
     'JAMA Psychiatry',
     'JAMA Surg',
     )

# TODO
# doiserbia (Library of Serbia) articles can be grabbed by doing the_doi_2step,
# then ...?
doiserbia_journals = ['Genetika']

# JSTAGE: mostly free (yay)
# Examples:
# J Biochem: https://www.jstage.jst.go.jp/article/biochemistry1922/125/4/125_4_803/_pdf
# Drug Metab Pharmacokinet: https://www.jstage.jst.go.jp/article/dmpk/20/2/20_2_144/_article --> https://www.jstage.jst.go.jp/article/dmpk/20/2/20_2_144/_pdf
jstage_journals = [
    'Intern Med',
    'J Periodontol',
    'J Biochem',
    'Drug Metab Pharmacokinet',
    'Endocr J',
    ]

# cell journals
#cell_format = 'http://download.cell.com{ja}/pdf/PII{pii}.pdf'
cell_format = 'http://www.cell.com{ja}/pdf/{pii}.pdf'
cell_journals = {
    'Am J Hum Genet': { 'ja': '/AJHG' },
    'Biophys J': { 'ja': '/biophysj' },
    'Cancer Cell': { 'ja': '/cancer-cell' },
    'Cell': { 'ja': '' },
    'Cell Host Microbe': {'ja': '/cell-host-microbe' },
    'Cell Metab': {'ja': '/cell-metabolism' },
    'Cell Stem Cell': {'ja': '/cell-stem-cell' },
    'Chem Biol': {'ja': '/chemistry-biology' },
    'Curr Biol': {'ja': '/current-biology' },
    'Dev Cell': {'ja': '/developmental-cell' },
    'Immunity': {'ja': '/immunity' },
    'Mol Cell': {'ja': '/molecular-cell' },
    'Neuron': {'ja': '/neuron' },
    'Structure': {'ja': '/structure' },
    'Trends Mol Med': { 'ja': '/trends' },
    }

# nature journals -- COMPLETE
nature_format = 'http://www.nature.com/{ja}/journal/v{a.volume}/n{a.issue}/pdf/{a.pii}.pdf'
nature_journals = {
    'Eur J Clin Nutr': { 'ja': 'ejcn' },
    'Eur J Hum Genet': { 'ja': 'ejhg' },
    'Eye (Lond)': { 'ja': 'eye' },
    'Genes Immun': { 'ja': 'gene' },
    'Genet Med': { 'ja': 'gim' },
    'J Invest Dermatol': { 'ja': 'jid' },
    'J Hum Genet': { 'ja': 'jhg' },
    'Kidney Int': { 'ja': 'ki' },
    'Leukemia': { 'ja': 'leu' },
    'Mod Pathol': { 'ja': 'modpathol' },
    'Mol Psychiatry': { 'ja': 'mp' },
    'Nature': { 'ja': 'nature' },
    'Nat Chem': { 'ja': 'nchem' },
    'Nat Clin Pract Endocrinol Metab': { 'ja': 'nrendo' },
    'Nat Clin Pract Cardiovasc Med': { 'ja': 'nrcardio' },
    'Nat Clin Pract Oncol': { 'ja': 'nrclinonc' },
    'Nat Clin Pract Gastroenterol Hepatol': { 'ja': 'nrgastro' },
    'Nat Clin Pract Urol': { 'ja': 'nrurol' },
    'Nat Clin Pract Neurol': { 'ja': 'nrneurol' },
    'Nat Clin Pract Nephrol': { 'ja': 'nrneph' },
    'Nat Clin Pract Rheumatol': { 'ja': 'nrrheum' },
    'Nat Genet': { 'ja': 'ng' },
    'Nat Commun': {'ja': 'ncomms' },
    'Nat Nanotechnol': { 'ja': 'nnano' },
    'Nat Neurosci': { 'ja': 'neuro' },
    'Nat Mater': { 'ja': 'nmat' },
    'Nat Med': { 'ja': 'nm' },
    'Nat Methods': { 'ja': 'nmeth' },
    'Nat Protoc': { 'ja': 'nprot' },
    'Nat Rev Drug Discov': { 'ja': 'nrd' },
    'Nat Rev Cardiol': { 'ja': 'nrcardio' },
    'Nat Rev Clin Oncol': { 'ja': 'nrclinonc' },
    'Nat Rev Endocrinol': { 'ja': 'nrendo' },
    'Nat Rev Genet': { 'ja': 'nrg' },
    'Nat Rev Gastroenterol Hepatol': { 'ja': 'nrgastro' },
    'Nat Rev Nephrol': { 'ja': 'nrneph' },
    'Nat Rev Neurol': { 'ja': 'nrneurol' },
    'Nat Rev Rheumatol': { 'ja': 'nrrheum' },
    'Nat Rev Urol': { 'ja': 'nrurol' },
    'Nat Rev Immunol': { 'ja': 'nri' },
    'Neuropsychopharmacology': { 'ja': 'npp' },
    'Oncogene': { 'ja': 'onc' },
    'Pediatr Res': { 'ja': 'pr' },
    }


# simple_formats_pmid: links to PDFs that can be constructed using the pubmed ID
simple_formats_pmid = {
    'Medicina (B Aires)': 'http://www.medicinabuenosaires.com/PMID/{pmid}.pdf',
    }


# simple formats are used for URLs that can be deduced from PubMedArticle XML
#       
#       !ACHTUNG!  informa has been known to block IPs for the capital offense of 
#                  having "More than 25 sessions created in 5 minutes"
#
simple_formats_doi = {
    'Acta Oncol': format_templates['informa'],
    'Ann Hum Biol': format_templates['informa'],
    'Hemoglobin': format_templates['informa'],
    'J Matern Fetal Neonatal Med': format_templates['informa'],
    'Platelets': format_templates['informa'],
    'Ren Fail': format_templates['informa'],
    'Xenobiotica': format_templates['informa'],

    'Am J Public Health': 'http://ajph.aphapublications.org/doi/pdf/{a.doi}',

    'Am J Respir Cell Mol Biol': format_templates['ats'],
    'Am J Respir Crit Care Med': format_templates['ats'],

    'Anal Chem': format_templates['acs'],
    'Biochemistry': format_templates['acs'],
    'J Am Chem Soc': format_templates['acs'],

    'Child Obes': format_templates['liebert'],
    'Genet Test': format_templates['liebert'],
    'Genet Test Mol Biomarkers': format_templates['liebert'],
    'Thyroid': format_templates['liebert'],

    'Endocrinology': 'http://press.endocrine.org/doi/pdf/{a.doi}',
    'Mol Endocrinol': 'http://press.endocrine.org/doi/pdf/{a.doi}',
    'J Periodontol': 'http://www.joponline.org/doi/pdf/{a.doi}',

    'PLoS Biol': format_templates['plos'],
    'PLoS Comput Biol': format_templates['plos'],
    'PLoS Genet': format_templates['plos'],
    'PLoS Med': format_templates['plos'],
    'PLoS ONE': format_templates['plos'],
    'PLoS Pathog': format_templates['plos'],
    'N Engl J Med':  'http://www.nejm.org/doi/pdf/{a.doi}',
    }



simple_formats_pii = {
    'Am Heart J': 'http://www.ahjonline.com/article/{a.pii}/pdf', #ScienceDirect
    'Am J Cardiol': 'http://www.ajconline.org/article/{a.pii}/pdf', #ScienceDirect
    'Am J Ophthalmol': 'http://www.ajo.com/article/{a.pii}/pdf', #ScienceDirect
    'Am J Med': 'http://www.amjmed.com/article/{a.pii}/pdf', #ScienceDirect
    'Atherosclerosis': 'http://www.atherosclerosis-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Arch Med Res': 'http://www.arcmedres.com/article/{a.pii}/pdf', #ScienceDirect
    'Biol Psychiatry': 'http://www.biologicalpsychiatryjournal.com/article/{a.pii}/pdf', #ScienceDirect
    'Bone': 'http://www.thebonejournal.com/article/{a.pii}/pdf', #ScienceDirect
    'Brain Dev': 'http://www.brainanddevelopment.com/article/{a.pii}/pdf', #ScienceDirect
    'Cancer Cell Int': 'http://www.cancerci.com/content/pdf/{a.pii}.pdf', #Biomed Central
    'Cancer Genet Cytogenet': 'http://www.cancergeneticsjournal.org/article/{a.pii}/pdf', #ScienceDirect
    'Cancer Lett': 'http://www.cancerletters.info/article/{a.pii}/pdf', #ScienceDirect
    'Clin Neurol Neurosurg': 'http://www.clineu-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Diabetes Res Clin Pract': 'http://www.diabetesresearchclinicalpractice.com/article/{a.pii}/pdf', #ScienceDirect
    'Epilepsy Res': 'http://www.epires-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Eur J Paediatr Neurol': 'http://www.ejpn-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Exp Hematol': 'http://www.exphem.org/article/{a.pii}/pdf', #ScienceDirect
    'Fertil Steril': 'http://www.fertstert.org/article/{a.pii}/pdf',    #ScienceDirect
    'Gastroenterology': 'http://www.gastrojournal.org/article/{a.pii}/pdf',
    'Gynecol Oncol': 'http://www.gynecologiconcology-online.net/article/{a.pii}/pdf', #ScienceDirect
    'Heart Rhythm': 'http://www.heartrhythmjournal.com/article/{a.pii}/pdf',
    'Int J Pediatr Otorhinolaryngol': 'http://www.ijporlonline.com/article/{a.pii}/pdf', #ScienceDirect
    'Int J Cardiol': 'http://www.internationaljournalofcardiology.com/article/{a.pii}/pdf', #ScienceDirect
    'J Dermatol': 'http://www.jdsjournal.com/article/{a.pii}/pdf', #ScienceDirect
    'J Mol Cell Cardiol': 'http://www.jmmc-online.com/article/{a.pii}/pdf', #ScienceDirect
    'J Mol Diagn': 'http://jmd.amjpathol.org/article/{a.pii}/pdf',  #ScienceDirect
    'J Neurol Sci': 'http://www.jns-journal.com/article/{a.pii}/pdf',
    'J Pediatr': 'http://www.jpeds.com/article/{a.pii}/pdf',  #ScienceDirect
    'J Pediatr Urol': 'http://www.jpurol.com/article/{a.pii}/pdf',  #ScienceDirect
    'Ophthalmology': 'http://www.aaojournal.org/article/{a.pii}/pdf', #ScienceDirect
    'Orv Hetil': format_templates['akademii'],
    'Med Hypotheses': 'http://www.medical-hypotheses.com/article/{a.pii}/pdf', #ScienceDirect
    'Metabolism': 'http://www.metabolismjournal.com/article/{a.pii}/pdf', #ScienceDirect
    'Metab Clin Exp': 'http://www.metabolismjournal.com/article/{a.pii}/pdf', #ScienceDirect
    'Neurobiol Aging': 'http://www.neurobiologyofaging.org/article/{a.pii}/pdf', #ScienceDirect
    'Neuromuscul Disord': 'http://www.nmd-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Parkinsonism Relat Disord': 'http://www.prd-journal.com/article/{a.pii}/pdf', #ScienceDirect
    'Pediatr Neurol': 'http://www.pedneur.com/article/{a.pii}/pdf', #ScienceDirect
    'Placenta': 'http://www.placentajournal.org/article/{a.pii}/pdf', #ScienceDirect
    'Surg Neurol': 'http://www.worldneurosurgery.org/article/{a.pii}/pdf', #ScienceDirect
    'Thromb Res': 'http://www.thrombosisresearch.com/article/{a.pii}/pdf', #ScienceDirect
    }

#    The following were taken out of simple_formats_pii but kept in the sciencedirect_journals list:
#    'Mol Genet Metab': 'http://www.mgmjournal.com/article/{a.pii}/pdf', #ScienceDirect


# Many BMC journals start with "BMC" (they're covered automatically) --
#   this list covers the ones that don't.  #TODO: Gather up the ones not in here yet.
BMC_journals = (
    'Diagn Pathol',
    'Genome Biol',
    'Genome Med',
    'Hum Genomics',
    'J Clin Bioinforma',
    'J Transl Med',
    )

# the "aid" is the second half of the DOI string (after the slash)
BMC_format = 'http://www.biomedcentral.com/content/pdf/{aid}.pdf'

# vip = Volume-Issue-Page format 
#       URLs that have the same format except for the host name

vip_format = 'http://{host}/content/{a.volume}/{a.issue}/{a.first_page}.full.pdf'

vip_journals = {
        'Ann Clin Biochem': { 'host': 'acb.sagepub.com' },
        'Am J Clin Pathol': { 'host': 'ajcp.ascpjournals.org' },
        'Am J Hypertens': { 'host': 'ajh.oxfordjournals.org' },
        'Ann Oncol': { 'host' : 'annonc.oxfordjournals.org' },
        'Antimicrob Agents Chemother': { 'host': 'aac.asm.org' }, #TODO: backup_url: pmid lookup strategy, e.g. http://aac.asm.org/cgi/pmidlookup?view=long&pmid=7689822
        'Arterioscler Thromb Vasc Biol': { 'host' : 'atvb.ahajournals.org' },
        'Brain': { 'host': 'brain.oxfordjournals.org' },
        'Breast Cancer Res': { 'host': 'breast-cancer-research.com' },
        'Cancer Discov': { 'host': 'cancerdiscovery.aacrjournals.org' },
        'Cancer Epidemiol Biomarkers Prev': { 'host': 'cebp.aacrjournals.org' },
        'Cancer Res': { 'host': 'cancerres.aacrjournals.org' },
        'Can Fam Physician': { 'host': 'www.cfp.ca' }, #TODO: backup_url: pmid lookup strategy, e.g. http://www.cfp.ca/cgi/pmidlookup?view=long&pmid=19282532
        'Carcinogenesis': { 'host': 'carcin.oxfordjournals.org' } ,
        'Cardiovasc Res': { 'host' : 'cardiovascres.oxfordjournals.org' },
        'Circulation': { 'host': 'circ.ahajournals.org' },
        'Circ Arrhythm Electrophysiol': { 'host': 'circep.ahajournals.org' },
        'Circ Cardiovasc Genet': { 'host' : 'circgenetics.ahajournals.org' },
        'Circ Res': { 'host' : 'circres.ahajournals.org' },
        'Clin Cancer Res': { 'host' : 'clincancerres.aacrjournals.org' },
        'Clin Chem': { 'host' : 'clinchem.org' },
        'Clin Infect Dis': { 'host': 'cid.oxfordjournals.org' },
        'Clin Pediatr': { 'host': 'cpj.sagepub.com' },
        'Clin Pediatr (Phila)': { 'host': 'cpj.sagepub.com' },
        'Diabetes': { 'host': 'diabetes.diabetesjournals.org' },
        'Diabetes Care': { 'host': 'care.diabetesjournals.org' },
        'Drug Metab Dispos': { 'host': 'dmd.aspetjournals.org' },
        'EMBO J': { 'host': 'emboj.embopress.org' }, ##TODO: backup_url: pmid lookup strategy, http://emboj.embopress.org/cgi/pmidlookup?view=long&pmid=9501081
        'Endocr Relat Cancer': { 'host': 'erc.endocrinology-journals.org' },
        'Eur Heart J' : { 'host' : 'eurheartj.oxfordjournals.org' },
        'Eur J Endocrinol' : { 'host' : 'eje-online.org' },
        'FASEB J': { 'host' : 'fasebj.org' },
        'Genome Biol': { 'host' : 'genomebiology.com' },
        'Genome Res': { 'host': 'genome.cshlp.org' },
        'Genes Dev': { 'host': 'genesdev.cshlp.org' },
        'Gut': { 'host' : 'gut.bmj.com' },
        'Haematologica': { 'host' : 'haematologica.org' },
        'Hum Mol Genet': { 'host': 'hmg.oxfordjournals.org' },
        'Hum Reprod': { 'host': 'humrep.oxfordjournals.org' },
        'Hypertension': { 'host': 'hyper.ahajournals.org' },
        'Invest Ophthalmol Vis Sci': { 'host': 'www.iovs.org' },
        'IOVS': { 'host' : 'iovs.org' },
        'J Aging Health': { 'host': 'jah.sagepub.com' }, ##TODO: backup_url: pmid lookup strategy, http://jah.sagepub.com/cgi/pmidlookup?view=long&pmid=20056814
        'J Am Soc Nephrol': { 'host' : 'jasn.asnjournals.org' },
        'J Bacteriol': { 'host': 'jb.asm.org' },  #TODO: backup_url: pmid lookup strategy, http://jb.asm.org/cgi/pmidlookup?view=long&pmid=7683021
        'J Biol Chem': { 'host': 'www.jbc.org' },   #TODO backup_url: pmid lookup strategy, e.g. http://www.jbc.org/cgi/pmidlookup?view=long&pmid=14722075
        'J Cell Biol': { 'host' : 'jcb.rupress.org' },
        'J Cell Sci': { 'host' : 'jcs.biologists.org' },
        'J Child Neurol': { 'host': 'jcn.sagepub.com' },
        'J Clin Endocrinol Metab': { 'host': 'jcem.endojournals.org' },
        'J Clin Oncol': { 'host': 'jco.ascopubs.org' },
        'J Dent Res': { 'host': 'jdr.sagepub.com' },
        'J Gerontol A Biol Sci Med Sci': { 'host': 'biomedgerontology.oxfordjournals.org' },
        'J Immunol': { 'host' : 'jimmunol.org' },
        'J Infect Dis': { 'host': 'jid.oxfordjournals.org' },
        'J Lipid Res': { 'host': 'www.jlr.org' },
        'J Med Genet': { 'host': 'jmg.bmj.com' },
        'J Mol Endocrinol': { 'host': 'jme.endocrinology-journals.org' },
        'J Natl Cancer Inst': { 'host': 'jnci.oxfordjournals.org' },
        'J Neurol Neurosurg Psychiatry': { 'host': 'jnnp.bmj.com' },
        'J Neurosci': { 'host' : 'jneurosci.org' },
        'J Nutr': { 'host': 'jn.nutrition.org' }, #TODO:  backup_url: pmid lookup strategy, http://jn.nutrition.org/cgi/pmidlookup?view=long&pmid=10736367
        'J Pharmacol Exp Ther': { 'host': 'jpet.aspetjournals.org' },
        'J Rheumatol': { 'host': 'www.jrheum.org' },
        'J Virol': { 'host': 'jvi.asm.org' },
        'Mol Biol Cell': { 'host' : 'molbiolcell.org' },
        'Mol Cell Biol': { 'host': 'mcb.asm.org' },
        'Mol Canc Therapeut': { 'host' : 'mct.aacrjournals.org' },
        'Mol Hum Reprod': { 'host': 'molehr.oxfordjournals.org' },
        'Mol Pharmacol': { 'host' : 'molpharm.aspetjournals.org' },
        'Neurology': { 'host' : 'neurology.org' },
        'Nephrol Dial Transplant': { 'host': 'ndt.oxfordjournals.org' },
        'Nucleic Acids Res': { 'host' : 'nar.oxfordjournals.org' },
        'Orphanet J Rare Dis': { 'host' : 'ojrd.com' },
        'Pediatrics': { 'host': 'pediatrics.aappublications.org'},
        'Plant Cell': { 'host': 'www.plantcell.org' }, #TODO:  backup_url: pmid lookup strategy, e.g. http://www.plantcell.org/cgi/pmidlookup?view=long&pmid=9501112
        'Plant Cell Physiol': { 'host': 'pcp.oxfordjournals.org' },
        'Proc Natl Acad Sci USA': { 'host': 'pnas.org' },
        'Protein Eng': { 'host': 'peds.oxfordjournals.org' },
        'QJM': { 'host': 'qjmed.oxfordjournals.org'},
        'Science': { 'host': 'sciencemag.org' },
        'Thorax': { 'host': 'thorax.bmj.com' },
        }

# volume-issue-page type URLs but with a nonstandard baseurl construction.
# e.g. Blood: http://www.bloodjournal.org/content/bloodjournal/79/10/2507.full.pdf
#      BMJ:   http://www.bmj.com/content/bmj/350/bmj.h3317.full.pdf

# no trailing slash in baseurl (please)
vip_journals_nonstandard = { 
	#TODO: backup_url: pmid lookup strategy, e.g. http://www.bloodjournal.org/cgi/pmidlookup?view=long&pmid=1586703
    'Blood': 'http://www.bloodjournal.org/content/bloodjournal/{a.volume}/{a.issue}/{a.first_page}.full.pdf',
    'BMJ':   'http://www.bmj.com/content/bmj/{a.volume}/bmj.{a.first_page}.full.pdf', 
    }

# Science (AAAS) -- requires login "as a courtesy to the community".  Mkay.
aaas_format = 'http://{ja}.sciencemag.org/content/{a.volume}/{a.issue}/{a.pages}.full.pdf'
aaas_journals = {
        'Science': { 'ja': 'www' },
        'Sci Adv': { 'ja': 'advances' },
        'Sci Signal': { 'ja': 'stke' },
        'Sci Transl Med': { 'ja': 'stm' },
    }


# Spandidos: volume/issue/firstpage AND a journal abbreviation. Fancy.
spandidos_format = 'http://www.spandidos-publications.com/{ja}/{a.volume}/{a.issue}/{a.first_page}/download'
spandidos_journals = {
        'Int J Oncol': { 'ja' : 'ijo' },
        'Int J Mol Med': { 'ja': 'ijmm' },
        'Oncol Lett': { 'ja' : 'ol' },
        'Oncol Rep': { 'ja' : 'or' },
    }


wiley_journals = (
    'Acta Neurol Scand',
    'Acta Ophthalmol Scand',
    'Ann Hum Genet',
    'Ann Neurol',
    'Am J Hematol',
    'Am J Med Genet',
    'Am J Med Genet A',
    'Am J Med Genet B Neuropsychiatr Genet',
    'Arthritis Rheum',
    'Australas J Dermatol',
    'Basic Clin Pharmacol Toxicol',
    'BJU Int',
    'Breast J',
    'Br J Dermatol',
    'Br J Haematol',
    'Cancer',
    'Cancer Sci',
    'Clin Endocrinol (Oxf)',
    'Clin Exp Dermatol',
    'Clin Genet',
    'Clin Pharmacol Ther',
    'Diabet Med',
    'Dev Med Child Neurol',
    'Electrophoresis',
    'Environ Mol Mutagen',
    'Eur J Biochem',
    'Eur J Clin Invest',
    'Eur J Haematol',
    'Eur J Neurol',
    'Exp Dermatol',
    'Genes Chromosomes Cancer',
    'Genet Epidemiol',
    'Haemophilia',
    'Head Neck',
    'Headache',
    'Hepatology',
    'Hum Brain Mapp',
    'Hum Mutat',
    'Immunol Rev',
    'Int J Cancer',
    'Int J Immunogenet',
    'Int J Lab Hematol',
    'J Am Assoc Nurse Pract',
    'J Bone Miner Res',
    'J Dermatol',
    'J Eur Acad Dermatol Venereol',
    'J Gastroenterol Hepatol',
    'J Intern Med',
    'J Med Virol',
    'J Neurochem',
    'J Orthop Res',
    'J Pathol',
    'J Rural Health',
    'J Sch Health',
    'J Thromb Haemost',
    'J Viral Hepat',
    'Med Educ',
    'Mol Carcinog',
    'Mol Microbiol',
    'Mol Plant Pathol',
    'Mov Disord',
    'Muscle Nerve',
    'Neuropathol Appl Neurobiol',
    'Nihon Shokakibyo Gakkai Zasshi',
    'Obesity (Silver Spring)',
    'Pain Med',
    'Pediatr Blood Cancer',
    'Pediatr Diabetes',
    'Pediatr Int',
    'Prenat Diagn',
    'Prostate',
    'Protein Sci',
    'Proteins',
    'Scand J Immunol',
    'Tissue Antigens',
    'Transfus Med',
    'Transfusion',
    'Vox Sang',
    )

#TODO: De Gruyter (publisher)
#
# examples:
# 26110471 Arh Hig Rada Toksikol http://www.degruyter.com/view/j/aiht.2015.66.issue-2/aiht-2015-66-2582/aiht-2015-66-2582.xml
#12199334: J. Pediatr. Endocrinol. Metab. -- no URL because No URL format for Journal J Pediatr Endocrinol Metab
#12199344: J. Pediatr. Endocrinol. Metab. -- no URL because No URL format for Journal J Pediatr Endocrinol Metab
#
# load by dx.doi.org: http://dx.doi.org/10.2478/cdth-2014-0001
#       --> http://www.degruyter.com/view/j/cdth.2014.1.issue-1/cdth-2014-0001/cdth-2014-0001.xml
#   PDF --> http://www.degruyter.com/dg/viewarticle.fullcontentlink:pdfeventlink/$002fj$002fcdth.2014.1.issue-1$002fcdth-2014-0001$002fcdth-2014-0001.pdf?t:ac=j$002fcdth.2014.1.issue-1$002fcdth-2014-0001$002fcdth-2014-0001.xml
#
#

#TODO: Taylor & Francis (publisher)
#
# e.g. 25121990: http://www.tandfonline.com/doi/pdf/10.1080/10410236.2014.943634
taylorfrancis_journals = ( 
        'Health Commun',
        )

# Below: Journals with really annoying paywalls guarding their precious secrets.
schattauer_journals = [
    'Thromb Haemost',
    ]

# Royal Society of Chemistry
RSC_journals = [ 'Nat Prod Rep' ]

wolterskluwer_journals = [
    'AIDS',
    'Blood Coagul Fibrinolysis',
    'Clin Dysmorphol',
    'Curr Opin Hematol',
    'Eur J Gastroenterol Hepatol',
    'Fam Community Health',
    'J Dev Behav Pediatr',
    'J Glaucoma',
    'J Hypertens',
    'J Investig Med',
    'J Pediatr Hematol Oncol',
    'J Pediatr Gastroenterol Nutr',
    'J Trauma',
    'Medicine (Baltimore)',
    'Neuroreport',
    'Obstet Gynecol',
    'Pediatr Emerg Care',
    'Pediatr Infect Dis J',
    'Pharmacogenet Genomics',
    'Pharmacogenetics',
    'Plast Reconstr Surg',
    'Psychiatr Genet',
    ]

# karger: mostly paywalled, but sometimes...
# http://www.karger.com/Article/Pdf/351538

karger_journals = [
    'Acta Haematol',
    'Ann Nutr Metab',
    'Cell Physiol Biochem',
    'Cytogenet Genome Res',
    'Dermatology (Basel)',
    'Horm Res',
    'Hum Hered',
    'Nephron',
    'Nephron Physiol',
    ]

# springer is mostly paywalled, but sometimes...
# http://link.springer.com/content/pdf/10.1007%2Fs13238-015-0153-5.pdf
springer_journals = [
    'Acta Neuropathol',
    'Ann Hematol',
    'Ann Surg Oncol',
    'Arch Dermatol Res',
    'Biochem Genet',
    'Breast Cancer Res Treat',
    'Calcif Tissue Int',
    'Cell Mol Neurobiol',
    'Diabetologia',
    'Eur J Pediatr',
    'Eur J Nutr',
    'Fam Cancer',
    'Graefes Arch Clin Exp Ophthalmol',
    'HNO',
    'Hum Genet',
    'Immunogenetics',
    'Int J Colorectal Dis',
    'J Bone Miner Metab',
    'J Clin Immunol',
    'J Endocrinol Invest',
    'J Inherit Metab Dis',
    'J Neural Transm',
    'J Neurol',
    'J Mol Evol',
    'J Mol Med',
    'J Mol Med (Berl)',
    'J Mol Neurosci',
    'Matern Child Health J',
    'Mod Rheumatol',
    'Neurogenetics',
    'Ophthalmologe',
    'Osteoporos Int',
    'Pediatr Nephrol',
    'Pharm Res',
    'Physiol Genomics',
    'Protein Cell',
    'Rheumatol Int',
    'Tumour Biol',
    'Virchows Arch',
    'World J Surg',
    ]

# thieme journals so far don't seem to have any open access content.
# example links to article page: https://www.thieme-connect.com/DOI/DOI?10.1055/s-0028-1085467
#           https://www.thieme-connect.com/DOI/DOI?10.1055/s-2007-1004566
thieme_journals = ['Neuropediatrics', 'Semin Vasc Med', 'Exp Clin Endocrinol Diabetes',
                    'Int J Sports Med']

weird_paywall_publishers = ['J Ment Health Policy Econ' ]

paywall_journals = schattauer_journals + wolterskluwer_journals + thieme_journals + weird_paywall_publishers


#All in PMC (no need to write formats for):
 #Nat Comput
 #Nat Clim Chang
 #Nat Geosci
 #Nat Resour Model
 #Nat Lang Linguist Theory
 #Nat Photonics
 #Nat Phys
 #Nat Prod Bioprospect
 #Nat Lang Eng
 #Nat Rep Stem Cells
 #Nat Sci (Irvine)
 #Nat Sci Sleep
