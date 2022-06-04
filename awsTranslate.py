import boto3


access_key_id = 'AKIA3MTVG467OJTIA4MK'
secret_access_key = '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'

translate = boto3.client(service_name = 'translate',aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, region_name = 'eu-central-1')

result = translate.translate_text( Text = 'Selamın Aleyküm, dünya',
	SourceLanguageCode = 'tr', TargetLanguageCode = 'en')


print('TranslatedText: ' + result.get('TranslatedText'))

print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))

print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
