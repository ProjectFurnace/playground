![Furnace AWS Example](https://ignite-the-furnace.surge.sh/assets/diagrams/furnace_illustration_aws.svg)

# Multicloud Example

A sample stack that can be deployed to any supported platform without changing any code. 

## Sources
- Active Connector (Salesforce)

## Sinks
Sink will change depending on the platform this Stack is deployed to:
- (GCP) Firestore
- (AWS) DocumentDB
- (Azure) Storage Table

## Modules
- enrc-flatten 
- passthrough 
- tablesink

---

## Installation

### Prerequisites

1. An ignited furnace running on any supported platform.  Follow the [Getting Started Guide](https://docs.furnace.org/core/basics/getting-started) if you don't already have one.
2. A Salesforce account, you'll need your Login URL, Username, Password and SecurityToken 

### Main Install

1. Run `furnace new {stackname}` to create a new stack eg `furnace new multicloud`
2. Clone this repository `git clone https://github.com/ProjectFurnace/playground.git`
3. Copy the files in the `multicloud-example` over to your new stack `cp -r playground/multicloud-example/* multicloud/`
4.
5. Add the files to git `git add .`
6. Commit the new files `git commit -am 'Initial commit'`
7. Push the files to your git repo `git push origin master`

