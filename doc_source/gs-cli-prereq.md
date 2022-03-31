# Prerequisites<a name="gs-cli-prereq"></a>

Follow this procedure to create an Amazon S3 bucket, an Amazon SNS topic, and an IAM role with attached policies\. You can then use the AWS CLI to specify the bucket, topic, and role for AWS Config\.

**Contents**
+ [Creating an Amazon S3 Bucket](#gs-cli-create-s3bucket)
+ [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)
+ [Creating an IAM Role](#gs-cli-create-iamrole)

## Creating an Amazon S3 Bucket<a name="gs-cli-create-s3bucket"></a>

If you already have an Amazon S3 bucket in your account and want to use it, skip this step and go to [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)\.

### Using the S3 console<a name="create-bucket"></a>

**To create a bucket**

1. Open the Amazon S3 console at [https://console\.aws\.amazon\.com/s3/](https://console.aws.amazon.com/s3/)\.

1. Choose **Create bucket**\.

1. In **Bucket name**, enter a DNS\-compliant name for your bucket\.

   The bucket name must:
   + Be unique across all of Amazon S3\.
   + Be between 3 and 63 characters long\.
   + Not contain uppercase characters\.
   + Start with a lowercase letter or number\.

   After you create the bucket, you can't change its name\. Make sure the bucket name you choose is unique across all existing bucket names in Amazon S3\. For more information on bucket naming rules and conventions, see [Bucket restrictions and Limitations](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the *Amazon Simple Storage Service User Guide*\.
**Important**  
Avoid including sensitive information, such as account numbers, in the bucket name\. The bucket name is visible in the URLs that point to the objects in the bucket\.

1. In **Region**, choose the AWS Region where you want the bucket to reside\. 

   Choose a Region close to you to minimize latency and costs and address regulatory requirements\. Objects stored in a Region never leave that Region unless you explicitly transfer them to another Region\. For a list of Amazon S3 AWS Regions, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.

1. In **Bucket settings for Block Public Access**, choose the Block Public Access settings that you want to apply to the bucket\. 

   We recommend that you leave all settings enabled unless you know you need to turn one or more of them off for your use case, such as to host a public website\. Block public access settings that you enable for the bucket will also be enabled for all access points that you create on the bucket\. For more information about blocking public access, see [Using Amazon S3 Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html) in the *Amazon Simple Storage Service User Guide*\.

1. \(Optional\) If you want to enable S3 Object Lock:

   1. Choose **Advanced settings**, and read the message that appears\.
**Important**  
You can only enable S3 Object Lock for a bucket when you create it\. If you enable Object Lock for the bucket, you can't disable it later\. Enabling Object Lock also enables versioning for the bucket\. After you enable Object Lock for the bucket, you must configure the Object Lock settings before any objects in the bucket will be protected\. For more information about configuring protection for objects, see [Configuring S3 Object Lock using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-console.html)\.

   1. If you want to enable Object Lock, enter *enable* in the text box and choose **Confirm**\.

   For more information about the S3 Object Lock feature, see [Locking Objects Using Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html) in the *Amazon Simple Storage Service User Guide*\.

1. Choose **Create bucket**\.

### Using the AWS SDKs<a name="create-bucket-intro"></a>

When you use the AWS SDKs to create a bucket, you must create a client and then use the client to send a request to create a bucket\. As a best practice, you should create your client and bucket in the same AWS Region\. If you don't specify a Region when you create a client or a bucket, Amazon S3 uses the default Region US East \(N\. Virginia\)\. 

To create a client to access a dual\-stack endpoint, you must specify an AWS Region\. For more information, see [Amazon S3 dual\-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/dev/dual-stack-endpoints.html#dual-stack-endpoints-description)\. For a list of available AWS Regions, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *AWS General Reference*\. 

When you create a client, the Region maps to the Region\-specific endpoint\. The client uses this endpoint to communicate with Amazon S3: `s3.<region>.amazonaws.com`\. If your Region launched after March 20, 2019, your client and bucket must be in the same Region\. However, you can use a client in the US East \(N\. Virginia\) Region to create a bucket in any Region that launched before March 20, 2019\. For more information, see [Legacy Endpoints](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html#s3-legacy-endpoints)\.

These AWS SDK code examples perform the following tasks:
+ **Create a client by explicitly specifying an AWS Region** — In the example, the client uses the `s3.us-west-2.amazonaws.com` endpoint to communicate with Amazon S3\. You can specify any AWS Region\. For a list of AWS Regions, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *AWS General Reference*\. 
+ **Send a create bucket request by specifying only a bucket name** — The client sends a request to Amazon S3 to create the bucket in the Region where you created a client\. 
+ **Retrieve information about the location of the bucket** — Amazon S3 stores bucket location information in the *location* subresource that is associated with the bucket\.

------
#### [ Java ]

This example shows how to create an Amazon S3 bucket using the AWS SDK for Java\. For instructions on creating and testing a working sample, see [Testing the Amazon S3 Java Code Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingTheMPJavaAPI.html#TestingJavaSamples)\. 

```
import com.amazonaws.AmazonServiceException;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.CreateBucketRequest;
import com.amazonaws.services.s3.model.GetBucketLocationRequest;

import java.io.IOException;

public class CreateBucket2 {

    public static void main(String[] args) throws IOException {
        Regions clientRegion = Regions.DEFAULT_REGION;
        String bucketName = "*** Bucket name ***";

        try {
            AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                    .withCredentials(new ProfileCredentialsProvider())
                    .withRegion(clientRegion)
                    .build();

            if (!s3Client.doesBucketExistV2(bucketName)) {
                // Because the CreateBucketRequest object doesn't specify a region, the
                // bucket is created in the region specified in the client.
                s3Client.createBucket(new CreateBucketRequest(bucketName));

                // Verify that the bucket was created by retrieving it and checking its location.
                String bucketLocation = s3Client.getBucketLocation(new GetBucketLocationRequest(bucketName));
                System.out.println("Bucket location: " + bucketLocation);
            }
        } catch (AmazonServiceException e) {
            // The call was transmitted successfully, but Amazon S3 couldn't process 
            // it and returned an error response.
            e.printStackTrace();
        } catch (SdkClientException e) {
            // Amazon S3 couldn't be contacted for a response, or the client
            // couldn't parse the response from Amazon S3.
            e.printStackTrace();
        }
    }
}
```

------
#### [ \.NET ]

For information about how to create and test a working sample, see [Running the Amazon S3 \.NET Code Examples](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingTheMPDotNetAPI.html#TestingDotNetApiSamples)\.

**Example**  

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Util;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class CreateBucketTest
    {
        private const string bucketName = "*** bucket name ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 s3Client;
        public static void Main()
        {
            s3Client = new AmazonS3Client(bucketRegion);
            CreateBucketAsync().Wait();
        }

        static async Task CreateBucketAsync()
        {
            try
            {
                if (!(await AmazonS3Util.DoesS3BucketExistAsync(s3Client, bucketName)))
                {
                    var putBucketRequest = new PutBucketRequest
                    {
                        BucketName = bucketName,
                        UseClientRegion = true
                    };

                    PutBucketResponse putBucketResponse = await s3Client.PutBucketAsync(putBucketRequest);
                }
                // Retrieve the bucket location.
                string bucketLocation = await FindBucketLocationAsync(s3Client);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when writing an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when writing an object", e.Message);
            }
        }
        static async Task<string> FindBucketLocationAsync(IAmazonS3 client)
        {
            string bucketLocation;
            var request = new GetBucketLocationRequest()
            {
                BucketName = bucketName
            };
            GetBucketLocationResponse response = await client.GetBucketLocationAsync(request);
            bucketLocation = response.Location.ToString();
            return bucketLocation;
        }
    }
}
```

------
#### [ Ruby ]

For information about how to create and test a working sample, see [Using the AWS SDK for Ruby \- Version 3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingTheMPRubyAPI.html)\. 

**Example**  

```
require "aws-sdk-s3"

# Wraps Amazon S3 bucket actions.
class BucketCreateWrapper
  attr_reader :bucket

  # @param bucket [Aws::S3::Bucket] An Amazon S3 bucket initialized with a name. This is a client-side object until
  #                                 create is called.
  def initialize(bucket)
    @bucket = bucket
  end

  # Creates an Amazon S3 bucket in the specified AWS Region.
  #
  # @param region [String] The Region where the bucket is created.
  # @return [Boolean] True when the bucket is created; otherwise, false.
  def create?(region)
    @bucket.create(create_bucket_configuration: { location_constraint: region })
    true
  rescue Aws::Errors::ServiceError => e
    puts "Couldn't create bucket. Here's why: #{e.message}"
    false
  end

  # Gets the Region where the bucket is located.
  #
  # @return [String] The location of the bucket.
  def location
    if @bucket.nil?
      "None. You must create a bucket before you can get it's location!"
    else
      @bucket.client.get_bucket_location(bucket: @bucket.name).location_constraint
    end
  rescue Aws::Errors::ServiceError => e
    "Couldn't get the location of #{@bucket.name}. Here's why: #{e.message}"
  end
end

def run_demo
  region = "us-west-2"
  wrapper = BucketCreateWrapper.new(Aws::S3::Bucket.new("doc-example-bucket-#{Random.uuid}"))
  return unless wrapper.create?(region)

  puts "Created bucket #{wrapper.bucket.name}."
  puts "Your bucket's region is: #{wrapper.location}"
end

run_demo if $PROGRAM_NAME == __FILE__
```

------

### Using the AWS CLI<a name="creating-bucket-cli"></a>

You can also use the AWS Command Line Interface \(AWS CLI\) to create an S3 bucket\. For more information, see [create\-bucket](https://docs.aws.amazon.com/cli/latest/reference/s3api/create-bucket.html) in the *AWS CLI Command Reference*\.

For information about the AWS CLI, see [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS Command Line Interface User Guide*\. 

**Note**  
You can also use an Amazon S3 bucket from a different account, but you may need to create a policy for the bucket that grants access permissions to AWS Config\. For information on granting permissions to an Amazon S3 bucket, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md), and then go to [Creating an Amazon SNS Topic](#gs-cli-create-snstopic)\.

## Creating an Amazon SNS Topic<a name="gs-cli-create-snstopic"></a>

If you already have an Amazon SNS topic in your account and want to use it, skip this step and go to [Creating an IAM Role](#gs-cli-create-iamrole)\.

### Using the SNS console<a name="create-snstopic"></a>

**To create an Amazon SNS topic**

1. Open the Amazon SNS console at [https://console\.aws\.amazon\.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home)\.

1. Do one of the following:
   + If no topics have ever been created under your AWS account before, read the description of Amazon SNS on the home page\.
   + If topics have been created under your AWS account before, on the navigation panel, choose **Topics**\.

1. On the **Topics** page, choose **Create topic**\.

1. On the **Create topic** page, in the **Details** section, do the following:

   1. For **Type**, choose a topic type \(**Standard** or **FIFO**\)\.

   1. Enter a **Name** for the topic\. For a [FIFO topic](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html), add **\.fifo** to the end of the name\.

   1. \(Optional\) Enter a **Display name** for the topic\.

   1. \(Optional\) For a FIFO topic, you can choose **content\-based message deduplication** to enable default message deduplication\. For more information, see [Message deduplication for FIFO topics](https://docs.aws.amazon.com/sns/latest/dg/fifo-message-dedup.html)\.

1. \(Optional\) Expand the **Encryption** section and do the following\. For more information, see [Encryption at rest](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html)\.

   1. Choose **Enable encryption**\.

   1. Specify the customer master key \(CMK\)\. For more information, see [Key terms](https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms)\.

      For each CMK type, the **Description**, **Account**, and **CMK ARN** are displayed\.
**Important**  
If you aren't the owner of the CMK, or if you log in with an account that doesn't have the `kms:ListAliases` and `kms:DescribeKey` permissions, you won't be able to view information about the CMK on the Amazon SNS console\.  
Ask the owner of the CMK to grant you these permissions\. For more information, see the [AWS KMS API Permissions: Actions and Resources Reference](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) in the *AWS Key Management Service Developer Guide*\.
      + The AWS managed CMK for Amazon SNS **\(Default\) alias/aws/sns** is selected by default\.
**Note**  
Keep the following in mind:  
The first time you use the AWS Management Console to specify the AWS managed CMK for Amazon SNS for a topic, AWS KMS creates the AWS managed CMK for Amazon SNS\.
Alternatively, the first time you use the `Publish` action on a topic with SSE enabled, AWS KMS creates the AWS managed CMK for Amazon SNS\.
      + To use a custom CMK from your AWS account, choose the **Customer master key \(CMK\)** field and then choose the custom CMK from the list\.
**Note**  
For instructions on creating custom CMKs, see [Creating Keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*
      + To use a custom CMK ARN from your AWS account or from another AWS account, enter it into the **Customer master key \(CMK\)** field\.

1. \(Optional\) By default, only the topic owner can publish or subscribe to the topic\. To configure additional access permissions, expand the **Access policy** section\. For more information, see [Identity and access management in Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-authentication-and-access-control.html) and [Example cases for Amazon SNS access control](https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-use-cases.html)\. 
**Note**  
When you create a topic using the console, the default policy uses the `aws:SourceOwner` condition key\. This key is similar to `aws:SourceAccount`\. 

1. \(Optional\) To configure how Amazon SNS retries failed message delivery attempts, expand the **Delivery retry policy \(HTTP/S\)** section\. For more information, see [Amazon SNS message delivery retries](https://docs.aws.amazon.com/sns/latest/dg/sns-message-delivery-retries.html)\.

1. \(Optional\) To configure how Amazon SNS logs the delivery of messages to CloudWatch, expand the **Delivery status logging** section\. For more information, see [Amazon SNS message delivery status](https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html)\.

1. \(Optional\) To add metadata tags to the topic, expand the **Tags** section, enter a **Key** and a **Value** \(optional\) and choose **Add tag**\. For more information, see [Amazon SNS topic tagging](https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html)\.

1. Choose **Create topic**\.

   The topic is created and the ***MyTopic*** page is displayed\.

   The topic's **Name**, **ARN**, \(optional\) **Display name**, and **Topic owner**'s AWS account ID are displayed in the **Details** section\.

1. Copy the topic ARN to the clipboard, for example:

   ```
   arn:aws:sns:us-east-2:123456789012:MyTopic
   ```

**To subscribe an email address to the Amazon SNS topic**

1. Open the Amazon SNS console at [https://console\.aws\.amazon\.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home)\.

1. In the left navigation pane, choose **Subscriptions**\.

1. On the **Subscriptions** page, choose **Create subscription**\.

1. On the **Create subscription** page, in the **Details** section, do the following:

   1. For **Topic ARN**, choose the Amazon Resource Name \(ARN\) of a topic\.

   1. For **Protocol**, choose an endpoint type\.  The available endpoint types are:
      + [HTTP/HTTPS](https://docs.aws.amazon.com/sns/latest/dg/sns-http-https-endpoint-as-subscriber.html)
      + [Email/Email\-JSON](https://docs.aws.amazon.com/sns/latest/dg/sns-email-notifications.html)
      + [Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html)
      + [Amazon SQS](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)
**Note**  
To subscribe to an [SNS FIFO topic](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html), choose this option\.
      + [AWS Lambda](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda-as-subscriber.html)
      + [Platform application endpoint](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html)
      + [SMS](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-phone-number-as-subscriber.html)

   1. For **Endpoint**, enter the endpoint value, such as an email address or the ARN of an Amazon SQS queue\.

   1. Kinesis Data Firehose endpoints only: For **Subscription role ARN**, specify the ARN of the IAM role that you created for writing to Kinesis Data Firehose delivery streams\. For more information, see [Prerequisites for subscribing Kinesis Data Firehose delivery streams to Amazon SNS topics](https://docs.aws.amazon.com/sns/latest/dg/prereqs-kinesis-data-firehose.html)\.

   1. \(Optional\) For Kinesis Data Firehose, Amazon SQS, HTTP/S endpoints, you can also enable raw message delivery\. For more information, see [Amazon SNS raw message delivery](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html)\.

   1. \(Optional\) To configure a filter policy, expand the **Subscription filter policy** section\. For more information, see [Amazon SNS subscription filter policies](https://docs.aws.amazon.com/sns/latest/dg/sns-subscription-filter-policies.html)\.

   1. \(Optional\) To configure a dead\-letter queue for the subscription, expand the **Redrive policy \(dead\-letter queue\)** section\. For more information, see [Amazon SNS dead\-letter queues \(DLQs\)](https://docs.aws.amazon.com/sns/latest/dg/sns-dead-letter-queues.html)\.

   1. Choose **Create subscription**\.

      The console creates the subscription and opens the subscription's **Details** page\.

### Using the AWS SDKs<a name="create-snstopic-intro"></a>

To use an AWS SDK, you must configure it with your credentials\. For more information, see [The shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) in the *AWS SDKs and Tools Reference Guide*\.

The following code examples show how to create an Amazon SNS topic\.

------
#### [ \.NET ]

**AWS SDK for \.NET**  
  

```
        /// <summary>
        /// Creates a new SNS topic using the supplied topic name.
        /// </summary>
        /// <param name="client">The initialized SNS client object used to
        /// create the new topic.</param>
        /// <param name="topicName">A string representing the topic name.</param>
        /// <returns>The Amazon Resource Name (ARN) of the created topic.</returns>
        public static async Task<string> CreateSNSTopicAsync(IAmazonSimpleNotificationService client, string topicName)
        {
            var request = new CreateTopicRequest
            {
                Name = topicName,
            };

            var response = await client.CreateTopicAsync(request);

            return response.TopicArn;
        }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/SNS#code-examples)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/DotNetSDKV3/sns-2010-03-31/CreateTopic) in *AWS SDK for \.NET API Reference*\. 

------
#### [ C\+\+ ]

**SDK for C\+\+**  
  

```
  Aws::SDKOptions options;
  Aws::InitAPI(options);
  {
    Aws::String topic_name = argv[1];
    Aws::SNS::SNSClient sns;

    Aws::SNS::Model::CreateTopicRequest ct_req;
    ct_req.SetName(topic_name);

    auto ct_out = sns.CreateTopic(ct_req);

    if (ct_out.IsSuccess())
    {
      std::cout << "Successfully created topic " << topic_name << std::endl;
    }
    else
    {
      std::cout << "Error creating topic " << topic_name << ":" <<
        ct_out.GetError().GetMessage() << std::endl;
    }
  }

  Aws::ShutdownAPI(options);
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sns#code-examples)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/CreateTopic) in *AWS SDK for C\+\+ API Reference*\. 

------
#### [ Go ]

**SDK for Go V2**  
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/sns/CreateTopic#code-examples)\. 
+  For API details, see [CreateTopic](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sns#Client.CreateTopic) in *AWS SDK for Go API Reference*\. 

------
#### [ Java ]

**SDK for Java 2\.x**  
  

```
    public static String createSNSTopic(SnsClient snsClient, String topicName ) {

        CreateTopicResponse result = null;
        try {
            CreateTopicRequest request = CreateTopicRequest.builder()
                    .name(topicName)
                    .build();

            result = snsClient.createTopic(request);
            return result.topicArn();
        } catch (SnsException e) {

            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sns#readme)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/CreateTopic) in *AWS SDK for Java 2\.x API Reference*\. 

------
#### [ JavaScript ]

**SDK for JavaScript V3**  
Create the client in a separate module and export it\.  

```
import  { SNSClient } from "@aws-sdk/client-sns";
// Set the AWS Region.
const REGION = "REGION"; //e.g. "us-east-1"
// Create SNS service object.
const snsClient = new SNSClient({ region: REGION });
export  { snsClient };
```
Import the SDK and client modules and call the API\.  

```
// Import required AWS SDK clients and commands for Node.js
import {CreateTopicCommand } from "@aws-sdk/client-sns";
import {snsClient } from "./libs/snsClient.js";

// Set the parameters
const params = { Name: "TOPIC_NAME" }; //TOPIC_NAME

const run = async () => {
  try {
    const data = await snsClient.send(new CreateTopicCommand(params));
    console.log("Success.",  data);
    return data; // For unit tests.
  } catch (err) {
    console.log("Error", err.stack);
  }
};
run();
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sns#code-examples)\. 
+  For more information, see [AWS SDK for JavaScript Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/sns-examples-managing-topics.html#sns-examples-managing-topics-createtopic)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-sns/classes/createtopiccommand.html) in *AWS SDK for JavaScript API Reference*\. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
This is prerelease documentation for a feature in preview release\. It is subject to change\.
  

```
suspend fun createSNSTopic(topicName: String): String {

       val request = CreateTopicRequest {
            name = topicName
        }

       SnsClient { region = "us-east-1" }.use { snsClient ->
        val result = snsClient.createTopic(request)
        return result.topicArn.toString()
       }
 }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sns#code-examples)\. 
+  For API details, see [CreateTopic](https://github.com/awslabs/aws-sdk-kotlin#generating-api-documentation) in *AWS SDK for Kotlin API reference*\. 

------
#### [ PHP ]

**SDK for PHP**  
  

```
require 'vendor/autoload.php';

use Aws\Sns\SnsClient; 
use Aws\Exception\AwsException;

/**
 * Create a Simple Notification Service topics in your AWS account at the requested region.
 *
 * This code expects that you have AWS credentials set up per:
 * https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials.html
 */
 
$SnSclient = new SnsClient([
    'profile' => 'default',
    'region' => 'us-east-1',
    'version' => '2010-03-31'
]);

$topicname = 'myTopic';

try {
    $result = $SnSclient->createTopic([
        'Name' => $topicname,
    ]);
    var_dump($result);
} catch (AwsException $e) {
    // output error message if fails
    error_log($e->getMessage());
}
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/sns#code-examples)\. 
+  For more information, see [AWS SDK for PHP Developer Guide](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/sns-examples-managing-topics.html#create-a-topic)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/CreateTopic) in *AWS SDK for PHP API Reference*\. 

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
  

```
class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""
    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/sns#code-examples)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/CreateTopic) in *AWS SDK for Python \(Boto3\) API Reference*\. 

------
#### [ Ruby ]

**SDK for Ruby**  
  

```
require 'aws-sdk-sns'  # v2: require 'aws-sdk'

def topic_created?(sns_client, topic_name)

sns_client.create_topic(name: topic_name)
rescue StandardError => e
  puts "Error while creating the topic named '#{topic_name}': #{e.message}"
end

# Full example call:
def run_me
  topic_name = 'TOPIC_NAME'
  region = 'REGION'

  sns_client = Aws::SNS::Client.new(region: region)

  puts "Creating the topic '#{topic_name}'..."

  if topic_created?(sns_client, topic_name)
    puts 'The topic was created.'
  else
    puts 'The topic was not created. Stopping program.'
    exit 1
  end
end

run_me if $PROGRAM_NAME == __FILE__
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/sns#code-examples)\. 
+  For more information, see [AWS SDK for Ruby Developer Guide](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/sns-example-create-topic.html)\. 
+  For API details, see [CreateTopic](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/CreateTopic) in *AWS SDK for Ruby API Reference*\. 

------
#### [ Rust ]

**SDK for Rust**  
This documentation is for an SDK in preview release\. The SDK is subject to change and should not be used in production\.
  

```
async fn make_topic(client: &Client, topic_name: &str) -> Result<(), Error> {
    let resp = client.create_topic().name(topic_name).send().await?;

    println!(
        "Created topic with ARN: {}",
        resp.topic_arn().unwrap_or_default()
    );

    Ok(())
}
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rust_dev_preview/sns#code-examples)\. 
+  For API details, see [CreateTopic](https://docs.rs/releases/search?query=aws-sdk) in *AWS SDK for Rust API reference*\. 

------

### Using the AWS CLI<a name="creating-snstopic-cli"></a>

You can also use the AWS Command Line Interface \(AWS CLI\) to create an an Amazon SNS topic\. For more information, see [create\-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html) in the *AWS CLI Command Reference*\.

For information about the AWS CLI, see [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS Command Line Interface User Guide*\. 

**Note**  
You can also use an Amazon SNS topic in a different account, but in that case you might need to create a policy for topic that grants access permissions to AWS Config\. For information on granting permissions to an Amazon SNS topic, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md) and then go to [Creating an IAM Role](#gs-cli-create-iamrole)\.

## Creating an IAM Role<a name="gs-cli-create-iamrole"></a>

### Using the IAM console<a name="create-iamrole"></a>

You can use the IAM console to create an IAM role that grants AWS Config permissions to access your Amazon S3 bucket, access your Amazon SNS topic, and get configuration details for supported AWS resources\. When you use the console to create an IAM role, AWS Config automatically attaches the required permissions to the role for you\. 

**To create a role for an AWS service**

1. Sign in to the AWS Management Console and open the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\.

1. In the navigation pane of the IAM console, choose **Roles**, and then choose **Create role**\.

1. For **Select trusted entity**, choose **AWS service**\. 

1. Choose the use case you want for AWS Config: **Config \- Customizable**, **Config \- Organizations**, **Config**, or **Config \- Conformance Packs**\. Then, choose **Next**\.

1. On the **Name, review, and create** page, review the details about your role, and choose **Create Role**\.

### Using the AWS SDKs<a name="create-iamrole-intro"></a>

To use an AWS SDK, you must configure it with your credentials\. For more information, see [The shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/creds-config-files.html) in the *AWS SDKs and Tools Reference Guide*\.

The following code examples show how to create an IAM role\.

------
#### [ Java ]

**SDK for Java 2\.x**  
  

```
    public static String createIAMRole(IamClient iam, String rolename, String fileLocation ) {

        try {

            JSONObject jsonObject = (JSONObject) readJsonSimpleDemo(fileLocation);

            CreateRoleRequest request = CreateRoleRequest.builder()
                    .roleName(rolename)
                    .assumeRolePolicyDocument(jsonObject.toJSONString())
                    .description("Created using the AWS SDK for Java")
                    .build();

            CreateRoleResponse response = iam.createRole(request);
            System.out.println("The ARN of the role is "+response.role().arn());

        } catch (IamException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "";
    }

    public static Object readJsonSimpleDemo(String filename) throws Exception {
        FileReader reader = new FileReader(filename);
        JSONParser jsonParser = new JSONParser();
        return jsonParser.parse(reader);
    }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/iam#readme)\. 
+  For API details, see [CreateRole](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/CreateRole) in *AWS SDK for Java 2\.x API Reference*\. 

------
#### [ JavaScript ]

**SDK for JavaScript V3**  
Create the client\.  

```
import { IAMClient } from "@aws-sdk/client-iam";
// Set the AWS Region.
const REGION = "REGION"; // For example, "us-east-1".
// Create an IAM service client object.
const iamClient = new IAMClient({ region: REGION });
export { iamClient };
```
Create the role\.  

```
// Import required AWS SDK clients and commands for Node.js.
import { iamClient } from "./libs/iamClient.js";
import { CreateRoleCommand } from "@aws-sdk/client-iam";

// Sample assume role policy JSON.
const role_json = {
    Version: "2012-10-17",
    Statement: [
        {
            Effect: "Allow",
            Principal: {
                AWS: "USER_ARN", // The ARN of the user.
            },
            Action: "sts:AssumeRole",
        },
    ],
};
// Stringify the assume role policy JSON.
const myJson = JSON.stringify(role_json);

// Set the parameters.
const params = {
    AssumeRolePolicyDocument: myJson,
    Path: "/",
    RoleName: "ROLE_NAME"
};

const run = async () => {
    try {
        const data = await iamClient.send(new CreateRoleCommand(params));
        console.log("Success. Role created. Role Arn: ", data.Role.RoleName);
        } catch (err) {
            console.log("Error", err);
        }
};
run();
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples)\. 
+  For API details, see [CreateRole](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-iam/classes/createrolecommand.html) in *AWS SDK for JavaScript API Reference*\. 

------
#### [ PHP ]

**SDK for PHP**  
  

```
$uuid = uniqid();
$service = new IamService();

$assumeRolePolicyDocument = "{
                \"Version\": \"2012-10-17\",
                \"Statement\": [{
                    \"Effect\": \"Allow\",
                    \"Principal\": {\"AWS\": \"{$user['Arn']}\"},
                    \"Action\": \"sts:AssumeRole\"
                }]
            }";
$assumeRoleRole = $service->createRole("iam_demo_role_$uuid", $assumeRolePolicyDocument);
echo "Created role: {$assumeRoleRole['RoleName']}\n";

    /**
     * @param string $roleName
     * @param string $rolePolicyDocument
     * @return array
     * @throws AwsException
     */
    public function createRole(string $roleName, string $rolePolicyDocument)
    {
        $result = $this->customWaiter(function () use ($roleName, $rolePolicyDocument) {
            return $this->iamClient->createRole([
                'AssumeRolePolicyDocument' => $rolePolicyDocument,
                'RoleName' => $roleName,
            ]);
        });
        return $result['Role'];
    }
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/iam/iam_basics#code-examples)\. 
+  For API details, see [CreateRole](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/CreateRole) in *AWS SDK for PHP API Reference*\. 

------
#### [ Python ]

**SDK for Python \(Boto3\)**  
  

```
def create_role(role_name, allowed_services):
    """
    Creates a role that lets a list of specified services assume the role.

    :param role_name: The name of the role.
    :param allowed_services: The services that can assume the role.
    :return: The newly created role.
    """
    trust_policy = {
        'Version': '2012-10-17',
        'Statement': [{
                'Effect': 'Allow',
                'Principal': {'Service': service},
                'Action': 'sts:AssumeRole'
            } for service in allowed_services
        ]
    }

    try:
        role = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy))
        logger.info("Created role %s.", role.name)
    except ClientError:
        logger.exception("Couldn't create role %s.", role_name)
        raise
    else:
        return role
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam/iam_basics#code-examples)\. 
+  For API details, see [CreateRole](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/CreateRole) in *AWS SDK for Python \(Boto3\) API Reference*\. 

------
#### [ Ruby ]

**SDK for Ruby**  
  

```
  # Creates a role that can be assumed by a user.
  #
  # @param role_name [String] The name to give the role.
  # @param user [Aws::IAM::User] The user who is granted permission to assume the role.
  # @return [Aws::IAM::Role] The newly created role.
  def create_role(role_name, user)
    role = @iam_resource.create_role(
      role_name: role_name,
      assume_role_policy_document: {
        Version: "2012-10-17",
        Statement: [{
          Effect: "Allow",
          Principal: {'AWS': user.arn},
          Action: "sts:AssumeRole"
        }]
      }.to_json)
    puts("Created role #{role.name}.")
  rescue Aws::Errors::ServiceError => e
    puts("Couldn't create a role for the demo. Here's why: ")
    puts("\t#{e.code}: #{e.message}")
    raise
  else
    role
  end
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/iam#code-examples)\. 
+  For API details, see [CreateRole](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/CreateRole) in *AWS SDK for Ruby API Reference*\. 

------
#### [ Rust ]

**SDK for Rust**  
This documentation is for an SDK in preview release\. The SDK is subject to change and should not be used in production\.
  

```
async fn make_role(client: &Client, policy_file: &str, name: &str) -> Result<(), Error> {
    // Read policy doc from file as a string
    let doc = fs::read_to_string(policy_file).expect("Unable to read file");

    let resp = client
        .create_role()
        .assume_role_policy_document(doc)
        .role_name(name)
        .send()
        .await?;

    println!(
        "Created role with ARN {}",
        resp.role().unwrap().arn().unwrap()
    );

    Ok(())
}
```
+  Find instructions and more code on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rust_dev_preview/iam#code-examples)\. 
+  For API details, see [CreateRole](https://docs.rs/releases/search?query=aws-sdk) in *AWS SDK for Rust API reference*\. 

------

### Using the AWS CLI<a name="creating-iamrole-cli"></a>

You can also use the AWS Command Line Interface \(AWS CLI\) to create an an Amazon SNS topic\. For more information, see [create\-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) in the *AWS CLI Command Reference*\. You can then attach a policy to the role with the [attach\-role\-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/attach-role-policy.html) command\.

For information about the AWS CLI, see [What is the AWS Command Line Interface?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS Command Line Interface User Guide*\. 