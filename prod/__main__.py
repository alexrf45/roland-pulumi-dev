"""An AWS Python Pulumi program"""

import pulumi


# # Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('prod')

# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

# open template readme and read contents into stack output
with open('Pulumi.README.md') as f:
    pulumi.export('readme', f.read())