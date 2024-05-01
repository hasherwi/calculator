# calculator
An AWS Calculator Webapp Demo

Editing:
- NotePad++ to GitHub Desktop.

Deployment:
- GitHub Connection to AWS CodeCommit.
- Repository sync to AWS CloudFormation.
- Custom IAM Role for Auth: Trust Policy included, Permissions not yet.

Architecture:
- Public S3 Bucket.

Observability:
- Amazon CloudWatch.
- Account Level Monitoring (that I'm not going to detail to you).

Todo:
- Consider a simple mode versus complex mode.
- More testing?
- Add S3 Lifecycle Rules.
- Add S3 Server Access Logs.
- Add IAM permissions policy?
- Add Lambda Custom Helper to Stack to empty S3 bucket on stack delete?
- Expand S3 Uploader to support multiple files (so eventually less Python can be defined in the CFN template).
- Throttle the Lambda function.
- Parameterize more things.
- Support updates to the HTML pushing to AWS.
