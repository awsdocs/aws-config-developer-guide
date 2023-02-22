# Custom Conformance Pack<a name="custom-conformance-pack"></a>

A custom conformance pack is a unique collection of AWS Config rules and remediation actions that you can deploy together in an account and an AWS Region, or across an organization in AWS Organizations\.

To make a custom conformance pack, follow the steps in the following **Customizing the template **section to author a YAML file that contains the list of [AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) or [AWS Config Custom Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) that you want to work with\.

**Note**  
**AWS Config Managed Rules**  
AWS Config Managed rules are predefined rules owned by AWS Config\.  
**AWS Config Custom Rules**  
AWS Config Custom Rules are rules that you create from scratch\. There are two ways to create AWS Config custom rules: with Lambda functions \([AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-function)\) and with Guard \([Guard GitHub Repository](https://github.com/aws-cloudformation/cloudformation-guard)\), a policy\-as\-code language\. AWS Config custom rules created with AWS Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules*\.

## Customizing the template<a name="create-yaml-file.title"></a>

 **Creating your YAML file** 

To create a YAML file, open a text editor and save the file as *\.yaml*\. 

**Note**  
Your file will contain a **Parameters** and **Resources** section\.

** Parameters**

The `Parameters` section in your YAML file is for the rule parameters for the set of AWS Config rules that you will add later in the `Resources` section\. Create the `Parameters` section by copying and pasting the following code block into your YAML file, customizing it as needed and repeating for each rule parameter\.

```
Parameters:    
    NameOfRuleParamNameOfRuleParameter: 
        Default: Parameter value
        Type: Type    
    ...
```

For example:

```
Parameters:
    IamPasswordPolicyParamMinimumPasswordLength:
        Default: '14'
        Type: String
```

**Note**  
When selecting the AWS Config Rules to build your custom conformance pack, check you have the resources provisioned within your account that will be evaluated for the AWS Config Rules\.

1. The first line in the parameter section after `Parameters:` is a concatenated string of *NameOfRule* \+ Param \+ *NameOfRuleParameter*\.

   1. Replace `NameOfRule` with a consistent name that you create for the rule\. For example, that could be **IamPasswordPolicy** for the **iam\-password\-policy **rule\.

   1. Type `Param`\.

   1. Then, replace `NameOfRuleParameter` with the name of the rule parameter for your specific rule\. For AWS Config Managed Rules, the name of the rule parameter is located in the [ List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) \(for example, **MinimumPasswordLength** is a name of a rule parameter for the **iam\-password\-policy** rule\)\. For AWS Config Custom Rules, the name of the rule parameter is the name that you chose when you created the rule\.

1. If you are using an AWS Config Managed Rule, find the appropriate AWS Config rule in the list of managed rules so you'll know the accepted values for `Default` and `Type` for your particular rule\. For AWS Config Custom Rules, use the values you selected when creating your rule\.
**Note**  
For each parameter, `Type` must be specified\. `Type` can be one of "String", "int", "double", "CSV", "boolean" and "StringMap"\.

** Resources**

The `Resources` section lists the rules that are being added to your Custom Conformance Pack\. Add the following `Resources` block directly beneath your `Parameters` section, customizing it as needed and repeating for each rule\. For more information on the specifications, see [AWS::Config::ConfigRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#aws-resource-config-configrule-syntax)\.

```
Resources:
     NameOfRule:
        Properties:
            ConfigRuleName: ActualConfigRuleName  
            InputParameters:
                NameOfRuleParameter: NameOfRuleParamNameOfRuleParameter
            Source:
                Owner: Owner
                SourceIdentifier: SOURCE_IDENTIFIER
        Type: AWS::Config::ConfigRule
     ...
```

For example:

```
Resources:
    IamPasswordPolicy:
        Properties:
            ConfigRuleName: iam-password-policy
            InputParameters:
                MinimumPasswordLength: IamPasswordPolicyParamMinimumPasswordLength
            Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
        Type: AWS::Config::ConfigRule
```

**Note**  
When selecting the AWS Config rules to build your custom conformance pack, check that you have the resources that will be evaluated for the AWS Config rules provisioned within your account\. For more information, see [Supported Resource Types](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html)\.

1. Replace `NameOfRule` with the same name you created in the `Parameters` section\. 

1. For AWS Config Managed Rules, replace `ActualConfigRuleName` with the title of the appropriate rule page on the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)\. For AWS Config Custom Rules, use the Config Rule name you chose at the time of the rule's creation\. 

1. Replace `NameOfRuleParameter` with the same name you used in the `Parameters` section\. After the colon, copy and paste the same concatenated string of *NameOfRule* \+ Param \+ *NameOfRuleParameter* that you created in `Parameters` section\.

1. Change `Owner` to the appropriate value\.
**Note**  
**AWS Config Managed Rules**  
For AWS Config Managed Rules, the value for `Owner` will be `AWS`\.  
**AWS Config Custom Rules**  
For AWS Config custom rules created with Guard, the value for `Owner` will be `CUSTOM_POLICY`\. For AWS Config custom rules created with Lambda, the value for `Owner` will be `CUSTOM_LAMBDA`\.

1. Change `SOURCE_IDENTIFIER` to the appropriate value\.
**Note**  
**AWS Config Managed Rules**  
For AWS Config Managed Rules, copy the identifier by following the link from the rule you select from the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) \(for example, the source identifier for the **access\-keys\-rotated** rule is **ACCESS\_KEYS\_ROTATED**\)\.   
**AWS Config Custom Rules**  
For AWS Config custom rules created with Lambda, the `SourceIdentifier` is the Amazon Resource Name \(ARN\) of the rule's AWS Lambda function, such as `arn:aws:lambda:us-east-2:123456789012:function:ActualConfigRuleName`\. For AWS Config custom rules created with Guard, this field is not needed\.

Altogether, your filled out custom conformance pack should begin to look similar to the following, which is an example using these AWS Config Managed Rules: **iam\-password\-policy**, **access\-keys\-rotated**, and **iam\-user\-unused\-credentials\-check**\.

```
Parameters:
    IamPasswordPolicyParamMinimumPasswordLength:
        Default: '14'
        Type: String
    AccessKeysRotatedParamMaxAccessKeyAge:
        Default: '90'
        Type: String
    IamUserUnusedCredentialsCheckParamMaxCredentialUsageAge:
        Default: '45'
        Type: String
Resources:
    IamPasswordPolicy:
        Properties:
            ConfigRuleName: iam-password-policy
            InputParameters:
                MinimumPasswordLength: IamPasswordPolicyParamMinimumPasswordLength
            Source:
                Owner: AWS
                SourceIdentifier: IAM_PASSWORD_POLICY
        Type: AWS::Config::ConfigRule    
    AccessKeysRotated:
        Properties:
            ConfigRuleName: access-keys-rotated
            InputParameters:
                maxAccessKeyAge: AccessKeysRotatedParamMaxAccessKeyAge
            Source:
                Owner: AWS
                SourceIdentifier: ACCESS_KEYS_ROTATED
        Type: AWS::Config::ConfigRule
    IamUserUnusedCredentialsCheck:
        Properties:
            ConfigRuleName: iam-user-unused-credentials-check
            InputParameters:
                maxCredentialUsageAge: IamUserUnusedCredentialsCheckParamMaxCredentialUsageAge
            Source:
                Owner: AWS
                SourceIdentifier: IAM_USER_UNUSED_CREDENTIALS_CHECK
        Type: AWS::Config::ConfigRule
```

## Deploying your custom conformance pack<a name="deploy-custom-cpack.title"></a>

To deploy your custom conformance pack, see [Deploying a Conformance Pack Using  the AWS Config Console](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-console.html) and [Deploying a Conformance Pack Using the AWS Config Command Line Interface](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-cli.html)\.  