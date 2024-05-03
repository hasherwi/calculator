# calculator
An AWS Calculator Webapp Demo

Editing:
- NotePad++ to GitHub Desktop.

Deployment:
- GitHub Connection to AWS CodeCommit.
- Repository sync to AWS CloudFormation.
- Custom IAM Role for Auth: Trust Policy included, Permissions not yet.

Architecture:
- Public S3 Bucket with an HTML file, pointing to...
- An AWS Lambda with a Function URL.

Observability:
- Amazon CloudWatch.
- Account Level Monitoring (that I'm not going to detail to you).

Todo:
- Major: Support changing the Function URL in the HTML dynamically.
- Consider a simple mode versus complex mode.
- More testing?
- Add S3 Lifecycle Rules.
- Add S3 Server Access Logs.
- Add IAM permissions policy for CFN?
- Can we be more restrictive in IAM?
- Add Lambda Custom Helper to Stack to empty S3 bucket on stack delete?
- Expand S3 Uploader to support multiple files (so eventually less Python can be defined in the CFN template).
- Parameterize more things.
- Support updates to the HTML pushing to AWS.
- Add constraints to the CFN parameters.
- Support no bucketname listed with conditions.
- Add favicon.ico.
- Add robots.txt.
- Include a Route 53 option?
- TLS cert option?
