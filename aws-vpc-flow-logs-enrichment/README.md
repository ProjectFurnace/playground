![Furnace AWS Example](https://ignite-the-furnace.surge.sh/assets/diagrams/furnace_illustration_aws.svg)

# AWS VPC FlowLogs Security Example Stack

A sample stack to consume messages from AWS VPC Flow Logs, enrich them with security focused information and store them in ElasticSearch.

## Sources
- AWS VPC Flow Logs

## Sinks
- ElasticSearch

## Modules
- aws-vpcfl
- aws-lookup-sg
- lookup-geo
- lookup-protocol
- lookup-port
- enrc-flatten

## Installation

### Prerequisites

1. An ignited furnace running on AWS.  Follow the [Getting Started Guide](https://docs.furnace.org/core/basics/getting-started) if you don't already have one.
2. [VPC Flow Logs set up and logging to a Cloud Watch Log Group](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-cwl.html) 

### Main Install

1. Run `furnace new {stackname}` to create a new stack eg `furnace new aws-vpcfl`
2. Clone this repository `git clone https://github.com/ProjectFurnace/playground.git`
3. Copy the files in the `aws-vpc-flow-logs-enrichment` over to your new stack `cp -r playground/aws-vpc-flow-logs-enrichment/* aws-vpcfl/`
4. Add the files to git `git add .`
5. Commit the new files `git commit -am 'Initial commit'`
6. Push the files to your git repo `git push origin master`

### Hooking up the logs

Once the stack has built you will need to stream the VPC Flow Logs from Cloud Watch to the Tap.

1. Follow the steps outlined here [https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html) to add a subscription to the Source.  You'll want to follow the steps for "Creating a subscription to Kinesis" 
2. For the `Subscription Filter` you will want to use something like `[version, account_id, interface_id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, log_status]`


After a while you should start to see logs being indexed in the Elastic Search instance that was created.

### Removing the Stack

To remove the stack run `furnace destroy` from the root of the Stack folder. 
