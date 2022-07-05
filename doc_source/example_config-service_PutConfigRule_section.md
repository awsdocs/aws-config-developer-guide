# Put an AWS Config rule using an AWS SDK<a name="example_config-service_PutConfigRule_section"></a>

The following code example shows how to put an AWS Config rule\.

**Note**  
The source code for these examples is in the [AWS Code Examples GitHub repository](https://github.com/awsdocs/aws-doc-sdk-examples)\. Have feedback on a code example? [Create an Issue](https://github.com/awsdocs/aws-doc-sdk-examples/issues/new/choose) in the code examples repo\. 

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
 To learn how to set up and run this example, see [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/config#code-examples)\. 
  

```
class ConfigWrapper:
    """
    Encapsulates AWS Config functions.
    """
    def __init__(self, config_client):
        """
        :param config_client: A Boto3 AWS Config client.
        """
        self.config_client = config_client

    def put_config_rule(self, rule_name):
        """
        Sets a configuration rule that prohibits making Amazon S3 buckets publicly
        readable.

        :param rule_name: The name to give the rule.
        """
        try:
            self.config_client.put_config_rule(
                ConfigRule={
                    'ConfigRuleName': rule_name,
                    'Description': 'S3 Public Read Prohibited Bucket Rule',
                    'Scope': {
                        'ComplianceResourceTypes': [
                            'AWS::S3::Bucket',
                        ],
                    },
                    'Source': {
                        'Owner': 'AWS',
                        'SourceIdentifier': 'S3_BUCKET_PUBLIC_READ_PROHIBITED',
                    },
                    'InputParameters': '{}',
                    'ConfigRuleState': 'ACTIVE'
                }
            )
            logger.info("Created configuration rule %s.", rule_name)
        except ClientError:
            logger.exception("Couldn't create configuration rule %s.", rule_name)
            raise
```
+  For API details, see [PutConfigRule](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/PutConfigRule) in *AWS SDK for Python \(Boto3\) API Reference*\. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Config with an AWS SDK](sdk-general-information-section.md)\. This topic also includes information about getting started and details about previous SDK versions\.