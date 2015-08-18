from django.db import models
from datetime import date


class ProjectCharter(models.Model):

	# Pre-filled Data
	# 	Need to pull this from db? See question for source_lang_name
	# -------- THIS -----------
	SOURCE_LANGS = (
		('en', 'English'),
		('sp', 'Spanish'),
		('de', 'Deutsch'),
		('fr', 'Francois'),
	)
	# -------- OR ----------
	LANG_NAMES = (
		('english', 'English'),
		('spanish', 'Spanish'),
		('german', 'German'),
		('france', 'France'),
	)
	LANG_CODES = (
		('en', 'EN'),
		('sp', 'SP'),
		('de', 'DE'),
		('fr', 'FR'),
	)
	# ----------------------

	OUTPUT_TARGETS = (
		('pr', 'Print'),
		('dg', 'Digital'),
		('au', 'Audio'),
		('ot', 'Other')
	)

	CONTENTS = (
		('luke', 'Gospel of Luke'),
		('tA', 'Translation Audio'),
		('obs', 'OBS'),
		('ot', 'Other')
	)

	CHECK_LVLS = (
		(1, '1'),
		(2, '2'),
		(3, '3'),
	)

	proj_name = models.CharField(
		max_length   = 100,
		unique = True,
		verbose_name = "project name"
	)
	acc_num = models.CharField(
		max_length   = 10,
		primary_key  = True,
		blank        = False,
		verbose_name = "account number"
	)

	# QUESTION: Should we have only 1 field (name) instead of 2 (name and tag)?
	src_lang_name = models.CharField(
		max_length   = 50,
		choices      = LANG_NAMES,
		verbose_name = "source language",
		help_text    = "The language of the source text"
	)
	# Lookup IETF Language tag to see how long each tag can be
	src_lang_ietf = models.SlugField(
		max_length   = 20,
		choices      = LANG_CODES,
		verbose_name = "source language IETF tag"
	)
	# QUESTION: Same question as src_lang_name
	des_lang_name = models.CharField(
		max_length   = 50,
		choices      = LANG_NAMES,
		verbose_name = "translation language",
		help_text    = "The language of the translation"
	)
	des_lang_ietf = models.SlugField(
		max_length   = 20,
		choices      = LANG_CODES,
		verbose_name = "translation language IETF tag"
	)
	
	# QUESTION: Should this be country or city?
	# Should we make this a textfield or ddl (pre-populated)?
	location_general = models.CharField(
		max_length   = 100
	)
	
	#
	start_date = models.DateField(
		help_text = 'YYYY-MM-DD'
	)
	completion_date = models.DateField(
		help_text = 'YYYY-MM-DD'
	)

	op_responsible = models.CharField(
		max_length = 200,
		verbose_name = 'operational responsibility',
		help_text = 'Department or network that is responsible for this project'
	)

	#
	funding_src = models.CharField(
		max_length   = 200,
		verbose_name = 'funding source',
		help_text = 'Who generally funds this project?'
	)

	# Write model for Source materials here
	# Desired render: input + checkbox
	# 
	#     MATERIALS                LICENSED
	#
	#     -----------------------  -----
	#     | my material         |  |   |
	#     -----------------------  -----
	#     -----------------------  -----
	#     | your material       |  | X |
	#     -----------------------  -----
	#

	#
	output_target = models.CharField(
		max_length   = 2,
		choices      = OUTPUT_TARGETS,
		help_text    = 'Medium for the translation',
	)
	output_other = models.CharField(
		max_length   = 50,
		null         = True,
		blank        = True,
		verbose_name = 'other target',
		help_text    = 'Describe, if you chose "other" as medium.'
	)
	content_aided = models.CharField(
		max_length = 50,
		choices    = CONTENTS,
		help_text  = 'What translated content is this project hoping to achieve?'
	)
	content_other = models.CharField(
		max_length   = 50,
		null         = True,
		blank        = True,
		verbose_name = "Other content",
		help_text    = 'Describe, if you chose "other" content.'
	)


	#
	check_lvl = models.PositiveSmallIntegerField(
		choices      = CHECK_LVLS,
		verbose_name = 'checking level',
		help_text    = 'The targeted checking level for the output of this project'
	)
	check_workflow = models.TextField(
		max_length   = 1500,
		verbose_name = 'checking workflow',
		help_text    = 'How will church leaders, church networks, exegetes, consultants, etc. be involved to achieve this checking level?'
	)

	#
	content_flow = models.TextField(
		max_length   = 1500,
		help_text    = 'How will the translated content be safely transfered to digital publishing pipeline?'
	)
	content_person = models.CharField(
		max_length   = 50,
		verbose_name = 'accountable person',
		help_text    = 'The person responsible for the translated contents integrity during and after the project'
	)

	def __unicode__(self):
		return self.proj_name



class Material(models.Model):
	project  = models.ForeignKey(ProjectCharter)
	name     = models.CharField(
		max_length = 200
	)
	licensed = models.BooleanField(
		default = False
	)

	def __unicode__(self):
		return self.name
