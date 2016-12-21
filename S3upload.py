import boto

AWS_ACCESS_KEY_ID = 'AKIAJI6TFV4NVQNYZLHQ'
AWS_SECRET_ACCESS_KEY = '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' 
bucket_name = AWS_ACCESS_KEY_ID.lower() + 'terascripts123'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket('targetdata123', validate=True)
testfile = "test.json"

from boto.s3.key import Key
k = Key(bucket)
k.key = 'Backup_files.json'
k.set_contents_from_filename(testfile)
k.make_public()
