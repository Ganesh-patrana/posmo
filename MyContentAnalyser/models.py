import uuid
from email.policy import default
from tabnanny import verbose
from django.db import models


class Links(models.Model):
    channel_id = models.CharField(max_length = 30, primary_key = True)
    #channel  = models.ForeignKey('Channel')
    url = models.URLField()
    parameters = models.TextField(verbose_name='parameters',null= False)
    title=models.TextField(null=False,verbose_name='Title',max_length = 200, default="Content Title")
    def __str__(self):

        return self.channel_id 

class Content(models.Model):
    link = models.OneToOneField(
        Links,
        on_delete=models.CASCADE,
        primary_key=True
    )
    #scraped content - whole page keywords - viewConten
    main_content=models.TextField(verbose_name='Main Content',null= False)

    #number_of_words=models.IntegerField(verbose_name="Number Of Words",default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.link.channel_id


class ContentFetchInfo(models.Model):
    content = models.OneToOneField(
        Content,
        on_delete=models.CASCADE,
        primary_key=True
    )
    #processed content - summary keywords - viewContenSummary   
    processed_words = models.TextField(verbose_name = "Processed Words", null = False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.content.link.channel_id


class MappedKeyWords(models.Model):
    content_info = models.OneToOneField(
        ContentFetchInfo,
        on_delete=models.CASCADE,
        primary_key=True
    )
    '''
    Structure of json for mapped keywords
    {
        'tagline': {
            'keyword': {
                'louisiana': {
                    'similar': [],
                    'word_count': 0
                },
                'loyal': {
                    'similar': ['notoriously', 'experience', 'extensive', 'personal', 'safe', 'great', 'beat',       'efficient', 'important', 'love', 'affection', 'base', 'long', 'experienced', 'ensure', 'throughout', 'aware', 'local', 'many', 'among'],
                    'word_count': 20}
            },
            'count': 20
        }
    }
    '''
    mapped_keywords = models.TextField(verbose_name='Mapped keywords',null= False)
    mapped_keywords_count = models.IntegerField(verbose_name = "No. of Mapped Words", null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.content_info.content.link.channel_id


class UnmappedKeywords(models.Model):
    content_info = models.OneToOneField(
        ContentFetchInfo,
        on_delete=models.CASCADE,
        primary_key=True
    )
    unmapped_keywords=models.TextField(verbose_name="Unmapped Keywords",null=True)
    unmapped_keywords_count = models.IntegerField(verbose_name = "No. of Unmapped Words", null = True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):

        return self.content_info.content.link.channel_id