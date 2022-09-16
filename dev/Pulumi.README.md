# Pulumi Service for development

This is a README detailing work associated with this environement. I will test deploying an app, build containers, etc.

A development environment to work out the kinks.

To review all resources by the Dev Environment Tag use the following command:

```bash
$ aws resourcegroupstaggingapi get-resources --tag-filters "Key=Environment,Values=Dev" --output table
```