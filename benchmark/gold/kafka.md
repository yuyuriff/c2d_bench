# AK 4.3.X

## Navigation

- [AK 4.3.X](#index)
  - [Getting Started](#getting-started)
    - [Introduction](#getting-started-introduction)
    - [Use Cases](#getting-started-uses)
    - [Quick Start](#getting-started-quickstart)
    - [Ecosystem](#getting-started-ecosystem)
    - [Upgrading](#getting-started-upgrade)
    - [KRaft vs ZooKeeper](#getting-started-zk2kraft)
    - [Compatibility](#getting-started-compatibility)
    - [Docker](#getting-started-docker)
  - [API](#apis)
  - [Configuration](#configuration)
    - [Broker Configs](#configuration-broker-configs)
    - [Topic Configs](#configuration-topic-configs)
    - [Group Configs](#configuration-group-configs)
    - [Producer Configs](#configuration-producer-configs)
    - [Consumer and Share Consumer Configs](#configuration-consumer-configs)
    - [Kafka Connect Configs](#configuration-kafka-connect-configs)
    - [Kafka Streams Configs](#configuration-kafka-streams-configs)
    - [Admin Configs](#configuration-admin-configs)
    - [MirrorMaker Configs](#configuration-mirrormaker-configs)
    - [System Properties](#configuration-system-properties)
    - [Tiered Storage Configs](#configuration-tiered-storage-configs)
    - [Configuration Providers](#configuration-configuration-providers)
  - [Design](#design)
    - [Design](#design-design)
    - [Protocol](#design-protocol)
  - [Implementation](#implementation)
    - [Network Layer](#implementation-network-layer)
    - [Messages](#implementation-messages)
    - [Message Format](#implementation-message-format)
    - [Log](#implementation-log)
    - [Distribution](#implementation-distribution)
  - [Operations](#operations)
    - [Basic Kafka Operations](#operations-basic-kafka-operations)
    - [Datacenters](#operations-datacenters)
    - [Geo-Replication (Cross-Cluster Data Mirroring)](#operations-geo-replication-cross-cluster-data-mirroring)
    - [Multi-Tenancy](#operations-multi-tenancy)
    - [Java Version](#operations-java-version)
    - [Hardware and OS](#operations-hardware-and-os)
    - [Monitoring](#operations-monitoring)
    - [KRaft](#operations-kraft)
    - [Tiered Storage](#operations-tiered-storage)
    - [Consumer Rebalance Protocol](#operations-consumer-rebalance-protocol)
    - [Transaction Protocol](#operations-transaction-protocol)
    - [Eligible Leader Replicas](#operations-eligible-leader-replicas)
  - [Security](#security)
    - [Security Overview](#security-security-overview)
    - [Listener Configuration](#security-listener-configuration)
    - [Encryption and Authentication using SSL](#security-encryption-and-authentication-using-ssl)
    - [Authentication using SASL](#security-authentication-using-sasl)
    - [Authorization and ACLs](#security-authorization-and-acls)
    - [Incorporating Security Features in a Running Cluster](#security-incorporating-security-features-in-a-running-cluster)
  - [Kafka Connect](#kafka-connect)
    - [Overview](#kafka-connect-overview)
    - [User Guide](#kafka-connect-user-guide)
    - [Connector Development Guide](#kafka-connect-connector-development-guide)
    - [Administration](#kafka-connect-administration)
  - [Kafka Streams](#streams)
    - [Introduction](#streams-introduction)
    - [Quick Start](#streams-quickstart)
    - [Write a streams app](#streams-tutorial)
    - [Core Concepts](#streams-core-concepts)
    - [Architecture](#streams-architecture)
    - [Upgrade Guide](#streams-upgrade-guide)
    - [Streams Developer Guide](#streams-developer-guide)
      - [Writing a Streams Application](#streams-developer-guide-write-streams-app)
      - [Configuring a Streams Application](#streams-developer-guide-config-streams)
      - [Streams DSL](#streams-developer-guide-dsl-api)
      - [Processor API](#streams-developer-guide-processor-api)
      - [Naming Operators in a Streams DSL application](#streams-developer-guide-dsl-topology-naming)
      - [Data Types and Serialization](#streams-developer-guide-datatypes)
      - [Testing a Streams Application](#streams-developer-guide-testing)
      - [Interactive Queries](#streams-developer-guide-interactive-queries)
      - [Memory Management](#streams-developer-guide-memory-mgmt)
      - [Running Streams Applications](#streams-developer-guide-running-app)
      - [Managing Streams Application Topics](#streams-developer-guide-manage-topics)
      - [Streams Security](#streams-developer-guide-security)
      - [Application Reset Tool](#streams-developer-guide-app-reset-tool)
      - [Streams Rebalance Protocol](#streams-developer-guide-streams-rebalance-protocol)
      - [Kafka Streams Groups Tool](#streams-developer-guide-kafka-streams-group-sh)
      - [Migrating from Streams Scala to Java API](#streams-developer-guide-scala-migration)

<a id="index"></a>

---

<a id="getting-started"></a>

<a id="getting-started--getting-started"></a>

# Getting Started

This section provides an overview of what Kafka is, why it is useful, and how to get started using it.

---

<a id="getting-started--introduction"></a>

##### [Introduction](#getting-started-introduction)

<a id="getting-started--use-cases"></a>

##### [Use Cases](#getting-started-uses)

<a id="getting-started--quick-start"></a>

##### [Quick Start](#getting-started-quickstart)

<a id="getting-started--ecosystem"></a>

##### [Ecosystem](#getting-started-ecosystem)

<a id="getting-started--upgrading"></a>

##### [Upgrading](#getting-started-upgrade)

<a id="getting-started--kraft-vs-zookeeper"></a>

##### [KRaft vs ZooKeeper](#getting-started-zk2kraft)

<a id="getting-started--compatibility"></a>

##### [Compatibility](#getting-started-compatibility)

<a id="getting-started--docker"></a>

##### [Docker](#getting-started-docker)

---

<a id="getting-started-introduction"></a>

<a id="getting-started-introduction--introduction"></a>

# Introduction

<a id="getting-started-introduction--what-is-event-streaming"></a>

## What is event streaming?

Event streaming is the digital equivalent of the human body’s central nervous system. It is the technological foundation for the ‘always-on’ world where businesses are increasingly software-defined and automated, and where the user of software is more software.

Technically speaking, event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed. Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time.

<a id="getting-started-introduction--what-can-i-use-event-streaming-for"></a>

## What can I use event streaming for?

Event streaming is applied to a [wide variety of use cases](https://kafka.apache.org/powered-by) across a plethora of industries and organizations. Its many examples include:

- To process payments and financial transactions in real-time, such as in stock exchanges, banks, and insurances.
- To track and monitor cars, trucks, fleets, and shipments in real-time, such as in logistics and the automotive industry.
- To continuously capture and analyze sensor data from IoT devices or other equipment, such as in factories and wind parks.
- To collect and immediately react to customer interactions and orders, such as in retail, the hotel and travel industry, and mobile applications.
- To monitor patients in hospital care and predict changes in condition to ensure timely treatment in emergencies.
- To connect, store, and make available data produced by different divisions of a company.
- To serve as the foundation for data platforms, event-driven architectures, and microservices.

<a id="getting-started-introduction--apache-kafka-is-an-event-streaming-platform-what-does-that-mean"></a>
<a id="getting-started-introduction--apache-kafka-is-an-event-streaming-platform.-what-does-that-mean"></a>

## Apache Kafka® is an event streaming platform. What does that mean?

Kafka combines three key capabilities so you can implement [your use cases](https://kafka.apache.org/powered-by) for event streaming end-to-end with a single battle-tested solution:

1. To **publish** (write) and **subscribe to** (read) streams of events, including continuous import/export of your data from other systems.
2. To **store** streams of events durably and reliably for as long as you want.
3. To **process** streams of events as they occur or retrospectively.

And all this functionality is provided in a distributed, highly scalable, elastic, fault-tolerant, and secure manner. Kafka can be deployed on bare-metal hardware, virtual machines, and containers, and on-premises as well as in the cloud. You can choose between self-managing your Kafka environments and using fully managed services offered by a variety of vendors.

<a id="getting-started-introduction--how-does-kafka-work-in-a-nutshell"></a>

## How does Kafka work in a nutshell?

Kafka is a distributed system consisting of **servers** and **clients** that communicate via a high-performance [TCP network protocol](https://kafka.apache.org/protocol.html). It can be deployed on bare-metal hardware, virtual machines, and containers in on-premise as well as cloud environments.

**Servers** : Kafka is run as a cluster of one or more servers that can span multiple datacenters or cloud regions. Some of these servers form the storage layer, called the brokers. Other servers run [Kafka Connect](https://kafka.apache.org/documentation/#connect) to continuously import and export data as event streams to integrate Kafka with your existing systems such as relational databases as well as other Kafka clusters. To let you implement mission-critical use cases, a Kafka cluster is highly scalable and fault-tolerant: if any of its servers fails, the other servers will take over their work to ensure continuous operations without any data loss.

**Clients** : They allow you to write distributed applications and microservices that read, write, and process streams of events in parallel, at scale, and in a fault-tolerant manner even in the case of network problems or machine failures. Kafka ships with some such clients included, which are augmented by [dozens of clients](https://cwiki.apache.org/confluence/x/3gDVAQ) provided by the Kafka community: clients are available for Java and Scala including the higher-level [Kafka Streams](https://kafka.apache.org/documentation/streams/) library, for Go, Python, C/C++, and many other programming languages as well as REST APIs.

<a id="getting-started-introduction--main-concepts-and-terminology"></a>

## Main Concepts and Terminology

An **event** records the fact that “something happened” in the world or in your business. It is also called record or message in the documentation. When you read or write data to Kafka, you do this in the form of events. Conceptually, an event has a key, value, timestamp, and optional metadata headers. Here’s an example event:

- Event key: “Alice”
- Event value: “Made a payment of $200 to Bob”
- Event timestamp: “Jun. 25, 2020 at 2:06 p.m.”

**Producers** are those client applications that publish (write) events to Kafka, and **consumers** are those that subscribe to (read and process) these events. In Kafka, producers and consumers are fully decoupled and agnostic of each other, which is a key design element to achieve the high scalability that Kafka is known for. For example, producers never need to wait for consumers. Kafka provides various [guarantees](https://kafka.apache.org/documentation/#semantics) such as the ability to process events exactly-once.

Events are organized and durably stored in **topics**. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder. An example topic name could be “payments”. Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. Events in a topic can be read as often as needed-unlike traditional messaging systems, events are not deleted after consumption. Instead, you define for how long Kafka should retain your events through a per-topic configuration setting, after which old events will be discarded. Kafka’s performance is effectively constant with respect to data size, so storing data for a long time is perfectly fine.

Topics are **partitioned** , meaning a topic is spread over a number of “buckets” located on different Kafka brokers. This distributed placement of your data is very important for scalability because it allows client applications to both read and write the data from/to many brokers at the same time. When a new event is published to a topic, it is actually appended to one of the topic’s partitions. Events with the same event key (e.g., a customer or vehicle ID) are written to the same partition, and Kafka [guarantees](https://kafka.apache.org/documentation/#semantics) that any consumer of a given topic-partition will always read that partition’s events in exactly the same order as they were written.

To make your data fault-tolerant and highly-available, every topic can be **replicated** , even across geo-regions or datacenters, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i.e., there will always be three copies of your data. This replication is performed at the level of topic-partitions.

This primer should be sufficient for an introduction. The [Design](https://kafka.apache.org/documentation/#design) section of the documentation explains Kafka’s various concepts in full detail, if you are interested.

<a id="getting-started-introduction--kafka-apis"></a>

## Kafka APIs

In addition to command line tooling for management and administration tasks, Kafka has five core APIs for Java and Scala:

- The [Admin API](https://kafka.apache.org/documentation.html#adminapi) to manage and inspect topics, brokers, and other Kafka objects.
- The [Producer API](https://kafka.apache.org/documentation.html#producerapi) to publish (write) a stream of events to one or more Kafka topics.
- The [Consumer API](https://kafka.apache.org/documentation.html#consumerapi) to subscribe to (read) one or more topics and to process the stream of events produced to them.
- The [Kafka Streams API](https://kafka.apache.org/documentation/streams) to implement stream processing applications and microservices. It provides higher-level functions to process event streams, including transformations, stateful operations like aggregations and joins, windowing, processing based on event-time, and more. Input is read from one or more topics in order to generate output to one or more topics, effectively transforming the input streams to output streams.
- The [Kafka Connect API](https://kafka.apache.org/documentation.html#connect) to build and run reusable data import/export connectors that consume (read) or produce (write) streams of events from and to external systems and applications so they can integrate with Kafka. For example, a connector to a relational database like PostgreSQL might capture every change to a set of tables. However, in practice, you typically don’t need to implement your own connectors because the Kafka community already provides hundreds of ready-to-use connectors.

<a id="getting-started-introduction--where-to-go-from-here"></a>

## Where to go from here

- To get hands-on experience with Kafka, follow the [Quickstart](https://kafka.apache.org/quickstart).
- To understand Kafka in more detail, read the [Documentation](https://kafka.apache.org/documentation/). You also have your choice of [Kafka books and academic papers](https://kafka.apache.org/books-and-papers).
- Browse through the [Use Cases](https://kafka.apache.org/powered-by) to learn how other users in our world-wide community are getting value out of Kafka.
- Join a [local Kafka meetup group](https://kafka.apache.org/events) and [watch talks from Kafka Summit](https://kafka-summit.org/past-events/), the main conference of the Kafka community.

---

<a id="getting-started-uses"></a>

<a id="getting-started-uses--use-cases"></a>

# Use Cases

Here is a description of a few of the popular use cases for Apache Kafka®. For an overview of a number of these areas in action, see [this blog post](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying/).

<a id="getting-started-uses--messaging"></a>

## Messaging

Kafka works well as a replacement for a more traditional message broker. Message brokers are used for a variety of reasons (to decouple processing from data producers, to buffer unprocessed messages, etc). In comparison to most messaging systems Kafka has better throughput, built-in partitioning, replication, and fault-tolerance which makes it a good solution for large scale message processing applications.

In our experience messaging uses are often comparatively low-throughput, but may require low end-to-end latency and often depend on the strong durability guarantees Kafka provides.

In this domain Kafka is comparable to traditional messaging systems such as [ActiveMQ](https://activemq.apache.org) or [RabbitMQ](https://www.rabbitmq.com).

<a id="getting-started-uses--website-activity-tracking"></a>

## Website Activity Tracking

The original use case for Kafka was to be able to rebuild a user activity tracking pipeline as a set of real-time publish-subscribe feeds. This means site activity (page views, searches, or other actions users may take) is published to central topics with one topic per activity type. These feeds are available for subscription for a range of use cases including real-time processing, real-time monitoring, and loading into Hadoop or offline data warehousing systems for offline processing and reporting.

Activity tracking is often very high volume as many activity messages are generated for each user page view.

<a id="getting-started-uses--metrics"></a>

## Metrics

Kafka is often used for operational monitoring data. This involves aggregating statistics from distributed applications to produce centralized feeds of operational data.

<a id="getting-started-uses--log-aggregation"></a>

## Log Aggregation

Many people use Kafka as a replacement for a log aggregation solution. Log aggregation typically collects physical log files off servers and puts them in a central place (a file server or HDFS perhaps) for processing. Kafka abstracts away the details of files and gives a cleaner abstraction of log or event data as a stream of messages. This allows for lower-latency processing and easier support for multiple data sources and distributed data consumption. In comparison to log-centric systems like Scribe or Flume, Kafka offers equally good performance, stronger durability guarantees due to replication, and much lower end-to-end latency.

<a id="getting-started-uses--stream-processing"></a>

## Stream Processing

Many users of Kafka process data in processing pipelines consisting of multiple stages, where raw input data is consumed from Kafka topics and then aggregated, enriched, or otherwise transformed into new topics for further consumption or follow-up processing. For example, a processing pipeline for recommending news articles might crawl article content from RSS feeds and publish it to an “articles” topic; further processing might normalize or deduplicate this content and publish the cleansed article content to a new topic; a final processing stage might attempt to recommend this content to users. Such processing pipelines create graphs of real-time data flows based on the individual topics. Starting in 0.10.0.0, a light-weight but powerful stream processing library called [Kafka Streams](https://kafka.apache.org/documentation/streams) is available in Apache Kafka to perform such data processing as described above. Apart from Kafka Streams, alternative open source stream processing tools include [Apache Storm](https://storm.apache.org/) and [Apache Samza](https://samza.apache.org/).

<a id="getting-started-uses--event-sourcing"></a>

## Event Sourcing

[Event sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) is a style of application design where state changes are logged as a time-ordered sequence of records. Kafka’s support for very large stored log data makes it an excellent backend for an application built in this style.

<a id="getting-started-uses--commit-log"></a>

## Commit Log

Kafka can serve as a kind of external commit-log for a distributed system. The log helps replicate data between nodes and acts as a re-syncing mechanism for failed nodes to restore their data. The [log compaction](https://kafka.apache.org/documentation.html#compaction) feature in Kafka helps support this usage. In this usage Kafka is similar to [Apache BookKeeper](https://bookkeeper.apache.org/) project.

---

<a id="getting-started-quickstart"></a>

<a id="getting-started-quickstart--quick-start"></a>

# Quick Start

<a id="getting-started-quickstart--step-1-get-kafka"></a>
<a id="getting-started-quickstart--step-1:-get-kafka"></a>

## Step 1: Get Kafka

[Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/4.3.1/kafka_2.13-4.3.1.tgz) the latest Kafka release and extract it:

```bash
$ tar -xzf kafka_2.13-4.3.1.tgz
$ cd kafka_2.13-4.3.1
```

<a id="getting-started-quickstart--step-2-start-the-kafka-environment"></a>
<a id="getting-started-quickstart--step-2:-start-the-kafka-environment"></a>

## Step 2: Start the Kafka environment

NOTE: Your local environment must have Java 17+ installed.

Kafka can be run using local scripts and downloaded files or the docker image.

<a id="getting-started-quickstart--using-downloaded-files"></a>

### Using downloaded files

Generate a Cluster UUID

```bash
$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

Format Log Directories

```bash
$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

Start the Kafka Server

```bash
$ bin/kafka-server-start.sh config/server.properties
```

Once the Kafka server has successfully launched, you will have a basic Kafka environment running and ready to use.

<a id="getting-started-quickstart--using-jvm-based-apache-kafka-docker-image"></a>

### Using JVM Based Apache Kafka Docker Image

Get the Docker image:

```bash
$ docker pull apache/kafka:4.3.1
```

Start the Kafka Docker container:

```bash
$ docker run -p 9092:9092 apache/kafka:4.3.1
```

<a id="getting-started-quickstart--using-graalvm-based-native-apache-kafka-docker-image"></a>

### Using GraalVM Based Native Apache Kafka Docker Image

Get the Docker image:

```bash
$ docker pull apache/kafka-native:4.3.1
```

Start the Kafka Docker container:

```bash
$ docker run -p 9092:9092 apache/kafka-native:4.3.1
```

<a id="getting-started-quickstart--step-3-create-a-topic-to-store-your-events"></a>
<a id="getting-started-quickstart--step-3:-create-a-topic-to-store-your-events"></a>

## Step 3: Create a topic to store your events

Kafka is a distributed *event streaming platform* that lets you read, write, store, and process [*events*](https://kafka.apache.org/documentation/#messages) (also called *records* or *messages* in the documentation) across many machines.

Example events are payment transactions, geolocation updates from mobile phones, shipping orders, sensor measurements from IoT devices or medical equipment, and much more. These events are organized and stored in [*topics*](#getting-started-introduction--main-concepts-and-terminology). Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder.

So before you can write your first events, you must create a topic. Open another terminal session and run:

```bash
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
```

All of Kafka’s command line tools have additional options: run the `kafka-topics.sh` command without any arguments to display usage information. For example, it can also show you [details such as the partition count](#getting-started-introduction--main-concepts-and-terminology) of the new topic:

```bash
$ bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092 Topic: quickstart-events TopicId: NPmZHyhbR9y00wMglMH2sg PartitionCount: 1 ReplicationFactor: 1 Configs:Topic: quickstart-events Partition: 0 Leader: 0 Replicas: 0 Isr: 0
```

<a id="getting-started-quickstart--step-4-write-some-events-into-the-topic"></a>
<a id="getting-started-quickstart--step-4:-write-some-events-into-the-topic"></a>

## Step 4: Write some events into the topic

A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need-even forever.

Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.

```bash
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092 >This is my first event >This is my second event
```

You can stop the producer client with `Ctrl-C` at any time.

<a id="getting-started-quickstart--step-5-read-the-events"></a>
<a id="getting-started-quickstart--step-5:-read-the-events"></a>

## Step 5: Read the events

Open another terminal session and run the console consumer client to read the events you just created:

```bash
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092 This is my first event This is my second event
```

You can stop the consumer client with `Ctrl-C` at any time.

Feel free to experiment: for example, switch back to your producer terminal (previous step) to write additional events, and see how the events immediately show up in your consumer terminal.

Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want. You can easily verify this by opening yet another terminal session and re-running the previous command again.

<a id="getting-started-quickstart--step-6-importexport-your-data-as-streams-of-events-with-kafka-connect"></a>
<a id="getting-started-quickstart--step-6:-import-export-your-data-as-streams-of-events-with-kafka-connect"></a>

## Step 6: Import/export your data as streams of events with Kafka Connect

You probably have lots of data in existing systems like relational databases or traditional messaging systems, along with many applications that already use these systems. [Kafka Connect](https://kafka.apache.org/documentation/#connect) allows you to continuously ingest data from external systems into Kafka, and vice versa. It is an extensible tool that runs *connectors* , which implement the custom logic for interacting with an external system. It is thus very easy to integrate existing systems with Kafka. To make this process even easier, there are hundreds of such connectors readily available.

In this quickstart we’ll see how to run Kafka Connect with simple connectors that import data from a file to a Kafka topic and export data from a Kafka topic to a file.

First, make sure to add `connect-file-4.3.1.jar` to the `plugin.path` property in the Connect worker’s configuration. For the purpose of this quickstart we’ll use a relative path and consider the connectors’ package as an uber jar, which works when the quickstart commands are run from the installation directory. However, it’s worth noting that for production deployments using absolute paths is always preferable. See [plugin.path](#configuration-kafka-connect-configs--connectconfigs_plugin.path) for a detailed description of how to set this config.

Edit the `config/connect-standalone.properties` file, add or change the `plugin.path` configuration property match the following, and save the file:

```bash
$ echo "plugin.path=libs/connect-file-4.3.1.jar" >> config/connect-standalone.properties
```

Then, start by creating some seed data to test with:

```bash
$ echo -e "foo bar" > test.txt
```

Or on Windows:

```bash
$ echo foo > test.txt
$ echo bar >> test.txt
```

Next, we’ll start two connectors running in *standalone* mode, which means they run in a single, local, dedicated process. We provide three configuration files as parameters. The first is always the configuration for the Kafka Connect process, containing common configuration such as the Kafka brokers to connect to and the serialization format for data. The remaining configuration files each specify a connector to create. These files include a unique connector name, the connector class to instantiate, and any other configuration required by the connector.

```bash
$ bin/connect-standalone.sh config/connect-standalone.properties config/connect-file-source.properties config/connect-file-sink.properties
```

These sample configuration files, included with Kafka, use the default local cluster configuration you started earlier and create two connectors: the first is a source connector that reads lines from an input file and produces each to a Kafka topic and the second is a sink connector that reads messages from a Kafka topic and produces each as a line in an output file.

During startup you’ll see a number of log messages, including some indicating that the connectors are being instantiated. Once the Kafka Connect process has started, the source connector should start reading lines from `test.txt` and producing them to the topic `connect-test`, and the sink connector should start reading messages from the topic `connect-test` and write them to the file `test.sink.txt`. We can verify the data has been delivered through the entire pipeline by examining the contents of the output file:

```bash
$ more test.sink.txt foo bar
```

Note that the data is being stored in the Kafka topic `connect-test`, so we can also run a console consumer to see the data in the topic (or use custom consumer code to process it):

```bash
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic connect-test --from-beginning {"schema":{"type":"string","optional":false},"payload":"foo"} {"schema":{"type":"string","optional":false},"payload":"bar"} …
```

The connectors continue to process data, so we can add data to the file and see it move through the pipeline:

```bash
$ echo "Another line" >> test.txt
```

You should see the line appear in the console consumer output and in the sink file.

<a id="getting-started-quickstart--step-7-process-your-events-with-kafka-streams"></a>
<a id="getting-started-quickstart--step-7:-process-your-events-with-kafka-streams"></a>

## Step 7: Process your events with Kafka Streams

Once your data is stored in Kafka as events, you can process the data with the [Kafka Streams](https://kafka.apache.org/documentation/streams) client library for Java/Scala. It allows you to implement mission-critical real-time applications and microservices, where the input and/or output data is stored in Kafka topics. Kafka Streams combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology to make these applications highly scalable, elastic, fault-tolerant, and distributed. The library supports exactly-once processing, stateful operations and aggregations, windowing, joins, processing based on event-time, and much more.

To give you a first taste, here’s how one would implement the popular `WordCount` algorithm:

```java
KStream<String, String> textLines = builder.stream("quickstart-events");

KTable<String, Long> wordCounts = textLines
            .flatMapValues(line -> Arrays.asList(line.toLowerCase().split(" ")))
            .groupBy((keyIgnored, word) -> word)
            .count();

wordCounts.toStream().to("output-topic", Produced.with(Serdes.String(), Serdes.Long()));
```

The [Kafka Streams demo](https://kafka.apache.org/documentation/streams/quickstart) and the [app development tutorial](#documentation-streams-tutorial) demonstrate how to code and run such a streaming application from start to finish.

<a id="getting-started-quickstart--step-8-terminate-the-kafka-environment"></a>
<a id="getting-started-quickstart--step-8:-terminate-the-kafka-environment"></a>

## Step 8: Terminate the Kafka environment

Now that you reached the end of the quickstart, feel free to tear down the Kafka environment-or continue playing around.

1. Stop the producer and consumer clients with `Ctrl-C`, if you haven’t done so already.
2. Stop the Kafka broker with `Ctrl-C`.

If you also want to delete any data of your local Kafka environment including any events you have created along the way, run the command:

```bash
$ rm -rf /tmp/kafka-logs /tmp/kraft-combined-logs
```

<a id="getting-started-quickstart--congratulations"></a>

## Congratulations!

You have successfully finished the Apache Kafka quickstart.

To learn more, we suggest the following next steps:

- Read through the brief [Introduction](https://kafka.apache.org/intro) to learn how Kafka works at a high level, its main concepts, and how it compares to other technologies. To understand Kafka in more detail, head over to the [Documentation](https://kafka.apache.org/documentation/).
- Browse through the [Use Cases](https://kafka.apache.org/powered-by) to learn how other users in our world-wide community are getting value out of Kafka.
- Join a [local Kafka meetup group](https://kafka.apache.org/events) and [watch talks from Kafka Summit](https://kafka-summit.org/past-events/), the main conference of the Kafka community.

---

<a id="getting-started-ecosystem"></a>

<a id="getting-started-ecosystem--ecosystem"></a>

# Ecosystem

There are a plethora of tools that integrate with Kafka outside the main distribution. The [ecosystem page](https://cwiki.apache.org/confluence/x/Ri3VAQ) lists many of these, including stream processing systems, Hadoop integration, monitoring, and deployment tools.

---

<a id="getting-started-upgrade"></a>

# Upgrading

---

<a id="getting-started-zk2kraft"></a>

<a id="getting-started-zk2kraft--kraft-vs-zookeeper"></a>

# KRaft vs ZooKeeper

<a id="getting-started-zk2kraft--differences-between-kraft-mode-and-zookeeper-mode"></a>

# Differences Between KRaft mode and ZooKeeper mode

<a id="getting-started-zk2kraft--removed-zookeeper-features"></a>

# Removed ZooKeeper Features

This section documents differences in behavior between KRaft mode and ZooKeeper mode. Specifically, several configurations, metrics and features have changed or are no longer required in KRaft mode. To migrate an existing cluster from ZooKeeper mode to KRaft mode, please refer to the [ZooKeeper to KRaft Migration](https://kafka.apache.org/39/operations/kraft/#zookeeper-to-kraft-migration) section.

<a id="getting-started-zk2kraft--configurations"></a>

## Configurations

- Removed password encoder-related configurations. These configurations were used in ZooKeeper mode to define the key and backup key for encrypting sensitive data (e.g., passwords), specify the algorithm and key generation method for password encryption (e.g., AES, RSA), and control the key length and encryption strength.

  - `password.encoder.secret`
  - `password.encoder.old.secret`
  - `password.encoder.keyfactory.algorithm`
  - `password.encoder.cipher.algorithm`
  - `password.encoder.key.length`
  - `password.encoder.iterations`

  In KRaft mode, Kafka stores sensitive data in records, and the data is not encrypted in Kafka.
- Removed `control.plane.listener.name`. Kafka relies on ZooKeeper to manage metadata, but some internal operations (e.g., communication between controllers (a.k.a., broker controller) and brokers) still require Kafka’s internal control plane for coordination.

  In KRaft mode, Kafka eliminates its dependency on ZooKeeper, and the control plane functionality is fully integrated into Kafka itself. The process roles are clearly separated: brokers handle data-related requests, while the controllers (a.k.a., quorum controller) manages metadata-related requests. The controllers use the Raft protocol for internal communication, which operates differently from the ZooKeeper model. Use the following parameters to configure the control plane listener:

  - `controller.listener.names`
  - `listeners`
  - `listener.security.protocol.map`
- Removed graceful broker shutdowns-related configurations. These configurations were used in ZooKeeper mode to define the maximum number of retries and the retry backoff time for controlled shutdowns. It can reduce the risk of unplanned leader changes and data inconsistencies.

  - `controlled.shutdown.max.retries`
  - `controlled.shutdown.retry.backoff.ms`

  In KRaft mode, Kafka uses the Raft protocol to manage metadata. The broker shutdown process differs from ZooKeeper mode as it is managed by the quorum-based controller. The shutdown process is more reliable and efficient due to automated leader transfers and metadata updates handled by the controller.
- Removed the broker id generation-related configurations. These configurations were used in ZooKeeper mode to specify the broker id auto generation and control the broker id generation process.

  - `reserved.broker.max.id`
  - `broker.id.generation.enable`

  Kafka uses the node id in KRaft mode to identify servers.

  - `node.id`
- Removed broker protocol version-related configurations. These configurations were used in ZooKeeper mode to define communication protocol version between brokers. In KRaft mode, Kafka uses `metadata.version` to control the feature level of the cluster, which can be managed using `bin/kafka-features.sh`.

  - `inter.broker.protocol.version`
- Removed dynamic configurations which relied on ZooKeeper. In KRaft mode, to change these configurations, you need to restart the broker/controller.

  - `advertised.listeners`
- Removed the leader imbalance configuration used only in ZooKeeper. `leader.imbalance.per.broker.percentage` was used to limit the preferred leader election frequency in ZooKeeper.

  - `leader.imbalance.per.broker.percentage`
- Removed ZooKeeper related configurations.

  - `zookeeper.connect`
  - `zookeeper.session.timeout.ms`
  - `zookeeper.connection.timeout.ms`
  - `zookeeper.set.acl`
  - `zookeeper.max.in.flight.requests`
  - `zookeeper.ssl.client.enable`
  - `zookeeper.clientCnxnSocket`
  - `zookeeper.ssl.keystore.location`
  - `zookeeper.ssl.keystore.password`
  - `zookeeper.ssl.keystore.type`
  - `zookeeper.ssl.truststore.location`
  - `zookeeper.ssl.truststore.password`
  - `zookeeper.ssl.truststore.type`
  - `zookeeper.ssl.protocol`
  - `zookeeper.ssl.enabled.protocols`
  - `zookeeper.ssl.cipher.suites`
  - `zookeeper.ssl.endpoint.identification.algorithm`
  - `zookeeper.ssl.crl.enable`
  - `zookeeper.ssl.ocsp.enable`

<a id="getting-started-zk2kraft--dynamic-log-levels"></a>

## Dynamic Log Levels

- The dynamic log levels feature allows you to change the log4j settings of a running broker or controller process without restarting it. The command-line syntax for setting dynamic log levels on brokers has not changed in KRaft mode. Here is an example of setting the log level on a broker:

```bash
./bin/kafka-configs.sh --bootstrap-server localhost:9092 \
    --entity-type broker-loggers \
    --entity-name 1 \
    --alter \
    --add-config org.apache.kafka.raft.KafkaNetworkChannel=TRACE
```

- When setting dynamic log levels on the controllers, the `--bootstrap-controller` flag must be used. Here is an example of setting the log level ona controller:

```bash
./bin/kafka-configs.sh --bootstrap-controller localhost:9093 \
    --entity-type broker-loggers \
    --entity-name 1 \
    --alter \
    --add-config org.apache.kafka.raft.KafkaNetworkChannel=TRACE
```

  Note that the entity-type must be specified as `broker-loggers`, even though we are changing a controller’s log level rather than a broker’s log level.
- When changing the log level of a combined node, which has both broker and controller roles, either –bootstrap-servers or –bootstrap-controllers may be used. Combined nodes have only a single set of log levels; there are not different log levels for the broker and controller parts of the process.

<a id="getting-started-zk2kraft--dynamic-controller-configurations"></a>

## Dynamic Controller Configurations

- Some Kafka configurations can be changed dynamically, without restarting the process. The command-line syntax for setting dynamic log levels on brokers has not changed in KRaft mode. Here is an example of setting the number of IO threads on a broker:

```bash
./bin/kafka-configs.sh --bootstrap-server localhost:9092 \
    --entity-type brokers \
    --entity-name 1 \
    --alter \
    --add-config num.io.threads=5
```

- Controllers will apply all applicable cluster-level dynamic configurations. For example, the following command-line will change the `max.connections` setting on all of the brokers and all of the controllers in the cluster:

```bash
./bin/kafka-configs.sh --bootstrap-server localhost:9092 \
    --entity-type brokers \
    --entity-default \
    --alter \
    --add-config max.connections=10000
```

Prior to version 4.3, dynamic configuration updates were not supported unless a static quorum was used.

<a id="getting-started-zk2kraft--metrics"></a>

# Metrics

- Removed the following metrics related to ZooKeeper. `ControlPlaneNetworkProcessorAvgIdlePercent` is to monitor the average fraction of time the network processors are idle. The other `ControlPlaneExpiredConnectionsKilledCount` is to monitor the total number of connections disconnected, across all processors.

  - `ControlPlaneNetworkProcessorAvgIdlePercent`
  - `ControlPlaneExpiredConnectionsKilledCount`

  In KRaft mode, Kafka also provides metrics to monitor the network processors and expired connections. Use the following metrics to monitor the network processors and expired connections:

  - `NetworkProcessorAvgIdlePercent`
  - `ExpiredConnectionsKilledCount`
- Removed the metrics which are only used in ZooKeeper mode.

  - `kafka.controller:type=ControllerChannelManager,name=QueueSize`
  - `kafka.controller:type=ControllerChannelManager,name=RequestRateAndQueueTimeMs`
  - `kafka.controller:type=ControllerEventManager,name=EventQueueSize`
  - `kafka.controller:type=ControllerEventManager,name=EventQueueTimeMs`
  - `kafka.controller:type=ControllerStats,name=AutoLeaderBalanceRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=ControlledShutdownRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=ControllerChangeRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=ControllerShutdownRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=IdleRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=IsrChangeRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=LeaderAndIsrResponseReceivedRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=LeaderElectionRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=ListPartitionReassignmentRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=LogDirChangeRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=ManualLeaderBalanceRateAndTimeMs`
  - `kafka.controller:type=KafkaController,name=MigratingZkBrokerCount`
  - `kafka.controller:type=ControllerStats,name=PartitionReassignmentRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=TopicChangeRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=TopicDeletionRateAndTimeMs`
  - `kafka.controller:type=KafkaController,name=TopicsIneligibleToDeleteCount`
  - `kafka.controller:type=ControllerStats,name=TopicUncleanLeaderElectionEnableRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=UncleanLeaderElectionEnableRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=UncleanLeaderElectionsPerSec`
  - `kafka.controller:type=ControllerStats,name=UpdateFeaturesRateAndTimeMs`
  - `kafka.controller:type=ControllerStats,name=UpdateMetadataResponseReceivedRateAndTimeMs`
  - `kafka.controller:type=KafkaController,name=ActiveBrokerCount`
  - `kafka.controller:type=KafkaController,name=ActiveControllerCount`
  - `kafka.controller:type=KafkaController,name=ControllerState`
  - `kafka.controller:type=KafkaController,name=FencedBrokerCount`
  - `kafka.controller:type=KafkaController,name=GlobalPartitionCount`
  - `kafka.controller:type=KafkaController,name=GlobalTopicCount`
  - `kafka.controller:type=KafkaController,name=OfflinePartitionsCount`
  - `kafka.controller:type=KafkaController,name=PreferredReplicaImbalanceCount`
  - `kafka.controller:type=KafkaController,name=ReplicasIneligibleToDeleteCount`
  - `kafka.controller:type=KafkaController,name=ReplicasToDeleteCount`
  - `kafka.controller:type=KafkaController,name=TopicsToDeleteCount`
  - `kafka.controller:type=KafkaController,name=ZkMigrationState`
  - `kafka.server:type=DelayedOperationPurgatory,name=PurgatorySize,delayedOperation=ElectLeader`
  - `kafka.server:type=DelayedOperationPurgatory,name=PurgatorySize,delayedOperation=topic`
  - `kafka.server:type=DelayedOperationPurgatory,name=NumDelayedOperations,delayedOperation=ElectLeader`
  - `kafka.server:type=DelayedOperationPurgatory,name=NumDelayedOperations,delayedOperation=topic`
  - `kafka.server:type=SessionExpireListener,name=SessionState`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperAuthFailuresPerSec`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperDisconnectsPerSec`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperExpiresPerSec`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperReadOnlyConnectsPerSec`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperSaslAuthenticationsPerSec`
  - `kafka.server:type=SessionExpireListener,name=ZooKeeperSyncConnectsPerSec`
  - `kafka.server:type=ZooKeeperClientMetrics,name=ZooKeeperRequestLatencyMs`

<a id="getting-started-zk2kraft--behavioral-change-reference"></a>

# Behavioral Change Reference

This document catalogs the functional and operational differences between ZooKeeper mode and KRaft mode.

- **Configuration Value Size Limitation** : KRaft mode restricts configuration values to a maximum size of `Short.MAX_VALUE`, which prevents using the append operation to create larger configuration values.
- **Policy Class Deployment** : In KRaft mode, the `CreateTopicPolicy` and `AlterConfigPolicy` plugins run on the controller instead of the broker. This requires users to deploy the policy class JAR files on the controller and configure the parameters (`create.topic.policy.class.name` and `alter.config.policy.class.name`) on the controller.

  Note: If migrating from ZooKeeper mode, ensure policy JARs are moved from brokers to controllers.
- **Custom implementations of`KafkaPrincipalBuilder`**: In KRaft mode, custom implementations of `KafkaPrincipalBuilder` must also implement `KafkaPrincipalSerde`; otherwise brokers will not be able to forward requests to the controller.

---

<a id="getting-started-compatibility"></a>

<a id="getting-started-compatibility--compatibility"></a>

# Compatibility

With the release of Kafka 4.0, significant changes have been introduced that impact compatibility across various components. To assist users in planning upgrades and ensuring seamless interoperability, a comprehensive compatibility matrix has been prepared.

<a id="getting-started-compatibility--jdk-compatibility-across-kafka-versions"></a>

# JDK Compatibility Across Kafka Versions

| Module | Kafka Version | Java 11 | Java 17 | Java 23 |
| --- | --- | --- | --- | --- |
| Clients | 4.0.0 | ✅ | ✅ | ✅ |
| Streams | 4.0.0 | ✅ | ✅ | ✅ |
| Connect | 4.0.0 | ❌ | ✅ | ✅ |
| Server | 4.0.0 | ❌ | ✅ | ✅ |

**Note: Java 8 is removed in Kafka 4.0 and is no longer supported.**

<a id="getting-started-compatibility--server-compatibility"></a>

# Server Compatibility

| KRaft Cluster Version | Compatibility 4.0 Server (dynamic voter) | Compatibility 4.0 Server (static voter) |
| --- | --- | --- |
| before 3.2.x | ❌ | ❌ |
| 3.3.x | ❌ | ✅ |
| 3.4.x | ❌ | ✅ |
| 3.5.x | ❌ | ✅ |
| 3.6.x | ❌ | ✅ |
| 3.7.x | ❌ | ✅ |
| 3.8.x | ❌ | ✅ |
| 3.9.x | ✅ | ✅ |
| 4.0.x | ✅ | ✅ |

**Note: Can’t upgrade server from static voter to dynamic voter, see [KAFKA-16538](https://issues.apache.org/jira/browse/KAFKA-16538).**

<a id="getting-started-compatibility--clientbroker-forward-compatibility"></a>
<a id="getting-started-compatibility--client-broker-forward-compatibility"></a>

## Client/Broker Forward Compatibility

<table><tr><th>Kafka Version</th><th>Module</th><th>Compatibility with Kafka 4.0</th><th>Key Differences/Limitations</th></tr><tr><td rowspan="3">0.x, 1.x, 2.0</td><td>Client</td><td>❌ Not Compatible</td><td><p>Pre-0.10.x protocols are fully removed in Kafka 4.0 (<a href="https://cwiki.apache.org/confluence/x/K5sODg" rel="noopener" target="_blank">KIP-896</a>).</p></td></tr><tr><td>Streams</td><td>❌ Not Compatible</td><td><p>Pre-0.10.x protocols are fully removed in Kafka 4.0 (<a href="https://cwiki.apache.org/confluence/x/K5sODg" rel="noopener" target="_blank">KIP-896</a>).</p></td></tr><tr><td>Connect</td><td>❌ Not Compatible</td><td><p>Pre-0.10.x protocols are fully removed in Kafka 4.0 (<a href="https://cwiki.apache.org/confluence/x/K5sODg" rel="noopener" target="_blank">KIP-896</a>).</p></td></tr><tr><td rowspan="3">2.1 ~ 2.8</td><td>Client</td><td>⚠️ Partially Compatible</td><td><p>More details in the <a href="https://kafka.apache.org/40/documentation.html#upgrade_400_notable_consumer">Consumer</a>, <a href="https://kafka.apache.org/40/documentation.html#upgrade_400_notable_producer">Producer</a>, and <a href="https://kafka.apache.org/40/documentation.html#upgrade_400_notable_admin_client">Admin Client</a> section.</p></td></tr><tr><td>Streams</td><td>⚠️ Limited Compatibility</td><td><p>More details in the <a href="https://kafka.apache.org/40/documentation.html#upgrade_400_notable_kafka_streams">Kafka Streams</a> section.</p></td></tr><tr><td>Connect</td><td>⚠️ Limited Compatibility</td><td><p>More details in the <a href="https://kafka.apache.org/40/documentation.html#upgrade_400_notable_connect">Connect</a> section.</p></td></tr><tr><td rowspan="3">3.x</td><td>Client</td><td>✅ Fully Compatible</td><td>—</td></tr><tr><td>Streams</td><td>✅ Fully Compatible</td><td>—</td></tr><tr><td>Connect</td><td>✅ Fully Compatible</td><td>—</td></tr></table>

Note: Starting with Kafka 4.0, the `--zookeeper` option in AdminClient commands has been removed. Users must use the `--bootstrap-server` option to interact with the Kafka cluster. This change aligns with the transition to KRaft mode.

---

<a id="getting-started-docker"></a>

<a id="getting-started-docker--docker"></a>

# Docker

<a id="getting-started-docker--jvm-based-apache-kafka-docker-image"></a>

## JVM Based Apache Kafka Docker Image

[Docker](https://www.docker.com/) is a popular container runtime. Docker images for the JVM based Apache Kafka can be found on [Docker Hub](https://hub.docker.com/r/apache/kafka) and are available from version 3.7.0.

Docker image can be pulled from Docker Hub using the following command:

```bash
$ docker pull apache/kafka:4.3.1
```

If you want to fetch the latest version of the Docker image use following command:

```bash
$ docker pull apache/kafka:latest
```

To start the Kafka container using this Docker image with default configs and on default port 9092:

```bash
$ docker run -p 9092:9092 apache/kafka:4.3.1
```

<a id="getting-started-docker--graalvm-based-native-apache-kafka-docker-image"></a>

## GraalVM Based Native Apache Kafka Docker Image

Docker images for the GraalVM Based Native Apache Kafka can be found on [Docker Hub](https://hub.docker.com/r/apache/kafka-native) and are available from version 3.8.0. NOTE: This image is experimental and intended for local development and testing purposes only; it is not recommended for production use.

Docker image can be pulled from Docker Hub using the following command:

```bash
$ docker pull apache/kafka-native:4.3.1
```

If you want to fetch the latest version of the Docker image use following command:

```bash
$ docker pull apache/kafka-native:latest
```

To start the Kafka container using this Docker image with default configs and on default port 9092:

```bash
$ docker run -p 9092:9092 apache/kafka-native:4.3.1
```

<a id="getting-started-docker--usage-guide"></a>

## Usage guide

Detailed instructions for using the Docker image are mentioned [here](https://github.com/apache/kafka/blob/trunk/docker/examples/README.md).

---

<a id="apis"></a>

<a id="apis--api"></a>

# API

Kafka includes six core apis:

1. The Producer API allows applications to send streams of data to topics in the Kafka cluster.
2. The Consumer API allows applications to read streams of data from topics in the Kafka cluster.
3. The Share consumer API allows applications in a share group to cooperatively consume and process data from Kafka topics.
4. The Streams API allows transforming streams of data from input topics to output topics.
5. The Connect API allows implementing connectors that continually pull from some source system or application into Kafka or push from Kafka into some sink system or application.
6. The Admin API allows managing and inspecting topics, brokers, and other Kafka objects.
   Kafka exposes all its functionality over a language-independent protocol which has clients available in many programming languages. However only the Java clients are maintained as part of the main Kafka project, the others are available as independent open source projects. A list of non-Java clients is available [here](https://cwiki.apache.org/confluence/x/3gDVAQ).

<a id="apis--producer-api"></a>

# Producer API

The Producer API allows applications to send streams of data to topics in the Kafka cluster.

To use the producer, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>4.3.1</version>
</dependency>
```

<a id="apis--consumer-api"></a>

# Consumer API

The Consumer API allows applications to read streams of data from topics in the Kafka cluster.

To use the consumer, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>4.3.1</version>
</dependency>
```

<a id="apis--share-consumer-api"></a>

# Share Consumer API

The Share Consumer API enables applications in a share group to cooperatively consume and process data from Kafka topics.

To use the share consumer, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>4.3.1</version>
</dependency>
```

<a id="apis--streams-api"></a>

# Streams API

The [Streams](#documentation-streams) API allows transforming streams of data from input topics to output topics.

Additional documentation on using the Streams API is available [here](#documentation-streams).

To use Kafka Streams, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-streams</artifactId>
	<version>4.3.1</version>
</dependency>
```

When using Scala you may optionally include the `kafka-streams-scala` library. Additional documentation on using the Kafka Streams DSL for Scala is available [in the developer guide](#documentation-streams-developer-guide-dsl-api--scala-dsl).

To use Kafka Streams DSL for Scala 2.13, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-streams-scala_2.13</artifactId>
	<version>4.3.1</version>
</dependency>
```

<a id="apis--connect-api"></a>

# Connect API

The Connect API allows implementing connectors that continually pull from some source data system into Kafka or push from Kafka into some sink data system.

Many users of Connect won’t need to use this API directly, though, they can use pre-built connectors without needing to write any code. Additional information on using Connect is available [here](https://kafka.apache.org/documentation.html#connect).

<a id="apis--admin-api"></a>

# Admin API

The Admin API supports managing and inspecting topics, brokers, acls, and other Kafka objects.

To use the Admin API, add the following Maven dependency to your project:

```xml
<dependency>
	<groupId>org.apache.kafka</groupId>
	<artifactId>kafka-clients</artifactId>
	<version>4.3.1</version>
</dependency>
```

<a id="configuration"></a>

<a id="configuration--configuration"></a>

# Configuration

---

<a id="configuration--broker-configs"></a>

##### [Broker Configs](#configuration-broker-configs)

Broker Configs

<a id="configuration--topic-configs"></a>

##### [Topic Configs](#configuration-topic-configs)

Topic Configs

<a id="configuration--group-configs"></a>

##### [Group Configs](#configuration-group-configs)

Group Configs

<a id="configuration--producer-configs"></a>

##### [Producer Configs](#configuration-producer-configs)

Producer Configs

<a id="configuration--consumer-and-share-consumer-configs"></a>

##### [Consumer and Share Consumer Configs](#configuration-consumer-configs)

Consumer and Share Consumer Configs

<a id="configuration--kafka-connect-configs"></a>

##### [Kafka Connect Configs](#configuration-kafka-connect-configs)

Kafka Connect Configs

<a id="configuration--kafka-streams-configs"></a>

##### [Kafka Streams Configs](#configuration-kafka-streams-configs)

Kafka Streams Configs

<a id="configuration--admin-configs"></a>

##### [Admin Configs](#configuration-admin-configs)

Admin Configs

<a id="configuration--mirrormaker-configs"></a>

##### [MirrorMaker Configs](#configuration-mirrormaker-configs)

MirrorMaker Configs

<a id="configuration--system-properties"></a>

##### [System Properties](#configuration-system-properties)

System Properties

<a id="configuration--tiered-storage-configs"></a>

##### [Tiered Storage Configs](#configuration-tiered-storage-configs)

Tiered Storage Configs

<a id="configuration--configuration-providers"></a>

##### [Configuration Providers](#configuration-configuration-providers)

Configuration Providers

<a id="configuration-broker-configs"></a>

<a id="configuration-broker-configs--broker-configs"></a>

# Broker Configs

Broker Configs

The essential configurations are the following:

- `node.id`
- `log.dirs`
- `process.roles`
- `controller.quorum.bootstrap.servers`
- `controller.listener.names`

Broker configurations and defaults are discussed in more detail below.

-

<a id="configuration-broker-configs--controller.listener.names"></a>

  #### [controller.listener.names](#configuration-broker-configs--brokerconfigs_controller.listener.names)

  A comma-separated list of the names of the listeners used by the controller. This is required when communicating with the controller quorum, the broker will always use the first listener in this list.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--node.id"></a>

  #### [node.id](#configuration-broker-configs--brokerconfigs_node.id)

  The node ID associated with the roles this process is playing when `process.roles` is non-empty. This is required configuration when running in KRaft mode.

| Type: | int |
| --- | --- |
| Default: |  |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--process.roles"></a>

  #### [process.roles](#configuration-broker-configs--brokerconfigs_process.roles)

  The roles that this process plays: 'broker', 'controller', or 'broker,controller' if it is both.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: | [broker, controller] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--add.partitions.to.txn.retry.backoff.max.ms"></a>

  #### [add.partitions.to.txn.retry.backoff.max.ms](#configuration-broker-configs--brokerconfigs_add.partitions.to.txn.retry.backoff.max.ms)

  The maximum allowed timeout for adding partitions to transactions on the server side. It only applies to the actual add partition operations, not the verification. It will not be effective if it is larger than request.timeout.ms

| Type: | int |
| --- | --- |
| Default: | 100 |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--add.partitions.to.txn.retry.backoff.ms"></a>

  #### [add.partitions.to.txn.retry.backoff.ms](#configuration-broker-configs--brokerconfigs_add.partitions.to.txn.retry.backoff.ms)

  The server-side retry backoff when the server attemptsto add the partition to the transaction

| Type: | int |
| --- | --- |
| Default: | 20 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--advertised.listeners"></a>

  #### [advertised.listeners](#configuration-broker-configs--brokerconfigs_advertised.listeners)

  Specifies the listener addresses that the Kafka brokers will advertise to clients and other brokers. The config is useful where the actual listener configuration `listeners` does not represent the addresses that clients should use to connect, such as in cloud environments. The addresses are published to and managed by the controller, the brokers pull these data from the controller as needed. In IaaS environments, this may need to be different from the interface to which the broker binds. If this is not set, the value for `listeners` will be used. Unlike `listeners`, it is not valid to advertise the 0.0.0.0 meta-address.
  Also unlike `listeners`, there can be duplicated ports in this property, so that one listener can be configured to advertise another listener's address. This can be useful in some cases where external load balancers are used.

| Type: | list |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--auto.create.topics.enable"></a>

  #### [auto.create.topics.enable](#configuration-broker-configs--brokerconfigs_auto.create.topics.enable)

  Enable auto creation of topic on the server.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--auto.leader.rebalance.enable"></a>

  #### [auto.leader.rebalance.enable](#configuration-broker-configs--brokerconfigs_auto.leader.rebalance.enable)

  Enables auto leader balancing. A background thread checks the distribution of partition leaders at regular intervals, configurable by leader.imbalance.check.interval.seconds. If the leader is imbalanced, leader rebalance to the preferred leader for partitions is triggered.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--background.threads"></a>

  #### [background.threads](#configuration-broker-configs--brokerconfigs_background.threads)

  The number of threads to use for various background processing tasks

| Type: | int |
| --- | --- |
| Default: | 10 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--broker.id"></a>

  #### [broker.id](#configuration-broker-configs--brokerconfigs_broker.id)

  The broker id for this server.

| Type: | int |
| --- | --- |
| Default: | -1 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--compression.type"></a>

  #### [compression.type](#configuration-broker-configs--brokerconfigs_compression.type)

  Specify the final compression type for a given topic. This configuration accepts the standard compression codecs ('gzip', 'snappy', 'lz4', 'zstd'). It additionally accepts 'uncompressed' which is equivalent to no compression; and 'producer' which means retain the original compression codec set by the producer.

| Type: | string |
| --- | --- |
| Default: | producer |
| Valid Values: | [uncompressed, zstd, lz4, snappy, gzip, producer] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--controller.quorum.bootstrap.servers"></a>

  #### [controller.quorum.bootstrap.servers](#configuration-broker-configs--brokerconfigs_controller.quorum.bootstrap.servers)

  List of endpoints to use for bootstrapping the cluster metadata. The endpoints are specified in comma-separated list of `{host}:{port}` entries. For example: `localhost:9092,localhost:9093,localhost:9094`.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: | non-empty list |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--controller.quorum.election.backoff.max.ms"></a>

  #### [controller.quorum.election.backoff.max.ms](#configuration-broker-configs--brokerconfigs_controller.quorum.election.backoff.max.ms)

  Maximum time in milliseconds before starting new elections. This is used in the binary exponential backoff mechanism that helps prevent gridlocked elections

| Type: | int |
| --- | --- |
| Default: | 1000 (1 second) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--controller.quorum.election.timeout.ms"></a>

  #### [controller.quorum.election.timeout.ms](#configuration-broker-configs--brokerconfigs_controller.quorum.election.timeout.ms)

  Maximum time in milliseconds to wait without being able to fetch from the leader before triggering a new election

| Type: | int |
| --- | --- |
| Default: | 1000 (1 second) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--controller.quorum.fetch.timeout.ms"></a>

  #### [controller.quorum.fetch.timeout.ms](#configuration-broker-configs--brokerconfigs_controller.quorum.fetch.timeout.ms)

  Maximum time without a successful fetch from the current leader before becoming a candidate and triggering an election for voters; Maximum time a leader can go without receiving valid fetch or fetchSnapshot request from a majority of the quorum before resigning.

| Type: | int |
| --- | --- |
| Default: | 2000 (2 seconds) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--controller.quorum.voters"></a>

  #### [controller.quorum.voters](#configuration-broker-configs--brokerconfigs_controller.quorum.voters)

  Map of id/endpoint information for the set of voters in a comma-separated list of `{id}@{host}:{port}` entries. This is the old way of defining membership for controller quorums and should NOT be set if using dynamic quorums. Instead, controller.quorum.bootstrap.servers should be set,and the voter set is determined by the --standalone or --initial-controllers flags when formatting.For example: `1@localhost:9092,2@localhost:9093,3@localhost:9094`

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: | non-empty list |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--delete.topic.enable"></a>

  #### [delete.topic.enable](#configuration-broker-configs--brokerconfigs_delete.topic.enable)

  When set to true, topics can be deleted by the admin client. When set to false, deletion requests will be explicitly rejected by the broker.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--early.start.listeners"></a>

  #### [early.start.listeners](#configuration-broker-configs--brokerconfigs_early.start.listeners)

  A comma-separated list of listener names which may be started before the authorizer has finished initialization. This is useful when the authorizer is dependent on the cluster itself for bootstrapping, as is the case for the StandardAuthorizer (which stores ACLs in the metadata log.) By default, all listeners included in controller.listener.names will also be early start listeners. A listener should not appear in this list if it accepts external traffic.

| Type: | list |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--group.coordinator.background.threads"></a>

  #### [group.coordinator.background.threads](#configuration-broker-configs--brokerconfigs_group.coordinator.background.threads)

  The number of threads used by the group coordinator for processing background tasks (e.g. updating regular expression subscriptions and offloaded assignments).

| Type: | int |
| --- | --- |
| Default: | 2 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--group.coordinator.threads"></a>

  #### [group.coordinator.threads](#configuration-broker-configs--brokerconfigs_group.coordinator.threads)

  The number of threads used by the group coordinator for processing requests.

| Type: | int |
| --- | --- |
| Default: | 4 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--leader.imbalance.check.interval.seconds"></a>

  #### [leader.imbalance.check.interval.seconds](#configuration-broker-configs--brokerconfigs_leader.imbalance.check.interval.seconds)

  The frequency with which the partition rebalance check is triggered by the controller

| Type: | long |
| --- | --- |
| Default: | 300 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--listeners"></a>

  #### [listeners](#configuration-broker-configs--brokerconfigs_listeners)

  Listener List - Comma-separated list of URIs we will listen on and the listener names. If the listener name is not a security protocol, `listener.security.protocol.map` must also be set.
  Listener names and port numbers must be unique unless one listener is an IPv4 address and the other listener is an IPv6 address (for the same port).
  Specify hostname as 0.0.0.0 to bind to all interfaces.
  Leave hostname empty to bind to default interface.
  Examples of legal listener lists:
  `PLAINTEXT://myhost:9092,SSL://:9091`
  `CLIENT://0.0.0.0:9092,REPLICATION://localhost:9093`
  `PLAINTEXT://127.0.0.1:9092,SSL://[::1]:9092`

| Type: | list |
| --- | --- |
| Default: | PLAINTEXT://:9092 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | per-broker |

-

<a id="configuration-broker-configs--log.dir"></a>

  #### [log.dir](#configuration-broker-configs--brokerconfigs_log.dir)

  A comma-separated list of the directories where the log data is stored. (supplemental to log.dirs property)

| Type: | list |
| --- | --- |
| Default: | /tmp/kafka-logs |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.dirs"></a>

  #### [log.dirs](#configuration-broker-configs--brokerconfigs_log.dirs)

  A comma-separated list of the directories where the log data is stored. If not set, the value in log.dir is used.

| Type: | list |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.flush.interval.messages"></a>

  #### [log.flush.interval.messages](#configuration-broker-configs--brokerconfigs_log.flush.interval.messages)

  The number of messages accumulated on a log partition before messages are flushed to disk.

| Type: | long |
| --- | --- |
| Default: | 9223372036854775807 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.flush.interval.ms"></a>

  #### [log.flush.interval.ms](#configuration-broker-configs--brokerconfigs_log.flush.interval.ms)

  The maximum time in ms that a message in any topic is kept in memory before flushed to disk. If not set, the value in log.flush.scheduler.interval.ms is used

| Type: | long |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.flush.offset.checkpoint.interval.ms"></a>

  #### [log.flush.offset.checkpoint.interval.ms](#configuration-broker-configs--brokerconfigs_log.flush.offset.checkpoint.interval.ms)

  The frequency with which we update the persistent record of the last flush which acts as the log recovery point.

| Type: | int |
| --- | --- |
| Default: | 60000 (1 minute) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.flush.scheduler.interval.ms"></a>

  #### [log.flush.scheduler.interval.ms](#configuration-broker-configs--brokerconfigs_log.flush.scheduler.interval.ms)

  The frequency in ms that the log flusher checks whether any log needs to be flushed to disk

| Type: | long |
| --- | --- |
| Default: | 9223372036854775807 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.flush.start.offset.checkpoint.interval.ms"></a>

  #### [log.flush.start.offset.checkpoint.interval.ms](#configuration-broker-configs--brokerconfigs_log.flush.start.offset.checkpoint.interval.ms)

  The frequency with which we update the persistent record of log start offset

| Type: | int |
| --- | --- |
| Default: | 60000 (1 minute) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.retention.bytes"></a>

  #### [log.retention.bytes](#configuration-broker-configs--brokerconfigs_log.retention.bytes)

  The maximum size of the log before deleting it

| Type: | long |
| --- | --- |
| Default: | -1 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.retention.hours"></a>

  #### [log.retention.hours](#configuration-broker-configs--brokerconfigs_log.retention.hours)

  The number of hours to keep a log file before deleting it (in hours), tertiary to log.retention.ms property

| Type: | int |
| --- | --- |
| Default: | 168 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.retention.minutes"></a>

  #### [log.retention.minutes](#configuration-broker-configs--brokerconfigs_log.retention.minutes)

  The number of minutes to keep a log file before deleting it (in minutes), secondary to log.retention.ms property. If not set, the value in log.retention.hours is used

| Type: | int |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.retention.ms"></a>

  #### [log.retention.ms](#configuration-broker-configs--brokerconfigs_log.retention.ms)

  The number of milliseconds to keep a log file before deleting it (in milliseconds), If not set, the value in log.retention.minutes is used. If set to -1, no time limit is applied.

| Type: | long |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.roll.hours"></a>

  #### [log.roll.hours](#configuration-broker-configs--brokerconfigs_log.roll.hours)

  The maximum time before a new log segment is rolled out (in hours), secondary to log.roll.ms property

| Type: | int |
| --- | --- |
| Default: | 168 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.roll.jitter.hours"></a>

  #### [log.roll.jitter.hours](#configuration-broker-configs--brokerconfigs_log.roll.jitter.hours)

  The maximum jitter to subtract from logRollTimeMillis (in hours), secondary to log.roll.jitter.ms property

| Type: | int |
| --- | --- |
| Default: | 0 |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--log.roll.jitter.ms"></a>

  #### [log.roll.jitter.ms](#configuration-broker-configs--brokerconfigs_log.roll.jitter.ms)

  The maximum jitter to subtract from logRollTimeMillis (in milliseconds). If not set, the value in log.roll.jitter.hours is used

| Type: | long |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.roll.ms"></a>

  #### [log.roll.ms](#configuration-broker-configs--brokerconfigs_log.roll.ms)

  The maximum time before a new log segment is rolled out (in milliseconds). If not set, the value in log.roll.hours is used

| Type: | long |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.segment.bytes"></a>

  #### [log.segment.bytes](#configuration-broker-configs--brokerconfigs_log.segment.bytes)

  The maximum size of a single log file

| Type: | int |
| --- | --- |
| Default: | 1073741824 (1 gibibyte) |
| Valid Values: | [1048576,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--log.segment.delete.delay.ms"></a>

  #### [log.segment.delete.delay.ms](#configuration-broker-configs--brokerconfigs_log.segment.delete.delay.ms)

  The amount of time to wait before deleting a file from the filesystem. If the value is 0 and there is no file to delete, the system will wait 1 millisecond. Low value will cause busy waiting

| Type: | long |
| --- | --- |
| Default: | 60000 (1 minute) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--message.max.bytes"></a>

  #### [message.max.bytes](#configuration-broker-configs--brokerconfigs_message.max.bytes)

  The largest record batch size allowed by Kafka (after compression if compression is enabled).This can be set per topic with the topic level `max.message.bytes` config.

| Type: | int |
| --- | --- |
| Default: | 1048588 |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--metadata.log.dir"></a>

  #### [metadata.log.dir](#configuration-broker-configs--brokerconfigs_metadata.log.dir)

  This configuration determines where we put the metadata log. If it is not set, the metadata log is placed in the first log directory from log.dirs.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.log.max.record.bytes.between.snapshots"></a>

  #### [metadata.log.max.record.bytes.between.snapshots](#configuration-broker-configs--brokerconfigs_metadata.log.max.record.bytes.between.snapshots)

  This is the maximum number of bytes in the log between the latest snapshot and the high-watermark needed before generating a new snapshot. The default value is 20971520. To generate snapshots based on the time elapsed, see the `metadata.log.max.snapshot.interval.ms` configuration. The Kafka node will generate a snapshot when either the maximum time interval is reached or the maximum bytes limit is reached.

| Type: | long |
| --- | --- |
| Default: | 20971520 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.log.max.snapshot.interval.ms"></a>

  #### [metadata.log.max.snapshot.interval.ms](#configuration-broker-configs--brokerconfigs_metadata.log.max.snapshot.interval.ms)

  This is the maximum number of milliseconds to wait to generate a snapshot if there are committed records in the log that are not included in the latest snapshot. A value of zero disables time based snapshot generation. The default value is 3600000. To generate snapshots based on the number of metadata bytes, see the `metadata.log.max.record.bytes.between.snapshots` configuration. The Kafka node will generate a snapshot when either the maximum time interval is reached or the maximum bytes limit is reached.

| Type: | long |
| --- | --- |
| Default: | 3600000 (1 hour) |
| Valid Values: | [0,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.log.segment.bytes"></a>

  #### [metadata.log.segment.bytes](#configuration-broker-configs--brokerconfigs_metadata.log.segment.bytes)

  The maximum size of a single metadata log file.

| Type: | int |
| --- | --- |
| Default: | 1073741824 (1 gibibyte) |
| Valid Values: | [8388608,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.log.segment.ms"></a>

  #### [metadata.log.segment.ms](#configuration-broker-configs--brokerconfigs_metadata.log.segment.ms)

  The maximum time before a new metadata log file is rolled out (in milliseconds).

| Type: | long |
| --- | --- |
| Default: | 604800000 (7 days) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.max.retention.bytes"></a>

  #### [metadata.max.retention.bytes](#configuration-broker-configs--brokerconfigs_metadata.max.retention.bytes)

  The maximum combined size of the metadata log and snapshots before deleting old snapshots and log files. Since at least one snapshot must exist before any logs can be deleted, this is a soft limit.

| Type: | long |
| --- | --- |
| Default: | 104857600 (100 mebibytes) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--metadata.max.retention.ms"></a>

  #### [metadata.max.retention.ms](#configuration-broker-configs--brokerconfigs_metadata.max.retention.ms)

  The number of milliseconds to keep a metadata log file or snapshot before deleting it. Since at least one snapshot must exist before any logs can be deleted, this is a soft limit.

| Type: | long |
| --- | --- |
| Default: | 604800000 (7 days) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--min.insync.replicas"></a>

  #### [min.insync.replicas](#configuration-broker-configs--brokerconfigs_min.insync.replicas)

  Specifies the *minimum* number of in-sync replicas (including the leader) required for a write to succeed when a producer sets `acks` to "all" (or "-1"). In the `acks=all` case, every in-sync replica must acknowledge a write for it to be considered successful. E.g., if a topic has `replication.factor` of 3 and the ISR set includes all three replicas, then all three replicas must acknowledge an `acks=all` write for it to succeed, even if `min.insync.replicas` happens to be less than 3. If `acks=all` and the current ISR set contains fewer than `min.insync.replicas` members, then the producer will raise an exception (either `NotEnoughReplicas` or `NotEnoughReplicasAfterAppend`).
  Regardless of the `acks` setting, the messages will not be visible to the consumers until they are replicated to all in-sync replicas and the `min.insync.replicas` condition is met.
  When used together, `min.insync.replicas` and `acks` allow you to enforce greater durability guarantees. A typical scenario would be to create a topic with a replication factor of 3, set `min.insync.replicas` to 2, and produce with `acks` of "all". This ensures that a majority of replicas must persist a write before it's considered successful by the producer and it's visible to consumers.

  Note that when the Eligible Leader Replicas feature is enabled, the semantics of this config changes. Please refer to [the ELR section](#configuration-broker-configs--eligible_leader_replicas) for more info.

| Type: | int |
| --- | --- |
| Default: | 1 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--num.io.threads"></a>

  #### [num.io.threads](#configuration-broker-configs--brokerconfigs_num.io.threads)

  The number of threads that the server uses for processing requests, which may include disk I/O

| Type: | int |
| --- | --- |
| Default: | 8 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--num.network.threads"></a>

  #### [num.network.threads](#configuration-broker-configs--brokerconfigs_num.network.threads)

  The number of threads that the server uses for receiving requests from the network and sending responses to the network. Noted: each listener (except for controller listener) creates its own thread pool.

| Type: | int |
| --- | --- |
| Default: | 3 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--num.recovery.threads.per.data.dir"></a>

  #### [num.recovery.threads.per.data.dir](#configuration-broker-configs--brokerconfigs_num.recovery.threads.per.data.dir)

  The number of threads per data directory to be used for log recovery at startup and flushing at shutdown

| Type: | int |
| --- | --- |
| Default: | 2 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--num.replica.alter.log.dirs.threads"></a>

  #### [num.replica.alter.log.dirs.threads](#configuration-broker-configs--brokerconfigs_num.replica.alter.log.dirs.threads)

  The number of threads that can move replicas between log directories, which may include disk I/O. The default value is equal to the number of directories specified in the `log.dir` or `log.dirs` configuration property.

| Type: | int |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--num.replica.fetchers"></a>

  #### [num.replica.fetchers](#configuration-broker-configs--brokerconfigs_num.replica.fetchers)

  Number of fetcher threads used to replicate records from each source broker. The total number of fetchers on each broker is bound by `num.replica.fetchers` multiplied by the number of brokers in the cluster.Increasing this value can increase the degree of I/O parallelism in the follower and leader broker at the cost of higher CPU and memory utilization.

| Type: | int |
| --- | --- |
| Default: | 1 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--offset.metadata.max.bytes"></a>

  #### [offset.metadata.max.bytes](#configuration-broker-configs--brokerconfigs_offset.metadata.max.bytes)

  The maximum size for a metadata entry associated with an offset commit.

| Type: | int |
| --- | --- |
| Default: | 4096 (4 kibibytes) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.commit.timeout.ms"></a>

  #### [offsets.commit.timeout.ms](#configuration-broker-configs--brokerconfigs_offsets.commit.timeout.ms)

  Offset commit will be delayed until all replicas for the offsets topic receive the commit or this timeout is reached. This is similar to the producer request timeout. This is applied to all the writes made by the coordinator.

| Type: | int |
| --- | --- |
| Default: | 5000 (5 seconds) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.load.buffer.size"></a>

  #### [offsets.load.buffer.size](#configuration-broker-configs--brokerconfigs_offsets.load.buffer.size)

  Batch size for reading from the offsets segments when loading group metadata into the cache (soft-limit, overridden if records are too large).

| Type: | int |
| --- | --- |
| Default: | 5242880 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.retention.check.interval.ms"></a>

  #### [offsets.retention.check.interval.ms](#configuration-broker-configs--brokerconfigs_offsets.retention.check.interval.ms)

  Frequency at which to check for stale offsets

| Type: | long |
| --- | --- |
| Default: | 600000 (10 minutes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.retention.minutes"></a>

  #### [offsets.retention.minutes](#configuration-broker-configs--brokerconfigs_offsets.retention.minutes)

  For subscribed consumers, committed offset of a specific partition will be expired and discarded when 1) this retention period has elapsed after the consumer group loses all its consumers (i.e. becomes empty); 2) this retention period has elapsed since the last time an offset is committed for the partition and the group is no longer subscribed to the corresponding topic. For standalone consumers (using manual assignment), offsets will be expired after this retention period has elapsed since the time of last commit. Note that when a group is deleted via the delete-group request, its committed offsets will also be deleted without extra retention period; also when a topic is deleted via the delete-topic request, upon propagated metadata update any group's committed offsets for that topic will also be deleted without extra retention period.

| Type: | int |
| --- | --- |
| Default: | 10080 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.topic.compression.codec"></a>

  #### [offsets.topic.compression.codec](#configuration-broker-configs--brokerconfigs_offsets.topic.compression.codec)

  Compression codec for the offsets topic - compression may be used to achieve "atomic" commits.

| Type: | int |
| --- | --- |
| Default: | 0 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.topic.num.partitions"></a>

  #### [offsets.topic.num.partitions](#configuration-broker-configs--brokerconfigs_offsets.topic.num.partitions)

  The number of partitions for the offset commit topic (should not change after deployment).

| Type: | int |
| --- | --- |
| Default: | 50 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.topic.replication.factor"></a>

  #### [offsets.topic.replication.factor](#configuration-broker-configs--brokerconfigs_offsets.topic.replication.factor)

  The replication factor for the offsets topic (set higher to ensure availability). Internal topic creation will fail until the cluster size meets this replication factor requirement.

| Type: | short |
| --- | --- |
| Default: | 3 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--offsets.topic.segment.bytes"></a>

  #### [offsets.topic.segment.bytes](#configuration-broker-configs--brokerconfigs_offsets.topic.segment.bytes)

  The offsets topic segment bytes should be kept relatively small in order to facilitate faster log compaction and cache loads.

| Type: | int |
| --- | --- |
| Default: | 104857600 (100 mebibytes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--queued.max.requests"></a>

  #### [queued.max.requests](#configuration-broker-configs--brokerconfigs_queued.max.requests)

  The number of queued requests allowed for data-plane, before blocking the network threads

| Type: | int |
| --- | --- |
| Default: | 500 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.fetch.min.bytes"></a>

  #### [replica.fetch.min.bytes](#configuration-broker-configs--brokerconfigs_replica.fetch.min.bytes)

  Minimum bytes expected for each fetch response. If not enough bytes, wait up to `replica.fetch.wait.max.ms` (broker config). Even if the total data available in the broker exceeds replica.fetch.min.bytes, the actual returned size may still be less than this value due to per-partition limits replica.fetch.max.bytes and max returned limits replica.fetch.response.max.bytes

| Type: | int |
| --- | --- |
| Default: | 1 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.fetch.wait.max.ms"></a>

  #### [replica.fetch.wait.max.ms](#configuration-broker-configs--brokerconfigs_replica.fetch.wait.max.ms)

  The maximum wait time for each fetcher request issued by follower replicas. This value should always be less than the replica.lag.time.max.ms at all times to prevent frequent shrinking of ISR for low throughput topics

| Type: | int |
| --- | --- |
| Default: | 500 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.high.watermark.checkpoint.interval.ms"></a>

  #### [replica.high.watermark.checkpoint.interval.ms](#configuration-broker-configs--brokerconfigs_replica.high.watermark.checkpoint.interval.ms)

  The frequency with which the high watermark is saved out to disk

| Type: | long |
| --- | --- |
| Default: | 5000 (5 seconds) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.lag.time.max.ms"></a>

  #### [replica.lag.time.max.ms](#configuration-broker-configs--brokerconfigs_replica.lag.time.max.ms)

  If a follower hasn't sent any fetch requests or hasn't consumed up to the leader's log end offset for at least this time, the leader will remove the follower from ISR

| Type: | long |
| --- | --- |
| Default: | 30000 (30 seconds) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.socket.receive.buffer.bytes"></a>

  #### [replica.socket.receive.buffer.bytes](#configuration-broker-configs--brokerconfigs_replica.socket.receive.buffer.bytes)

  The socket receive buffer for network requests to the leader for replicating data

| Type: | int |
| --- | --- |
| Default: | 65536 (64 kibibytes) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--replica.socket.timeout.ms"></a>

  #### [replica.socket.timeout.ms](#configuration-broker-configs--brokerconfigs_replica.socket.timeout.ms)

  The socket timeout for network requests. Its value should be at least replica.fetch.wait.max.ms

| Type: | int |
| --- | --- |
| Default: | 30000 (30 seconds) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--request.timeout.ms"></a>

  #### [request.timeout.ms](#configuration-broker-configs--brokerconfigs_request.timeout.ms)

  The configuration controls the maximum amount of time the client will wait for the response of a request. If the response is not received before the timeout elapses the client will resend the request if necessary or fail the request if retries are exhausted.

| Type: | int |
| --- | --- |
| Default: | 30000 (30 seconds) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--sasl.mechanism.controller.protocol"></a>

  #### [sasl.mechanism.controller.protocol](#configuration-broker-configs--brokerconfigs_sasl.mechanism.controller.protocol)

  SASL mechanism used for communication with controllers. Default is GSSAPI.

| Type: | string |
| --- | --- |
| Default: | GSSAPI |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.load.buffer.size"></a>

  #### [share.coordinator.load.buffer.size](#configuration-broker-configs--brokerconfigs_share.coordinator.load.buffer.size)

  Batch size for reading from the share-group state topic when loading state information into the cache (soft-limit, overridden if records are too large).

| Type: | int |
| --- | --- |
| Default: | 5242880 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.state.topic.compression.codec"></a>

  #### [share.coordinator.state.topic.compression.codec](#configuration-broker-configs--brokerconfigs_share.coordinator.state.topic.compression.codec)

  Compression codec for the share-group state topic.

| Type: | int |
| --- | --- |
| Default: | 0 |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.state.topic.min.isr"></a>

  #### [share.coordinator.state.topic.min.isr](#configuration-broker-configs--brokerconfigs_share.coordinator.state.topic.min.isr)

  Overridden min.insync.replicas for the share-group state topic.

| Type: | short |
| --- | --- |
| Default: | 2 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.state.topic.num.partitions"></a>

  #### [share.coordinator.state.topic.num.partitions](#configuration-broker-configs--brokerconfigs_share.coordinator.state.topic.num.partitions)

  The number of partitions for the share-group state topic (should not change after deployment).

| Type: | int |
| --- | --- |
| Default: | 50 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.state.topic.replication.factor"></a>

  #### [share.coordinator.state.topic.replication.factor](#configuration-broker-configs--brokerconfigs_share.coordinator.state.topic.replication.factor)

  Replication factor for the share-group state topic. Topic creation will fail until the cluster size meets this replication factor requirement.

| Type: | short |
| --- | --- |
| Default: | 3 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.state.topic.segment.bytes"></a>

  #### [share.coordinator.state.topic.segment.bytes](#configuration-broker-configs--brokerconfigs_share.coordinator.state.topic.segment.bytes)

  The log segment size for the share-group state topic.

| Type: | int |
| --- | --- |
| Default: | 104857600 (100 mebibytes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--share.coordinator.write.timeout.ms"></a>

  #### [share.coordinator.write.timeout.ms](#configuration-broker-configs--brokerconfigs_share.coordinator.write.timeout.ms)

  The duration in milliseconds that the share coordinator will wait for all replicas of the share-group state topic to receive a write.

| Type: | int |
| --- | --- |
| Default: | 5000 (5 seconds) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--socket.receive.buffer.bytes"></a>

  #### [socket.receive.buffer.bytes](#configuration-broker-configs--brokerconfigs_socket.receive.buffer.bytes)

  The SO\_RCVBUF buffer of the socket server sockets. If the value is -1, the OS default will be used.

| Type: | int |
| --- | --- |
| Default: | 102400 (100 kibibytes) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--socket.request.max.bytes"></a>

  #### [socket.request.max.bytes](#configuration-broker-configs--brokerconfigs_socket.request.max.bytes)

  The maximum number of bytes in a socket request

| Type: | int |
| --- | --- |
| Default: | 104857600 (100 mebibytes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--socket.send.buffer.bytes"></a>

  #### [socket.send.buffer.bytes](#configuration-broker-configs--brokerconfigs_socket.send.buffer.bytes)

  The SO\_SNDBUF buffer of the socket server sockets. If the value is -1, the OS default will be used.

| Type: | int |
| --- | --- |
| Default: | 102400 (100 kibibytes) |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.max.timeout.ms"></a>

  #### [transaction.max.timeout.ms](#configuration-broker-configs--brokerconfigs_transaction.max.timeout.ms)

  The maximum allowed timeout for transactions. If a client’s requested transaction time exceed this, then the broker will return an error in InitProducerIdRequest. This prevents a client from too large of a timeout, which can stall consumers reading from topics included in the transaction.

| Type: | int |
| --- | --- |
| Default: | 900000 (15 minutes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.state.log.load.buffer.size"></a>

  #### [transaction.state.log.load.buffer.size](#configuration-broker-configs--brokerconfigs_transaction.state.log.load.buffer.size)

  Batch size for reading from the transaction log segments when loading producer ids and transactions into the cache (soft-limit, overridden if records are too large).

| Type: | int |
| --- | --- |
| Default: | 5242880 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.state.log.min.isr"></a>

  #### [transaction.state.log.min.isr](#configuration-broker-configs--brokerconfigs_transaction.state.log.min.isr)

  The minimum number of replicas that must acknowledge a write to transaction topic in order to be considered successful.

| Type: | int |
| --- | --- |
| Default: | 2 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.state.log.num.partitions"></a>

  #### [transaction.state.log.num.partitions](#configuration-broker-configs--brokerconfigs_transaction.state.log.num.partitions)

  The number of partitions for the transaction topic (should not change after deployment).

| Type: | int |
| --- | --- |
| Default: | 50 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.state.log.replication.factor"></a>

  #### [transaction.state.log.replication.factor](#configuration-broker-configs--brokerconfigs_transaction.state.log.replication.factor)

  The replication factor for the transaction topic (set higher to ensure availability). Internal topic creation will fail until the cluster size meets this replication factor requirement.

| Type: | short |
| --- | --- |
| Default: | 3 |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transaction.state.log.segment.bytes"></a>

  #### [transaction.state.log.segment.bytes](#configuration-broker-configs--brokerconfigs_transaction.state.log.segment.bytes)

  The transaction topic segment bytes should be kept relatively small in order to facilitate faster log compaction and cache loads

| Type: | int |
| --- | --- |
| Default: | 104857600 (100 mebibytes) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--transactional.id.expiration.ms"></a>

  #### [transactional.id.expiration.ms](#configuration-broker-configs--brokerconfigs_transactional.id.expiration.ms)

  The time in ms that the transaction coordinator will wait without receiving any transaction status updates for the current transaction before expiring its transactional id. Transactional IDs will not expire while a the transaction is still ongoing.

| Type: | int |
| --- | --- |
| Default: | 604800000 (7 days) |
| Valid Values: | [1,...] |
| Importance: | high |
| Update Mode: | read-only |

-

<a id="configuration-broker-configs--unclean.leader.election.enable"></a>

  #### [unclean.leader.election.enable](#configuration-broker-configs--brokerconfigs_unclean.leader.election.enable)

  Indicates whether to enable replicas not in the ISR set to be elected as leader as a last resort, even though doing so may result in data loss

  Note: In KRaft mode, when enabling this config dynamically, it needs to wait for the unclean leader election thread to trigger election periodically (default is 5 minutes). Please run `kafka-leader-election.sh` with `unclean` option to trigger the unclean leader election immediately if needed.

| Type: | boolean |
| --- | --- |
| Default: | false |
| Valid Values: |  |
| Importance: | high |
| Update Mode: | cluster-wide |

-

<a id="configuration-broker-configs--broker.heartbeat.interval.ms"></a>

  #### [broker.heartbeat.interval.ms](#configuration-broker-configs--brokerconfigs_broker.heartbeat.interval.ms)

  The length of time in milliseconds between broker heartbeats.

| Type: | int |
| --- | --- |
| Default: | 2000 (2 seconds) |
| Valid Values: |  |

<a id="configuration-topic-configs"></a>

<a id="configuration-topic-configs--topic-configs"></a>

# Topic Configs

Topic Configs

Configurations pertinent to topics have both a server default as well an optional per-topic override. If no per-topic configuration is given the server default is used. The override can be set at topic creation time by giving one or more `--config` options. This example creates a topic named *my-topic* with a custom max message size and flush rate:

```bash
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic --partitions 1 \ --replication-factor 1 --config max.message.bytes=64000 --config flush.messages=1
```

Overrides can also be changed or set later using the alter configs command. This example updates the max message size for *my-topic* :

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic \ --alter --add-config max.message.bytes=128000
```

To check overrides set on the topic you can do

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic --describe
```

To remove an override you can do

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my-topic \ --alter --delete-config max.message.bytes
```

Below is the topic configuration. The server’s default configuration for this property is given under the Server Default Property heading. A given server default config value only applies to a topic if it does not have an explicit topic config override.

-

<a id="configuration-topic-configs--cleanup.policy"></a>

  #### [cleanup.policy](#configuration-topic-configs--topicconfigs_cleanup.policy)

  This config designates the retention policy to use on log segments. The "delete" policy (which is the default) will discard old segments when their retention time or size limit has been reached. The "compact" policy will enable [log compaction](#configuration-topic-configs--compaction), which retains the latest value for each key. It is also possible to specify both policies in a comma-separated list (e.g. "delete,compact"). In this case, old segments will be discarded per the retention time and size configuration, while retained segments will be compacted. An empty list means infinite retention - no cleanup policies will be applied and log segments will be retained indefinitely. Note that with remote storage enabled, local retention limits (log.local.retention.ms and log.local.retention.bytes) are still applied to local segments.

| Type: | list |
| --- | --- |
| Default: | delete |
| Valid Values: | [compact, delete] |
| Server Default Property: | log.cleanup.policy |

<a id="configuration-group-configs"></a>

<a id="configuration-group-configs--group-configs"></a>

# Group Configs

Group Configs

Below is the group configuration:

-

<a id="configuration-group-configs--consumer.assignment.interval.ms"></a>

  #### [consumer.assignment.interval.ms](#configuration-group-configs--groupconfigs_consumer.assignment.interval.ms)

  The interval between assignment updates for a consumer group.

| Type: | int |
| --- | --- |
| Default: | 1000 (1 second) |
| Valid Values: | [0,...] |

<a id="configuration-producer-configs"></a>

<a id="configuration-producer-configs--producer-configs"></a>

# Producer Configs

Producer Configs

Below is the producer configuration:

-

<a id="configuration-producer-configs--bootstrap.servers"></a>

  #### [bootstrap.servers](#configuration-producer-configs--producerconfigs_bootstrap.servers)

  A list of host/port pairs used to establish the initial connection to the Kafka cluster. Clients use this list to bootstrap and discover the full set of Kafka brokers. While the order of servers in the list does not matter, we recommend including more than one server to ensure resilience if any servers are down. This list does not need to contain the entire set of brokers, as Kafka clients automatically manage and update connections to the cluster efficiently. This list must be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--key.serializer"></a>

  #### [key.serializer](#configuration-producer-configs--producerconfigs_key.serializer)

  Serializer class for key that implements the `org.apache.kafka.common.serialization.Serializer` interface.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--value.serializer"></a>

  #### [value.serializer](#configuration-producer-configs--producerconfigs_value.serializer)

  Serializer class for value that implements the `org.apache.kafka.common.serialization.Serializer` interface.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--buffer.memory"></a>

  #### [buffer.memory](#configuration-producer-configs--producerconfigs_buffer.memory)

  The total bytes of memory the producer can use to buffer records waiting to be sent to the server. If records are sent faster than they can be delivered to the server the producer will block for `max.block.ms` after which it will fail with an exception.

  This setting should correspond roughly to the total memory the producer will use, but is not a hard bound since not all memory the producer uses is used for buffering. Some additional memory will be used for compression (if compression is enabled) as well as for maintaining in-flight requests.

| Type: | long |
| --- | --- |
| Default: | 33554432 |
| Valid Values: | [0,...] |
| Importance: | high |

-

<a id="configuration-producer-configs--compression.type"></a>

  #### [compression.type](#configuration-producer-configs--producerconfigs_compression.type)

  The compression type for all data generated by the producer. The default is none (i.e. no compression). Valid values are `none`, `gzip`, `snappy`, `lz4`, or `zstd`. Compression is of full batches of data, so the efficacy of batching will also impact the compression ratio (more batching means better compression).

| Type: | string |
| --- | --- |
| Default: | none |
| Valid Values: | [none, gzip, snappy, lz4, zstd] |
| Importance: | high |

-

<a id="configuration-producer-configs--retries"></a>

  #### [retries](#configuration-producer-configs--producerconfigs_retries)

  Number of times to retry a request that fails with a transient error. Setting a value greater than zero will cause the client to resend any record whose send fails with a potentially transient error. Requests will be retried this many times until they succeed, fail with a non-transient error, or the `delivery.timeout.ms` expires. Note that this automatic retry will simply resend the same record upon receiving the error. Setting a value of zero will disable this automatic retry behaviour, so that the transient errors will be propagated to the application to be handled. Users should generally prefer to leave this config unset and instead use `delivery.timeout.ms` to control retry behavior.

  Enabling idempotence requires this config value to be greater than 0. If conflicting configurations are set and idempotence is not explicitly enabled, idempotence is disabled.

  Allowing retries while setting `enable.idempotence` to `false` and `max.in.flight.requests.per.connection` to greater than 1 will potentially change the ordering of records because if two batches are sent to a single partition, and the first fails and is retried but the second succeeds, then the records in the second batch may appear first.

| Type: | int |
| --- | --- |
| Default: | 2147483647 |
| Valid Values: | [0,...,2147483647] |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.key.password"></a>

  #### [ssl.key.password](#configuration-producer-configs--producerconfigs_ssl.key.password)

  The password of the private key in the key store file or the PEM key specified in 'ssl.keystore.key'.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.keystore.certificate.chain"></a>

  #### [ssl.keystore.certificate.chain](#configuration-producer-configs--producerconfigs_ssl.keystore.certificate.chain)

  Certificate chain in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with a list of X.509 certificates

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.keystore.key"></a>

  #### [ssl.keystore.key](#configuration-producer-configs--producerconfigs_ssl.keystore.key)

  Private key in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with PKCS#8 keys. If the key is encrypted, key password must be specified using 'ssl.key.password'

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.keystore.location"></a>

  #### [ssl.keystore.location](#configuration-producer-configs--producerconfigs_ssl.keystore.location)

  The location of the key store file. This is optional for client and can be used for two-way authentication for client.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.keystore.password"></a>

  #### [ssl.keystore.password](#configuration-producer-configs--producerconfigs_ssl.keystore.password)

  The store password for the key store file. This is optional for client and only needed if 'ssl.keystore.location' is configured. Key store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.truststore.certificates"></a>

  #### [ssl.truststore.certificates](#configuration-producer-configs--producerconfigs_ssl.truststore.certificates)

  Trusted certificates in the format specified by 'ssl.truststore.type'. Default SSL engine factory supports only PEM format with X.509 certificates.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.truststore.location"></a>

  #### [ssl.truststore.location](#configuration-producer-configs--producerconfigs_ssl.truststore.location)

  The location of the trust store file.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--ssl.truststore.password"></a>

  #### [ssl.truststore.password](#configuration-producer-configs--producerconfigs_ssl.truststore.password)

  The password for the trust store file. If a password is not set, trust store file configured will still be used, but integrity checking is disabled. Trust store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-producer-configs--batch.size"></a>

  #### [batch.size](#configuration-producer-configs--producerconfigs_batch.size)

  The producer will attempt to batch records together into fewer requests whenever multiple records are being sent to the same partition. This helps performance on both the client and the server. This configuration controls the default batch size in bytes.

  No attempt will be made to batch records larger than this size.

  Requests sent to brokers will contain multiple batches, one for each partition with data available to be sent.

  A small batch size will make batching less common and may reduce throughput (a batch size of zero will disable batching entirely). A very large batch size may use memory a bit more wastefully as we will always allocate a buffer of the specified batch size in anticipation of additional records.

  Note: This setting gives the upper bound of the batch size to be sent. If we have fewer than this many bytes accumulated for this partition, we will 'linger' for the `linger.ms` time waiting for more records to show up. This `linger.ms` setting defaults to 5, which means the producer will wait for 5ms or until the record batch is of `batch.size` (whichever happens first) before sending the record batch. Note that broker backpressure can result in a higher effective linger time than this setting. The default changed from 0 to 5 in Apache Kafka 4.0 as the efficiency gains from larger batches typically result in similar or lower producer latency despite the increased linger.

| Type: | int |
| --- | --- |
| Default: | 16384 |
| Valid Values: | [0,...] |

<a id="configuration-consumer-configs"></a>

<a id="configuration-consumer-configs--consumer-and-share-consumer-configs"></a>

# Consumer and Share Consumer Configs

Consumer and Share Consumer Configs

Below is the consumer and share consumer configuration:

-

<a id="configuration-consumer-configs--bootstrap.servers"></a>

  #### [bootstrap.servers](#configuration-consumer-configs--consumerconfigs_bootstrap.servers)

  A list of host/port pairs used to establish the initial connection to the Kafka cluster. Clients use this list to bootstrap and discover the full set of Kafka brokers. While the order of servers in the list does not matter, we recommend including more than one server to ensure resilience if any servers are down. This list does not need to contain the entire set of brokers, as Kafka clients automatically manage and update connections to the cluster efficiently. This list must be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--key.deserializer"></a>

  #### [key.deserializer](#configuration-consumer-configs--consumerconfigs_key.deserializer)

  Deserializer class for key that implements the `org.apache.kafka.common.serialization.Deserializer` interface.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--value.deserializer"></a>

  #### [value.deserializer](#configuration-consumer-configs--consumerconfigs_value.deserializer)

  Deserializer class for value that implements the `org.apache.kafka.common.serialization.Deserializer` interface.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--fetch.min.bytes"></a>

  #### [fetch.min.bytes](#configuration-consumer-configs--consumerconfigs_fetch.min.bytes)

  The minimum amount of data the server should return for a fetch request. If insufficient data is available the request will wait for that much data to accumulate before answering the request. The default setting of 1 byte means that fetch requests are answered as soon as that many byte(s) of data is available or the fetch request times out waiting for data to arrive. Setting this to a larger value will cause the server to wait for larger amounts of data to accumulate which can improve server throughput a bit at the cost of some additional latency. Even if the total data available in the broker exceeds fetch.min.bytes, the actual returned size may still be less than this value due to per-partition limits max.partition.fetch.bytes and max returned limits fetch.max.bytes.

| Type: | int |
| --- | --- |
| Default: | 1 |
| Valid Values: | [0,...] |
| Importance: | high |

-

<a id="configuration-consumer-configs--group.id"></a>

  #### [group.id](#configuration-consumer-configs--consumerconfigs_group.id)

  A unique string that identifies the consumer group this consumer belongs to. This property is required if the consumer uses either the group management functionality by using `subscribe(topic)` or the Kafka-based offset management strategy.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--group.protocol"></a>

  #### [group.protocol](#configuration-consumer-configs--consumerconfigs_group.protocol)

  The group protocol that the consumer uses. The supported values are `classic` or `consumer`. The default value is `classic`.

| Type: | string |
| --- | --- |
| Default: | classic |
| Valid Values: | (case insensitive) [CONSUMER, CLASSIC] |
| Importance: | high |

-

<a id="configuration-consumer-configs--heartbeat.interval.ms"></a>

  #### [heartbeat.interval.ms](#configuration-consumer-configs--consumerconfigs_heartbeat.interval.ms)

  The expected time between heartbeats to the consumer coordinator when using Kafka's group management facilities. Heartbeats are used to ensure that the consumer's session stays active and to facilitate rebalancing when new consumers join or leave the group. This config is only supported if `group.protocol` is set to "classic". In that case, the value must be set lower than `session.timeout.ms`, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances.If `group.protocol` is set to "consumer", this config is not supported, as the heartbeat interval is controlled by the broker with `group.consumer.heartbeat.interval.ms`.

| Type: | int |
| --- | --- |
| Default: | 3000 (3 seconds) |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--max.partition.fetch.bytes"></a>

  #### [max.partition.fetch.bytes](#configuration-consumer-configs--consumerconfigs_max.partition.fetch.bytes)

  The maximum amount of data per-partition the server will return. Records are fetched in batches by the consumer. If the first record batch in the first non-empty partition of the fetch is larger than this limit, the batch will still be returned to ensure that the consumer can make progress. The maximum record batch size accepted by the broker is defined via `message.max.bytes` (broker config) or `max.message.bytes` (topic config). See fetch.max.bytes for limiting the consumer request size.

| Type: | int |
| --- | --- |
| Default: | 1048576 (1 mebibyte) |
| Valid Values: | [0,...] |
| Importance: | high |

-

<a id="configuration-consumer-configs--session.timeout.ms"></a>

  #### [session.timeout.ms](#configuration-consumer-configs--consumerconfigs_session.timeout.ms)

  The timeout used to detect client failures when using Kafka's group management facility. The client sends periodic heartbeats to indicate its liveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker will remove this client from the group and initiate a rebalance. Note that the value must be in the allowable range as configured in the broker configuration by `group.min.session.timeout.ms` and `group.max.session.timeout.ms`. Note that this client configuration is not supported when `group.protocol` is set to "consumer". In that case, session timeout is controlled by the broker config `group.consumer.session.timeout.ms`.

| Type: | int |
| --- | --- |
| Default: | 45000 (45 seconds) |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.key.password"></a>

  #### [ssl.key.password](#configuration-consumer-configs--consumerconfigs_ssl.key.password)

  The password of the private key in the key store file or the PEM key specified in 'ssl.keystore.key'.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.keystore.certificate.chain"></a>

  #### [ssl.keystore.certificate.chain](#configuration-consumer-configs--consumerconfigs_ssl.keystore.certificate.chain)

  Certificate chain in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with a list of X.509 certificates

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.keystore.key"></a>

  #### [ssl.keystore.key](#configuration-consumer-configs--consumerconfigs_ssl.keystore.key)

  Private key in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with PKCS#8 keys. If the key is encrypted, key password must be specified using 'ssl.key.password'

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.keystore.location"></a>

  #### [ssl.keystore.location](#configuration-consumer-configs--consumerconfigs_ssl.keystore.location)

  The location of the key store file. This is optional for client and can be used for two-way authentication for client.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.keystore.password"></a>

  #### [ssl.keystore.password](#configuration-consumer-configs--consumerconfigs_ssl.keystore.password)

  The store password for the key store file. This is optional for client and only needed if 'ssl.keystore.location' is configured. Key store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.truststore.certificates"></a>

  #### [ssl.truststore.certificates](#configuration-consumer-configs--consumerconfigs_ssl.truststore.certificates)

  Trusted certificates in the format specified by 'ssl.truststore.type'. Default SSL engine factory supports only PEM format with X.509 certificates.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.truststore.location"></a>

  #### [ssl.truststore.location](#configuration-consumer-configs--consumerconfigs_ssl.truststore.location)

  The location of the trust store file.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--ssl.truststore.password"></a>

  #### [ssl.truststore.password](#configuration-consumer-configs--consumerconfigs_ssl.truststore.password)

  The password for the trust store file. If a password is not set, trust store file configured will still be used, but integrity checking is disabled. Trust store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-consumer-configs--allow.auto.create.topics"></a>

  #### [allow.auto.create.topics](#configuration-consumer-configs--consumerconfigs_allow.auto.create.topics)

  Allow automatic topic creation on the broker when subscribing to or assigning a topic. A topic being subscribed to will be automatically created only if the broker allows for it using `auto.create.topics.enable` broker configuration.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |

<a id="configuration-kafka-connect-configs"></a>

<a id="configuration-kafka-connect-configs--kafka-connect-configs"></a>

# Kafka Connect Configs

Kafka Connect Configs

Below is the Kafka Connect framework configuration.

-

<a id="configuration-kafka-connect-configs--bootstrap.servers"></a>

  #### [bootstrap.servers](#configuration-kafka-connect-configs--connectconfigs_bootstrap.servers)

  A list of host/port pairs used to establish the initial connection to the Kafka cluster. Clients use this list to bootstrap and discover the full set of Kafka brokers. While the order of servers in the list does not matter, we recommend including more than one server to ensure resilience if any servers are down. This list does not need to contain the entire set of brokers, as Kafka clients automatically manage and update connections to the cluster efficiently. This list must be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--config.storage.topic"></a>

  #### [config.storage.topic](#configuration-kafka-connect-configs--connectconfigs_config.storage.topic)

  The name of the Kafka topic where connector configurations are stored

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--group.id"></a>

  #### [group.id](#configuration-kafka-connect-configs--connectconfigs_group.id)

  A unique string that identifies the Connect cluster group this worker belongs to.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--key.converter"></a>

  #### [key.converter](#configuration-kafka-connect-configs--connectconfigs_key.converter)

  Converter class used to convert between Kafka Connect format and the serialized form that is written to Kafka. This controls the format of the keys in messages written to or read from Kafka, and since this is independent of connectors it allows any connector to work with any serialization format. Examples of common formats include JSON and Avro.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--offset.storage.topic"></a>

  #### [offset.storage.topic](#configuration-kafka-connect-configs--connectconfigs_offset.storage.topic)

  The name of the Kafka topic where source connector offsets are stored

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--status.storage.topic"></a>

  #### [status.storage.topic](#configuration-kafka-connect-configs--connectconfigs_status.storage.topic)

  The name of the Kafka topic where connector and task status are stored

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--value.converter"></a>

  #### [value.converter](#configuration-kafka-connect-configs--connectconfigs_value.converter)

  Converter class used to convert between Kafka Connect format and the serialized form that is written to Kafka. This controls the format of the values in messages written to or read from Kafka, and since this is independent of connectors it allows any connector to work with any serialization format. Examples of common formats include JSON and Avro.

| Type: | class |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--exactly.once.source.support"></a>

  #### [exactly.once.source.support](#configuration-kafka-connect-configs--connectconfigs_exactly.once.source.support)

  Whether to enable exactly-once support for source connectors in the cluster by using transactions to write source records and their source offsets, and by proactively fencing out old task generations before bringing up new ones. To enable exactly-once source support on a new cluster, set this property to 'enabled'. To enable support on an existing cluster, first set to 'preparing' on every worker in the cluster, then set to 'enabled'. A rolling upgrade may be used for both changes. For more information on this feature, see the [exactly-once source support documentation](https://kafka.apache.org/documentation.html#connect_exactlyoncesource).

| Type: | string |
| --- | --- |
| Default: | disabled |
| Valid Values: | (case insensitive) [DISABLED, ENABLED, PREPARING] |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--heartbeat.interval.ms"></a>

  #### [heartbeat.interval.ms](#configuration-kafka-connect-configs--connectconfigs_heartbeat.interval.ms)

  The expected time between heartbeats to the group coordinator when using Kafka's group management facilities. Heartbeats are used to ensure that the worker's session stays active and to facilitate rebalancing when new members join or leave the group. The value must be set lower than `session.timeout.ms`, but typically should be set no higher than 1/3 of that value. It can be adjusted even lower to control the expected time for normal rebalances.

| Type: | int |
| --- | --- |
| Default: | 3000 (3 seconds) |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--rebalance.timeout.ms"></a>

  #### [rebalance.timeout.ms](#configuration-kafka-connect-configs--connectconfigs_rebalance.timeout.ms)

  The maximum allowed time for each worker to join the group once a rebalance has begun. This is basically a limit on the amount of time needed for all tasks to flush any pending data and commit offsets. If the timeout is exceeded, then the worker will be removed from the group, which will cause offset commit failures.

| Type: | int |
| --- | --- |
| Default: | 60000 (1 minute) |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--session.timeout.ms"></a>

  #### [session.timeout.ms](#configuration-kafka-connect-configs--connectconfigs_session.timeout.ms)

  The timeout used to detect worker failures. The worker sends periodic heartbeats to indicate its liveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker will remove the worker from the group and initiate a rebalance. Note that the value must be in the allowable range as configured in the broker configuration by `group.min.session.timeout.ms` and `group.max.session.timeout.ms`.

| Type: | int |
| --- | --- |
| Default: | 10000 (10 seconds) |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.key.password"></a>

  #### [ssl.key.password](#configuration-kafka-connect-configs--connectconfigs_ssl.key.password)

  The password of the private key in the key store file or the PEM key specified in 'ssl.keystore.key'.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.keystore.certificate.chain"></a>

  #### [ssl.keystore.certificate.chain](#configuration-kafka-connect-configs--connectconfigs_ssl.keystore.certificate.chain)

  Certificate chain in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with a list of X.509 certificates

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.keystore.key"></a>

  #### [ssl.keystore.key](#configuration-kafka-connect-configs--connectconfigs_ssl.keystore.key)

  Private key in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with PKCS#8 keys. If the key is encrypted, key password must be specified using 'ssl.key.password'

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.keystore.location"></a>

  #### [ssl.keystore.location](#configuration-kafka-connect-configs--connectconfigs_ssl.keystore.location)

  The location of the key store file. This is optional for client and can be used for two-way authentication for client.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.keystore.password"></a>

  #### [ssl.keystore.password](#configuration-kafka-connect-configs--connectconfigs_ssl.keystore.password)

  The store password for the key store file. This is optional for client and only needed if 'ssl.keystore.location' is configured. Key store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.truststore.certificates"></a>

  #### [ssl.truststore.certificates](#configuration-kafka-connect-configs--connectconfigs_ssl.truststore.certificates)

  Trusted certificates in the format specified by 'ssl.truststore.type'. Default SSL engine factory supports only PEM format with X.509 certificates.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.truststore.location"></a>

  #### [ssl.truststore.location](#configuration-kafka-connect-configs--connectconfigs_ssl.truststore.location)

  The location of the trust store file.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--ssl.truststore.password"></a>

  #### [ssl.truststore.password](#configuration-kafka-connect-configs--connectconfigs_ssl.truststore.password)

  The password for the trust store file. If a password is not set, trust store file configured will still be used, but integrity checking is disabled. Trust store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-connect-configs--client.dns.lookup"></a>

  #### [client.dns.lookup](#configuration-kafka-connect-configs--connectconfigs_client.dns.lookup)

  Controls how the client uses DNS lookups. If set to `use_all_dns_ips`, connect to each returned IP address in sequence until a successful connection is established. After a disconnection, the next IP is used. Once all IPs have been used once, the client resolves the IP(s) from the hostname again (both the JVM and the OS cache DNS name lookups, however). If set to `resolve_canonical_bootstrap_servers_only`, resolve each bootstrap address into a list of canonical names. After the bootstrap phase, this behaves the same as `use_all_dns_ips`.

| Type: | string |
| --- | --- |
| Default: | use\_all\_dns\_ips |
| Valid Values: | [use\_all\_dns\_ips, resolve\_canonical\_bootstrap\_servers\_only] |

<a id="configuration-kafka-streams-configs"></a>

<a id="configuration-kafka-streams-configs--kafka-streams-configs"></a>

# Kafka Streams Configs

Kafka Streams Configs

Below is the Kafka Streams client library configuration.

-

<a id="configuration-kafka-streams-configs--application.id"></a>

  #### [application.id](#configuration-kafka-streams-configs--streamsconfigs_application.id)

  An identifier for the stream processing application. Must be unique within the Kafka cluster. It is used as 1) the default client-id prefix, 2) the group-id for membership management, 3) the changelog topic prefix.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--bootstrap.servers"></a>

  #### [bootstrap.servers](#configuration-kafka-streams-configs--streamsconfigs_bootstrap.servers)

  A list of host/port pairs used to establish the initial connection to the Kafka cluster. Clients use this list to bootstrap and discover the full set of Kafka brokers. While the order of servers in the list does not matter, we recommend including more than one server to ensure resilience if any servers are down. This list does not need to contain the entire set of brokers, as Kafka clients automatically manage and update connections to the cluster efficiently. This list must be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--ensure.explicit.internal.resource.naming"></a>

  #### [ensure.explicit.internal.resource.naming](#configuration-kafka-streams-configs--streamsconfigs_ensure.explicit.internal.resource.naming)

  Whether to enforce explicit naming for all internal resources of the topology, including internal topics (e.g., changelog and repartition topics) and their associated state stores. When enabled, the application will refuse to start if any internal resource has an auto-generated name.

| Type: | boolean |
| --- | --- |
| Default: | false |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--num.standby.replicas"></a>

  #### [num.standby.replicas](#configuration-kafka-streams-configs--streamsconfigs_num.standby.replicas)

  The number of standby replicas for each task.

| Type: | int |
| --- | --- |
| Default: | 0 |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--processing.exception.handler.global.enabled"></a>

  #### [processing.exception.handler.global.enabled](#configuration-kafka-streams-configs--streamsconfigs_processing.exception.handler.global.enabled)

  Whether to use the configured `processing.exception.handler` during global store/KTable processing. Disabled by default. This config will be removed in Kafka Streams 5.0, where global exception handling will be enabled by default

| Type: | boolean |
| --- | --- |
| Default: | false |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--state.dir"></a>

  #### [state.dir](#configuration-kafka-streams-configs--streamsconfigs_state.dir)

  Directory location for state store. This path must be unique for each streams instance sharing the same underlying filesystem. Note that if not configured, then the default location will be different in each environment as it is computed using System.getProperty("java.io.tmpdir")

| Type: | string |
| --- | --- |
| Default: | ${java.io.tmpdir} |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-kafka-streams-configs--acceptable.recovery.lag"></a>

  #### [acceptable.recovery.lag](#configuration-kafka-streams-configs--streamsconfigs_acceptable.recovery.lag)

  The maximum acceptable lag (number of offsets to catch up) for a client to be considered caught-up enough to receive an active task assignment. Upon assignment, it will still restore the rest of the changelog before processing. To avoid a pause in processing during rebalances, this config should correspond to a recovery time of well under a minute for a given workload. Must be at least 0.

| Type: | long |
| --- | --- |
| Default: | 10000 |
| Valid Values: | [0,...] |

<a id="configuration-admin-configs"></a>

<a id="configuration-admin-configs--admin-configs"></a>

# Admin Configs

Admin Configs

Below is the Kafka Admin client library configuration.

-

<a id="configuration-admin-configs--bootstrap.controllers"></a>

  #### [bootstrap.controllers](#configuration-admin-configs--adminclientconfigs_bootstrap.controllers)

  A list of host/port pairs to use for establishing the initial connection to the KRaft controller quorum. This list should be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--bootstrap.servers"></a>

  #### [bootstrap.servers](#configuration-admin-configs--adminclientconfigs_bootstrap.servers)

  A list of host/port pairs used to establish the initial connection to the Kafka cluster. Clients use this list to bootstrap and discover the full set of Kafka brokers. While the order of servers in the list does not matter, we recommend including more than one server to ensure resilience if any servers are down. This list does not need to contain the entire set of brokers, as Kafka clients automatically manage and update connections to the cluster efficiently. This list must be in the form `host1:port1,host2:port2,...`.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.key.password"></a>

  #### [ssl.key.password](#configuration-admin-configs--adminclientconfigs_ssl.key.password)

  The password of the private key in the key store file or the PEM key specified in 'ssl.keystore.key'.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.keystore.certificate.chain"></a>

  #### [ssl.keystore.certificate.chain](#configuration-admin-configs--adminclientconfigs_ssl.keystore.certificate.chain)

  Certificate chain in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with a list of X.509 certificates

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.keystore.key"></a>

  #### [ssl.keystore.key](#configuration-admin-configs--adminclientconfigs_ssl.keystore.key)

  Private key in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with PKCS#8 keys. If the key is encrypted, key password must be specified using 'ssl.key.password'

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.keystore.location"></a>

  #### [ssl.keystore.location](#configuration-admin-configs--adminclientconfigs_ssl.keystore.location)

  The location of the key store file. This is optional for client and can be used for two-way authentication for client.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.keystore.password"></a>

  #### [ssl.keystore.password](#configuration-admin-configs--adminclientconfigs_ssl.keystore.password)

  The store password for the key store file. This is optional for client and only needed if 'ssl.keystore.location' is configured. Key store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.truststore.certificates"></a>

  #### [ssl.truststore.certificates](#configuration-admin-configs--adminclientconfigs_ssl.truststore.certificates)

  Trusted certificates in the format specified by 'ssl.truststore.type'. Default SSL engine factory supports only PEM format with X.509 certificates.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.truststore.location"></a>

  #### [ssl.truststore.location](#configuration-admin-configs--adminclientconfigs_ssl.truststore.location)

  The location of the trust store file.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--ssl.truststore.password"></a>

  #### [ssl.truststore.password](#configuration-admin-configs--adminclientconfigs_ssl.truststore.password)

  The password for the trust store file. If a password is not set, trust store file configured will still be used, but integrity checking is disabled. Trust store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-admin-configs--client.dns.lookup"></a>

  #### [client.dns.lookup](#configuration-admin-configs--adminclientconfigs_client.dns.lookup)

  Controls how the client uses DNS lookups. If set to `use_all_dns_ips`, connect to each returned IP address in sequence until a successful connection is established. After a disconnection, the next IP is used. Once all IPs have been used once, the client resolves the IP(s) from the hostname again (both the JVM and the OS cache DNS name lookups, however). If set to `resolve_canonical_bootstrap_servers_only`, resolve each bootstrap address into a list of canonical names. After the bootstrap phase, this behaves the same as `use_all_dns_ips`.

| Type: | string |
| --- | --- |
| Default: | use\_all\_dns\_ips |
| Valid Values: | [use\_all\_dns\_ips, resolve\_canonical\_bootstrap\_servers\_only] |

<a id="configuration-mirrormaker-configs"></a>

<a id="configuration-mirrormaker-configs--mirrormaker-configs"></a>

# MirrorMaker Configs

MirrorMaker Configs

Below is the configuration of the connectors that make up MirrorMaker 2.

<a id="configuration-mirrormaker-configs--mirrormaker-common-configs"></a>

## MirrorMaker Common Configs

Below is the common configuration that applies to all three connectors.

-

<a id="configuration-mirrormaker-configs--source.cluster.alias"></a>

  #### [source.cluster.alias](#configuration-mirrormaker-configs--mirror_connector_source.cluster.alias)

  Alias of source cluster

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.key.password"></a>

  #### [ssl.key.password](#configuration-mirrormaker-configs--mirror_connector_ssl.key.password)

  The password of the private key in the key store file or the PEM key specified in 'ssl.keystore.key'.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.keystore.certificate.chain"></a>

  #### [ssl.keystore.certificate.chain](#configuration-mirrormaker-configs--mirror_connector_ssl.keystore.certificate.chain)

  Certificate chain in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with a list of X.509 certificates

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.keystore.key"></a>

  #### [ssl.keystore.key](#configuration-mirrormaker-configs--mirror_connector_ssl.keystore.key)

  Private key in the format specified by 'ssl.keystore.type'. Default SSL engine factory supports only PEM format with PKCS#8 keys. If the key is encrypted, key password must be specified using 'ssl.key.password'

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.keystore.location"></a>

  #### [ssl.keystore.location](#configuration-mirrormaker-configs--mirror_connector_ssl.keystore.location)

  The location of the key store file. This is optional for client and can be used for two-way authentication for client.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.keystore.password"></a>

  #### [ssl.keystore.password](#configuration-mirrormaker-configs--mirror_connector_ssl.keystore.password)

  The store password for the key store file. This is optional for client and only needed if 'ssl.keystore.location' is configured. Key store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.truststore.certificates"></a>

  #### [ssl.truststore.certificates](#configuration-mirrormaker-configs--mirror_connector_ssl.truststore.certificates)

  Trusted certificates in the format specified by 'ssl.truststore.type'. Default SSL engine factory supports only PEM format with X.509 certificates.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.truststore.location"></a>

  #### [ssl.truststore.location](#configuration-mirrormaker-configs--mirror_connector_ssl.truststore.location)

  The location of the trust store file.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--ssl.truststore.password"></a>

  #### [ssl.truststore.password](#configuration-mirrormaker-configs--mirror_connector_ssl.truststore.password)

  The password for the trust store file. If a password is not set, trust store file configured will still be used, but integrity checking is disabled. Trust store password is not supported for PEM format.

| Type: | password |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--target.cluster.alias"></a>

  #### [target.cluster.alias](#configuration-mirrormaker-configs--mirror_connector_target.cluster.alias)

  Alias of target cluster. Used in metrics reporting.

| Type: | string |
| --- | --- |
| Default: | target |
| Valid Values: |  |
| Importance: | high |

-

<a id="configuration-mirrormaker-configs--sasl.client.callback.handler.class"></a>

  #### [sasl.client.callback.handler.class](#configuration-mirrormaker-configs--mirror_connector_sasl.client.callback.handler.class)

  The fully qualified name of a SASL client callback handler class that implements the AuthenticateCallbackHandler interface.

| Type: | class |
| --- | --- |
| Default: | null |
| Valid Values: |  |

<a id="configuration-system-properties"></a>

<a id="configuration-system-properties--system-properties"></a>

# System Properties

System Properties

Kafka supports some configuration that can be enabled through Java system properties. System properties are usually set by passing the -D flag to the Java virtual machine in which Kafka components are running. Below are the supported system properties.

-

<a id="configuration-system-properties--orgapachekafkasasloauthbearerallowedfiles"></a>
<a id="configuration-system-properties--org.apache.kafka.sasl.oauthbearer.allowed.files"></a>

  #### org.apache.kafka.sasl.oauthbearer.allowed.files

This system property is used to determine which files, if any, are allowed to be read by the SASL OAUTHBEARER plugin. This property accepts comma-separated list of files. By default the value is an empty list.

If users want to enable some files, users need to explicitly set the system property like below.

```bash
-Dorg.apache.kafka.sasl.oauthbearer.allowed.files=/tmp/token,/tmp/private_key.pem
```

| Since: | 4.1.0 |
| --- | --- |
| Default Value: |  |

-

<a id="configuration-system-properties--orgapachekafkasasloauthbearerallowedurls"></a>
<a id="configuration-system-properties--org.apache.kafka.sasl.oauthbearer.allowed.urls"></a>

  #### org.apache.kafka.sasl.oauthbearer.allowed.urls

This system property is used to set the allowed URLs as SASL OAUTHBEARER token or jwks endpoints. This property accepts comma-separated list of URLs. By default the value is an empty list.

If users want to enable some URLs, users need to explicitly set the system property like below.

```bash
-Dorg.apache.kafka.sasl.oauthbearer.allowed.urls=https://www.example.com,file:///tmp/token
```

| Since: | 4.0.0 |
| --- | --- |
| Default Value: |  |

-

<a id="configuration-system-properties--orgapachekafkadisallowedloginmodules"></a>
<a id="configuration-system-properties--org.apache.kafka.disallowed.login.modules"></a>

  #### org.apache.kafka.disallowed.login.modules

This system property is used to disable the problematic login modules usage in SASL JAAS configuration. This property accepts comma-separated list of loginModule names. By default **com.sun.security.auth.module.JndiLoginModule** and **com.sun.security.auth.module.LdapLoginModule** loginModule is disabled.

If users want to enable JndiLoginModule or LdapLoginModule, users need to explicitly reset the system property like below. We advise the users to validate configurations and only allow trusted JNDI configurations. For more details [CVE-2023-25194](https://kafka.apache.org/community/cve-list/#CVE-2023-25194).

```bash
-Dorg.apache.kafka.disallowed.login.modules=
```

To disable more loginModules, update the system property with comma-separated loginModule names. Make sure to explicitly add **JndiLoginModule** module name to the comma-separated list like below.

```bash
-Dorg.apache.kafka.disallowed.login.modules=com.sun.security.auth.module.JndiLoginModule,com.ibm.security.auth.module.LdapLoginModule,com.ibm.security.auth.module.Krb5LoginModule
```

| Since: | 3.4.0 |
| --- | --- |
| Default Value: | com.sun.security.auth.module.JndiLoginModule,com.sun.security.auth.module.LdapLoginModule |

-

<a id="configuration-system-properties--orgapachekafkaallowedloginmodules"></a>
<a id="configuration-system-properties--org.apache.kafka.allowed.login.modules"></a>

  #### org.apache.kafka.allowed.login.modules

If both properties are set, `org.apache.kafka.allowed.login.modules` takes precedence.

Since:

4.2.0

Default Value:

-

<a id="configuration-system-properties--orgapachekafkaautomaticconfigproviders"></a>
<a id="configuration-system-properties--org.apache.kafka.automatic.config.providers"></a>

  #### org.apache.kafka.automatic.config.providers

This system property controls the automatic loading of ConfigProvider implementations in Apache Kafka. ConfigProviders are used to dynamically supply configuration values from sources such as files, directories, or environment variables. This property accepts a comma-separated list of ConfigProvider names. By default, all built-in ConfigProviders are enabled, including **FileConfigProvider** , **DirectoryConfigProvider** , and **EnvVarConfigProvider**.

If users want to disable all automatic ConfigProviders, they need to explicitly set the system property as shown below. Disabling automatic ConfigProviders is recommended in environments where configuration data comes from untrusted sources or where increased security is required. For more details, see [CVE-2024-31141](https://kafka.apache.org/community/cve-list/#CVE-2024-31141).

```bash
-Dorg.apache.kafka.automatic.config.providers=none
```

To allow specific ConfigProviders, update the system property with a comma-separated list of fully qualified ConfigProvider class names. For example, to enable only the **EnvVarConfigProvider** , set the property as follows:

```bash
-Dorg.apache.kafka.automatic.config.providers=org.apache.kafka.common.config.provider.EnvVarConfigProvider
```

To use multiple ConfigProviders, include their names in a comma-separated list as shown below:

```bash
-Dorg.apache.kafka.automatic.config.providers=org.apache.kafka.common.config.provider.FileConfigProvider,org.apache.kafka.common.config.provider.EnvVarConfigProvider
```

| Since: | 3.8.0 |
| --- | --- |
| Default Value: | All built-in ConfigProviders are enabled |

<a id="configuration-tiered-storage-configs"></a>

<a id="configuration-tiered-storage-configs--tiered-storage-configs"></a>

# Tiered Storage Configs

Tiered Storage Configs

Below is the Tiered Storage configuration.

-

<a id="configuration-tiered-storage-configs--log.local.retention.bytes"></a>

  #### [log.local.retention.bytes](#configuration-tiered-storage-configs--remote_log_manager_log.local.retention.bytes)

  The maximum size of local log segments that can grow for a partition before it gets eligible for deletion. Default value is -2, it represents `log.retention.bytes` value to be used. The effective value should always be less than or equal to `log.retention.bytes` value.

| Type: | long |
| --- | --- |
| Default: | -2 |
| Valid Values: | [-2,...] |

<a id="configuration-configuration-providers"></a>

# Configuration Providers

---

<a id="design"></a>

<a id="design--design"></a>

# Design

---

<a id="design--design-2"></a>

##### [Design](#design-design)

<a id="design--protocol"></a>

##### [Protocol](#design-protocol)

<a id="design-design"></a>

<a id="design-design--design"></a>

# Design

<a id="design-design--motivation"></a>

## Motivation

We designed Kafka to be able to act as a unified platform for handling all the real-time data feeds a large company might have. To do this we had to think through a fairly broad set of use cases.

It would have to have high-throughput to support high volume event streams such as real-time log aggregation.

It would need to deal gracefully with large data backlogs to be able to support periodic data loads from offline systems.

It also meant the system would have to handle low-latency delivery to handle more traditional messaging use-cases.

We wanted to support partitioned, distributed, real-time processing of these feeds to create new, derived feeds. This motivated our partitioning and consumer model.

Finally in cases where the stream is fed into other data systems for serving, we knew the system would have to be able to guarantee fault-tolerance in the presence of machine failures.

Supporting these uses led us to a design with a number of unique elements, more akin to a database log than a traditional messaging system. We will outline some elements of the design in the following sections.

<a id="design-design--persistence"></a>

## Persistence

<a id="design-design--dont-fear-the-filesystem"></a>
<a id="design-design--don-t-fear-the-filesystem"></a>

### Don’t fear the filesystem!

Kafka relies heavily on the filesystem for storing and caching messages. There is a general perception that “disks are slow” which makes people skeptical that a persistent structure can offer competitive performance. In fact disks are both much slower and much faster than people expect depending on how they are used; and a properly designed disk structure can often be as fast as the network.

The key fact about disk performance is that the throughput of hard drives has been diverging from the latency of a disk seek for the last decade. As a result the performance of linear writes on a [JBOD](https://en.wikipedia.org/wiki/Non-RAID_drive_architectures) configuration with six 7200rpm SATA RAID-5 array is about 600MB/sec but the performance of random writes is only about 100kB/sec–a difference of over 6000X. These linear reads and writes are the most predictable of all usage patterns, and are heavily optimized by the operating system. A modern operating system provides read-ahead and write-behind techniques that prefetch data in large block multiples and group smaller logical writes into large physical writes. A further discussion of this issue can be found in this [ACM Queue article](https://queue.acm.org/detail.cfm?id=1563874); they actually find that [sequential disk access can in some cases be faster than random memory access!](https://deliveryimages.acm.org/10.1145/1570000/1563874/jacobs3.jpg)

To compensate for this performance divergence, modern operating systems have become increasingly aggressive in their use of main memory for disk caching. A modern OS will happily divert *all* free memory to disk caching with little performance penalty when the memory is reclaimed. All disk reads and writes will go through this unified cache. This feature cannot easily be turned off without using direct I/O, so even if a process maintains an in-process cache of the data, this data will likely be duplicated in OS pagecache, effectively storing everything twice.

Furthermore, we are building on top of the JVM, and anyone who has spent any time with Java memory usage knows two things:

1. The memory overhead of objects is very high, often doubling the size of the data stored (or worse).
2. Java garbage collection becomes increasingly fiddly and slow as the in-heap data increases.

As a result of these factors using the filesystem and relying on pagecache is superior to maintaining an in-memory cache or other structure–we at least double the available cache by having automatic access to all free memory, and likely double again by storing a compact byte structure rather than individual objects. Doing so will result in a cache of up to 28-30GB on a 32GB machine without GC penalties. Furthermore, this cache will stay warm even if the service is restarted, whereas the in-process cache will need to be rebuilt in memory (which for a 10GB cache may take 10 minutes) or else it will need to start with a completely cold cache (which likely means terrible initial performance). This also greatly simplifies the code as all logic for maintaining coherency between the cache and filesystem is now in the OS, which tends to do so more efficiently and more correctly than one-off in-process attempts. If your disk usage favors linear reads then read-ahead is effectively pre-populating this cache with useful data on each disk read.

This suggests a design which is very simple: rather than maintain as much as possible in-memory and flush it all out to the filesystem in a panic when we run out of space, we invert that. All data is immediately written to a persistent log on the filesystem without necessarily flushing to disk. In effect this just means that it is transferred into the kernel’s pagecache.

This style of pagecache-centric design is described in an [article](https://varnish-cache.org/wiki/ArchitectNotes) on the design of Varnish here (along with a healthy dose of arrogance).

<a id="design-design--constant-time-suffices"></a>

### Constant Time Suffices

The persistent data structure used in messaging systems are often a per-consumer queue with an associated BTree or other general-purpose random access data structures to maintain metadata about messages. BTrees are the most versatile data structure available, and make it possible to support a wide variety of transactional and non-transactional semantics in the messaging system. They do come with a fairly high cost, though: Btree operations are O(log N). Normally O(log N) is considered essentially equivalent to constant time, but this is not true for disk operations. Disk seeks come at 10 ms a pop, and each disk can do only one seek at a time so parallelism is limited. Hence even a handful of disk seeks leads to very high overhead. Since storage systems mix very fast cached operations with very slow physical disk operations, the observed performance of tree structures is often superlinear as data increases with fixed cache–i.e. doubling your data makes things much worse than twice as slow.

Intuitively a persistent queue could be built on simple reads and appends to files as is commonly the case with logging solutions. This structure has the advantage that all operations are O(1) and reads do not block writes or each other. This has obvious performance advantages since the performance is completely decoupled from the data size–one server can now take full advantage of a number of cheap, low-rotational speed 1+TB SATA drives. Though they have poor seek performance, these drives have acceptable performance for large reads and writes and come at 1/3 the price and 3x the capacity.

Having access to virtually unlimited disk space without any performance penalty means that we can provide some features not usually found in a messaging system. For example, in Kafka, instead of attempting to delete messages as soon as they are consumed, we can retain messages for a relatively long period (say a week). This leads to a great deal of flexibility for consumers, as we will describe.

<a id="design-design--efficiency"></a>

## Efficiency

We have put significant effort into efficiency. One of our primary use cases is handling web activity data, which is very high volume: each page view may generate dozens of writes. Furthermore, we assume each message published is read by at least one consumer (often many), hence we strive to make consumption as cheap as possible.

We have also found, from experience building and running a number of similar systems, that efficiency is a key to effective multi-tenant operations. If the downstream infrastructure service can easily become a bottleneck due to a small bump in usage by the application, such small changes will often create problems. By being very fast we help ensure that the application will tip over under load before the infrastructure. This is particularly important when trying to run a centralized service that supports dozens or hundreds of applications on a centralized cluster as changes in usage patterns are a near-daily occurrence.

We discussed disk efficiency in the previous section. Once poor disk access patterns have been eliminated, there are two common causes of inefficiency in this type of system: too many small I/O operations, and excessive byte copying.

The small I/O problem happens both between the client and the server and in the server’s own persistent operations.

To avoid this, our protocol is built around a “message set” abstraction that naturally groups messages together. This allows network requests to group messages together and amortize the overhead of the network roundtrip rather than sending a single message at a time. The server in turn appends chunks of messages to its log in one go, and the consumer fetches large linear chunks at a time.

This simple optimization produces orders of magnitude speed up. Batching leads to larger network packets, larger sequential disk operations, contiguous memory blocks, and so on, all of which allows Kafka to turn a bursty stream of random message writes into linear writes that flow to the consumers.

The other inefficiency is in byte copying. At low message rates this is not an issue, but under load the impact is significant. To avoid this we employ a standardized binary message format that is shared by the producer, the broker, and the consumer (so data chunks can be transferred without modification between them).

The message log maintained by the broker is itself just a directory of files, each populated by a sequence of message sets that have been written to disk in the same format used by the producer and consumer. Maintaining this common format allows optimization of the most important operation: network transfer of persistent log chunks. Modern Unix operating systems offer a highly optimized code path for transferring data out of pagecache to a socket; in Linux this is done with the [sendfile system call](https://man7.org/linux/man-pages/man2/sendfile.2.html).

To understand the impact of sendfile, it is important to understand the common data path for transfer of data from file to socket:

1. The operating system reads data from the disk into pagecache in kernel space
2. The application reads the data from kernel space into a user-space buffer
3. The application writes the data back into kernel space into a socket buffer
4. The operating system copies the data from the socket buffer to the NIC buffer where it is sent over the network

This is clearly inefficient, there are four copies and two system calls. Using sendfile, this re-copying is avoided by allowing the OS to send the data from pagecache to the network directly. So in this optimized path, only the final copy to the NIC buffer is needed.

We expect a common use case to be multiple consumers on a topic. Using the zero-copy optimization above, data is copied into pagecache exactly once and reused on each consumption instead of being stored in memory and copied out to user-space every time it is read. This allows messages to be consumed at a rate that approaches the limit of the network connection.

This combination of pagecache and sendfile means that on a Kafka cluster where the consumers are mostly caught up you will see no read activity on the disks whatsoever as they will be serving data entirely from cache.

TLS/SSL libraries operate at the user space (in-kernel `SSL_sendfile` is currently not supported by Kafka). Due to this restriction, `sendfile` is not used when SSL is enabled. For enabling SSL configuration, refer to `security.protocol` and `security.inter.broker.protocol`

For more background on the sendfile and zero-copy support in Java, see this [article](https://developer.ibm.com/articles/j-zerocopy/).

<a id="design-design--end-to-end-batch-compression"></a>

### End-to-end Batch Compression

In some cases the bottleneck is actually not CPU or disk but network bandwidth. This is particularly true for a data pipeline that needs to send messages between data centers over a wide-area network. Of course, the user can always compress its messages one at a time without any support needed from Kafka, but this can lead to very poor compression ratios as much of the redundancy is due to repetition between messages of the same type (e.g. field names in JSON or user agents in web logs or common string values). Efficient compression requires compressing multiple messages together rather than compressing each message individually.

Kafka supports this with an efficient batching format. A batch of messages can be grouped together, compressed, and sent to the server in this form. The broker decompresses the batch in order to validate it. For example, it validates that the number of records in the batch is same as what batch header states. This batch of messages is then written to disk in compressed form. The batch will remain compressed in the log and it will also be transmitted to the consumer in compressed form. The consumer decompresses any compressed data that it receives.

Kafka supports GZIP, Snappy, LZ4 and ZStandard compression protocols. More details on compression can be found [here](https://cwiki.apache.org/confluence/x/S5qoAQ).

<a id="design-design--the-producer"></a>

## The Producer

<a id="design-design--load-balancing"></a>

### Load balancing

The producer sends data directly to the broker that is the leader for the partition without any intervening routing tier. To help the producer do this all Kafka nodes can answer a request for metadata about which servers are alive and where the leaders for the partitions of a topic are at any given time to allow the producer to appropriately direct its requests.

The client controls which partition it publishes messages to. This can be done at random, implementing a kind of random load balancing, or it can be done by some semantic partitioning function. We expose the interface for semantic partitioning by allowing the user to specify a key to partition by and using this to hash to a partition (there is also an option to override the partition function if need be). For example if the key chosen was a user id then all data for a given user would be sent to the same partition. This in turn will allow consumers to make locality assumptions about their consumption. This style of partitioning is explicitly designed to allow locality-sensitive processing in consumers.

<a id="design-design--asynchronous-send"></a>

### Asynchronous send

Batching is one of the big drivers of efficiency, and to enable batching the Kafka producer will attempt to accumulate data in memory and to send out larger batches in a single request. The batching can be configured to accumulate no more than a fixed number of messages and to wait no longer than some fixed latency bound (say 64kB or 10 ms). This allows the accumulation of more bytes to send, and few larger I/O operations on the servers. This buffering is configurable and gives a mechanism to trade off a small amount of additional latency for better throughput.

Details on configuration and the api for the producer can be found elsewhere in the documentation.

<a id="design-design--the-consumer"></a>

## The Consumer

The Kafka consumer works by issuing “fetch” requests to the brokers leading the partitions it wants to consume. The consumer specifies its offset in the log with each request and receives back a chunk of log beginning from that position. The consumer thus has significant control over this position and can rewind it to re-consume data if need be.

<a id="design-design--push-vs-pull"></a>
<a id="design-design--push-vs.-pull"></a>

### Push vs. pull

An initial question we considered is whether consumers should pull data from brokers or brokers should push data to the consumer. In this respect Kafka follows a more traditional design, shared by most messaging systems, where data is pushed to the broker from the producer and pulled from the broker by the consumer. Some logging-centric systems, such as [Scribe](https://github.com/facebook/scribe) and [Apache Flume](https://flume.apache.org/), follow a very different push-based path where data is pushed downstream. There are pros and cons to both approaches. However, a push-based system has difficulty dealing with diverse consumers as the broker controls the rate at which data is transferred. The goal is generally for the consumer to be able to consume at the maximum possible rate; unfortunately, in a push system this means the consumer tends to be overwhelmed when its rate of consumption falls below the rate of production (a denial of service attack, in essence). A pull-based system has the nicer property that the consumer simply falls behind and catches up when it can. This can be mitigated with some kind of backoff protocol by which the consumer can indicate it is overwhelmed, but getting the rate of transfer to fully utilize (but never over-utilize) the consumer is trickier than it seems. Previous attempts at building systems in this fashion led us to go with a more traditional pull model.

Another advantage of a pull-based system is that it lends itself to aggressive batching of data sent to the consumer. A push-based system must choose to either send a request immediately or accumulate more data and then send it later without knowledge of whether the downstream consumer will be able to immediately process it. If tuned for low latency, this will result in sending a single message at a time only for the transfer to end up being buffered anyway, which is wasteful. A pull-based design fixes this as the consumer always pulls all available messages after its current position in the log (or up to some configurable max size). So one gets optimal batching without introducing unnecessary latency.

The deficiency of a naive pull-based system is that if the broker has no data the consumer may end up polling in a tight loop, effectively busy-waiting for data to arrive. To avoid this we have parameters in our pull request that allow the consumer request to block in a “long poll” waiting until data arrives (and optionally waiting until a given number of bytes is available to ensure large transfer sizes).

You could imagine other possible designs which would be only pull, end-to-end. The producer would locally write to a local log, and brokers would pull from that with consumers pulling from them. A similar type of “store-and-forward” producer is often proposed. This is intriguing but we felt not very suitable for our target use cases which have thousands of producers. Our experience running persistent data systems at scale led us to feel that involving thousands of disks in the system across many applications would not actually make things more reliable and would be a nightmare to operate. And in practice we have found that we can run a pipeline with strong SLAs at large scale without a need for producer persistence.

<a id="design-design--consumer-position"></a>

### Consumer Position

Keeping track of *what* has been consumed is, surprisingly, one of the key performance points of a messaging system.

Most messaging systems keep metadata about what messages have been consumed on the broker. That is, as a message is handed out to a consumer, the broker either records that fact locally immediately or it may wait for acknowledgement from the consumer. This is a fairly intuitive choice, and indeed for a single machine server it is not clear where else this state could go. Since the data structures used for storage in many messaging systems scale poorly, this is also a pragmatic choice–since the broker knows what is consumed it can immediately delete it, keeping the data size small.

What is perhaps not obvious is that getting the broker and consumer to come into agreement about what has been consumed is not a trivial problem. If the broker records a message as **consumed** immediately every time it is handed out over the network, then if the consumer fails to process the message (say because it crashes or the request times out or whatever) that message will be lost. To solve this problem, many messaging systems add an acknowledgement feature which means that messages are only marked as **sent** not **consumed** when they are sent; the broker waits for a specific acknowledgement from the consumer to record the message as **consumed**. This strategy fixes the problem of losing messages, but creates new problems. First of all, if the consumer processes the message but fails before it can send an acknowledgement then the message will be consumed twice. The second problem is around performance, now the broker must keep multiple states about every single message (first to lock it so it is not given out a second time, and then to mark it as permanently consumed so that it can be removed). Tricky problems must be dealt with, like what to do with messages that are sent but never acknowledged.

Kafka handles this differently. Our topic is divided into a set of totally ordered partitions, each of which is consumed by exactly one consumer within each subscribing consumer group at any given time. This means that the position of a consumer in each partition is just a single integer, the offset of the next message to consume. This makes the state about what has been consumed very small, just one number for each partition. This state can be periodically checkpointed. This makes the equivalent of message acknowledgements very cheap.

There is a side benefit of this decision. A consumer can deliberately *rewind* back to an old offset and re-consume data. This violates the common contract of a queue, but turns out to be an essential feature for many consumers. For example, if the consumer code has a bug and is discovered after some messages are consumed, the consumer can re-consume those messages once the bug is fixed.

<a id="design-design--offline-data-load"></a>

### Offline Data Load

Scalable persistence allows for the possibility of consumers that only periodically consume such as batch data loads that periodically bulk-load data into an offline system such as Hadoop or a relational data warehouse.

In the case of Hadoop we parallelize the data load by splitting the load over individual map tasks, one for each node/topic/partition combination, allowing full parallelism in the loading. Hadoop provides the task management, and tasks which fail can restart without danger of duplicate data–they simply restart from their original position.

<a id="design-design--static-membership"></a>

### Static Membership

Static membership aims to improve the availability of stream applications, consumer groups and other applications built on top of the group rebalance protocol. The rebalance protocol relies on the group coordinator to allocate entity ids to group members. These generated ids are ephemeral and will change when members restart and rejoin. For consumer based apps, this “dynamic membership” can cause a large percentage of tasks re-assigned to different instances during administrative operations such as code deploys, configuration updates and periodic restarts. For large state applications, shuffled tasks need a long time to recover their local states before processing and cause applications to be partially or entirely unavailable. Motivated by this observation, Kafka’s group management protocol allows group members to provide persistent entity ids. Group membership remains unchanged based on those ids, thus no rebalance will be triggered.

If you want to use static membership,

- Upgrade both broker cluster and client apps to 2.3 or beyond, and also make sure the upgraded brokers are using `inter.broker.protocol.version` of 2.3 or beyond as well.
- Set the config `ConsumerConfig#GROUP_INSTANCE_ID_CONFIG` to a unique value for each consumer instance under one group.
- For Kafka Streams applications, it is sufficient to set a unique `ConsumerConfig#GROUP_INSTANCE_ID_CONFIG` per KafkaStreams instance, independent of the number of used threads for an instance.

If your broker is on an older version than 2.3, but you choose to set `ConsumerConfig#GROUP_INSTANCE_ID_CONFIG` on the client side, the application will detect the broker version and then throws an UnsupportedException. If you accidentally configure duplicate ids for different instances, a fencing mechanism on broker side will inform your duplicate client to shutdown immediately by triggering a `org.apache.kafka.common.errors.FencedInstanceIdException`. For more details, see [KIP-345](https://cwiki.apache.org/confluence/x/kRg0BQ)

<a id="design-design--message-delivery-semantics"></a>

## Message Delivery Semantics

Now that we understand a little about how producers and consumers work, let’s discuss the semantic guarantees Kafka provides between producer and consumer. Clearly there are multiple possible message delivery guarantees that could be provided:

- *At most once* –Messages may be lost but are never redelivered.
- *At least once* –Messages are never lost but may be redelivered.
- *Exactly once* –Each message is processed once and only once.

It’s worth noting that this breaks down into two problems: the durability guarantees for publishing a message and the guarantees when consuming a message.

Many systems claim to provide “exactly-once” delivery semantics, but it is important to read the fine print, because sometimes these claims are misleading (i.e. they don’t translate to the case where consumers or producers can fail, cases where there are multiple consumer processes, or cases where data written to disk can be lost).

Kafka’s semantics are straightforward. When publishing a message we have a notion of the message being “committed” to the log. A message is considered committed only when all replicas in the in-sync replicas (ISR) for that partition have applied it to their log. Once a published message is committed, it will not be lost as long as one broker that replicates the partition to which this message was written remains “alive”. The definition of committed message and alive partition as well as a description of which types of failures we attempt to handle will be described in more detail in the next section. For now let’s assume a perfect, lossless broker and try to understand the guarantees to the producer and consumer. If a producer attempts to publish a message and experiences a network error, it cannot be sure if this error happened before or after the message was committed. This is similar to the semantics of inserting into a database table with an autogenerated key.

Prior to 0.11.0.0, if a producer failed to receive a response indicating that a message was committed, it had little choice but to resend the message. This provides at-least-once delivery semantics since the message may be written to the log again during resending if the original request had in fact succeeded. Since 0.11.0.0, the Kafka producer also supports an idempotent delivery option which guarantees that resending will not result in duplicate entries in the log. To achieve this, the broker assigns each producer an ID and deduplicates messages using a sequence number that is sent by the producer along with every message. Also beginning with 0.11.0.0, the producer supports the ability to send messages atomically to multiple topic partitions using transactions, so that either all messages are successfully written or none of them are.

Not all use cases require such strong guarantees. For use cases which are latency-sensitive, we allow the producer to specify the durability level it desires. If the producer specifies that it wants to wait on the message being committed, this can take on the order of 10 ms. However the producer can also specify that it wants to perform the send completely asynchronously or that it wants to wait only until the leader (but not necessarily the followers) have the message.

Now let’s describe the semantics from the point of view of the consumer. All replicas have the exact same log with the same offsets. The consumer controls its position in this log. If the consumer never crashed it could just store this position in memory, but if the consumer fails and we want this topic partition to be taken over by another process, the new process will need to choose an appropriate position from which to start processing. Let’s say the consumer reads some messages – it has several options for processing the messages and updating its position.

1. It can read the messages, then save its position in the log, and finally process the messages. In this case there is a possibility that the consumer process crashes after saving its position but before saving the output of its message processing. In this case the process that took over processing would start at the saved position even though a few messages prior to that position had not been processed. This corresponds to “at-most-once” semantics as in the case of a consumer failure messages may not be processed.
2. It can read the messages, process the messages, and finally save its position. In this case there is a possibility that the consumer process crashes after processing messages but before saving its position. In this case when the new process takes over the first few messages it receives will already have been processed. This corresponds to the “at-least-once” semantics in the case of consumer failure. In many cases messages have a primary key and so the updates are idempotent (receiving the same message twice just overwrites a record with another copy of itself).

So what about exactly-once semantics? When consuming from a Kafka topic and producing to another topic (as in a [Kafka Streams](https://kafka.apache.org/documentation/streams) application), we can leverage the new transactional producer capabilities in 0.11.0.0 that were mentioned above. The consumer’s position is stored as a message in an internal topic, so we can write the offset to Kafka in the same transaction as the output topics receiving the processed data. If the transaction is aborted, the consumer’s stored position will revert to its old value (although the consumer has to refetch the committed offset because it does not automatically rewind) and the produced data on the output topics will not be visible to other consumers, depending on their “isolation level”. In the default “read\_uncommitted” isolation level, all messages are visible to consumers even if they were part of an aborted transaction, but in “read\_committed” isolation level, the consumer will only return messages from transactions which were committed (and any messages which were not part of a transaction).

When writing to an external system, the limitation is in the need to coordinate the consumer’s position with what is actually stored as output. The classic way of achieving this would be to introduce a two-phase commit between the storage of the consumer position and the storage of the consumers output. This can be handled more simply and generally by letting the consumer store its offset in the same place as its output. This is better because many of the output systems a consumer might want to write to will not support a two-phase commit. As an example of this, consider a [Kafka Connect](https://kafka.apache.org/documentation/#connect) connector which populates data in HDFS along with the offsets of the data it reads so that it is guaranteed that either data and offsets are both updated or neither is. We follow similar patterns for many other data systems which require these stronger semantics and for which the messages do not have a primary key to allow for deduplication.

As a result, Kafka supports exactly-once delivery in [Kafka Streams](https://kafka.apache.org/documentation/streams), and the transactional producer and the consumer using read-committed isolation level can be used generally to provide exactly-once delivery when reading, processing and writing data on Kafka topics. Exactly-once delivery for other destination systems generally requires cooperation with such systems, but Kafka provides the primitives which makes implementing this feasible (see also [Kafka Connect](https://kafka.apache.org/documentation/#connect)). Otherwise, Kafka guarantees at-least-once delivery by default, and allows the user to implement at-most-once delivery by disabling retries on the producer and committing offsets in the consumer prior to processing a batch of messages.

<a id="design-design--using-transactions"></a>

## Using Transactions

As mentioned above, the simplest way to get exactly-once semantics from Kafka is to use [Kafka Streams](https://kafka.apache.org/documentation/streams). However, it is also possible to achieve the same transactional guarantees using the Kafka producer and consumer directly by using them in the same way as Kafka Streams does.

Kafka transactions are a bit different from transactions in other messaging systems. In Kafka, the consumer and producer are separate, and it is only the producer which is transactional. It is however able to make transactional updates to the consumer’s position (confusingly called the “committed offset”), and it is this which gives the overall exactly-once behavior.

There are three key aspects to exactly-once processing using the producer and consumer, which match how Kafka Streams works.

1. The consumer uses partition assignment to ensure that it is the only consumer in the consumer group currently processing each partition.
2. The producer uses transactions so that all the records it produces, and any offsets it updates on behalf of the consumer, are performed atomically.
3. In order to handle transactions properly in combination with rebalancing, it is advisable to use one producer instance for each consumer instance. More complicated and efficient schemes are possible, but at the cost of greater complexity.

In addition, it is generally considered a good practice to use the read-committed isolation level if trying to achieve exactly-once processing. Strictly speaking, the consumer doesn’t have to use read-committed isolation level, but if it does not, it will see records from aborted transactions and also open transactions which have not yet completed.

The consumer configuration must include `isolation.level=read_committed` and `enable.auto.commit=false`. The producer configuration must set `transactional.id` to the name of the transactional ID to be used, which configures the producer for transactional delivery and also makes sure that a restarted application causes any in-flight transaction from the previous instance to abort. Only the producer has the `transactional.id` configuration.

Here’s an example of a [transactional message copier](https://github.com/apache/kafka/blob/trunk/tools/src/main/java/org/apache/kafka/tools/TransactionalMessageCopier.java) which uses these principles. It uses a `KafkaConsumer` to consume records from one topic and a `KafkaProducer` to produce records to another topic. It uses transactions to ensure that there is no duplication or loss of records as they are copied, provided that the `--use-group-metadata` option is set.

It is important to handle exceptions and aborted transactions correctly. Any records written by the transactional producer will be marked as being part of the transactions, and then when the transaction commits or aborts, transaction marker records are written to indicate the outcome of the transaction. This is how the read-committed consumer does not see records from aborted transactions. However, in the event of a transaction abort, the application’s state and in particular the current position of the consumer must be reset explicitly so that it can reprocess the records processed by the aborted transaction.

The error handling for transactional producer has been standardized which ensures consistent behavior and clearer error handling patterns. The exception categories are now more precisely defined:

1. **RetriableException** : Temporary exceptions that are retried automatically by the client. These are handled internally and don’t bubble up to the application.
2. **RefreshRetriableException** : Exceptions requiring metadata refresh before retry. These are handled internally by the client after refreshing metadata and don’t bubble up to the application.
3. **AbortableException** : Exceptions that require transaction abort and reprocessing. These bubble up to the application, which must handle them by aborting the transaction and resetting the consumer position.
4. **ApplicationRecoverableException** : Exceptions that bubble up to the application and require application handling. The application must implement its own recovery strategy, which must include restarting the producer.
5. **InvalidConfigurationException** : Configuration-related exceptions that bubble up to the application and require application handling. The producer doesn’t need to restart, but the application may choose to restart it.
6. **KafkaException** : General Kafka exceptions that don’t fit into the above categories. These bubble up to the application for handling.

Example template code for handling transaction exceptions link : [Transaction Client Demo](https://github.com/apache/kafka/blob/trunk/examples/src/main/java/kafka/examples/TransactionalClientDemo.java)

A simple policy for handling exceptions and aborted transactions is to discard and recreate the Kafka producer and consumer objects and start afresh. As part of recreating the consumer, the consumer group will rebalance and fetch the last committed offset, which has the effect of rewinding back to the state before the transaction aborted. Alternatively, a more sophisticated application (such as the transactional message copier) can choose not to use `KafkaConsumer.committed` to retrieve the committed offset from Kafka, and then `KafkaConsumer.seek` to rewind the current position.

<a id="design-design--the-share-consumer"></a>

## The Share Consumer

Most consumption of data from Kafka is performed by consumers in consumer groups. The way that consumer groups assign partitions to members of the group gives a powerful combination of ordering and scalability. However, some traditional messaging workloads are not a good fit for consumer groups.

Share groups are another type of group, existing alongside traditional consumer groups. They offer an alternative to consumer groups, particularly when applications require finer-grained sharing of partitions and records. Share groups enable consumers to cooperatively consume and process records from topics. The consumers in a share group are called share consumers, and they use a familiar but different programming interface.

The fundamental differences between a share group and a consumer group are:

- The consumers in a share group cooperatively consume records, and partitions may be assigned to multiple consumers.
- The number of consumers in a share group can exceed the number of partitions in a topic.
- Records are acknowledged individually, though the system is optimized for batch processing to improve efficiency.
- Delivery attempts to consumers in a share group are counted, which enables automated handling of unprocessable records.

All share consumers in the same share group subscribed to the same topic will cooperatively consume the records of that topic. If a topic is accessed by consumers in multiple share groups, each share group consumes from that topic independently of the others.

Each share consumer can dynamically set its list of subscribed topics. In practice, all consumers in a share group typically subscribe to the same topic or topics.

When a share consumer fetches records, it receives available records from any of the topic-partitions matching its subscriptions. Records are acquired for delivery to this share consumer with a time-limited acquisition lock. While a record is acquired, it is unavailable to other consumers in the same share group for the duration of the lock.

By default, the lock duration is 30 seconds, but you can control it using the group configuration parameter `share.record.lock.duration.ms`. The lock is released automatically once its duration elapses, making the record available to another delivery attempt. A share consumer holding the lock can handle the record in the following ways:

- Acknowledge successful processing of the record.
- Release the record, making it available for another delivery attempt.
- Reject the record, indicating it’s unprocessable and preventing further delivery attempts for that record.
- Renew the record, extending the delivery attempt because the record is still being processed.
- Do nothing, in which case the lock is automatically released when its duration elapses.

The Kafka cluster limits the number of records for each topic-partition acquired by share consumers in each share group. Once this limit is reached, fetching operations will temporarily yield no further records until the number of acquired records decreases (as locks naturally time out). This limit is controlled by the broker configuration property `group.share.partition.max.record.locks`. By limiting the duration of the acquisition lock and automatically releasing the locks, the broker ensures delivery progresses even in the presence of consumer failures.

<a id="design-design--replication"></a>

## Replication

Kafka replicates the log for each topic’s partitions across a configurable number of servers (you can set this replication factor on a topic-by-topic basis). This allows automatic failover to these replicas when a server in the cluster fails so messages remain available in the presence of failures.

Other messaging systems provide some replication-related features, but, in our (totally biased) opinion, this appears to be a tacked-on thing, not heavily used, and with large downsides: replicas are inactive, throughput is heavily impacted, it requires fiddly manual configuration, etc. Kafka is meant to be used with replication by default–in fact we implement un-replicated topics as replicated topics where the replication factor is one.

The unit of replication is the topic partition. Under non-failure conditions, each partition in Kafka has a single leader and zero or more followers. The total number of replicas including the leader constitute the replication factor. All writes go to the leader of the partition, and reads can go to the leader or the followers of the partition. Typically, there are many more partitions than brokers and the leaders are evenly distributed among brokers. The logs on the followers are identical to the leader’s log–all have the same offsets and messages in the same order (though, of course, at any given time the leader may have a few as-yet unreplicated messages at the end of its log).

Followers consume messages from the leader just as a normal Kafka consumer would and apply them to their own log. Having the followers pull from the leader has the nice property of allowing the follower to naturally batch together log entries they are applying to their log.

As with most distributed systems, automatically handling failures requires a precise definition of what it means for a node to be “alive.” In Kafka, a special node known as the “controller” is responsible for managing the registration of brokers in the cluster. Broker liveness has two conditions:

1. Brokers must maintain an active session with the controller in order to receive regular metadata updates.
2. Brokers acting as followers must replicate the writes from the leader and not fall “too far” behind.

What is meant by an “active session” depends on the cluster configuration. For KRaft clusters, an active session is maintained by sending periodic heartbeats to the controller. If the controller fails to receive a heartbeat before the timeout configured by `broker.session.timeout.ms` expires, then the node is considered offline.

We refer to nodes satisfying these two conditions as being “in sync” to avoid the vagueness of “alive” or “failed”. The leader keeps track of the set of “in sync” replicas, which is known as the ISR. If either of these conditions fail to be satisfied, then the broker will be removed from the ISR. For example, if a follower dies, then the controller will notice the failure through the loss of its session, and will remove the broker from the ISR. On the other hand, if the follower lags too far behind the leader but still has an active session, then the leader can also remove it from the ISR. The determination of lagging replicas is controlled through the `replica.lag.time.max.ms` configuration. Replicas that cannot catch up to the end of the log on the leader within the max time set by this configuration are removed from the ISR.

In distributed systems terminology we only attempt to handle a “fail/recover” model of failures where nodes suddenly cease working and then later recover (perhaps without knowing that they have died). Kafka does not handle so-called “Byzantine” failures in which nodes produce arbitrary or malicious responses (perhaps due to bugs or foul play).

Only committed messages are ever given out to the consumer. This means that the consumer need not worry about potentially seeing a message that could be lost if the leader fails. Producers, on the other hand, have the option of either waiting for the message to be committed or not, depending on their preference for tradeoff between latency and durability. This preference is controlled by the `acks` setting that the producer uses. Note that topics have a setting for the minimum number of in-sync replicas (`min.insync.replicas`) that is checked when the producer requests acknowledgment that a message has been written to the full set of in-sync replicas. If a less stringent acknowledgment is requested by the producer, then the message is committed asynchronously across the set of in-sync replicas if `acks=0`, or synchronously only on the leader if `acks=1`. Regardless of the `acks` setting, the messages will not be visible to the consumers until all the following conditions are met:

1. The messages are replicated to all the in-sync replicas.
2. The number of the in-sync replicas is no less than the `min.insync.replicas` setting.

The guarantee that Kafka offers is that a committed message will not be lost, as long as there is at least one in sync replica alive, at all times.

Kafka will remain available in the presence of node failures after a short fail-over period, but may not remain available in the presence of network partitions.

<a id="design-design--replicated-logs-quorums-isrs-and-state-machines-oh-my"></a>
<a id="design-design--replicated-logs:-quorums-isrs-and-state-machines-oh-my"></a>

### Replicated Logs: Quorums, ISRs, and State Machines (Oh my!)

At its heart a Kafka partition is a replicated log. The replicated log is one of the most basic primitives in distributed data systems, and there are many approaches for implementing one. A replicated log can be used by other systems as a primitive for implementing other distributed systems in the [state-machine style](https://en.wikipedia.org/wiki/State_machine_replication).

A replicated log models the process of coming into consensus on the order of a series of values (generally numbering the log entries 0, 1, 2, …). There are many ways to implement this, but the simplest and fastest is with a leader who chooses the ordering of values provided to it. As long as the leader remains alive, all followers need to only copy the values and ordering the leader chooses.

Of course if leaders didn’t fail we wouldn’t need followers! When the leader does die we need to choose a new leader from among the followers. But followers themselves may fall behind or crash so we must ensure we choose an up-to-date follower. The fundamental guarantee a log replication algorithm must provide is that if we tell the client a message is committed, and the leader fails, the new leader we elect must also have that message. This yields a tradeoff: if the leader waits for more followers to acknowledge a message before declaring it committed then there will be more potentially electable leaders.

If you choose the number of acknowledgements required and the number of logs that must be compared to elect a leader such that there is guaranteed to be an overlap, then this is called a Quorum.

A common approach to this tradeoff is to use a majority vote for both the commit decision and the leader election. This is not what Kafka does, but let’s explore it anyway to understand the tradeoffs. Let’s say we have 2 *f* +1 replicas. If *f* +1 replicas must receive a message prior to a commit being declared by the leader, and if we elect a new leader by electing the follower with the most complete log from at least *f* +1 replicas, then, with no more than *f* failures, the leader is guaranteed to have all committed messages. This is because among any *f* +1 replicas, there must be at least one replica that contains all committed messages. That replica’s log will be the most complete and therefore will be selected as the new leader. There are many remaining details that each algorithm must handle (such as precisely defined what makes a log more complete, ensuring log consistency during leader failure or changing the set of servers in the replica set) but we will ignore these for now.

This majority vote approach has a very nice property: the latency is dependent on only the fastest servers. That is, if the replication factor is three, the latency is determined by the faster follower not the slower one.

There are a rich variety of algorithms in this family including ZooKeeper’s [Zab](https://web.archive.org/web/20140602093727/https:/www.stanford.edu/class/cs347/reading/zab.pdf), [Raft](https://www.usenix.org/system/files/conference/atc14/atc14-paper-ongaro.pdf), and [Viewstamped Replication](https://pmg.csail.mit.edu/papers/vr-revisited.pdf). The most similar academic publication we are aware of to Kafka’s actual implementation is [PacificA](https://research.microsoft.com/apps/pubs/default.aspx?id=66814) from Microsoft.

The downside of majority vote is that it doesn’t take many failures to leave you with no electable leaders. To tolerate one failure requires three copies of the data, and to tolerate two failures requires five copies of the data. In our experience having only enough redundancy to tolerate a single failure is not enough for a practical system, but doing every write five times, with 5x the disk space requirements and 1/5th the throughput, is not very practical for large volume data problems. This is likely why quorum algorithms more commonly appear for shared cluster configuration such as ZooKeeper but are less common for primary data storage. For example in HDFS the namenode’s high-availability feature is built on a [majority-vote-based journal](https://blog.cloudera.com/blog/2012/10/quorum-based-journaling-in-cdh4-1), but this more expensive approach is not used for the data itself.

Kafka takes a slightly different approach to choosing its quorum set. Instead of majority vote, Kafka dynamically maintains a set of in-sync replicas (ISR) that are caught-up to the leader. Only members of this set are eligible for election as leader. A write to a Kafka partition is not considered committed until *all* in-sync replicas have received the write. This ISR set is persisted in the cluster metadata whenever it changes. Because of this, any replica in the ISR is eligible to be elected leader. This is an important factor for Kafka’s usage model where there are many partitions and ensuring leadership balance is important. With this ISR model and *f+1* replicas, a Kafka topic can tolerate *f* failures without losing committed messages.

For most use cases we hope to handle, we think this tradeoff is a reasonable one. In practice, to tolerate *f* failures, both the majority vote and the ISR approach will wait for the same number of replicas to acknowledge before committing a message (e.g. to survive one failure a majority quorum needs three replicas and one acknowledgement and the ISR approach requires two replicas and one acknowledgement). The ability to commit without the slowest servers is an advantage of the majority vote approach. However, we think it is ameliorated by allowing the client to choose whether they block on the message commit or not, and the additional throughput and disk space due to the lower required replication factor is worth it.

Another important design distinction is that Kafka does not require that crashed nodes recover with all their data intact. It is not uncommon for replication algorithms in this space to depend on the existence of “stable storage” that cannot be lost in any failure-recovery scenario without potential consistency violations. There are two primary problems with this assumption. First, disk errors are the most common problem we observe in real operation of persistent data systems and they often do not leave data intact. Secondly, even if this were not a problem, we do not want to require the use of fsync on every write for our consistency guarantees as this can reduce performance by two to three orders of magnitude. Our protocol for allowing a replica to rejoin the ISR ensures that before rejoining, it must fully re-sync again even if it lost unflushed data in its crash.

<a id="design-design--unclean-leader-election-what-if-they-all-die"></a>
<a id="design-design--unclean-leader-election:-what-if-they-all-die"></a>

### Unclean leader election: What if they all die?

Note that Kafka’s guarantee with respect to data loss is predicated on at least one replica remaining in sync. If all the nodes replicating a partition die, this guarantee no longer holds.

However a practical system needs to do something reasonable when all the replicas die. If you are unlucky enough to have this occur, it is important to consider what will happen. There are two behaviors that could be implemented:

1. Wait for a replica in the ISR to come back to life and choose this replica as the leader (hopefully it still has all its data).
2. Choose the first replica (not necessarily in the ISR) that comes back to life as the leader.

This is a simple tradeoff between availability and consistency. If we wait for replicas in the ISR, then we will remain unavailable as long as those replicas are down. If such replicas were destroyed or their data was lost, then we are permanently down. If, on the other hand, a non-in-sync replica comes back to life and we allow it to become leader, then its log becomes the source of truth even though it is not guaranteed to have every committed message. By default from version 0.11.0.0, Kafka chooses the first strategy and favor waiting for a consistent replica. This behavior can be changed using configuration property `unclean.leader.election.enable`, to support use cases where uptime is preferable to consistency.

This dilemma is not specific to Kafka. It exists in any quorum-based scheme. For example in a majority voting scheme, if a majority of servers suffer a permanent failure, then you must either choose to lose 100% of your data or violate consistency by taking what remains on an existing server as your new source of truth.

<a id="design-design--availability-and-durability-guarantees"></a>

### Availability and Durability Guarantees

When writing to Kafka, producers can choose whether they wait for the message to be acknowledged by 0,1 or all (-1) replicas. Note that “acknowledgement by all replicas” does not guarantee that the full set of assigned replicas have received the message. By default, when acks=all, acknowledgement happens as soon as all the current in-sync replicas have received the message. For example, if a topic is configured with only two replicas and one fails (i.e., only one in sync replica remains), then writes that specify acks=all will succeed. However, these writes could be lost if the remaining replica also fails. Although this ensures maximum availability of the partition, this behavior may be undesirable to some users who prefer durability over availability. Therefore, we provide two topic configurations that can be used to prefer message durability over availability:

1. Disable unclean leader election - if all replicas become unavailable, then the partition will remain unavailable until the most recent leader becomes available again. This effectively prefers unavailability over the risk of message loss. See the previous section on Unclean Leader Election for clarification.
2. Specify a minimum ISR size - the partition will only accept writes if the size of the ISR is above a certain minimum, in order to prevent the loss of messages that were written to just a single replica, which subsequently becomes unavailable. This setting only takes effect if the producer uses acks=all and guarantees that the message will be acknowledged by at least this many in-sync replicas. This setting offers a trade-off between consistency and availability. A higher setting for minimum ISR size guarantees better consistency since the message is guaranteed to be written to more replicas which reduces the probability that it will be lost. However, it reduces availability since the partition will be unavailable for writes if the number of in-sync replicas drops below the minimum threshold.

<a id="design-design--replica-management"></a>

### Replica Management

The above discussion on replicated logs really covers only a single log, i.e. one topic partition. However a Kafka cluster will manage hundreds or thousands of these partitions. We attempt to balance partitions within a cluster in a round-robin fashion to avoid clustering all partitions for high-volume topics on a small number of nodes. Likewise we try to balance leadership so that each node is the leader for a proportional share of its partitions.

It is also important to optimize the leadership election process as that is the critical window of unavailability. A naive implementation of leader election would end up running an election per partition for all partitions a node hosted when that node failed. As discussed above in the section on replication, Kafka clusters have a special role known as the “controller” which is responsible for managing the registration of brokers. If the controller detects the failure of a broker, it is responsible for electing one of the remaining members of the ISR to serve as the new leader. The result is that we are able to batch together many of the required leadership change notifications which makes the election process far cheaper and faster for a large number of partitions. If the controller itself fails, then another controller will be elected.

<a id="design-design--log-compaction"></a>

## Log Compaction

Log compaction ensures that Kafka will always retain at least the last known value for each message key within the log of data for a single topic partition. It addresses use cases and scenarios such as restoring state after application crashes or system failure, or reloading caches after application restarts during operational maintenance. Let’s dive into these use cases in more detail and then describe how compaction works.

So far we have described only the simpler approach to data retention where old log data is discarded after a fixed period of time or when the log reaches some predetermined size. This works well for temporal event data such as logging where each record stands alone. However an important class of data streams are the log of changes to keyed, mutable data (for example, the changes to a database table).

Let’s discuss a concrete example of such a stream. Say we have a topic containing user email addresses; every time a user updates their email address we send a message to this topic using their user id as the primary key. Now say we send the following messages over some time period for a user with id 123, each message corresponding to a change in email address (messages for other ids are omitted):

```text
123 => bill@microsoft.com...123 => bill@gatesfoundation.org...123 => bill@gmail.com
```

Log compaction gives us a more granular retention mechanism so that we are guaranteed to retain at least the last update for each primary key (e.g. `bill@gmail.com`). By doing this we guarantee that the log contains a full snapshot of the final value for every key not just keys that changed recently. This means downstream consumers can restore their own state off this topic without us having to retain a complete log of all changes.

Let’s start by looking at a few use cases where this is useful, then we’ll see how it can be used.

1. *Database change subscription*. It is often necessary to have a data set in multiple data systems, and often one of these systems is a database of some kind (either a RDBMS or perhaps a new-fangled key-value store). For example you might have a database, a cache, a search cluster, and a Hadoop cluster. Each change to the database will need to be reflected in the cache, the search cluster, and eventually in Hadoop. In the case that one is only handling the real-time updates you only need recent log. But if you want to be able to reload the cache or restore a failed search node you may need a complete data set.
2. *Event sourcing*. This is a style of application design which co-locates query processing with application design and uses a log of changes as the primary store for the application.
3. *Journaling for high-availability*. A process that does local computation can be made fault-tolerant by logging out changes that it makes to its local state so another process can reload these changes and carry on if it should fail. A concrete example of this is handling counts, aggregations, and other “group by”-like processing in a stream query system. Samza, a real-time stream-processing framework, [uses this feature](https://samza.apache.org/learn/documentation/0.7.0/container/state-management.html) for exactly this purpose.
   In each of these cases one needs primarily to handle the real-time feed of changes, but occasionally, when a machine crashes or data needs to be re-loaded or re-processed, one needs to do a full load. Log compaction allows feeding both of these use cases off the same backing topic. This style of usage of a log is described in more detail in [this blog post](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying).

The general idea is quite simple. If we had infinite log retention, and we logged each change in the above cases, then we would have captured the state of the system at each time from when it first began. Using this complete log, we could restore to any point in time by replaying the first N records in the log. This hypothetical complete log is not very practical for systems that update a single record many times as the log will grow without bound even for a stable dataset. The simple log retention mechanism which throws away old updates will bound space but the log is no longer a way to restore the current state–now restoring from the beginning of the log no longer recreates the current state as old updates may not be captured at all.

Log compaction is a mechanism to give finer-grained per-record retention, rather than the coarser-grained time-based retention. The idea is to selectively remove records where we have a more recent update with the same primary key. This way the log is guaranteed to have at least the last state for each key.

This retention policy can be set per-topic, so a single cluster can have some topics where retention is enforced by size or time and other topics where retention is enforced by compaction.

This functionality is inspired by one of LinkedIn’s oldest and most successful pieces of infrastructure–a database changelog caching service called [Databus](https://github.com/linkedin/databus). Unlike most log-structured storage systems Kafka is built for subscription and organizes data for fast linear reads and writes. Unlike Databus, Kafka acts as a source-of-truth store so it is useful even in situations where the upstream data source would not otherwise be replayable.

<a id="design-design--log-compaction-basics"></a>

### Log Compaction Basics

Here is a high-level picture that shows the logical structure of a Kafka log with the offset for each message.

The head of the log is identical to a traditional Kafka log. It has dense, sequential offsets and retains all messages. Log compaction adds an option for handling the tail of the log. The picture above shows a log with a compacted tail. Note that the messages in the tail of the log retain the original offset assigned when they were first written–that never changes. Note also that all offsets remain valid positions in the log, even if the message with that offset has been compacted away; in this case this position is indistinguishable from the next highest offset that does appear in the log. For example, in the picture above the offsets 36, 37, and 38 are all equivalent positions and a read beginning at any of these offsets would return a message set beginning with 38.

Compaction also allows for deletes. A message with a key and a null payload will be treated as a delete from the log. Such a record is sometimes referred to as a *tombstone*. This delete marker will cause any prior message with that key to be removed (as would any new message with that key), but delete markers are special in that they will themselves be cleaned out of the log after a period of time to free up space. The point in time at which deletes are no longer retained is marked as the “delete retention point” in the above diagram.

The compaction is done in the background by periodically recopying log segments. Cleaning does not block reads and can be throttled to use no more than a configurable amount of I/O throughput to avoid impacting producers and consumers. The actual process of compacting a log segment looks something like this:

<a id="design-design--what-guarantees-does-log-compaction-provide"></a>

### What guarantees does log compaction provide?

Log compaction guarantees the following:

1. Any consumer that stays caught-up to within the head of the log will see every message that is written; these messages will have sequential offsets. The topic’s `min.compaction.lag.ms` can be used to guarantee the minimum length of time must pass after a message is written before it could be compacted, that is, it provides a lower bound on how long each message will remain in the (uncompacted) head. The topic’s `max.compaction.lag.ms` can be used to guarantee the maximum delay between the time a message is written and the time the message becomes eligible for compaction.
2. Ordering of messages is always maintained. Compaction will never re-order messages, just remove some.
3. The offset for a message never changes. It is the permanent identifier for a position in the log.
4. Any consumer progressing from the start of the log will see at least the final state of all records in the order they were written. Additionally, all delete markers for deleted records will be seen, provided the consumer reaches the head of the log in a time period less than the topic’s `delete.retention.ms` setting (the default is 24 hours). In other words: since the removal of delete markers happens concurrently with reads, it is possible for a consumer to miss delete markers if it lags by more than `delete.retention.ms`.

<a id="design-design--log-compaction-details"></a>

### Log Compaction Details

Log compaction is handled by the log cleaner, a pool of background threads that recopy log segment files, removing records whose key appears in the head of the log. Each compactor thread works as follows:

1. It chooses the log that has the highest ratio of log head to log tail
2. It creates a succinct summary of the last offset for each key in the head of the log
3. It recopies the log from beginning to end removing keys which have a later occurrence in the log. New, clean segments are swapped into the log immediately so the additional disk space required is just one additional log segment (not a full copy of the log).
4. The summary of the log head is essentially just a space-compact hash table. It uses exactly 24 bytes per entry. As a result with 8GB of cleaner buffer one cleaner iteration can clean around 366GB of log head (assuming 1kB messages).

<a id="design-design--configuring-the-log-cleaner"></a>

### Configuring The Log Cleaner

The log cleaner is enabled by default. This will start the pool of cleaner threads. To enable log cleaning on a particular topic, add the log-specific property

```properties
log.cleanup.policy=compact
```

The `log.cleanup.policy` property is a broker configuration setting defined in the broker’s `server.properties` file; it affects all of the topics in the cluster that do not have a configuration override in place as documented [here](https://kafka.apache.org/documentation.html#brokerconfigs). The log cleaner can be configured to retain a minimum amount of the uncompacted “head” of the log. This is enabled by setting the compaction time lag.

```properties
log.cleaner.min.compaction.lag.ms
```

This can be used to prevent messages newer than a minimum message age from being subject to compaction. If not set, all log segments are eligible for compaction except for the last segment, i.e. the one currently being written to. The active segment will not be compacted even if all of its messages are older than the minimum compaction time lag. The log cleaner can be configured to ensure a maximum delay after which the uncompacted “head” of the log becomes eligible for log compaction.

```properties
log.cleaner.max.compaction.lag.ms
```

This can be used to prevent log with low produce rate from remaining ineligible for compaction for an unbounded duration. If not set, logs that do not exceed min.cleanable.dirty.ratio are not compacted. Note that this compaction deadline is not a hard guarantee since it is still subjected to the availability of log cleaner threads and the actual compaction time. You will want to monitor the uncleanable-partitions-count, max-clean-time-secs and max-compaction-delay-secs metrics.

Further cleaner configurations are described [here](https://kafka.apache.org/documentation.html#brokerconfigs).

<a id="design-design--quotas"></a>

## Quotas

Kafka cluster has the ability to enforce quotas on requests to control the broker resources used by clients. Two types of client quotas can be enforced by Kafka brokers for each group of clients sharing a quota:

1. Network bandwidth quotas define byte-rate thresholds (since 0.9)
2. Request rate quotas define CPU utilization thresholds as a percentage of network and I/O threads (since 0.11)

<a id="design-design--why-are-quotas-necessary"></a>

### Why are quotas necessary?

It is possible for producers and consumers to produce/consume very high volumes of data or generate requests at a very high rate and thus monopolize broker resources, cause network saturation and generally DOS other clients and the brokers themselves. Having quotas protects against these issues and is all the more important in large multi-tenant clusters where a small set of badly behaved clients can degrade user experience for the well behaved ones. In fact, when running Kafka as a service this even makes it possible to enforce API limits according to an agreed upon contract.

<a id="design-design--client-groups"></a>

### Client groups

The identity of Kafka clients is the user principal which represents an authenticated user in a secure cluster. In a cluster that supports unauthenticated clients, user principal is a grouping of unauthenticated users chosen by the broker using a configurable `PrincipalBuilder`. Client-id is a logical grouping of clients with a meaningful name chosen by the client application. The tuple (user, client-id) defines a secure logical group of clients that share both user principal and client-id.

Quotas can be applied to (user, client-id), user or client-id groups. For a given connection, the most specific quota matching the connection is applied. All connections of a quota group share the quota configured for the group. For example, if (user=“test-user”, client-id=“test-client”) has a produce quota of 10MB/sec, this is shared across all producer instances of user “test-user” with the client-id “test-client”.

<a id="design-design--quota-configuration"></a>

### Quota Configuration

Quota configuration may be defined for (user, client-id), user and client-id groups. It is possible to override the default quota at any of the quota levels that needs a higher (or even lower) quota. The mechanism is similar to the per-topic log config overrides. User and (user, client-id) quota overrides are written to the metadata log. These overrides are read by all brokers and are effective immediately. This lets us change quotas without having to do a rolling restart of the entire cluster. See here for details. Default quotas for each group may also be updated dynamically using the same mechanism.

The order of precedence for quota configuration is:

1. matching user and client-id quotas
2. matching user and default client-id quotas
3. matching user quota
4. default user and matching client-id quotas
5. default user and default client-id quotas
6. default user quota
7. matching client-id quota
8. default client-id quota

<a id="design-design--network-bandwidth-quotas"></a>

### Network Bandwidth Quotas

Network bandwidth quotas are defined as the byte rate threshold for each group of clients sharing a quota. By default, each unique client group receives a fixed quota in bytes/sec as configured by the cluster. This quota is defined on a per-broker basis. Each group of clients can publish/fetch a maximum of X bytes/sec per broker before clients are throttled.

<a id="design-design--request-rate-quotas"></a>

### Request Rate Quotas

Request rate quotas are defined as the percentage of time a client can utilize on request handler I/O threads and network threads of each broker within a quota window. A quota of `n%` represents `n%` of one thread, so the quota is out of a total capacity of `((num.io.threads + num.network.threads) * 100)%`. Each group of clients may use a total percentage of upto `n%` across all I/O and network threads in a quota window before being throttled. Since the number of threads allocated for I/O and network threads are typically based on the number of cores available on the broker host, request rate quotas represent the total percentage of CPU that may be used by each group of clients sharing the quota.

<a id="design-design--enforcement"></a>

### Enforcement

By default, each unique client group receives a fixed quota as configured by the cluster. This quota is defined on a per-broker basis. Each client can utilize this quota per broker before it gets throttled. We decided that defining these quotas per broker is much better than having a fixed cluster wide bandwidth per client because that would require a mechanism to share client quota usage among all the brokers. This can be harder to get right than the quota implementation itself!

How does a broker react when it detects a quota violation? In our solution, the broker first computes the amount of delay needed to bring the violating client under its quota and returns a response with the delay immediately. In case of a fetch request, the response will not contain any data. Then, the broker mutes the channel to the client, not to process requests from the client anymore, until the delay is over. Upon receiving a response with a non-zero delay duration, the Kafka client will also refrain from sending further requests to the broker during the delay. Therefore, requests from a throttled client are effectively blocked from both sides. Even with older client implementations that do not respect the delay response from the broker, the back pressure applied by the broker via muting its socket channel can still handle the throttling of badly behaving clients. Those clients who sent further requests to the throttled channel will receive responses only after the delay is over.

Byte-rate and thread utilization are measured over multiple small windows (e.g. 30 windows of 1 second each) in order to detect and correct quota violations quickly. Typically, having large measurement windows (for e.g. 10 windows of 30 seconds each) leads to large bursts of traffic followed by long delays which is not great in terms of user experience.

---

<a id="design-protocol"></a>

<a id="design-protocol--protocol"></a>

# Protocol

<a id="design-protocol--kafka-protocol-guide"></a>

# Kafka protocol guide

This document covers the wire protocol implemented in Kafka. It is meant to give a readable guide to the protocol that covers the available requests, their binary format, and the proper way to make use of them to implement a client. This document assumes you understand the basic design and terminology described [here](https://kafka.apache.org/documentation.html#design)

<a id="design-protocol--preliminaries"></a>

## Preliminaries

<a id="design-protocol--network"></a>

### Network

Kafka uses a binary protocol over TCP. The protocol defines all APIs as request response message pairs. All messages are size delimited and are made up of the following primitive types.

The client initiates a socket connection and then writes a sequence of request messages and reads back the corresponding response message. No handshake is required on connection or disconnection. TCP is happier if you maintain persistent connections used for many requests to amortize the cost of the TCP handshake, but beyond this penalty connecting is pretty cheap.

The client will likely need to maintain a connection to multiple brokers, as data is partitioned and the clients will need to talk to the server that has their data. However it should not generally be necessary to maintain multiple connections to a single broker from a single client instance (i.e. connection pooling).

The server guarantees that on a single TCP connection, requests will be processed in the order they are sent and responses will return in that order as well. The broker’s request processing allows only a single in-flight request per connection in order to guarantee this ordering. Note that clients can (and ideally should) use non-blocking IO to implement request pipelining and achieve higher throughput. i.e., clients can send requests even while awaiting responses for preceding requests since the outstanding requests will be buffered in the underlying OS socket buffer. All requests are initiated by the client, and result in a corresponding response message from the server except where noted.

The server has a configurable maximum limit on request size and any request that exceeds this limit will result in the socket being disconnected.

<a id="design-protocol--partitioning-and-bootstrapping"></a>

### Partitioning and bootstrapping

Kafka is a partitioned system so not all servers have the complete data set. Instead recall that topics are split into a pre-defined number of partitions, P, and each partition is replicated with some replication factor, N. Topic partitions themselves are just ordered “commit logs” numbered 0, 1, …, P-1.

All systems of this nature have the question of how a particular piece of data is assigned to a particular partition. Kafka clients directly control this assignment, the brokers themselves enforce no particular semantics of which messages should be published to a particular partition. Rather, to publish messages the client directly addresses messages to a particular partition, and when fetching messages, fetches from a particular partition. If two clients want to use the same partitioning scheme they must use the same method to compute the mapping of key to partition.

These requests to publish or fetch data must be sent to the broker that is currently acting as the leader for a given partition. This condition is enforced by the broker, so a request for a particular partition to the wrong broker will result in the NotLeaderForPartition error code (described below).

How can the client find out which topics exist, what partitions they have, and which brokers currently host those partitions so that it can direct its requests to the right hosts? This information is dynamic, so you can’t just configure each client with some static mapping file. Instead all Kafka brokers can answer a metadata request that describes the current state of the cluster: what topics there are, which partitions those topics have, which broker is the leader for those partitions, and the host and port information for these brokers.

In other words, the client needs to somehow find one broker and that broker will tell the client about all the other brokers that exist and what partitions they host. This first broker may itself go down so the best practice for a client implementation is to take a list of two or three URLs to bootstrap from. The user can then choose to use a load balancer or just statically configure two or three of their Kafka hosts in the clients.

The client does not need to keep polling to see if the cluster has changed; it can fetch metadata once when it is instantiated cache that metadata until it receives an error indicating that the metadata is out of date. This error can come in two forms: (1) a socket error indicating the client cannot communicate with a particular broker, (2) an error code in the response to a request indicating that this broker no longer hosts the partition for which data was requested.

1. Cycle through a list of “bootstrap” Kafka URLs until we find one we can connect to. Fetch cluster metadata.
2. Process fetch or produce requests, directing them to the appropriate broker based on the topic/partitions they send to or fetch from.
3. If we get an appropriate error, refresh the metadata and try again.

<a id="design-protocol--partitioning-strategies"></a>

### Partitioning Strategies

As mentioned above the assignment of messages to partitions is something the producing client controls. That said, how should this functionality be exposed to the end-user?

Partitioning really serves two purposes in Kafka:

1. It balances data and request load over brokers
2. It serves as a way to divvy up processing among consumer processes while allowing local state and preserving order within the partition. We call this semantic partitioning.

For a given use case you may care about only one of these or both.

To accomplish simple load balancing a simple approach would be for the client to just round robin requests over all brokers. Another alternative, in an environment where there are many more producers than brokers, would be to have each client choose a single partition at random and publish to that. This latter strategy will result in far fewer TCP connections.

Semantic partitioning means using some key in the message to assign messages to partitions. For example if you were processing a click message stream you might want to partition the stream by the user id so that all data for a particular user would go to a single consumer. To accomplish this the client can take a key associated with the message and use some hash of this key to choose the partition to which to deliver the message.

<a id="design-protocol--batching"></a>

### Batching

Our APIs encourage batching small things together for efficiency. We have found this is a very significant performance win. Both our API to send messages and our API to fetch messages always work with a sequence of messages not a single message to encourage this. A clever client can make use of this and support an “asynchronous” mode in which it batches together messages sent individually and sends them in larger clumps. We go even further with this and allow the batching across multiple topics and partitions, so a produce request may contain data to append to many partitions and a fetch request may pull data from many partitions all at once.

The client implementer can choose to ignore this and send everything one at a time if they like.

<a id="design-protocol--compatibility"></a>

### Compatibility

Kafka has a “bidirectional” client compatibility policy. In other words, new clients can talk to old servers, and old clients can talk to new servers. This allows users to upgrade either clients or servers without experiencing any downtime.

Since the Kafka protocol has changed over time, clients and servers need to agree on the schema of the message that they are sending over the wire. This is done through API versioning.

Before each request is sent, the client sends the API key and the API version. These two 16-bit numbers, when taken together, uniquely identify the schema of the message to follow.

The intention is that clients will support a range of API versions. When communicating with a particular broker, a given client should use the highest API version supported by both and indicate this version in their requests.

The server will reject requests with a version it does not support, and will always respond to the client with exactly the protocol format it expects based on the version it included in its request. The intended upgrade path is that new features would first be rolled out on the server (with the older clients not making use of them) and then as newer clients are deployed these new features would gradually be taken advantage of. Note there is an exceptional case while retrieving supported API versions where the server can respond with a different version.

Note that [KIP-482 tagged fields](https://cwiki.apache.org/confluence/x/OhMyBw) can be added to a request without incrementing the version number. This offers an additional way of evolving the message schema without breaking compatibility. Tagged fields do not take up any space when the field is not set. Therefore, if a field is rarely used, it is more efficient to make it a tagged field than to put it in the mandatory schema. However, tagged fields are ignored by recipients that don’t know about them, which could pose a challenge if this is not the behavior that the sender wants. In such cases, a version bump may be more appropriate.

<a id="design-protocol--retrieving-supported-api-versions"></a>

### Retrieving Supported API versions

In order to work against multiple broker versions, clients need to know what versions of various APIs a broker supports. The broker exposes this information since 0.10.0.0 as described in [KIP-35](https://cwiki.apache.org/confluence/x/KK6nAw). Clients should use the supported API versions information to choose the highest API version supported by both client and broker. If no such version exists, an error should be reported to the user.

The following sequence may be used by a client to obtain supported API versions from a broker.

1. Client sends `ApiVersionsRequest` to a broker after connection has been established with the broker. If SSL is enabled, this happens after SSL connection has been established.
2. On receiving `ApiVersionsRequest`, a broker returns its full list of supported ApiKeys and versions regardless of current authentication state (e.g., before SASL authentication on an SASL listener, do note that no Kafka protocol requests may take place on an SSL listener before the SSL handshake is finished). If this is considered to leak information about the broker version a workaround is to use SSL with client authentication which is performed at an earlier stage of the connection where the `ApiVersionRequest` is not available. Also, note that broker versions older than 0.10.0.0 do not support this API and will either ignore the request or close connection in response to the request. Also note that if the client `ApiVersionsRequest` version is unsupported by the broker (client is ahead), and the broker version is 2.4.0 or greater, then the broker will respond with a version 0 ApiVersionsResponse with the error code set to `UNSUPPORTED_VERSION` and the `api_versions` field populated with the supported version of the `ApiVersionsRequest`. It is then up to the client to retry, making another `ApiVersionsRequest` using the highest version supported by the client and broker. See [KIP-511: Collect and Expose Client’s Name and Version in the Brokers](https://cwiki.apache.org/confluence/x/qRJ4Bw)
3. If multiple versions of an API are supported by broker and client, clients are recommended to use the latest version supported by the broker and itself.
5. Supported API versions obtained from a broker are only valid for the connection on which that information is obtained. In the event of disconnection, the client should obtain the information from the broker again, as the broker might have been upgraded/downgraded in the meantime.

<a id="design-protocol--sasl-authentication-sequence"></a>

### SASL Authentication Sequence

The following sequence is used for SASL authentication:

1. Kafka `ApiVersionsRequest` may be sent by the client to obtain the version ranges of requests supported by the broker. This is optional.
2. Kafka `SaslHandshakeRequest` containing the SASL mechanism for authentication is sent by the client. If the requested mechanism is not enabled in the server, the server responds with the list of supported mechanisms and closes the client connection. If the mechanism is enabled in the server, the server sends a successful response and continues with SASL authentication.
3. The actual SASL authentication is now performed. If `SaslHandshakeRequest` version is v0, a series of SASL client and server tokens corresponding to the mechanism are sent as opaque packets without wrapping the messages with Kafka protocol headers. If `SaslHandshakeRequest` version is v1, the `SaslAuthenticate` request/response are used, where the actual SASL tokens are wrapped in the Kafka protocol. The error code in the final message from the broker will indicate if authentication succeeded or failed.
4. If authentication succeeds, subsequent packets are handled as Kafka API requests. Otherwise, the client connection is closed.

For interoperability with 0.9.0.x clients, the first packet received by the server is handled as a SASL/GSSAPI client token if it is not a valid Kafka request. SASL/GSSAPI authentication is performed starting with this packet, skipping the first two steps above.

<a id="design-protocol--the-protocol"></a>

## The Protocol

<a id="design-protocol--protocol-primitive-types"></a>

### Protocol Primitive Types

The protocol is built out of the following primitive types.

| Type | Description |
| --- | --- |
| BOOLEAN | Represents a boolean value in a byte. Values 0 and 1 are used to represent false and true respectively. When reading a boolean value, any non-zero value is considered true. |
| INT8 | Represents an integer between -27 and 27-1 inclusive. |
| INT16 | Represents an integer between -215 and 215-1 inclusive. The values are encoded using two bytes in network byte order (big-endian). |
| INT32 | Represents an integer between -231 and 231-1 inclusive. The values are encoded using four bytes in network byte order (big-endian). |
| INT64 | Represents an integer between -263 and 263-1 inclusive. The values are encoded using eight bytes in network byte order (big-endian). |
| UINT16 | Represents an integer between 0 and 65535 inclusive. The values are encoded using two bytes in network byte order (big-endian). |
| UINT32 | Represents an integer between 0 and 232-1 inclusive. The values are encoded using four bytes in network byte order (big-endian). |
| VARINT | Represents an integer between -231 and 231-1 inclusive. Encoding follows the variable-length zig-zag encoding from [Google Protocol Buffers](https://code.google.com/apis/protocolbuffers/docs/encoding.html). |
| VARLONG | Represents an integer between -263 and 263-1 inclusive. Encoding follows the variable-length zig-zag encoding from [Google Protocol Buffers](https://code.google.com/apis/protocolbuffers/docs/encoding.html). |
| UUID | Represents a type 4 immutable universally unique identifier (Uuid). The values are encoded using sixteen bytes in network byte order (big-endian). |
| FLOAT64 | Represents a double-precision 64-bit format IEEE 754 value. The values are encoded using eight bytes in network byte order (big-endian). |
| STRING | Represents a sequence of characters. First the length N is given as an INT16. Then N bytes follow which are the UTF-8 encoding of the character sequence. Length must not be negative. |
| COMPACT\_STRING | Represents a sequence of characters. First the length N + 1 is given as an UNSIGNED\_VARINT . Then N bytes follow which are the UTF-8 encoding of the character sequence. |
| NULLABLE\_STRING | Represents a sequence of characters or null. For non-null strings, first the length N is given as an INT16. Then N bytes follow which are the UTF-8 encoding of the character sequence. A null value is encoded with length of -1 and there are no following bytes. |
| COMPACT\_NULLABLE\_STRING | Represents a sequence of characters. First the length N + 1 is given as an UNSIGNED\_VARINT . Then N bytes follow which are the UTF-8 encoding of the character sequence. A null string is represented with a length of 0. |
| BYTES | Represents a raw sequence of bytes. First the length N is given as an INT32. Then N bytes follow. |
| COMPACT\_BYTES | Represents a raw sequence of bytes. First the length N+1 is given as an UNSIGNED\_VARINT. Then N bytes follow. |
| NULLABLE\_BYTES | Represents a raw sequence of bytes or null. For non-null values, first the length N is given as an INT32. Then N bytes follow. A null value is encoded with length of -1 and there are no following bytes. |
| COMPACT\_NULLABLE\_BYTES | Represents a raw sequence of bytes. First the length N+1 is given as an UNSIGNED\_VARINT. Then N bytes follow. A null object is represented with a length of 0. |
| RECORDS | Represents a sequence of Kafka records as BYTES. For a detailed description of records see [Message Sets](https://kafka.apache.org/documentation/#messageformat). |
| COMPACT\_RECORDS | Represents a sequence of Kafka records as COMPACT\_BYTES. For a detailed description of records see [Message Sets](https://kafka.apache.org/documentation/#messageformat). |
| NULLABLE\_RECORDS | Represents a sequence of Kafka records as NULLABLE\_BYTES. For a detailed description of records see [Message Sets](https://kafka.apache.org/documentation/#messageformat). |
| COMPACT\_NULLABLE\_RECORDS | Represents a sequence of Kafka records as COMPACT\_NULLABLE\_BYTES. For a detailed description of records see [Message Sets](https://kafka.apache.org/documentation/#messageformat). |
| ARRAY | Represents a sequence of objects of a given type T. Type T can be either a primitive type (e.g. STRING) or a structure. First, the length N is given as an INT32. Then N instances of type T follow. In protocol documentation an array of T instances is referred to as [T]. |
| COMPACT\_ARRAY | Represents a sequence of objects of a given type T. Type T can be either a primitive type (e.g. STRING) or a structure. First, the length N + 1 is given as an UNSIGNED\_VARINT. Then N instances of type T follow. In protocol documentation a compact array of T instances is referred to as (T). |
| NULLABLE\_ARRAY | Represents a sequence of objects of a given type T. Type T can be either a primitive type (e.g. STRING) or a structure. First, the length N is given as an INT32. Then N instances of type T follow. A null array is represented with a length of -1. In protocol documentation a nullable array of T instances is referred to as ?[T]. |
| COMPACT\_NULLABLE\_ARRAY | Represents a sequence of objects of a given type T. Type T can be either a primitive type (e.g. STRING) or a structure. First, the length N + 1 is given as an UNSIGNED\_VARINT. Then N instances of type T follow. A null array is represented with a length of 0. In protocol documentation a compact nullable array of T instances is referred to as ?(T). |
| STRUCT | A struct is named by a string with a capitalized first letter and consists of one or more fields. It represents a composite object encoded as the serialization of each field in the order they are defined.In protocol documentation a struct containing multiple fields is enclosed by { and }. |
| NULLABLE\_STRUCT | A nullable struct is named by a string with a capitalized first letter and consists of one or more fields. It represents a composite object or null. For non-null values, the first byte has value 1, followed by the serialization of each field in the order they are defined. A null value is encoded as a byte with value -1 and there are no following bytes.In protocol documentation a nullable struct containing multiple fields is enclosed by ?{ and }. |

<a id="design-protocol--notes-on-reading-the-request-format-grammars"></a>

### Notes on reading the request format grammars

The [BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)s below give an exact context free grammar for the request and response binary format. The BNF is intentionally not compact in order to give human-readable name. As always in a BNF a sequence of productions indicates concatenation. When there are multiple possible productions these are separated with ‘|’ and may be enclosed in parenthesis for grouping. The top-level definition is always given first and subsequent sub-parts are indented.

<a id="design-protocol--common-request-and-response-structure"></a>

### Common Request and Response Structure

All requests and responses originate from the following grammar which will be incrementally describe through the rest of this document:

```
RequestOrResponse => Size (RequestMessage | ResponseMessage)
  Size => int32
```

| Field | Description |
| --- | --- |
| message\_size | The message\_size field gives the size of the subsequent request or response message in bytes. The client can read requests by first reading this 4 byte size as an integer N, and then reading and parsing the subsequent N bytes of the request. |

<a id="design-protocol--request-and-response-headers"></a>

### Request and Response Headers

Different request and response versions require different versions of the corresponding headers. These header versions are specified below together with API message descriptions.

<a id="design-protocol--record-batch"></a>

### Record Batch

A description of the record batch format can be found [here](https://kafka.apache.org/documentation/#recordbatch).

<a id="design-protocol--constants"></a>

## Constants

<a id="design-protocol--error-codes"></a>

### Error Codes

We use numeric codes to indicate what problem occurred on the server. These can be translated by the client into exceptions or whatever the appropriate error handling mechanism in the client language. Here is a table of the error codes currently in use:

| Error | Code | Retriable | Description |
| --- | --- | --- | --- |
| UNKNOWN\_SERVER\_ERROR | -1 | False | The server experienced an unexpected error when processing the request. |
| NONE | 0 | False |  |
| OFFSET\_OUT\_OF\_RANGE | 1 | False | The requested offset is not within the range of offsets maintained by the server. |
| CORRUPT\_MESSAGE | 2 | True | This message has failed its CRC checksum, exceeds the valid size, has a null key for a compacted topic, or is otherwise corrupt. |
| UNKNOWN\_TOPIC\_OR\_PARTITION | 3 | True | This server does not host this topic-partition. |
| INVALID\_FETCH\_SIZE | 4 | False | The requested fetch size is invalid. |
| LEADER\_NOT\_AVAILABLE | 5 | True | There is no leader for this topic-partition as we are in the middle of a leadership election. |
| NOT\_LEADER\_OR\_FOLLOWER | 6 | True | For requests intended only for the leader, this error indicates that the broker is not the current leader. For requests intended for any replica, this error indicates that the broker is not a replica of the topic partition. |
| REQUEST\_TIMED\_OUT | 7 | True | The request timed out. |
| BROKER\_NOT\_AVAILABLE | 8 | False | The broker is not available. |
| REPLICA\_NOT\_AVAILABLE | 9 | True | The replica is not available for the requested topic-partition. Produce/Fetch requests and other requests intended only for the leader or follower return NOT\_LEADER\_OR\_FOLLOWER if the broker is not a replica of the topic-partition. |
| MESSAGE\_TOO\_LARGE | 10 | False | The request included a message larger than the max message size the server will accept. |
| STALE\_CONTROLLER\_EPOCH | 11 | False | The controller moved to another broker. |
| OFFSET\_METADATA\_TOO\_LARGE | 12 | False | The metadata field of the offset request was too large. |
| NETWORK\_EXCEPTION | 13 | True | The server disconnected before a response was received. |
| COORDINATOR\_LOAD\_IN\_PROGRESS | 14 | True | The coordinator is loading and hence can't process requests. |
| COORDINATOR\_NOT\_AVAILABLE | 15 | True | The coordinator is not available. |
| NOT\_COORDINATOR | 16 | True | This is not the correct coordinator. |
| INVALID\_TOPIC\_EXCEPTION | 17 | False | The request attempted to perform an operation on an invalid topic. |
| RECORD\_LIST\_TOO\_LARGE | 18 | False | The request included message batch larger than the configured segment size on the server. |
| NOT\_ENOUGH\_REPLICAS | 19 | True | Messages are rejected since there are fewer in-sync replicas than required. |
| NOT\_ENOUGH\_REPLICAS\_AFTER\_APPEND | 20 | True | Messages are written to the log, but to fewer in-sync replicas than required. |
| INVALID\_REQUIRED\_ACKS | 21 | False | Produce request specified an invalid value for required acks. |
| ILLEGAL\_GENERATION | 22 | False | Specified group generation id is not valid. |
| INCONSISTENT\_GROUP\_PROTOCOL | 23 | False | The group member's supported protocols are incompatible with those of existing members or first group member tried to join with empty protocol type or empty protocol list. |
| INVALID\_GROUP\_ID | 24 | False | The group id is invalid. |
| UNKNOWN\_MEMBER\_ID | 25 | False | The coordinator is not aware of this member. |
| INVALID\_SESSION\_TIMEOUT | 26 | False | The session timeout is not within the range allowed by the broker (as configured by group.min.session.timeout.ms and group.max.session.timeout.ms). |
| REBALANCE\_IN\_PROGRESS | 27 | False | The group is rebalancing, so a rejoin is needed. |
| INVALID\_COMMIT\_OFFSET\_SIZE | 28 | False | The committing offset data size is not valid. |
| TOPIC\_AUTHORIZATION\_FAILED | 29 | False | Topic authorization failed. |
| GROUP\_AUTHORIZATION\_FAILED | 30 | False | Group authorization failed. |
| CLUSTER\_AUTHORIZATION\_FAILED | 31 | False | Cluster authorization failed. |
| INVALID\_TIMESTAMP | 32 | False | The timestamp of the message is out of acceptable range. |
| UNSUPPORTED\_SASL\_MECHANISM | 33 | False | The broker does not support the requested SASL mechanism. |
| ILLEGAL\_SASL\_STATE | 34 | False | Request is not valid given the current SASL state. |
| UNSUPPORTED\_VERSION | 35 | False | The version of API is not supported. |
| TOPIC\_ALREADY\_EXISTS | 36 | False | Topic with this name already exists. |
| INVALID\_PARTITIONS | 37 | False | Number of partitions is below 1. |
| INVALID\_REPLICATION\_FACTOR | 38 | False | Replication factor is below 1 or larger than the number of available brokers. |
| INVALID\_REPLICA\_ASSIGNMENT | 39 | False | Replica assignment is invalid. |
| INVALID\_CONFIG | 40 | False | Configuration is invalid. |
| NOT\_CONTROLLER | 41 | True | This is not the correct controller for this cluster. |
| INVALID\_REQUEST | 42 | False | This most likely occurs because of a request being malformed by the client library or the message was sent to an incompatible broker. See the broker logs for more details. |
| UNSUPPORTED\_FOR\_MESSAGE\_FORMAT | 43 | False | The message format version on the broker does not support the request. |
| POLICY\_VIOLATION | 44 | False | Request parameters do not satisfy the configured policy. |
| OUT\_OF\_ORDER\_SEQUENCE\_NUMBER | 45 | False | The broker received an out of order sequence number. |
| DUPLICATE\_SEQUENCE\_NUMBER | 46 | False | The broker received a duplicate sequence number. |
| INVALID\_PRODUCER\_EPOCH | 47 | False | Producer attempted to produce with an old epoch. |
| INVALID\_TXN\_STATE | 48 | False | The producer attempted a transactional operation in an invalid state. |
| INVALID\_PRODUCER\_ID\_MAPPING | 49 | False | The producer attempted to use a producer id which is not currently assigned to its transactional id. |
| INVALID\_TRANSACTION\_TIMEOUT | 50 | False | The transaction timeout is larger than the maximum value allowed by the broker (as configured by transaction.max.timeout.ms). |
| CONCURRENT\_TRANSACTIONS | 51 | True | The producer attempted to update a transaction while another concurrent operation on the same transaction was ongoing. |
| TRANSACTION\_COORDINATOR\_FENCED | 52 | False | Indicates that the transaction coordinator sending a WriteTxnMarker is no longer the current coordinator for a given producer. |
| TRANSACTIONAL\_ID\_AUTHORIZATION\_FAILED | 53 | False | Transactional Id authorization failed. |
| SECURITY\_DISABLED | 54 | False | Security features are disabled. |
| OPERATION\_NOT\_ATTEMPTED | 55 | False | The broker did not attempt to execute this operation. This may happen for batched RPCs where some operations in the batch failed, causing the broker to respond without trying the rest. |
| KAFKA\_STORAGE\_ERROR | 56 | True | Disk error when trying to access log file on the disk. |
| LOG\_DIR\_NOT\_FOUND | 57 | False | The user-specified log directory is not found in the broker config. |
| SASL\_AUTHENTICATION\_FAILED | 58 | False | SASL Authentication failed. |
| UNKNOWN\_PRODUCER\_ID | 59 | False | This exception is raised by the broker if it could not locate the producer metadata associated with the producerId in question. This could happen if, for instance, the producer's records were deleted because their retention time had elapsed. Once the last records of the producerId are removed, the producer's metadata is removed from the broker, and future appends by the producer will return this exception. |
| REASSIGNMENT\_IN\_PROGRESS | 60 | False | A partition reassignment is in progress. |
| DELEGATION\_TOKEN\_AUTH\_DISABLED | 61 | False | Delegation Token feature is not enabled. |
| DELEGATION\_TOKEN\_NOT\_FOUND | 62 | False | Delegation Token is not found on server. |
| DELEGATION\_TOKEN\_OWNER\_MISMATCH | 63 | False | Specified Principal is not valid Owner/Renewer. |
| DELEGATION\_TOKEN\_REQUEST\_NOT\_ALLOWED | 64 | False | Delegation Token requests are not allowed on PLAINTEXT/1-way SSL channels and on delegation token authenticated channels. |
| DELEGATION\_TOKEN\_AUTHORIZATION\_FAILED | 65 | False | Delegation Token authorization failed. |
| DELEGATION\_TOKEN\_EXPIRED | 66 | False | Delegation Token is expired. |
| INVALID\_PRINCIPAL\_TYPE | 67 | False | Supplied principalType is not supported. |
| NON\_EMPTY\_GROUP | 68 | False | The group is not empty. |
| GROUP\_ID\_NOT\_FOUND | 69 | False | The group id does not exist. |
| FETCH\_SESSION\_ID\_NOT\_FOUND | 70 | True | The fetch session ID was not found. |
| INVALID\_FETCH\_SESSION\_EPOCH | 71 | True | The fetch session epoch is invalid. |
| LISTENER\_NOT\_FOUND | 72 | True | There is no listener on the leader broker that matches the listener on which metadata request was processed. |
| TOPIC\_DELETION\_DISABLED | 73 | False | Topic deletion is disabled. |
| FENCED\_LEADER\_EPOCH | 74 | True | The leader epoch in the request is older than the epoch on the broker. |
| UNKNOWN\_LEADER\_EPOCH | 75 | True | The leader epoch in the request is newer than the epoch on the broker. |
| UNSUPPORTED\_COMPRESSION\_TYPE | 76 | False | The requesting client does not support the compression type of given partition. |
| STALE\_BROKER\_EPOCH | 77 | False | Broker epoch has changed. |
| OFFSET\_NOT\_AVAILABLE | 78 | True | The leader high watermark has not caught up from a recent leader election so the offsets cannot be guaranteed to be monotonically increasing. |
| MEMBER\_ID\_REQUIRED | 79 | False | The group member needs to have a valid member id before actually entering a consumer group. |
| PREFERRED\_LEADER\_NOT\_AVAILABLE | 80 | True | The preferred leader was not available. |
| GROUP\_MAX\_SIZE\_REACHED | 81 | False | The group has reached its maximum size. |
| FENCED\_INSTANCE\_ID | 82 | False | The broker rejected this static consumer since another consumer with the same group.instance.id has registered with a different member.id. |
| ELIGIBLE\_LEADERS\_NOT\_AVAILABLE | 83 | True | Eligible topic partition leaders are not available. |
| ELECTION\_NOT\_NEEDED | 84 | True | Leader election not needed for topic partition. |
| NO\_REASSIGNMENT\_IN\_PROGRESS | 85 | False | No partition reassignment is in progress. |
| GROUP\_SUBSCRIBED\_TO\_TOPIC | 86 | False | Deleting offsets of a topic is forbidden while the consumer group is actively subscribed to it. |
| INVALID\_RECORD | 87 | False | This record has failed the validation on broker and hence will be rejected. |
| UNSTABLE\_OFFSET\_COMMIT | 88 | True | There are unstable offsets that need to be cleared. |
| THROTTLING\_QUOTA\_EXCEEDED | 89 | True | The throttling quota has been exceeded. |
| PRODUCER\_FENCED | 90 | False | There is a newer producer with the same transactionalId which fences the current one. |
| RESOURCE\_NOT\_FOUND | 91 | False | A request illegally referred to a resource that does not exist. |
| DUPLICATE\_RESOURCE | 92 | False | A request illegally referred to the same resource twice. |
| UNACCEPTABLE\_CREDENTIAL | 93 | False | Requested credential would not meet criteria for acceptability. |
| INCONSISTENT\_VOTER\_SET | 94 | False | Indicates that the either the sender or recipient of a voter-only request is not one of the expected voters. |
| INVALID\_UPDATE\_VERSION | 95 | False | The given update version was invalid. |
| FEATURE\_UPDATE\_FAILED | 96 | False | Unable to update finalized features due to an unexpected server error. |
| PRINCIPAL\_DESERIALIZATION\_FAILURE | 97 | False | Request principal deserialization failed during forwarding. This indicates an internal error on the broker cluster security setup. |
| SNAPSHOT\_NOT\_FOUND | 98 | False | Requested snapshot was not found. |
| POSITION\_OUT\_OF\_RANGE | 99 | False | Requested position is not greater than or equal to zero, and less than the size of the snapshot. |
| UNKNOWN\_TOPIC\_ID | 100 | True | This server does not host this topic ID. |
| DUPLICATE\_BROKER\_REGISTRATION | 101 | False | This broker ID is already in use. |
| BROKER\_ID\_NOT\_REGISTERED | 102 | False | The given broker ID was not registered. |
| INCONSISTENT\_TOPIC\_ID | 103 | True | The log's topic ID did not match the topic ID in the request. |
| INCONSISTENT\_CLUSTER\_ID | 104 | False | The clusterId in the request does not match that found on the server. |
| TRANSACTIONAL\_ID\_NOT\_FOUND | 105 | False | The transactionalId could not be found. |
| FETCH\_SESSION\_TOPIC\_ID\_ERROR | 106 | True | The fetch session encountered inconsistent topic ID usage. |
| INELIGIBLE\_REPLICA | 107 | False | The new ISR contains at least one ineligible replica. |
| NEW\_LEADER\_ELECTED | 108 | False | The AlterPartition request successfully updated the partition state but the leader has changed. |
| OFFSET\_MOVED\_TO\_TIERED\_STORAGE | 109 | False | The requested offset is moved to tiered storage. |
| FENCED\_MEMBER\_EPOCH | 110 | False | The member epoch is fenced by the group coordinator. The member must abandon all its partitions and rejoin. |
| UNRELEASED\_INSTANCE\_ID | 111 | False | The instance ID is still used by another member in the consumer group. That member must leave first. |
| UNSUPPORTED\_ASSIGNOR | 112 | False | The assignor or its version range is not supported by the consumer group. |
| STALE\_MEMBER\_EPOCH | 113 | False | The member epoch is stale. The member must retry after receiving its updated member epoch via the ConsumerGroupHeartbeat API. |
| MISMATCHED\_ENDPOINT\_TYPE | 114 | False | The request was sent to an endpoint of the wrong type. |
| UNSUPPORTED\_ENDPOINT\_TYPE | 115 | False | This endpoint type is not supported yet. |
| UNKNOWN\_CONTROLLER\_ID | 116 | False | This controller ID is not known. |
| UNKNOWN\_SUBSCRIPTION\_ID | 117 | False | Client sent a push telemetry request with an invalid or outdated subscription ID. |
| TELEMETRY\_TOO\_LARGE | 118 | False | Client sent a push telemetry request larger than the maximum size the broker will accept. |
| INVALID\_REGISTRATION | 119 | False | The controller has considered the broker registration to be invalid. |
| TRANSACTION\_ABORTABLE | 120 | False | The server encountered an error with the transaction. The client can abort the transaction to continue using this transactional ID. |
| INVALID\_RECORD\_STATE | 121 | False | The record state is invalid. The acknowledgement of delivery could not be completed. |
| SHARE\_SESSION\_NOT\_FOUND | 122 | True | The share session was not found. |
| INVALID\_SHARE\_SESSION\_EPOCH | 123 | True | The share session epoch is invalid. |
| FENCED\_STATE\_EPOCH | 124 | False | The share coordinator rejected the request because the share-group state epoch did not match. |
| INVALID\_VOTER\_KEY | 125 | False | The voter key doesn't match the receiving replica's key. |
| DUPLICATE\_VOTER | 126 | False | The voter is already part of the set of voters. |
| VOTER\_NOT\_FOUND | 127 | False | The voter is not part of the set of voters. |
| INVALID\_REGULAR\_EXPRESSION | 128 | False | The regular expression is not valid. |
| REBOOTSTRAP\_REQUIRED | 129 | False | Client metadata is stale. The client should rebootstrap to obtain new metadata. |
| STREAMS\_INVALID\_TOPOLOGY | 130 | False | The supplied topology is invalid. |
| STREAMS\_INVALID\_TOPOLOGY\_EPOCH | 131 | False | The supplied topology epoch is invalid. |
| STREAMS\_TOPOLOGY\_FENCED | 132 | False | The supplied topology epoch is outdated. |
| SHARE\_SESSION\_LIMIT\_REACHED | 133 | True | The limit of share sessions has been reached. |

<a id="design-protocol--api-keys"></a>

### Api Keys

The following are the numeric codes that the stable ApiKey in the request can take for each of the below request types.

| Name | Key |
| --- | --- |
| [Produce](#design-protocol--the_messages_produce) | 0 |
| [Fetch](#design-protocol--the_messages_fetch) | 1 |
| [ListOffsets](#design-protocol--the_messages_listoffsets) | 2 |
| [Metadata](#design-protocol--the_messages_metadata) | 3 |
| [OffsetCommit](#design-protocol--the_messages_offsetcommit) | 8 |
| [OffsetFetch](#design-protocol--the_messages_offsetfetch) | 9 |
| [FindCoordinator](#design-protocol--the_messages_findcoordinator) | 10 |
| [JoinGroup](#design-protocol--the_messages_joingroup) | 11 |
| [Heartbeat](#design-protocol--the_messages_heartbeat) | 12 |
| [LeaveGroup](#design-protocol--the_messages_leavegroup) | 13 |
| [SyncGroup](#design-protocol--the_messages_syncgroup) | 14 |
| [DescribeGroups](#design-protocol--the_messages_describegroups) | 15 |
| [ListGroups](#design-protocol--the_messages_listgroups) | 16 |
| [SaslHandshake](#design-protocol--the_messages_saslhandshake) | 17 |
| [ApiVersions](#design-protocol--the_messages_apiversions) | 18 |
| [CreateTopics](#design-protocol--the_messages_createtopics) | 19 |
| [DeleteTopics](#design-protocol--the_messages_deletetopics) | 20 |
| [DeleteRecords](#design-protocol--the_messages_deleterecords) | 21 |
| [InitProducerId](#design-protocol--the_messages_initproducerid) | 22 |
| [OffsetForLeaderEpoch](#design-protocol--the_messages_offsetforleaderepoch) | 23 |
| [AddPartitionsToTxn](#design-protocol--the_messages_addpartitionstotxn) | 24 |
| [AddOffsetsToTxn](#design-protocol--the_messages_addoffsetstotxn) | 25 |
| [EndTxn](#design-protocol--the_messages_endtxn) | 26 |
| [WriteTxnMarkers](#design-protocol--the_messages_writetxnmarkers) | 27 |
| [TxnOffsetCommit](#design-protocol--the_messages_txnoffsetcommit) | 28 |
| [DescribeAcls](#design-protocol--the_messages_describeacls) | 29 |
| [CreateAcls](#design-protocol--the_messages_createacls) | 30 |
| [DeleteAcls](#design-protocol--the_messages_deleteacls) | 31 |
| [DescribeConfigs](#design-protocol--the_messages_describeconfigs) | 32 |
| [AlterConfigs](#design-protocol--the_messages_alterconfigs) | 33 |
| [AlterReplicaLogDirs](#design-protocol--the_messages_alterreplicalogdirs) | 34 |
| [DescribeLogDirs](#design-protocol--the_messages_describelogdirs) | 35 |
| [SaslAuthenticate](#design-protocol--the_messages_saslauthenticate) | 36 |
| [CreatePartitions](#design-protocol--the_messages_createpartitions) | 37 |
| [CreateDelegationToken](#design-protocol--the_messages_createdelegationtoken) | 38 |
| [RenewDelegationToken](#design-protocol--the_messages_renewdelegationtoken) | 39 |
| [ExpireDelegationToken](#design-protocol--the_messages_expiredelegationtoken) | 40 |
| [DescribeDelegationToken](#design-protocol--the_messages_describedelegationtoken) | 41 |
| [DeleteGroups](#design-protocol--the_messages_deletegroups) | 42 |
| [ElectLeaders](#design-protocol--the_messages_electleaders) | 43 |
| [IncrementalAlterConfigs](#design-protocol--the_messages_incrementalalterconfigs) | 44 |
| [AlterPartitionReassignments](#design-protocol--the_messages_alterpartitionreassignments) | 45 |
| [ListPartitionReassignments](#design-protocol--the_messages_listpartitionreassignments) | 46 |
| [OffsetDelete](#design-protocol--the_messages_offsetdelete) | 47 |
| [DescribeClientQuotas](#design-protocol--the_messages_describeclientquotas) | 48 |
| [AlterClientQuotas](#design-protocol--the_messages_alterclientquotas) | 49 |
| [DescribeUserScramCredentials](#design-protocol--the_messages_describeuserscramcredentials) | 50 |
| [AlterUserScramCredentials](#design-protocol--the_messages_alteruserscramcredentials) | 51 |
| [DescribeQuorum](#design-protocol--the_messages_describequorum) | 55 |
| [UpdateFeatures](#design-protocol--the_messages_updatefeatures) | 57 |
| [DescribeCluster](#design-protocol--the_messages_describecluster) | 60 |
| [DescribeProducers](#design-protocol--the_messages_describeproducers) | 61 |
| [UnregisterBroker](#design-protocol--the_messages_unregisterbroker) | 64 |
| [DescribeTransactions](#design-protocol--the_messages_describetransactions) | 65 |
| [ListTransactions](#design-protocol--the_messages_listtransactions) | 66 |
| [ConsumerGroupHeartbeat](#design-protocol--the_messages_consumergroupheartbeat) | 68 |
| [ConsumerGroupDescribe](#design-protocol--the_messages_consumergroupdescribe) | 69 |
| [GetTelemetrySubscriptions](#design-protocol--the_messages_gettelemetrysubscriptions) | 71 |
| [PushTelemetry](#design-protocol--the_messages_pushtelemetry) | 72 |
| [ListConfigResources](#design-protocol--the_messages_listconfigresources) | 74 |
| [DescribeTopicPartitions](#design-protocol--the_messages_describetopicpartitions) | 75 |
| [ShareGroupHeartbeat](#design-protocol--the_messages_sharegroupheartbeat) | 76 |
| [ShareGroupDescribe](#design-protocol--the_messages_sharegroupdescribe) | 77 |
| [ShareFetch](#design-protocol--the_messages_sharefetch) | 78 |
| [ShareAcknowledge](#design-protocol--the_messages_shareacknowledge) | 79 |
| [AddRaftVoter](#design-protocol--the_messages_addraftvoter) | 80 |
| [RemoveRaftVoter](#design-protocol--the_messages_removeraftvoter) | 81 |
| [InitializeShareGroupState](#design-protocol--the_messages_initializesharegroupstate) | 83 |
| [ReadShareGroupState](#design-protocol--the_messages_readsharegroupstate) | 84 |
| [WriteShareGroupState](#design-protocol--the_messages_writesharegroupstate) | 85 |
| [DeleteShareGroupState](#design-protocol--the_messages_deletesharegroupstate) | 86 |
| [ReadShareGroupStateSummary](#design-protocol--the_messages_readsharegroupstatesummary) | 87 |
| [StreamsGroupHeartbeat](#design-protocol--the_messages_streamsgroupheartbeat) | 88 |
| [StreamsGroupDescribe](#design-protocol--the_messages_streamsgroupdescribe) | 89 |
| [DescribeShareGroupOffsets](#design-protocol--the_messages_describesharegroupoffsets) | 90 |
| [AlterShareGroupOffsets](#design-protocol--the_messages_altersharegroupoffsets) | 91 |
| [DeleteShareGroupOffsets](#design-protocol--the_messages_deletesharegroupoffsets) | 92 |

<a id="design-protocol--the-messages"></a>

## Some Common Philosophical Questions

Some people have asked why we don’t use HTTP. There are a number of reasons, the best is that client implementors can make use of some of the more advanced TCP features–the ability to multiplex requests, the ability to simultaneously poll many connections, etc. We have also found HTTP libraries in many languages to be surprisingly shabby.

Others have asked if maybe we shouldn’t support many different protocols. Prior experience with this was that it makes it very hard to add and test new features if they have to be ported across many protocol implementations. Our feeling is that most users don’t really see multiple protocols as a feature, they just want a good reliable client in the language of their choice.

Another question is why we don’t adopt XMPP, STOMP, AMQP or an existing protocol. The answer to this varies by protocol, but in general the problem is that the protocol does determine large parts of the implementation and we couldn’t do what we are doing if we didn’t have control over the protocol. Our belief is that it is possible to do better than existing messaging systems have in providing a truly distributed messaging system, and to do this we need to build something that works differently.

A final question is why we don’t use a system like Protocol Buffers or Thrift to define our request messages. These packages excel at helping you to managing lots and lots of serialized messages. However we have only a few messages. Support across languages is somewhat spotty (depending on the package). Finally the mapping between binary log format and wire protocol is something we manage somewhat carefully and this would not be possible with these systems. Finally we prefer the style of versioning APIs explicitly and checking this to inferring new values as nulls as it allows more nuanced control of compatibility.

<a id="implementation"></a>

<a id="implementation--implementation"></a>

# Implementation

---

<a id="implementation--network-layer"></a>

##### [Network Layer](#implementation-network-layer)

Network Layer

<a id="implementation--messages"></a>

##### [Messages](#implementation-messages)

Messages

<a id="implementation--message-format"></a>

##### [Message Format](#implementation-message-format)

Message Format

<a id="implementation--log"></a>

##### [Log](#implementation-log)

Log

<a id="implementation--distribution"></a>

##### [Distribution](#implementation-distribution)

Distribution

---

<a id="implementation-network-layer"></a>

<a id="implementation-network-layer--network-layer"></a>

# Network Layer

Network Layer

The network layer is a fairly straight-forward NIO server, and will not be described in great detail. The sendfile implementation is done by giving the `TransferableRecords` interface a `writeTo` method. This allows the file-backed message set to use the more efficient `transferTo` implementation instead of an in-process buffered write. The threading model is a single acceptor thread and *N* processor threads which handle a fixed number of connections each. This design has been pretty thoroughly tested [elsewhere](https://web.archive.org/web/20120619234320/https://sna-projects.com/blog/2009/08/introducing-the-nio-socketserver-implementation/) and found to be simple to implement and fast. The protocol is kept quite simple to allow for future implementation of clients in other languages.

---

<a id="implementation-messages"></a>

<a id="implementation-messages--messages"></a>

# Messages

Messages

Messages consist of a variable-length header, a variable-length opaque key byte array and a variable-length opaque value byte array. The format of the header is described in the following section. Leaving the key and value opaque is the right decision: there is a great deal of progress being made on serialization libraries right now, and any particular choice is unlikely to be right for all uses. Needless to say a particular application using Kafka would likely mandate a particular serialization type as part of its usage. The `RecordBatch` interface is simply an iterator over messages with specialized methods for bulk reading and writing to an NIO `Channel`.

---

<a id="implementation-message-format"></a>

<a id="implementation-message-format--message-format"></a>

# Message Format

Message Format

Messages (aka Records) are always written in batches. The technical term for a batch of messages is a record batch, and a record batch contains one or more records. In the degenerate case, we could have a record batch containing a single record. Record batches and records have their own headers. The format of each is described below.

<a id="implementation-message-format--record-batch"></a>

## Record Batch

The following is the on-disk format of a RecordBatch.

```text
baseOffset: int64
batchLength: int32
partitionLeaderEpoch: int32
magic: int8 (current magic value is 2)
crc: uint32
attributes: int16
    bit 0~2:
        0: no compression
        1: gzip
        2: snappy
        3: lz4
        4: zstd
    bit 3: timestampType
    bit 4: isTransactional (0 means not transactional)
    bit 5: isControlBatch (0 means not a control batch)
    bit 6: hasDeleteHorizonMs (0 means baseTimestamp is not set as the delete horizon for compaction)
    bit 7~15: unused
lastOffsetDelta: int32
baseTimestamp: int64
maxTimestamp: int64
producerId: int64
producerEpoch: int16
baseSequence: int32
recordsCount: int32
records: [Record]
```

Note that when compression is enabled, the compressed record data is serialized directly following the count of the number of records.

batchLength represents the number of bytes from the current position (immediately after the batchLength field) to the end of the batch. In other words, the total size of a record batch on disk is batchLength + 12 bytes, which includes the 8-byte baseOffset and the 4-byte batchLength field itself.

The CRC covers the data from the attributes to the end of the batch (i.e. all the bytes that follow the CRC). It is located after the magic byte, which means that clients must parse the magic byte before deciding how to interpret the bytes between the batch length and the magic byte. The partition leader epoch field is not included in the CRC computation to avoid the need to recompute the CRC when this field is assigned for every batch that is received by the broker. The CRC-32C (Castagnoli) polynomial is used for the computation.

On compaction, we preserve the first and last offset/sequence numbers from the original batch when the log is cleaned. This is required in order to be able to restore the producer’s state when the log is reloaded. If we did not retain the last sequence number, for example, then after a partition leader failure, the producer might see an OutOfSequence error. The base sequence number must be preserved for duplicate checking (the broker checks incoming Produce requests for duplicates by verifying that the first and last sequence numbers of the incoming batch match the last from that producer). As a result, it is possible to have empty batches in the log when all the records in the batch are cleaned but batch is still retained in order to preserve a producer’s last sequence number. One oddity here is that the baseTimestamp field is not preserved during compaction, so it will change if the first record in the batch is compacted away.

Compaction may also modify the baseTimestamp if the record batch contains records with a null payload or aborted transaction markers. The baseTimestamp will be set to the timestamp of when those records should be deleted with the delete horizon attribute bit also set.

<a id="implementation-message-format--control-batches"></a>

### Control Batches

A control batch contains a single record called the control record. Control records should not be passed on to applications. Instead, they are used by consumers to filter out aborted transactional messages.

The key of a control record conforms to the following schema:

```text
version: int16 (current version is 0)
type: int16 (0 indicates an abort marker, 1 indicates a commit)
```

The schema for the value of a control record is dependent on the type. The value is opaque to clients.

<a id="implementation-message-format--record"></a>

## Record

The on-disk format of each record is delineated below.

```text
length: varint
attributes: int8
    bit 0~7: unused
timestampDelta: varlong
offsetDelta: varint
keyLength: varint
key: byte[]
valueLength: varint
value: byte[]
headersCount: varint
Headers => [Header]
```

<a id="implementation-message-format--record-header"></a>

### Record Header

```text
headerKeyLength: varint
headerKey: String
headerValueLength: varint
Value: byte[]
```

The key of a record header is guaranteed to be non-null, while the value of a record header may be null. The order of headers in a record is preserved when producing and consuming.

We use the same varint encoding as Protobuf. More information on the latter can be found [here](https://developers.google.com/protocol-buffers/docs/encoding#varints). The count of headers in a record is also encoded as a varint.

<a id="implementation-message-format--old-message-format"></a>

## Old Message Format

Prior to Kafka 0.11, messages were transferred and stored in *message sets*. See [Old Message Format](https://kafka.apache.org/39/documentation/#messageset) for more details.

---

<a id="implementation-log"></a>

<a id="implementation-log--log"></a>

# Log

Log

A log for a topic named “my-topic” with two partitions consists of two directories (namely `my-topic-0` and `my-topic-1`) populated with data files containing the messages for that topic. The format of the log files is a sequence of “log entries”; each log entry is a 4 byte integer *N* storing the message length which is followed by the *N* message bytes. Each message is uniquely identified by a 64-bit integer *offset* giving the byte position of the start of this message in the stream of all messages ever sent to that topic on that partition. The on-disk format of each message is given below. Each log file is named with the offset of the first message it contains. So the first file created will be 00000000000000000000.log, and each additional file will have an integer name roughly *S* bytes from the previous file where *S* is the max log file size given in the configuration.

The exact binary format for records is versioned and maintained as a standard interface so record batches can be transferred between producer, broker, and client without recopying or conversion when desirable. The previous section included details about the on-disk format of records.

The use of the message offset as the message id is unusual. Our original idea was to use a GUID generated by the producer, and maintain a mapping from GUID to offset on each broker. But since a consumer must maintain an ID for each server, the global uniqueness of the GUID provides no value. Furthermore, the complexity of maintaining the mapping from a random id to an offset requires a heavy weight index structure which must be synchronized with disk, essentially requiring a full persistent random-access data structure. Thus to simplify the lookup structure we decided to use a simple per-partition atomic counter which could be coupled with the partition id and node id to uniquely identify a message; this makes the lookup structure simpler, though multiple seeks per consumer request are still likely. However once we settled on a counter, the jump to directly using the offset seemed natural–both after all are monotonically increasing integers unique to a partition. Since the offset is hidden from the consumer API this decision is ultimately an implementation detail and we went with the more efficient approach.

<a id="implementation-log--writes"></a>

## Writes

The log allows serial appends which always go to the last file. This file is rolled over to a fresh file when it reaches a configurable size (say 1GB). The log takes two configuration parameters: *M* , which gives the number of messages to write before forcing the OS to flush the file to disk, and *S* , which gives a number of seconds after which a flush is forced. This gives a durability guarantee of losing at most *M* messages or *S* seconds of data in the event of a system crash.

<a id="implementation-log--reads"></a>

## Reads

Reads are done by giving the 64-bit logical offset of a message and an *S* -byte max chunk size. This will return an iterator over the messages contained in the *S* -byte buffer. *S* is intended to be larger than any single message, but in the event of an abnormally large message, the read can be retried multiple times, each time doubling the buffer size, until the message is read successfully. A maximum message and buffer size can be specified to make the server reject messages larger than some size, and to give a bound to the client on the maximum it needs to ever read to get a complete message. It is likely that the read buffer ends with a partial message, this is easily detected by the size delimiting.

The actual process of reading from an offset requires first locating the log segment file in which the data is stored, calculating the file-specific offset from the global offset value, and then reading from that file offset. The search is done as a simple binary search variation against an in-memory range maintained for each file.

The log provides the capability of getting the most recently written message to allow clients to start subscribing as of “right now”. This is also useful in the case the consumer fails to consume its data within its SLA-specified number of days. In this case when the client attempts to consume a non-existent offset it is given an OutOfRangeException and can either reset itself or fail as appropriate to the use case.

The following is the format of the results sent to the consumer.

```text
MessageSetSend (fetch result)

total length     : 4 bytes
error code       : 2 bytes
message 1        : x bytes
...
message n        : x bytes

MultiMessageSetSend (multiFetch result)

total length       : 4 bytes
error code         : 2 bytes
messageSetSend 1
...
messageSetSend n
```

<a id="implementation-log--deletes"></a>

## Deletes

Data is deleted one log segment at a time. The log manager applies two metrics to identify segments which are eligible for deletion: time and size. For time-based policies, the record timestamps are considered, with the largest timestamp in a segment file (order of records is not relevant) defining the retention time for the entire segment. Size-based retention is disabled by default. When enabled the log manager keeps deleting the oldest segment file until the overall size of the partition is within the configured limit again. If both policies are enabled at the same time, a segment that is eligible for deletion due to either policy will be deleted. To avoid locking reads while still allowing deletes that modify the segment list we use a copy-on-write style segment list implementation that provides consistent views to allow a binary search to proceed on an immutable static snapshot view of the log segments while deletes are progressing.

<a id="implementation-log--guarantees"></a>

## Guarantees

The log provides a configuration parameter *M* which controls the maximum number of messages that are written before forcing a flush to disk. On startup a log recovery process is run that iterates over all messages in the newest log segment and verifies that each message entry is valid. A message entry is valid if the sum of its size and offset are less than the length of the file AND the CRC32 of the message payload matches the CRC stored with the message. In the event corruption is detected the log is truncated to the last valid offset.

Note that two kinds of corruption must be handled: truncation in which an unwritten block is lost due to a crash, and corruption in which a nonsense block is ADDED to the file. The reason for this is that in general the OS makes no guarantee of the write order between the file inode and the actual block data so in addition to losing written data the file can gain nonsense data if the inode is updated with a new size but a crash occurs before the block containing that data is written. The CRC detects this corner case, and prevents it from corrupting the log (though the unwritten messages are, of course, lost).

---

<a id="implementation-distribution"></a>

<a id="implementation-distribution--distribution"></a>

# Distribution

Distribution

<a id="implementation-distribution--consumer-offset-tracking"></a>

## Consumer Offset Tracking

Kafka consumer tracks the maximum offset it has consumed in each partition and has the capability to commit offsets so that it can resume from those offsets in the event of a restart. Kafka provides the option to store all the offsets for a given consumer group in a designated broker (for that group) called the group coordinator. i.e., any consumer instance in that consumer group should send its offset commits and fetches to that group coordinator (broker). Consumer groups are assigned to coordinators based on their group names. A consumer can look up its coordinator by issuing a FindCoordinatorRequest to any Kafka broker and reading the FindCoordinatorResponse which will contain the coordinator details. The consumer can then proceed to commit or fetch offsets from the coordinator broker. In case the coordinator moves, the consumer will need to rediscover the coordinator. Offset commits can be done automatically or manually by consumer instance.

When the group coordinator receives an OffsetCommitRequest, it appends the request to a special compacted Kafka topic named \_\_*consumer\_offsets*. The broker sends a successful offset commit response to the consumer only after all the replicas of the offsets topic receive the offsets. In case the offsets fail to replicate within a configurable timeout, the offset commit will fail and the consumer may retry the commit after backing off. The brokers periodically compact the offsets topic since it only needs to maintain the most recent offset commit per partition. The coordinator also caches the offsets in an in-memory table in order to serve offset fetches quickly.

When the coordinator receives an offset fetch request, it simply returns the last committed offset vector from the offsets cache. In case coordinator was just started or if it just became the coordinator for a new set of consumer groups (by becoming a leader for a partition of the offsets topic), it may need to load the offsets topic partition into the cache. In this case, the offset fetch will fail with an CoordinatorLoadInProgressException and the consumer may retry the OffsetFetchRequest after backing off.

---

<a id="operations"></a>

<a id="operations--operations"></a>

# Operations

---

<a id="operations--basic-kafka-operations"></a>

##### [Basic Kafka Operations](#operations-basic-kafka-operations)

Basic Kafka Operations

<a id="operations--datacenters"></a>

##### [Datacenters](#operations-datacenters)

Datacenters

<a id="operations--geo-replication-cross-cluster-data-mirroring"></a>

##### [Geo-Replication (Cross-Cluster Data Mirroring)](#operations-geo-replication-cross-cluster-data-mirroring)

Geo-Replication (Cross-Cluster Data Mirroring)

<a id="operations--multi-tenancy"></a>

##### [Multi-Tenancy](#operations-multi-tenancy)

Multi-Tenancy

<a id="operations--java-version"></a>

##### [Java Version](#operations-java-version)

Java Version

<a id="operations--hardware-and-os"></a>

##### [Hardware and OS](#operations-hardware-and-os)

Hardware and OS

<a id="operations--monitoring"></a>

##### [Monitoring](#operations-monitoring)

Monitoring

<a id="operations--kraft"></a>

##### [KRaft](#operations-kraft)

KRaft

<a id="operations--tiered-storage"></a>

##### [Tiered Storage](#operations-tiered-storage)

Tiered Storage

<a id="operations--consumer-rebalance-protocol"></a>

##### [Consumer Rebalance Protocol](#operations-consumer-rebalance-protocol)

Consumer Rebalance Protocol

<a id="operations--transaction-protocol"></a>

##### [Transaction Protocol](#operations-transaction-protocol)

Transaction Protocol

<a id="operations--eligible-leader-replicas"></a>

##### [Eligible Leader Replicas](#operations-eligible-leader-replicas)

Eligible Leader Replicas

---

<a id="operations-basic-kafka-operations"></a>

<a id="operations-basic-kafka-operations--basic-kafka-operations"></a>

# Basic Kafka Operations

Basic Kafka Operations

This section will review the most common operations you will perform on your Kafka cluster. All of the tools reviewed in this section are available under the `bin/` directory of the Kafka distribution and each tool will print details on all possible commandline options if it is run with no arguments.

<a id="operations-basic-kafka-operations--adding-and-removing-topics"></a>

## Adding and removing topics

You have the option of either adding topics manually or having them be created automatically when data is first published to a non-existent topic. If topics are auto-created then you may want to tune the default topic configurations used for auto-created topics.

Topics are added and modified using the topic tool:

```bash
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my_topic_name \ --partitions 20 --replication-factor 3 --config x=y
```

The replication factor controls how many servers will replicate each message that is written. If you have a replication factor of 3 then up to 2 servers can fail before you will lose access to your data. We recommend you use a replication factor of 2 or 3 so that you can transparently bounce machines without interrupting data consumption.

The partition count controls how many logs the topic will be sharded into. There are several impacts of the partition count. First each partition must fit entirely on a single server. So if you have 20 partitions the full data set (and read and write load) will be handled by no more than 20 servers (not counting replicas). Finally the partition count impacts the maximum parallelism of your consumers. This is discussed in greater detail in the concepts section.

Each sharded partition log is placed into its own folder under the Kafka log directory. The name of such folders consists of the topic name, appended by a dash (-) and the partition id. Since a typical folder name can not be over 255 characters long, there will be a limitation on the length of topic names. We assume the number of partitions will not ever be above 100,000. Therefore, topic names cannot be longer than 249 characters. This leaves just enough room in the folder name for a dash and a potentially 5 digit long partition id.

The configurations added on the command line override the default settings the server has for things like the length of time data should be retained. The complete set of per-topic configurations is documented here.

<a id="operations-basic-kafka-operations--modifying-topics"></a>

## Modifying topics

You can change the configuration or partitioning of a topic using the same topic tool.

To add partitions you can do

```bash
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --alter --topic my_topic_name \ --partitions 40
```

**Note:** Dynamically increasing the number of partitions for a topic has several important considerations and potential side effects:

- **Key Distribution Changes**: If data is partitioned by `hash(key) % number_of_partitions`, the default partitioner’s mapping logic changes when the partition count increases. This means that messages with the same key may be routed to different partitions after the expansion, potentially affecting message ordering guarantees for existing keys. Kafka will not attempt to automatically redistribute existing data.
- **Potential Data Loss with `auto.offset.reset=latest`**: Existing consumers configured with `auto.offset.reset=latest` might miss messages produced to the new partitions during the window between partition creation and consumer discovery. This occurs because consumers may not immediately detect the new partitions, and any messages produced to those partitions before the consumer rebalances will be skipped.
- **Metadata Propagation Delay**: New partitions are not immediately visible to producers and consumers due to metadata refresh intervals (controlled by `metadata.max.age.ms`). There will be a brief period where clients are unaware of the new partitions, which may result in uneven distribution of messages or consumer lag.
- **Risks with Internal Topics**: Users should **never** manually increase partitions for Kafka’s internal state topics such as `__consumer_offsets`, `__transaction_state`, `__share_group_state`, or `__cluster_metadata`. Doing so can break coordinator mapping logic, cause state inconsistencies, and lead to data corruption or system failures. These topics are managed automatically by Kafka and should not be modified manually.

To add configs:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my_topic_name --alter --add-config x=y
```

To remove a config:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name my_topic_name --alter --delete-config x
```

And finally deleting a topic:

```bash
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic my_topic_name
```

Kafka does not currently support reducing the number of partitions for a topic.

Instructions for changing the replication factor of a topic can be found here.

<a id="operations-basic-kafka-operations--graceful-shutdown"></a>

## Graceful shutdown

The Kafka cluster will automatically detect any broker shutdown or failure and elect new leaders for the partitions on that machine. This will occur whether a server fails or it is brought down intentionally for maintenance or configuration changes. For the latter cases Kafka supports a more graceful mechanism for stopping a server than just killing it. When a server is stopped gracefully it has two optimizations it will take advantage of:

1. It will sync all its logs to disk to avoid needing to do any log recovery when it restarts (i.e. validating the checksum for all messages in the tail of the log). Log recovery takes time so this speeds up intentional restarts.
2. It will migrate any partitions the server is the leader for to other replicas prior to shutting down. This will make the leadership transfer faster and minimize the time each partition is unavailable to a few milliseconds.
   Syncing the logs will happen automatically whenever the server is stopped other than by a hard kill, but the controlled leadership migration requires using a special setting:

```properties
controlled.shutdown.enable=true
```

Note that controlled shutdown will only succeed if *all* the partitions hosted on the broker have replicas (i.e. the replication factor is greater than 1 *and* at least one of these replicas is alive). This is generally what you want since shutting down the last replica would make that topic partition unavailable.

<a id="operations-basic-kafka-operations--balancing-leadership"></a>

## Balancing leadership

Whenever a broker stops or crashes, leadership for that broker’s partitions transfers to other replicas. When the broker is restarted it will only be a follower for all its partitions, meaning it will not be used for client reads and writes.

To avoid this imbalance, Kafka has a notion of preferred replicas. If the list of replicas for a partition is 1,5,9 then node 1 is preferred as the leader to either node 5 or 9 because it is earlier in the replica list. By default the Kafka cluster will try to restore leadership to the preferred replicas. This behaviour is configured with:

```properties
auto.leader.rebalance.enable=true
```

You can also set this to false, but you will then need to manually restore leadership to the restored replicas by running the command:

```bash
$ bin/kafka-leader-election.sh --bootstrap-server localhost:9092 --election-type preferred --all-topic-partitions
```

<a id="operations-basic-kafka-operations--balancing-replicas-across-racks"></a>

## Balancing replicas across racks

The rack awareness feature spreads replicas of the same partition across different racks. This extends the guarantees Kafka provides for broker-failure to cover rack-failure, limiting the risk of data loss should all the brokers on a rack fail at once. The feature can also be applied to other broker groupings such as availability zones in EC2.

You can specify that a broker belongs to a particular rack by adding a property to the broker config:

```properties
broker.rack=my-rack-id
```

When a topic is created, modified or replicas are redistributed, the rack constraint will be honoured, ensuring replicas span as many racks as they can (a partition will span min(#racks, replication-factor) different racks).

The algorithm used to assign replicas to brokers ensures that the number of leaders per broker will be constant, regardless of how brokers are distributed across racks. This ensures balanced throughput.

However if racks are assigned different numbers of brokers, the assignment of replicas will not be even. Racks with fewer brokers will get more replicas, meaning they will use more storage and put more resources into replication. Hence it is sensible to configure an equal number of brokers per rack.

<a id="operations-basic-kafka-operations--mirroring-data-between-clusters-geo-replication"></a>

## Mirroring data between clusters & Geo-replication

Kafka administrators can define data flows that cross the boundaries of individual Kafka clusters, data centers, or geographical regions. Please refer to the section on Geo-Replication for further information.

<a id="operations-basic-kafka-operations--checking-consumer-position"></a>

## Checking consumer position

Sometimes it’s useful to see the position of your consumers. We have a tool that will show the position of all consumers in a consumer group as well as how far behind the end of the log they are. To run this tool on a consumer group named *my-group* consuming a topic named *my-topic* would look like this:

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group TOPIC PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG CONSUMER-ID HOST CLIENT-ID my-topic 0 2 4 2 consumer-1-029af89c-873c-4751-a720-cefd41a669d6 /127.0.0.1 consumer-1 my-topic 1 2 3 1 consumer-1-029af89c-873c-4751-a720-cefd41a669d6 /127.0.0.1 consumer-1 my-topic 2 2 3 1 consumer-2-42c1abd4-e3b2-425d-a8bb-e1ea49b29bb2 /127.0.0.1 consumer-2
```

<a id="operations-basic-kafka-operations--managing-groups"></a>

## Managing groups

With the GroupCommand tool, we can list groups of all types, including consumer groups, share groups and streams groups. Each type of group has its own tool for administering groups of that type. For example, to list all groups in the cluster:

```bash
$ bin/kafka-groups.sh --bootstrap-server localhost:9092 --list GROUP TYPE PROTOCOL my-consumer-group Consumer consumer my-share-group Share share
```

<a id="operations-basic-kafka-operations--managing-consumer-groups"></a>

## Managing consumer groups

With the ConsumerGroupCommand tool, we can list, describe, or delete the consumer groups. The consumer group can be deleted manually, or automatically when the last committed offset for that group expires. Manual deletion works only if the group does not have any active members. For example, to list all consumer groups across all topics:

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list test-consumer-group
```

To view offsets, as mentioned earlier, we “describe” the consumer group like this:

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group TOPIC PARTITION CURRENT-OFFSET LOG-END-OFFSET LAG CONSUMER-ID HOST CLIENT-ID topic3 0 241019 395308 154289 consumer2-e76ea8c3-5d30-4299-9005-47eb41f3d3c4 /127.0.0.1 consumer2 topic2 1 520678 803288 282610 consumer2-e76ea8c3-5d30-4299-9005-47eb41f3d3c4 /127.0.0.1 consumer2 topic3 1 241018 398817 157799 consumer2-e76ea8c3-5d30-4299-9005-47eb41f3d3c4 /127.0.0.1 consumer2 topic1 0 854144 855809 1665 consumer1-3fc8d6f1-581a-4472-bdf3-3515b4aee8c1 /127.0.0.1 consumer1 topic2 0 460537 803290 342753 consumer1-3fc8d6f1-581a-4472-bdf3-3515b4aee8c1 /127.0.0.1 consumer1 topic3 2 243655 398812 155157 consumer4-117fe4d3-c6c1-4178-8ee9-eb4a3954bee0 /127.0.0.1 consumer4
```

Note that if the consumer group uses the consumer protocol, the admin client needs DESCRIBE access to all the topics used in the group (topics the members are subscribed to). In contrast, the classic protocol does not require all topics DESCRIBE authorization. There are a number of additional “describe” options that can be used to provide more detailed information about a consumer group:

- --members: This option provides the list of all active members in the consumer group.

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group --members CONSUMER-ID HOST CLIENT-ID #PARTITIONS consumer1-3fc8d6f1-581a-4472-bdf3-3515b4aee8c1 /127.0.0.1 consumer1 2 consumer4-117fe4d3-c6c1-4178-8ee9-eb4a3954bee0 /127.0.0.1 consumer4 1 consumer2-e76ea8c3-5d30-4299-9005-47eb41f3d3c4 /127.0.0.1 consumer2 3 consumer3-ecea43e4-1f01-479f-8349-f9130b75d8ee /127.0.0.1 consumer3 0
```

- --members –verbose: On top of the information reported by the “–members” options above, this option also provides the partitions assigned to each member.

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group --members --verbose CONSUMER-ID HOST CLIENT-ID #PARTITIONS ASSIGNMENT consumer1-3fc8d6f1-581a-4472-bdf3-3515b4aee8c1 /127.0.0.1 consumer1 2 topic1(0), topic2(0) consumer4-117fe4d3-c6c1-4178-8ee9-eb4a3954bee0 /127.0.0.1 consumer4 1 topic3(2) consumer2-e76ea8c3-5d30-4299-9005-47eb41f3d3c4 /127.0.0.1 consumer2 3 topic2(1), topic3(0,1) consumer3-ecea43e4-1f01-479f-8349-f9130b75d8ee /127.0.0.1 consumer3 0 -
```

- --offsets: This is the default describe option and provides the same output as the “–describe” option.
- --state: This option provides useful group-level information.

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group --state COORDINATOR (ID) ASSIGNMENT-STRATEGY STATE #MEMBERS localhost:9092 (0) range Stable 4
```

To manually delete one or multiple consumer groups, the “–delete” option can be used:

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --delete --group my-group --group my-other-group Deletion of requested consumer groups ('my-group', 'my-other-group') was successful.
```

To reset offsets of a consumer group, “–reset-offsets” option can be used. This option supports one consumer group at the time. It requires defining following scopes: –all-topics or –topic. One scope must be selected, unless you use ‘–from-file’ scenario. Also, first make sure that the consumer instances are inactive. See [KIP-122](https://cwiki.apache.org/confluence/x/_iEIB) for more details.

It has 3 execution options:

- (default) to display which offsets to reset.
- --execute : to execute –reset-offsets process.
- --export : to export the results to a CSV format.

--reset-offsets also has the following scenarios to choose from:

- --to-datetime <String: datetime> : Reset offsets to offsets from datetime. Format: ‘YYYY-MM-DDThh:mm:ss.sss’
- --to-earliest : Reset offsets to earliest offset.
- --to-latest : Reset offsets to latest offset.
- --shift-by <Long: number-of-offsets> : Reset offsets shifting current offset by ’n’, where ’n’ can be positive or negative.
- --from-file : Reset offsets to values defined in CSV file.
- --to-current : Resets offsets to current offset.
- --by-duration <String: duration> : Reset offsets to offset by duration from current timestamp. Format: ‘PnDTnHnMnS’
- --to-offset : Reset offsets to a specific offset.

Please note, that out of range offsets will be adjusted to available offset end. For example, if offset end is at 10 and offset shift request is of 15, then, offset at 10 will actually be selected.

For example, to reset offsets of a consumer group to the latest offset:

```bash
$ bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --reset-offsets --group my-group --topic topic1 --to-latest TOPIC PARTITION NEW-OFFSET topic1 0 0
```

<a id="operations-basic-kafka-operations--managing-share-groups"></a>

## Managing share groups

Use the ShareGroupCommand tool to list, describe, or delete the share groups. Only share groups without any active members can be deleted. For example, to list all share groups in a cluster:

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --list my-share-group
```

To view the current start offset and lag, use the “–describe” option:

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --describe --group my-share-group GROUP TOPIC PARTITION START-OFFSET LAG my-share-group topic1 0 4 0
```

The start offset is the earliest offset for in-flight records being evaluated for delivery to share consumers. Some records after the start offset may already have completed delivery. NOTE: The admin client needs DESCRIBE access to all the topics used in the group. There are many –describe options that provide more detailed information about a share group:

- --members: Describes active members in the share group.

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --describe --group my-share-group --members GROUP CONSUMER-ID HOST CLIENT-ID #PARTITIONS ASSIGNMENT my-share-group 94wrSQNmRda9Q6sk6jMO6Q /127.0.0.1 console-share-consumer 1 topic1:0 my-share-group EfI0sha8QSKSrL_-I_zaTA /127.0.0.1 console-share-consumer 1 topic1:0
```

You can see that both members have been assigned the same partition which they are sharing.

- --offsets: The default describe option. This provides the same output as the “–describe” option.
- --state: Describes a summary of the state of the share group.

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --describe --group my-share-group --state GROUP COORDINATOR (ID) STATE #MEMBERS my-share-group localhost:9092 (1) Stable 2
```

To reset the offsets of a share group, use the “–reset-offsets” option:

It has 2 execution options:

- --dry-run: to display which offsets to reset.
- --execute : to execute –reset-offsets process.

--reset-offsets also has the following scenarios to choose from:

- --to-datetime <String: datetime> : Reset offsets to offsets from datetime. Format: ‘YYYY-MM-DDThh:mm:ss.sss’
- --to-earliest : Reset offsets to earliest offset.
- --to-latest : Reset offsets to latest offset.

For example, to reset offsets of a share group to the latest offset:

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --reset-offsets --group my-share-group --topic topic1 --to-latest --execute GROUP TOPIC PARTITION NEW-OFFSET my-share-group topic1 0 10
```

To delete the offsets of individual topics in the share group, use the “–delete-offsets” option:

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --delete-offsets --group my-share-group --topic topic1 TOPIC STATUS topic1 Successful
```

To delete one or more share groups, use “–delete” option:

```bash
$ bin/kafka-share-groups.sh --bootstrap-server localhost:9092 --delete --group my-share-group Deletion of requested share groups ('my-share-group') was successful.
```

<a id="operations-basic-kafka-operations--expanding-your-cluster"></a>

## Expanding your cluster

Adding servers to a Kafka cluster is easy, just assign them a unique broker id and start up Kafka on your new servers. However these new servers will not automatically be assigned any data partitions, so unless partitions are moved to them they won’t be doing any work until new topics are created. So usually when you add machines to your cluster you will want to migrate some existing data to these machines.

The process of migrating data is manually initiated but fully automated. Under the covers what happens is that Kafka will add the new server as a follower of the partition it is migrating and allow it to fully replicate the existing data in that partition. When the new server has fully replicated the contents of this partition and joined the in-sync replica one of the existing replicas will delete their partition’s data.

The partition reassignment tool can be used to move partitions across brokers. An ideal partition distribution would ensure even data load and partition sizes across all brokers. The partition reassignment tool does not have the capability to automatically study the data distribution in a Kafka cluster and move partitions around to attain an even load distribution. As such, the admin has to figure out which topics or partitions should be moved around.

The partition reassignment tool can run in 3 mutually exclusive modes:

- --generate: In this mode, given a list of topics and a list of brokers, the tool generates a candidate reassignment to move all partitions of the specified topics to the new brokers. This option merely provides a convenient way to generate a partition reassignment plan given a list of topics and target brokers.
- --execute: In this mode, the tool kicks off the reassignment of partitions based on the user provided reassignment plan. (using the –reassignment-json-file option). This can either be a custom reassignment plan hand crafted by the admin or provided by using the –generate option
- --verify: In this mode, the tool verifies the status of the reassignment for all partitions listed during the last –execute. The status can be either of successfully completed, failed or in progress

<a id="operations-basic-kafka-operations--automatically-migrating-data-to-new-machines"></a>

### Automatically migrating data to new machines

The partition reassignment tool can be used to move some topics off of the current set of brokers to the newly added brokers. This is typically useful while expanding an existing cluster since it is easier to move entire topics to the new set of brokers, than moving one partition at a time. When used to do this, the user should provide a list of topics that should be moved to the new set of brokers and a target list of new brokers. The tool then evenly distributes all partitions for the given list of topics across the new set of brokers. During this move, the replication factor of the topic is kept constant. Effectively the replicas for all partitions for the input list of topics are moved from the old set of brokers to the newly added brokers.

For instance, the following example will move all partitions for topics foo1,foo2 to the new set of brokers 5,6. At the end of this move, all partitions for topics foo1 and foo2 will *only* exist on brokers 5,6.

Since the tool accepts the input list of topics as a json file, you first need to identify the topics you want to move and create the json file as follows:

```bash
$ cat topics-to-move.json {"topics": [{ "topic": "foo1" },{ "topic": "foo2" } ],"version": 1}
```

Once the json file is ready, use the partition reassignment tool to generate a candidate assignment:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --topics-to-move-json-file topics-to-move.json --broker-list "5,6" --generate Current partition replica assignment {"version":1,"partitions":[{"topic":"foo1","partition":0,"replicas":[2,1],"log_dirs":["any"]},{"topic":"foo1","partition":1,"replicas":[1,3],"log_dirs":["any"]},{"topic":"foo1","partition":2,"replicas":[3,4],"log_dirs":["any"]},{"topic":"foo2","partition":0,"replicas":[4,2],"log_dirs":["any"]},{"topic":"foo2","partition":1,"replicas":[2,1],"log_dirs":["any"]},{"topic":"foo2","partition":2,"replicas":[1,3],"log_dirs":["any"]}]}

Proposed partition reassignment configuration
{"version":1,
 "partitions":[{"topic":"foo1","partition":0,"replicas":[6,5],"log_dirs":["any"]},
               {"topic":"foo1","partition":1,"replicas":[5,6],"log_dirs":["any"]},
               {"topic":"foo1","partition":2,"replicas":[6,5],"log_dirs":["any"]},
               {"topic":"foo2","partition":0,"replicas":[5,6],"log_dirs":["any"]},
               {"topic":"foo2","partition":1,"replicas":[6,5],"log_dirs":["any"]},
               {"topic":"foo2","partition":2,"replicas":[5,6],"log_dirs":["any"]}]
}
```

The tool generates a candidate assignment that will move all partitions from topics foo1,foo2 to brokers 5,6. Note, however, that at this point, the partition movement has not started, it merely tells you the current assignment and the proposed new assignment. The current assignment should be saved in case you want to rollback to it. The new assignment should be saved in a json file (e.g. expand-cluster-reassignment.json) to be input to the tool with the –execute option as follows:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file expand-cluster-reassignment.json --execute Current partition replica assignment

{"version":1,
 "partitions":[{"topic":"foo1","partition":0,"replicas":[2,1],"log_dirs":["any"]},
               {"topic":"foo1","partition":1,"replicas":[1,3],"log_dirs":["any"]},
               {"topic":"foo1","partition":2,"replicas":[3,4],"log_dirs":["any"]},
               {"topic":"foo2","partition":0,"replicas":[4,2],"log_dirs":["any"]},
               {"topic":"foo2","partition":1,"replicas":[2,1],"log_dirs":["any"]},
               {"topic":"foo2","partition":2,"replicas":[1,3],"log_dirs":["any"]}]
}

Save this to use as the --reassignment-json-file option during rollback
Successfully started partition reassignments for foo1-0,foo1-1,foo1-2,foo2-0,foo2-1,foo2-2
```

Finally, the –verify option can be used with the tool to check the status of the partition reassignment. Note that the same expand-cluster-reassignment.json (used with the –execute option) should be used with the –verify option:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file expand-cluster-reassignment.json --verify Status of partition reassignment:Reassignment of partition [foo1,0] is completed Reassignment of partition [foo1,1] is still in progress Reassignment of partition [foo1,2] is still in progress Reassignment of partition [foo2,0] is completed Reassignment of partition [foo2,1] is completed Reassignment of partition [foo2,2] is completed
```

<a id="operations-basic-kafka-operations--custom-partition-assignment-and-migration"></a>

### Custom partition assignment and migration

The partition reassignment tool can also be used to selectively move replicas of a partition to a specific set of brokers. When used in this manner, it is assumed that the user knows the reassignment plan and does not require the tool to generate a candidate reassignment, effectively skipping the –generate step and moving straight to the –execute step

For instance, the following example moves partition 0 of topic foo1 to brokers 5,6 and partition 1 of topic foo2 to brokers 2,3:

The first step is to hand craft the custom reassignment plan in a json file:

```bash
$ cat custom-reassignment.json {"version":1,"partitions":[{"topic":"foo1","partition":0,"replicas":[5,6]},{"topic":"foo2","partition":1,"replicas":[2,3]}]}
```

Then, use the json file with the –execute option to start the reassignment process:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file custom-reassignment.json --execute Current partition replica assignment

{"version":1,
 "partitions":[{"topic":"foo1","partition":0,"replicas":[1,2],"log_dirs":["any"]},
               {"topic":"foo2","partition":1,"replicas":[3,4],"log_dirs":["any"]}]
}

Save this to use as the --reassignment-json-file option during rollback
Successfully started partition reassignments for foo1-0,foo2-1
```

The –verify option can be used with the tool to check the status of the partition reassignment. Note that the same custom-reassignment.json (used with the –execute option) should be used with the –verify option:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file custom-reassignment.json --verify Status of partition reassignment:Reassignment of partition [foo1,0] is completed Reassignment of partition [foo2,1] is completed
```

<a id="operations-basic-kafka-operations--decommissioning-brokers-and-log-directories"></a>

## Decommissioning brokers and log directories

<a id="operations-basic-kafka-operations--decommissioning-brokers"></a>

### Decommissioning brokers

The first step to decommission brokers is to mark them as cordoned via the Admin API.

For example to cordon broker 1:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config cordoned.log.dirs="*" --entity-type brokers --entity-name 1 Completed updating config for broker 1.
```

Then reassign all the partitions from that broker to other brokers in the cluster.
The partition reassignment tool does not have the ability to automatically generate a reassignment plan for decommissioning brokers yet.
As such, the admin has to come up with a reassignment plan to move the replica for all partitions hosted on the broker to be decommissioned, to the rest of the brokers.

Once all the reassignment is done, shutdown the broker and unregister it to remove it from the cluster.

For example to unregister broker 1:

```bash
$ bin/kafka-cluster.sh unregister --bootstrap-server localhost:9092 --id 1
```

<a id="operations-basic-kafka-operations--decommissioning-log-directories"></a>

### Decommissioning log directories

The first step to decommission log directories is to mark them as cordoned via the Admin API.

For example to cordon /data/dir1 from broker 1:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config cordoned.log.dirs=/data/dir1 --entity-type brokers --entity-name 1 Completed updating config for broker 1.
```

Then reassign all the partitions from the log directory to decommission to other log directories or brokers in the cluster.
The partition reassignment tool does not have the ability to automatically generate a reassignment plan for decommissioning a log directory yet.
As such, the admin has to come up with a reassignment plan to move the replica for all partitions hosted on the log directory to be decommissioned.

Once all the reassignment is done, shutdown the broker.

Then uncordon the log directory. Since the broker hosting that directory is offline, use –bootstrap-controller to do so.

For example:

```bash
$ bin/kafka-configs.sh --bootstrap-controller localhost:9093 --alter --delete-config cordoned.log.dirs --entity-type brokers --entity-name 1 Completed updating config for broker 1.
```

Update the configuration for the broker and remove the log directory to decommission from log.dir or log.dirs.

For example if the broker configuration contained:

```properties
log.dirs=/data/dir1,/data/dir2
```

Update it to:

```properties
log.dirs=/data/dir2
```

Finally restart the broker.

<a id="operations-basic-kafka-operations--increasing-replication-factor"></a>

## Increasing replication factor

Increasing the replication factor of an existing partition is easy. Just specify the extra replicas in the custom reassignment json file and use it with the –execute option to increase the replication factor of the specified partitions.

For instance, the following example increases the replication factor of partition 0 of topic foo from 1 to 3. Before increasing the replication factor, the partition’s only replica existed on broker 5. As part of increasing the replication factor, we will add more replicas on brokers 6 and 7.

The first step is to hand craft the custom reassignment plan in a json file:

```bash
$ cat increase-replication-factor.json {"version":1,"partitions":[{"topic":"foo","partition":0,"replicas":[5,6,7]}]}
```

Then, use the json file with the –execute option to start the reassignment process:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file increase-replication-factor.json --execute Current partition replica assignment

{"version":1,
 "partitions":[{"topic":"foo","partition":0,"replicas":[5],"log_dirs":["any"]}]}

Save this to use as the --reassignment-json-file option during rollback
Successfully started partition reassignment for foo-0
```

The –verify option can be used with the tool to check the status of the partition reassignment. Note that the same increase-replication-factor.json (used with the –execute option) should be used with the –verify option:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --reassignment-json-file increase-replication-factor.json --verify Status of partition reassignment:Reassignment of partition [foo,0] is completed
```

You can also verify the increase in replication factor with the kafka-topics.sh tool:

```bash
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --topic foo --describe Topic:foo PartitionCount:1 ReplicationFactor:3 Configs:Topic: foo Partition: 0 Leader: 5 Replicas: 5,6,7 Isr: 5,6,7
```

<a id="operations-basic-kafka-operations--limiting-bandwidth-usage-during-data-migration"></a>

## Limiting bandwidth usage during data migration

Kafka lets you apply a throttle to replication traffic, setting an upper bound on the bandwidth used to move replicas from machine to machine and from disk to disk. This is useful when rebalancing a cluster, adding or removing brokers or adding or removing disks, as it limits the impact these data-intensive operations will have on users.

There are two interfaces that can be used to engage a throttle. The simplest, and safest, is to apply a throttle when invoking the kafka-reassign-partitions.sh, but kafka-configs.sh can also be used to view and alter the throttle values directly.

So for example, if you were to execute a rebalance, with the below command, it would move partitions at no more than 50MB/s between brokers, and at no more than 100MB/s between disks on a broker.

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --execute --reassignment-json-file bigger-cluster.json --throttle 50000000 --replica-alter-log-dirs-throttle 100000000
```

When you execute this script you will see the throttle engage:

```text
The inter-broker throttle limit was set to 50000000 B/s
The replica-alter-dir throttle limit was set to 100000000 B/s
Successfully started partition reassignment for foo1-0
```

Should you wish to alter the throttle, during a rebalance, say to increase the inter-broker throughput so it completes quicker, you can do this by re-running the execute command with the –additional option passing the same reassignment-json-file:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --additional --execute --reassignment-json-file bigger-cluster.json --throttle 700000000 The inter-broker throttle limit was set to 700000000 B/s
```

Once the rebalance completes the administrator can check the status of the rebalance using the –verify option. If the rebalance has completed, the throttle will be removed via the –verify command. It is important that administrators remove the throttle in a timely manner once rebalancing completes by running the command with the –verify option. Failure to do so could cause regular replication traffic to be throttled.

When the –verify option is executed, and the reassignment has completed, the script will confirm that the throttle was removed:

```bash
$ bin/kafka-reassign-partitions.sh --bootstrap-server localhost:9092 --verify --reassignment-json-file bigger-cluster.json Status of partition reassignment:Reassignment of partition [my-topic,1] is completed Reassignment of partition [my-topic,0] is completed

Clearing broker-level throttles on brokers 1,2,3
Clearing topic-level throttles on topic my-topic
```

The administrator can also validate the assigned configs using the kafka-configs.sh. There are two sets of throttle configuration used to manage the throttling process. First set refers to the throttle value itself. This is configured, at a broker level, using the dynamic properties:

```properties
leader.replication.throttled.rate
follower.replication.throttled.rate
replica.alter.log.dirs.io.max.bytes.per.second
```

Then there is the configuration pair of enumerated sets of throttled replicas:

```properties
leader.replication.throttled.replicas
follower.replication.throttled.replicas
```

Which are configured per topic.

All five config values are automatically assigned by kafka-reassign-partitions.sh (discussed below).

To view the throttle limit configuration:

```bash
$ bin/kafka-configs.sh --describe --bootstrap-server localhost:9092 --entity-type brokers Configs for brokers '2' are leader.replication.throttled.rate=700000000,follower.replication.throttled.rate=700000000,replica.alter.log.dirs.io.max.bytes.per.second=1000000000 Configs for brokers '1' are leader.replication.throttled.rate=700000000,follower.replication.throttled.rate=700000000,replica.alter.log.dirs.io.max.bytes.per.second=1000000000
```

This shows the throttle applied to both leader and follower side of the replication protocol (by default both sides are assigned the same throttled throughput value), as well as the disk throttle.

To view the list of throttled replicas:

```bash
$ bin/kafka-configs.sh --describe --bootstrap-server localhost:9092 --entity-type topics Configs for topic 'my-topic' are leader.replication.throttled.replicas=1:102,0:101,
    follower.replication.throttled.replicas=1:101,0:102
```

Here we see the leader throttle is applied to partition 1 on broker 102 and partition 0 on broker 101. Likewise the follower throttle is applied to partition 1 on broker 101 and partition 0 on broker 102.

By default kafka-reassign-partitions.sh will apply the leader throttle to all replicas that exist before the rebalance, any one of which might be leader. It will apply the follower throttle to all move destinations. So if there is a partition with replicas on brokers 101,102, being reassigned to 102,103, a leader throttle, for that partition, would be applied to 101,102 and a follower throttle would be applied to 103 only.

If required, you can also use the –alter switch on kafka-configs.sh to alter the throttle configurations manually.

<a id="operations-basic-kafka-operations--safe-usage-of-throttled-replication"></a>

### Safe usage of throttled replication

Some care should be taken when using throttled replication. In particular:

*(1) Throttle Removal:*

The throttle should be removed in a timely manner once reassignment completes (by running `bin/kafka-reassign-partitions.sh --verify`).

*(2) Ensuring Progress:*

If the throttle is set too low, in comparison to the incoming write rate, it is possible for replication to not make progress. This occurs when:

```text
max(BytesInPerSec) > throttle
```

Where BytesInPerSec is the metric that monitors the write throughput of producers into each broker.

The administrator can monitor whether replication is making progress, during the rebalance, using the metric:

```text
kafka.server:type=FetcherLagMetrics,name=ConsumerLag,clientId=([-.\w]+),topic=([-.\w]+),partition=([0-9]+)
```

The lag should constantly decrease during replication. If the metric does not decrease the administrator should increase the throttle throughput as described above.

<a id="operations-basic-kafka-operations--setting-quotas"></a>

## Setting quotas

Quotas overrides and defaults may be configured at (user, client-id), user or client-id levels as described here. By default, clients receive an unlimited quota. It is possible to set custom quotas for each (user, client-id), user or client-id group.

Configure custom quota for (user=user1, client-id=clientA):

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type users --entity-name user1 --entity-type clients --entity-name clientA Updated config for entity: user-principal 'user1', client-id 'clientA'.
```

Configure custom quota for user=user1:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type users --entity-name user1 Updated config for entity: user-principal 'user1'.
```

Configure custom quota for client-id=clientA:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type clients --entity-name clientA Updated config for entity: client-id 'clientA'.
```

It is possible to set default quotas for each (user, client-id), user or client-id group by specifying *--entity-default* option instead of *--entity-name*.

Configure default client-id quota for user=user1:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type users --entity-name user1 --entity-type clients --entity-default Updated config for entity: user-principal 'user1', default client-id.
```

Configure default quota for user:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type users --entity-default Updated config for entity: default user-principal.
```

Configure default quota for client-id:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200' --entity-type clients --entity-default Updated config for entity: default client-id.
```

Here’s how to describe the quota for a given (user, client-id):

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users --entity-name user1 --entity-type clients --entity-name clientA Configs for user-principal 'user1', client-id 'clientA' are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200
```

Describe quota for a given user:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users --entity-name user1 Configs for user-principal 'user1' are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200
```

Describe quota for a given client-id:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type clients --entity-name clientA Configs for client-id 'clientA' are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200
```

Describe default quota for user:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users --entity-default Quota configs for the default user-principal are consumer_byte_rate=2048.0, request_percentage=200.0, producer_byte_rate=1024.0
```

Describe default quota for client-id:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type clients --entity-default Quota configs for the default client-id are consumer_byte_rate=2048.0, request_percentage=200.0, producer_byte_rate=1024.0
```

If entity name is not specified, all entities of the specified type are described. For example, describe all users:

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users Configs for user-principal 'user1' are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200 Configs for default user-principal are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200
```

Similarly for (user, client):

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users --entity-type clients Configs for user-principal 'user1', default client-id are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200 Configs for user-principal 'user1', client-id 'clientA' are producer_byte_rate=1024,consumer_byte_rate=2048,request_percentage=200
```

---

<a id="operations-datacenters"></a>

<a id="operations-datacenters--datacenters"></a>

# Datacenters

Datacenters

Some deployments will need to manage a data pipeline that spans multiple datacenters. Our recommended approach to this is to deploy a local Kafka cluster in each datacenter, with application instances in each datacenter interacting only with their local cluster and mirroring data between clusters (see the documentation on Geo-Replication for how to do this).

This deployment pattern allows datacenters to act as independent entities and allows us to manage and tune inter-datacenter replication centrally. This allows each facility to stand alone and operate even if the inter-datacenter links are unavailable: when this occurs the mirroring falls behind until the link is restored at which time it catches up.

For applications that need a global view of all data you can use mirroring to provide clusters which have aggregate data mirrored from the local clusters in *all* datacenters. These aggregate clusters are used for reads by applications that require the full data set.

This is not the only possible deployment pattern. It is possible to read from or write to a remote Kafka cluster over the WAN, though obviously this will add whatever latency is required to get the cluster.

Kafka naturally batches data in both the producer and consumer so it can achieve high-throughput even over a high-latency connection. To allow this though it may be necessary to increase the TCP socket buffer sizes for the producer, consumer, and broker using the `socket.send.buffer.bytes` and `socket.receive.buffer.bytes` configurations. The appropriate way to set this is documented [here](https://en.wikipedia.org/wiki/Bandwidth-delay_product).

It is generally *not* advisable to run a *single* Kafka cluster that spans multiple datacenters over a high-latency link. This will incur very high replication latency for Kafka writes, and Kafka will not remain available in all locations if the network between locations is unavailable.

---

<a id="operations-geo-replication-cross-cluster-data-mirroring"></a>

<a id="operations-geo-replication-cross-cluster-data-mirroring--geo-replication-cross-cluster-data-mirroring"></a>

# Geo-Replication (Cross-Cluster Data Mirroring)

Geo-Replication (Cross-Cluster Data Mirroring)

<a id="operations-geo-replication-cross-cluster-data-mirroring--geo-replication-overview"></a>

## Geo-Replication Overview

Kafka administrators can define data flows that cross the boundaries of individual Kafka clusters, data centers, or geo-regions. Such event streaming setups are often needed for organizational, technical, or legal requirements. Common scenarios include:

- Geo-replication
- Disaster recovery
- Feeding edge clusters into a central, aggregate cluster
- Physical isolation of clusters (such as production vs. testing)
- Cloud migration or hybrid cloud deployments
- Legal and compliance requirements

Administrators can set up such inter-cluster data flows with Kafka’s MirrorMaker (version 2), a tool to replicate data between different Kafka environments in a streaming manner. MirrorMaker is built on top of the Kafka Connect framework and supports features such as:

- Replicates topics (data plus configurations)
- Replicates consumer groups including offsets to migrate applications between clusters
- Replicates ACLs
- Preserves partitioning
- Automatically detects new topics and partitions
- Provides a wide range of metrics, such as end-to-end replication latency across multiple data centers/clusters
- Fault-tolerant and horizontally scalable operations

*Note: Geo-replication with MirrorMaker replicates data across Kafka clusters. This inter-cluster replication is different from Kafka’sintra-cluster replication, which replicates data within the same Kafka cluster.*

<a id="operations-geo-replication-cross-cluster-data-mirroring--what-are-replication-flows"></a>

## What Are Replication Flows

With MirrorMaker, Kafka administrators can replicate topics, topic configurations, consumer groups and their offsets, and ACLs from one or more source Kafka clusters to one or more target Kafka clusters, i.e., across cluster environments. In a nutshell, MirrorMaker uses Connectors to consume from source clusters and produce to target clusters.

These directional flows from source to target clusters are called replication flows. They are defined with the format `{source_cluster}->{target_cluster}` in the MirrorMaker configuration file as described later. Administrators can create complex replication topologies based on these flows.

Here are some example patterns:

- Active/Active high availability deployments: `A->B, B->A`
- Active/Passive or Active/Standby high availability deployments: `A->B`
- Aggregation (e.g., from many clusters to one): `A->K, B->K, C->K`
- Fan-out (e.g., from one to many clusters): `K->A, K->B, K->C`
- Forwarding: `A->B, B->C, C->D`

By default, a flow replicates all topics and consumer groups (except excluded ones). However, each replication flow can be configured independently. For instance, you can define that only specific topics or consumer groups are replicated from the source cluster to the target cluster.

Here is a first example on how to configure data replication from a `primary` cluster to a `secondary` cluster (an active/passive setup):

```properties
# Basic settings
clusters = primary, secondary
primary.bootstrap.servers = broker3-primary:9092
secondary.bootstrap.servers = broker5-secondary:9092

# Define replication flows
primary->secondary.enabled = true
primary->secondary.topics = foobar-topic, quux-.*
```

<a id="operations-geo-replication-cross-cluster-data-mirroring--configuring-geo-replication"></a>

## Configuring Geo-Replication

The following sections describe how to configure and run a dedicated MirrorMaker cluster. If you want to run MirrorMaker within an existing Kafka Connect cluster or other supported deployment setups, please refer to [KIP-382: MirrorMaker 2.0](https://cwiki.apache.org/confluence/x/ooOzBQ) and be aware that the names of configuration settings may vary between deployment modes.

Beyond what’s covered in the following sections, further examples and information on configuration settings are available at:

- [MirrorMakerConfig](https://github.com/apache/kafka/blob/trunk/connect/mirror/src/main/java/org/apache/kafka/connect/mirror/MirrorMakerConfig.java), [MirrorConnectorConfig](https://github.com/apache/kafka/blob/trunk/connect/mirror/src/main/java/org/apache/kafka/connect/mirror/MirrorConnectorConfig.java)
- [DefaultTopicFilter](https://github.com/apache/kafka/blob/trunk/connect/mirror/src/main/java/org/apache/kafka/connect/mirror/DefaultTopicFilter.java) for topics, [DefaultGroupFilter](https://github.com/apache/kafka/blob/trunk/connect/mirror/src/main/java/org/apache/kafka/connect/mirror/DefaultGroupFilter.java) for consumer groups
- Example configuration settings in [connect-mirror-maker.properties](https://github.com/apache/kafka/blob/trunk/config/connect-mirror-maker.properties), [KIP-382: MirrorMaker 2.0](https://cwiki.apache.org/confluence/x/ooOzBQ)

<a id="operations-geo-replication-cross-cluster-data-mirroring--configuration-file-syntax"></a>

### Configuration File Syntax

The MirrorMaker configuration file is typically named `connect-mirror-maker.properties`. You can configure a variety of components in this file:

- MirrorMaker settings: global settings including cluster definitions (aliases), plus custom settings per replication flow
- Kafka Connect and connector settings
- Kafka producer, consumer, and admin client settings

Example: Define MirrorMaker settings (explained in more detail later).

```properties
# Global settings
clusters = us-west, us-east   # defines cluster aliases
us-west.bootstrap.servers = broker3-west:9092
us-east.bootstrap.servers = broker5-east:9092

topics = .*   # all topics to be replicated by default

# Specific replication flow settings (here: flow from us-west to us-east)
us-west->us-east.enabled = true
us-west->us.east.topics = foo.*, bar.*  # override the default above
```

MirrorMaker is based on the Kafka Connect framework. Any Kafka Connect, source connector, and sink connector settings as described in the documentation chapter on Kafka Connect can be used directly in the MirrorMaker configuration, without having to change or prefix the name of the configuration setting.

Example: Define custom Kafka Connect settings to be used by MirrorMaker.

```properties
# Setting Kafka Connect defaults for MirrorMaker
tasks.max = 5
```

Most of the default Kafka Connect settings work well for MirrorMaker out-of-the-box, with the exception of `tasks.max`. In order to evenly distribute the workload across more than one MirrorMaker process, it is recommended to set `tasks.max` to at least `2` (preferably higher) depending on the available hardware resources and the total number of topic-partitions to be replicated.

You can further customize MirrorMaker’s Kafka Connect settings *per source or target cluster* (more precisely, you can specify Kafka Connect worker-level configuration settings “per connector”). Use the format of `{cluster}.{config_name}` in the MirrorMaker configuration file.

Example: Define custom connector settings for the `us-west` cluster.

```properties
# us-west custom settings
us-west.offset.storage.topic = my-mirrormaker-offsets
```

MirrorMaker internally uses the Kafka producer, consumer, and admin clients. Custom settings for these clients are often needed. To override the defaults, use the following format in the MirrorMaker configuration file:

- `{source}.consumer.{consumer_config_name}`
- `{target}.producer.{producer_config_name}`
- `{source_or_target}.admin.{admin_config_name}`

Example: Define custom producer, consumer, admin client settings.

```properties
# us-west cluster (from which to consume)
us-west.consumer.isolation.level = read_committed
us-west.admin.bootstrap.servers = broker57-primary:9092

# us-east cluster (to which to produce)
us-east.producer.compression.type = gzip
us-east.producer.buffer.memory = 32768
us-east.admin.bootstrap.servers = broker8-secondary:9092
```

<a id="operations-geo-replication-cross-cluster-data-mirroring--exactly-once"></a>

### Exactly once

Exactly-once semantics are supported for dedicated MirrorMaker clusters as of version 3.5.0.

For new MirrorMaker clusters, set the `exactly.once.source.support` property to enabled for all targeted Kafka clusters that should be written to with exactly-once semantics. For example, to enable exactly-once for writes to cluster `us-east`, the following configuration can be used:

```properties
us-east.exactly.once.source.support = enabled
```

For existing MirrorMaker clusters, a two-step upgrade is necessary. Instead of immediately setting the `exactly.once.source.support` property to enabled, first set it to `preparing` on all nodes in the cluster. Once this is complete, it can be set to `enabled` on all nodes in the cluster, in a second round of restarts.

In either case, it is also necessary to enable intra-cluster communication between the MirrorMaker nodes, as described in [KIP-710](https://cwiki.apache.org/confluence/x/4g5RCg). To do this, the `dedicated.mode.enable.internal.rest` property must be set to `true`. In addition, many of the REST-related [configuration properties available for Kafka Connect](https://kafka.apache.org/documentation/#connectconfigs) can be specified in the MirrorMaker config. For example, to enable intra-cluster communication in MirrorMaker cluster with each node listening on port 8080 of their local machine, the following should be added to the MirrorMaker config file:

```properties
dedicated.mode.enable.internal.rest = true
listeners = http://localhost:8080
```

\*\*Note that, if intra-cluster communication is enabled in production environments, it is highly recommended to secure the REST servers brought up by each MirrorMaker node. See the[configuration properties for Kafka Connect](https://kafka.apache.org/documentation/#connectconfigs) for information on how this can be accomplished. \*\*

It is also recommended to filter records from aborted transactions out from replicated data when running MirrorMaker. To do this, ensure that the consumer used to read from source clusters is configured with `isolation.level` set to `read_committed`. If replicating data from cluster `us-west`, this can be done for all replication flows that read from that cluster by adding the following to the MirrorMaker config file:

```properties
us-west.consumer.isolation.level = read_committed
```

As a final note, under the hood, MirrorMaker uses Kafka Connect source connectors to replicate data. For more information on exactly-once support for these kinds of connectors, see the [relevant docs page](https://kafka.apache.org/documentation/#connect_exactlyoncesource).

<a id="operations-geo-replication-cross-cluster-data-mirroring--creating-and-enabling-replication-flows"></a>

### Creating and Enabling Replication Flows

To define a replication flow, you must first define the respective source and target Kafka clusters in the MirrorMaker configuration file.

- `clusters` (required): comma-separated list of Kafka cluster “aliases”
- `{clusterAlias}.bootstrap.servers` (required): connection information for the specific cluster; comma-separated list of “bootstrap” Kafka brokers

Example: Define two cluster aliases `primary` and `secondary`, including their connection information.

```properties
clusters = primary, secondary
primary.bootstrap.servers = broker10-primary:9092,broker-11-primary:9092
secondary.bootstrap.servers = broker5-secondary:9092,broker6-secondary:9092
```

Secondly, you must explicitly enable individual replication flows with `{source}->{target}.enabled = true` as needed. Remember that flows are directional: if you need two-way (bidirectional) replication, you must enable flows in both directions.

```properties
# Enable replication from primary to secondary
primary->secondary.enabled = true
```

By default, a replication flow will replicate all but a few special topics and consumer groups from the source cluster to the target cluster, and automatically detect any newly created topics and groups. The names of replicated topics in the target cluster will be prefixed with the name of the source cluster (see section further below). For example, the topic `foo` in the source cluster `us-west` would be replicated to a topic named `us-west.foo` in the target cluster `us-east`.

The subsequent sections explain how to customize this basic setup according to your needs.

<a id="operations-geo-replication-cross-cluster-data-mirroring--configuring-replication-flows"></a>

### Configuring Replication Flows

The configuration of a replication flow is a combination of top-level default settings (e.g., `topics`), on top of which flow-specific settings, if any, are applied (e.g., `us-west->us-east.topics`). To change the top-level defaults, add the respective top-level setting to the MirrorMaker configuration file. To override the defaults for a specific replication flow only, use the syntax format `{source}->{target}.{config.name}`.

The most important settings are:

- `topics`: list of topics or a regular expression that defines which topics in the source cluster to replicate (default: `topics = .*`)
- `topics.exclude`: list of topics or a regular expression to subsequently exclude topics that were matched by the `topics` setting (default: `topics.exclude = .*[\-\.]internal, .*\.replica, __.*`)
- `groups`: list of topics or regular expression that defines which consumer groups in the source cluster to replicate (default: `groups = .*`)
- `groups.exclude`: list of topics or a regular expression to subsequently exclude consumer groups that were matched by the `groups` setting (default: `groups.exclude = console-consumer-.*, connect-.*, __.*`)
- `{source}->{target}.enable`: set to `true` to enable the replication flow (default: `false`)

Example:

```properties
# Custom top-level defaults that apply to all replication flows
topics = .*
groups = consumer-group1, consumer-group2

# Don't forget to enable a flow!
us-west->us-east.enabled = true

# Custom settings for specific replication flows
us-west->us-east.topics = foo.*
us-west->us-east.groups = bar.*
us-west->us-east.emit.heartbeats = false
```

Additional configuration settings are supported which can be left with their default values in most cases. See [MirrorMaker Configs](https://kafka.apache.org/documentation/#mirrormakerconfigs).

<a id="operations-geo-replication-cross-cluster-data-mirroring--securing-replication-flows"></a>

### Securing Replication Flows

MirrorMaker supports the same security settings as Kafka Connect, so please refer to the linked section for further information.

Example: Encrypt communication between MirrorMaker and the `us-east` cluster.

```properties
us-east.security.protocol=SSL
us-east.ssl.truststore.location=/path/to/truststore.jks
us-east.ssl.truststore.password=my-secret-password
us-east.ssl.keystore.location=/path/to/keystore.jks
us-east.ssl.keystore.password=my-secret-password
us-east.ssl.key.password=my-secret-password
```

<a id="operations-geo-replication-cross-cluster-data-mirroring--custom-naming-of-replicated-topics-in-target-clusters"></a>

### Custom Naming of Replicated Topics in Target Clusters

Replicated topics in a target cluster-sometimes called *remote* topics-are renamed according to a replication policy. MirrorMaker uses this policy to ensure that events (aka records, messages) from different clusters are not written to the same topic-partition. By default as per [DefaultReplicationPolicy](https://github.com/apache/kafka/blob/trunk/connect/mirror-client/src/main/java/org/apache/kafka/connect/mirror/DefaultReplicationPolicy.java), the names of replicated topics in the target clusters have the format `{source}.{source_topic_name}`:

```text
us-west         us-east
=========       =================
                bar-topic
foo-topic  -->  us-west.foo-topic
```

You can customize the separator (default: `.`) with the `replication.policy.separator` setting:

```properties
# Defining a custom separator
us-west->us-east.replication.policy.separator = _
```

If you need further control over how replicated topics are named, you can implement a custom `ReplicationPolicy` and override `replication.policy.class` (default is `DefaultReplicationPolicy`) in the MirrorMaker configuration.

<a id="operations-geo-replication-cross-cluster-data-mirroring--preventing-configuration-conflicts"></a>

### Preventing Configuration Conflicts

MirrorMaker processes share configuration via their target Kafka clusters. This behavior may cause conflicts when configurations differ among MirrorMaker processes that operate against the same target cluster.

For example, the following two MirrorMaker processes would be racy:

```properties
# Configuration of process 1
A->B.enabled = true
A->B.topics = foo

# Configuration of process 2
A->B.enabled = true
A->B.topics = bar
```

In this case, the two processes will share configuration via cluster `B`, which causes a conflict. Depending on which of the two processes is the elected “leader”, the result will be that either the topic `foo` or the topic `bar` is replicated, but not both.

It is therefore important to keep the MirrorMaker configuration consistent across replication flows to the same target cluster. This can be achieved, for example, through automation tooling or by using a single, shared MirrorMaker configuration file for your entire organization.

<a id="operations-geo-replication-cross-cluster-data-mirroring--best-practice-consume-from-remote-produce-to-local"></a>
<a id="operations-geo-replication-cross-cluster-data-mirroring--best-practice:-consume-from-remote-produce-to-local"></a>

### Best Practice: Consume from Remote, Produce to Local

To minimize latency (“producer lag”), it is recommended to locate MirrorMaker processes as close as possible to their target clusters, i.e., the clusters that it produces data to. That’s because Kafka producers typically struggle more with unreliable or high-latency network connections than Kafka consumers.

```text
First DC          Second DC
==========        =========================
primary --------- MirrorMaker --> secondary
(remote)                           (local)
```

To run such a “consume from remote, produce to local” setup, run the MirrorMaker processes close to and preferably in the same location as the target clusters, and explicitly set these “local” clusters in the `--clusters` command line parameter (blank-separated list of cluster aliases):

```bash
# Run in secondary's data center, reading from the remote `primary` cluster
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters secondary
```

The `--clusters secondary` tells the MirrorMaker process that the given cluster(s) are nearby, and prevents it from replicating data or sending configuration to clusters at other, remote locations.

<a id="operations-geo-replication-cross-cluster-data-mirroring--example-activepassive-high-availability-deployment"></a>
<a id="operations-geo-replication-cross-cluster-data-mirroring--example:-active-passive-high-availability-deployment"></a>

### Example: Active/Passive High Availability Deployment

The following example shows the basic settings to replicate topics from a primary to a secondary Kafka environment, but not from the secondary back to the primary. Please be aware that most production setups will need further configuration, such as security settings.

```properties
# Unidirectional flow (one-way) from primary to secondary cluster
primary.bootstrap.servers = broker1-primary:9092
secondary.bootstrap.servers = broker2-secondary:9092

primary->secondary.enabled = true
secondary->primary.enabled = false

primary->secondary.topics = foo.*  # only replicate some topics
```

<a id="operations-geo-replication-cross-cluster-data-mirroring--example-activeactive-high-availability-deployment"></a>
<a id="operations-geo-replication-cross-cluster-data-mirroring--example:-active-active-high-availability-deployment"></a>

### Example: Active/Active High Availability Deployment

The following example shows the basic settings to replicate topics between two clusters in both ways. Please be aware that most production setups will need further configuration, such as security settings.

```properties
# Bidirectional flow (two-way) between us-west and us-east clusters
clusters = us-west, us-east
us-west.bootstrap.servers = broker1-west:9092,broker2-west:9092
Us-east.bootstrap.servers = broker3-east:9092,broker4-east:9092

us-west->us-east.enabled = true
us-east->us-west.enabled = true
```

*Note on preventing replication “loops” (where topics will be originally replicated from A to B, then the replicated topics will be replicated yet again from B to A, and so forth)* : As long as you define the above flows in the same MirrorMaker configuration file, you do not need to explicitly add `topics.exclude` settings to prevent replication loops between the two clusters.

<a id="operations-geo-replication-cross-cluster-data-mirroring--example-multi-cluster-geo-replication"></a>
<a id="operations-geo-replication-cross-cluster-data-mirroring--example:-multi-cluster-geo-replication"></a>

### Example: Multi-Cluster Geo-Replication

Let’s put all the information from the previous sections together in a larger example. Imagine there are three data centers (west, east, north), with two Kafka clusters in each data center (e.g., `west-1`, `west-2`). The example in this section shows how to configure MirrorMaker (1) for Active/Active replication within each data center, as well as (2) for Cross Data Center Replication (XDCR).

First, define the source and target clusters along with their replication flows in the configuration:

```properties
# Basic settings
clusters: west-1, west-2, east-1, east-2, north-1, north-2
west-1.bootstrap.servers = ...
west-2.bootstrap.servers = ...
east-1.bootstrap.servers = ...
east-2.bootstrap.servers = ...
north-1.bootstrap.servers = ...
north-2.bootstrap.servers = ...

# Replication flows for Active/Active in West DC
west-1->west-2.enabled = true
west-2->west-1.enabled = true

# Replication flows for Active/Active in East DC
east-1->east-2.enabled = true
east-2->east-1.enabled = true

# Replication flows for Active/Active in North DC
north-1->north-2.enabled = true
north-2->north-1.enabled = true

# Replication flows for XDCR via west-1, east-1, north-1
west-1->east-1.enabled  = true
west-1->north-1.enabled = true
east-1->west-1.enabled  = true
east-1->north-1.enabled = true
north-1->west-1.enabled = true
north-1->east-1.enabled = true
```

Then, in each data center, launch one or more MirrorMaker as follows:

```bash
# In West DC:
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters west-1 west-2

# In East DC:
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters east-1 east-2

# In North DC:
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters north-1 north-2
```

With this configuration, records produced to any cluster will be replicated within the data center, as well as across to other data centers. By providing the `--clusters` parameter, we ensure that each MirrorMaker process produces data to nearby clusters only.

*Note:* The `--clusters` parameter is, technically, not required here. MirrorMaker will work fine without it. However, throughput may suffer from “producer lag” between data centers, and you may incur unnecessary data transfer costs.

<a id="operations-geo-replication-cross-cluster-data-mirroring--starting-geo-replication"></a>

## Starting Geo-Replication

You can run as few or as many MirrorMaker processes (think: nodes, servers) as needed. Because MirrorMaker is based on Kafka Connect, MirrorMaker processes that are configured to replicate the same Kafka clusters run in a distributed setup: They will find each other, share configuration (see section below), load balance their work, and so on. If, for example, you want to increase the throughput of replication flows, one option is to run additional MirrorMaker processes in parallel.

To start a MirrorMaker process, run the command:

```bash
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties
```

After startup, it may take a few minutes until a MirrorMaker process first begins to replicate data.

Optionally, as described previously, you can set the parameter `--clusters` to ensure that the MirrorMaker process produces data to nearby clusters only.

```bash
# Note: The cluster alias us-west must be defined in the configuration file
$ bin/connect-mirror-maker.sh connect-mirror-maker.properties --clusters us-west
```

*Note when testing replication of consumer groups:* By default, MirrorMaker does not replicate consumer groups created by the kafka-console-consumer.sh tool, which you might use to test your MirrorMaker setup on the command line. If you do want to replicate these consumer groups as well, set the `groups.exclude` configuration accordingly (default: `groups.exclude = console-consumer-.*, connect-.*, __.*`). Remember to update the configuration again once you completed your testing.

<a id="operations-geo-replication-cross-cluster-data-mirroring--stopping-geo-replication"></a>

## Stopping Geo-Replication

You can stop a running MirrorMaker process by sending a SIGTERM signal with the command:

```bash
$ kill <MirrorMaker pid>
```

<a id="operations-geo-replication-cross-cluster-data-mirroring--applying-configuration-changes"></a>

## Applying Configuration Changes

To make configuration changes take effect, the MirrorMaker process(es) must be restarted.

<a id="operations-geo-replication-cross-cluster-data-mirroring--monitoring-geo-replication"></a>

## Monitoring Geo-Replication

It is recommended to monitor MirrorMaker processes to ensure all defined replication flows are up and running correctly. MirrorMaker is built on the Connect framework and inherits all of Connect’s metrics, such `source-record-poll-rate`. In addition, MirrorMaker produces its own metrics under the `kafka.connect.mirror` metric group. Metrics are tagged with the following properties:

- `source`: alias of source cluster (e.g., `primary`)
- `target`: alias of target cluster (e.g., `secondary`)
- `topic`: replicated topic on target cluster
- `partition`: partition being replicated

Metrics are tracked for each replicated topic. The source cluster can be inferred from the topic name. For example, replicating `topic1` from `primary->secondary` will yield metrics like:

- `target=secondary`
- `topic=primary.topic1`
- `partition=1`

The following metrics are emitted:

```text
# MBean: kafka.connect.mirror:type=MirrorSourceConnector,target=([-.w]+),topic=([-.w]+),partition=([0-9]+)
record-count            # number of records replicated source -> target
record-rate             # average number of records/sec in replicated records
record-age-ms           # age of records when they are replicated
record-age-ms-min
record-age-ms-max
record-age-ms-avg
replication-latency-ms  # time it takes records to propagate source->target
replication-latency-ms-min
replication-latency-ms-max
replication-latency-ms-avg
byte-rate               # average number of bytes/sec in replicated records
byte-count              # number of bytes replicated source -> target

# MBean: kafka.connect.mirror:type=MirrorCheckpointConnector,source=([-.w]+),target=([-.w]+),group=([-.w]+),topic=([-.w]+),partition=([0-9]+)

checkpoint-latency-ms   # time it takes to replicate consumer offsets
checkpoint-latency-ms-min
checkpoint-latency-ms-max
checkpoint-latency-ms-avg
```

These metrics do not differentiate between created-at and log-append timestamps.

---

<a id="operations-multi-tenancy"></a>

<a id="operations-multi-tenancy--multi-tenancy"></a>

# Multi-Tenancy

Multi-Tenancy

<a id="operations-multi-tenancy--multi-tenancy-overview"></a>

## Multi-Tenancy Overview

As a highly scalable event streaming platform, Kafka is used by many users as their central nervous system, connecting in real-time a wide range of different systems and applications from various teams and lines of businesses. Such multi-tenant cluster environments command proper control and management to ensure the peaceful coexistence of these different needs. This section highlights features and best practices to set up such shared environments, which should help you operate clusters that meet SLAs/OLAs and that minimize potential collateral damage caused by “noisy neighbors”.

Multi-tenancy is a many-sided subject, including but not limited to:

- Creating user spaces for tenants (sometimes called namespaces)
- Configuring topics with data retention policies and more
- Securing topics and clusters with encryption, authentication, and authorization
- Isolating tenants with quotas and rate limits
- Monitoring and metering
- Inter-cluster data sharing (cf. geo-replication)

<a id="operations-multi-tenancy--creating-user-spaces-namespaces-for-tenants-with-topic-naming"></a>

## Creating User Spaces (Namespaces) For Tenants With Topic Naming

Kafka administrators operating a multi-tenant cluster typically need to define user spaces for each tenant. For the purpose of this section, “user spaces” are a collection of topics, which are grouped together under the management of a single entity or user.

In Kafka, the main unit of data is the topic. Users can create and name each topic. They can also delete them, but it is not possible to rename a topic directly. Instead, to rename a topic, the user must create a new topic, move the messages from the original topic to the new, and then delete the original. With this in mind, it is recommended to define logical spaces, based on an hierarchical topic naming structure. This setup can then be combined with security features, such as prefixed ACLs, to isolate different spaces and tenants, while also minimizing the administrative overhead for securing the data in the cluster.

These logical user spaces can be grouped in different ways, and the concrete choice depends on how your organization prefers to use your Kafka clusters. The most common groupings are as follows.

*By team or organizational unit:* Here, the team is the main aggregator. In an organization where teams are the main user of the Kafka infrastructure, this might be the best grouping.

Example topic naming structure:

- `<organization>.<team>.<dataset>.<event-name>`
  (e.g., “acme.infosec.telemetry.logins”)

*By project or product:* Here, a team manages more than one project. Their credentials will be different for each project, so all the controls and settings will always be project related.

Example topic naming structure:

- `<project>.<product>.<event-name>`
  (e.g., “mobility.payments.suspicious”)

Certain information should normally not be put in a topic name, such as information that is likely to change over time (e.g., the name of the intended consumer) or that is a technical detail or metadata that is available elsewhere (e.g., the topic’s partition count and other configuration settings).

To enforce a topic naming structure, several options are available:

- Use prefix ACLs (cf. [KIP-290](https://cwiki.apache.org/confluence/x/QpvLB)) to enforce a common prefix for topic names. For example, team A may only be permitted to create topics whose names start with `payments.teamA.`.
- Define a custom `CreateTopicPolicy` (cf. [KIP-108](https://cwiki.apache.org/confluence/x/Iw8IB) and the setting create.topic.policy.class.name) to enforce strict naming patterns. These policies provide the most flexibility and can cover complex patterns and rules to match an organization’s needs.
- Disable topic creation for normal users by denying it with an ACL, and then rely on an external process to create topics on behalf of users (e.g., scripting or your favorite automation toolkit).
- It may also be useful to disable the Kafka feature to auto-create topics on demand by setting `auto.create.topics.enable=false` in the broker configuration. Note that you should not rely solely on this option.

<a id="operations-multi-tenancy--configuring-topics-data-retention-and-more"></a>
<a id="operations-multi-tenancy--configuring-topics:-data-retention-and-more"></a>

## Configuring Topics: Data Retention And More

Kafka’s configuration is very flexible due to its fine granularity, and it supports a plethora of per-topic configuration settings to help administrators set up multi-tenant clusters. For example, administrators often need to define data retention policies to control how much and/or for how long data will be stored in a topic, with settings such as retention.bytes (size) and retention.ms (time). This limits storage consumption within the cluster, and helps complying with legal requirements such as GDPR.

<a id="operations-multi-tenancy--securing-clusters-and-topics-authentication-authorization-encryption"></a>
<a id="operations-multi-tenancy--securing-clusters-and-topics:-authentication-authorization-encryption"></a>

## Securing Clusters and Topics: Authentication, Authorization, Encryption

Because the documentation has a dedicated chapter on security that applies to any Kafka deployment, this section focuses on additional considerations for multi-tenant environments.

Security settings for Kafka fall into three main categories, which are similar to how administrators would secure other client-server data systems, like relational databases and traditional messaging systems.

1. **Encryption** of data transferred between Kafka brokers and Kafka clients, between brokers, and between brokers and other optional tools.
2. **Authentication** of connections from Kafka clients and applications to Kafka brokers, as well as connections between Kafka brokers.
3. **Authorization** of client operations such as creating, deleting, and altering the configuration of topics; writing events to or reading events from a topic; creating and deleting ACLs. Administrators can also define custom policies to put in place additional restrictions, such as a `CreateTopicPolicy` and `AlterConfigPolicy` (see [KIP-108](https://cwiki.apache.org/confluence/x/Iw8IB) and the settings create.topic.policy.class.name, alter.config.policy.class.name).

When securing a multi-tenant Kafka environment, the most common administrative task is the third category (authorization), i.e., managing the user/client permissions that grant or deny access to certain topics and thus to the data stored by users within a cluster. This task is performed predominantly through the setting of access control lists (ACLs). Here, administrators of multi-tenant environments in particular benefit from putting a hierarchical topic naming structure in place as described in a previous section, because they can conveniently control access to topics through prefixed ACLs (`--resource-pattern-type Prefixed`). This significantly minimizes the administrative overhead of securing topics in multi-tenant environments: administrators can make their own trade-offs between higher developer convenience (more lenient permissions, using fewer and broader ACLs) vs. tighter security (more stringent permissions, using more and narrower ACLs).

In the following example, user Alice-a new member of ACME corporation’s InfoSec team-is granted write permissions to all topics whose names start with “acme.infosec.”, such as “acme.infosec.telemetry.logins” and “acme.infosec.syslogs.events”.

```bash
# Grant permissions to user Alice
$ bin/kafka-acls.sh \ --bootstrap-server localhost:9092 \ --add --allow-principal User:Alice \ --producer \ --resource-pattern-type prefixed --topic acme.infosec.
```

You can similarly use this approach to isolate different customers on the same shared cluster.

<a id="operations-multi-tenancy--isolating-tenants-quotas-rate-limiting-throttling"></a>
<a id="operations-multi-tenancy--isolating-tenants:-quotas-rate-limiting-throttling"></a>

## Isolating Tenants: Quotas, Rate Limiting, Throttling

Multi-tenant clusters should generally be configured with quotas, which protect against users (tenants) eating up too many cluster resources, such as when they attempt to write or read very high volumes of data, or create requests to brokers at an excessively high rate. This may cause network saturation, monopolize broker resources, and impact other clients-all of which you want to avoid in a shared environment.

**Client quotas:** Kafka supports different types of (per-user principal) client quotas. Because a client’s quotas apply irrespective of which topics the client is writing to or reading from, they are a convenient and effective tool to allocate resources in a multi-tenant cluster. Request rate quotas, for example, help to limit a user’s impact on broker CPU usage by limiting the time a broker spends on the [request handling path](https://kafka.apache.org/protocol.html) for that user, after which throttling kicks in. In many situations, isolating users with request rate quotas has a bigger impact in multi-tenant clusters than setting incoming/outgoing network bandwidth quotas, because excessive broker CPU usage for processing requests reduces the effective bandwidth the broker can serve. Furthermore, administrators can also define quotas on topic operations-such as create, delete, and alter-to prevent Kafka clusters from being overwhelmed by highly concurrent topic operations (see [KIP-599](https://cwiki.apache.org/confluence/x/6DLcC) and the quota type `controller_mutation_rate`).

**Server quotas:** Kafka also supports different types of broker-side quotas. For example, administrators can set a limit on the rate with which the broker accepts new connections, set the maximum number of connections per broker, or set the maximum number of connections allowed from a specific IP address.

For more information, please refer to the quota overview and how to set quotas.

<a id="operations-multi-tenancy--monitoring-and-metering"></a>

## Monitoring and Metering

Monitoring is a broader subject that is covered elsewhere in the documentation. Administrators of any Kafka environment, but especially multi-tenant ones, should set up monitoring according to these instructions. Kafka supports a wide range of metrics, such as the rate of failed authentication attempts, request latency, consumer lag, total number of consumer groups, metrics on the quotas described in the previous section, and many more.

For example, monitoring can be configured to track the size of topic-partitions (with the JMX metric `kafka.log.Log.Size.<TOPIC-NAME>`), and thus the total size of data stored in a topic. You can then define alerts when tenants on shared clusters are getting close to using too much storage space.

<a id="operations-multi-tenancy--multi-tenancy-and-geo-replication"></a>

## Multi-Tenancy and Geo-Replication

Kafka lets you share data across different clusters, which may be located in different geographical regions, data centers, and so on. Apart from use cases such as disaster recovery, this functionality is useful when a multi-tenant setup requires inter-cluster data sharing. See the section Geo-Replication (Cross-Cluster Data Mirroring) for more information.

<a id="operations-multi-tenancy--further-considerations"></a>

## Further considerations

**Data contracts:** You may need to define data contracts between the producers and the consumers of data in a cluster, using event schemas. This ensures that events written to Kafka can always be read properly again, and prevents malformed or corrupt events being written. The best way to achieve this is to deploy a so-called schema registry alongside the cluster. (Kafka does not include a schema registry, but there are third-party implementations available.) A schema registry manages the event schemas and maps the schemas to topics, so that producers know which topics are accepting which types (schemas) of events, and consumers know how to read and parse events in a topic. Some registry implementations provide further functionality, such as schema evolution, storing a history of all schemas, and schema compatibility settings.

---

<a id="operations-java-version"></a>

<a id="operations-java-version--java-version"></a>

# Java Version

Java Version

Java 17, Java 21, and Java 25 are fully supported while Java 11 is supported for a subset of modules (clients, streams and related). Support for versions newer than the most recent LTS version are best-effort and the project typically only tests with the most recent non LTS version.

We generally recommend running Apache Kafka with the most recent LTS release (Java 25 at the time of writing) for performance, efficiency and support reasons. From a security perspective, we recommend the latest released patch version as older versions typically have disclosed security vulnerabilities.

Typical arguments for running Kafka with OpenJDK-based Java implementations (including Oracle JDK) are:

```bash
-Xmx6g -Xms6g -XX:MetaspaceSize=96m -XX:+UseG1GC
-XX:MaxGCPauseMillis=20 -XX:InitiatingHeapOccupancyPercent=35 -XX:G1HeapRegionSize=16M
-XX:MinMetaspaceFreeRatio=50 -XX:MaxMetaspaceFreeRatio=80 -XX:+ExplicitGCInvokesConcurrent
```

For reference, here are the stats for one of LinkedIn’s busiest clusters (at peak) that uses said Java arguments:

- 60 brokers
- 50k partitions (replication factor 2)
- 800k messages/sec in
- 300 MB/sec inbound, 1 GB/sec+ outbound

All of the brokers in that cluster have a 90% GC pause time of about 21ms with less than 1 young GC per second.

---

<a id="operations-hardware-and-os"></a>

<a id="operations-hardware-and-os--hardware-and-os"></a>

# Hardware and OS

Hardware and OS

We are using dual quad-core Intel Xeon machines with 24GB of memory.

You need sufficient memory to buffer active readers and writers. You can do a back-of-the-envelope estimate of memory needs by assuming you want to be able to buffer for 30 seconds and compute your memory need as write\_throughput\*30.

The disk throughput is important. We have 8x7200 rpm SATA drives. In general disk throughput is the performance bottleneck, and more disks is better. Depending on how you configure flush behavior you may or may not benefit from more expensive disks (if you force flush often then higher RPM SAS drives may be better).

<a id="operations-hardware-and-os--os"></a>

## OS

Kafka should run well on any unix system and has been tested on Linux and Solaris.

We have seen a few issues running on Windows and Windows is not currently a well supported platform though we would be happy to change that.

It is unlikely to require much OS-level tuning, but there are three potentially important OS-level configurations:

- File descriptor limits: Kafka uses file descriptors for log segments and open connections. If a broker hosts many partitions, consider that the broker needs at least (number\_of\_partitions)\*(partition\_size/segment\_size) to track all log segments in addition to the number of connections the broker makes. We recommend at least 100000 allowed file descriptors for the broker processes as a starting point. Note: The mmap() function adds an extra reference to the file associated with the file descriptor fildes which is not removed by a subsequent close() on that file descriptor. This reference is removed when there are no more mappings to the file.
- Max socket buffer size: can be increased to enable high-performance data transfer between data centers as [described here](https://www.psc.edu/index.php/networking/641-tcp-tune).
- Maximum number of memory map areas a process may have (aka vm.max\_map\_count). [See the Linux kernel documentation](https://kernel.org/doc/Documentation/sysctl/vm.txt). You should keep an eye at this OS-level property when considering the maximum number of partitions a broker may have. By default, on a number of Linux systems, the value of vm.max\_map\_count is somewhere around 65535. Each log segment, allocated per partition, requires a pair of index/timeindex files, and each of these files consumes 1 map area. In other words, each log segment uses 2 map areas. Thus, each partition requires minimum 2 map areas, as long as it hosts a single log segment. That is to say, creating 50000 partitions on a broker will result allocation of 100000 map areas and likely cause broker crash with OutOfMemoryError (Map failed) on a system with default vm.max\_map\_count. Keep in mind that the number of log segments per partition varies depending on the segment size, load intensity, retention policy and, generally, tends to be more than one.

<a id="operations-hardware-and-os--disks-and-filesystem"></a>

## Disks and Filesystem

We recommend using multiple drives to get good throughput and not sharing the same drives used for Kafka data with application logs or other OS filesystem activity to ensure good latency. You can either RAID these drives together into a single volume or format and mount each drive as its own directory. Since Kafka has replication the redundancy provided by RAID can also be provided at the application level. This choice has several tradeoffs.

If you configure multiple data directories partitions will be assigned round-robin to data directories. Each partition will be entirely in one of the data directories. If data is not well balanced among partitions this can lead to load imbalance between disks.

RAID can potentially do better at balancing load between disks (although it doesn’t always seem to) because it balances load at a lower level. The primary downside of RAID is that it is usually a big performance hit for write throughput and reduces the available disk space.

Another potential benefit of RAID is the ability to tolerate disk failures. However our experience has been that rebuilding the RAID array is so I/O intensive that it effectively disables the server, so this does not provide much real availability improvement.

<a id="operations-hardware-and-os--application-vs-os-flush-management"></a>
<a id="operations-hardware-and-os--application-vs.-os-flush-management"></a>

## Application vs. OS Flush Management

Kafka always immediately writes all data to the filesystem and supports the ability to configure the flush policy that controls when data is forced out of the OS cache and onto disk using the flush. This flush policy can be controlled to force data to disk after a period of time or after a certain number of messages has been written. There are several choices in this configuration.

Kafka must eventually call fsync to know that data was flushed. When recovering from a crash for any log segment not known to be fsync’d Kafka will check the integrity of each message by checking its CRC and also rebuild the accompanying offset index file as part of the recovery process executed on startup.

Note that durability in Kafka does not require syncing data to disk, as a failed node will always recover from its replicas.

We recommend using the default flush settings which disable application fsync entirely. This means relying on the background flush done by the OS and Kafka’s own background flush. This provides the best of all worlds for most uses: no knobs to tune, great throughput and latency, and full recovery guarantees. We generally feel that the guarantees provided by replication are stronger than sync to local disk, however the paranoid still may prefer having both and application level fsync policies are still supported.

The drawback of using application level flush settings is that it is less efficient in its disk usage pattern (it gives the OS less leeway to re-order writes) and it can introduce latency as fsync in most Linux filesystems blocks writes to the file whereas the background flushing does much more granular page-level locking.

In general you don’t need to do any low-level tuning of the filesystem, but in the next few sections we will go over some of this in case it is useful.

<a id="operations-hardware-and-os--understanding-linux-os-flush-behavior"></a>

## Understanding Linux OS Flush Behavior

In Linux, data written to the filesystem is maintained in [pagecache](https://en.wikipedia.org/wiki/Page_cache) until it must be written out to disk (due to an application-level fsync or the OS’s own flush policy). The flushing of data is done by a set of background threads called pdflush (or in post 2.6.32 kernels “flusher threads”).

Pdflush has a configurable policy that controls how much dirty data can be maintained in cache and for how long before it must be written back to disk. This policy is described [here](https://web.archive.org/web/20160518040713/http://www.westnet.com/~gsmith/content/linux-pdflush.htm). When Pdflush cannot keep up with the rate of data being written it will eventually cause the writing process to block incurring latency in the writes to slow down the accumulation of data.

You can see the current state of OS memory usage by doing

```bash
$ cat /proc/meminfo
```

The meaning of these values are described in the link above.

Using pagecache has several advantages over an in-process cache for storing data that will be written out to disk:

- The I/O scheduler will batch together consecutive small writes into bigger physical writes which improves throughput.
- The I/O scheduler will attempt to re-sequence writes to minimize movement of the disk head which improves throughput.
- It automatically uses all the free memory on the machine

<a id="operations-hardware-and-os--filesystem-selection"></a>

## Filesystem Selection

Kafka uses regular files on disk, and as such it has no hard dependency on a specific filesystem. The two filesystems which have the most usage, however, are EXT4 and XFS. Historically, EXT4 has had more usage, but recent improvements to the XFS filesystem have shown it to have better performance characteristics for Kafka’s workload with no compromise in stability.

Comparison testing was performed on a cluster with significant message loads, using a variety of filesystem creation and mount options. The primary metric in Kafka that was monitored was the “Request Local Time”, indicating the amount of time append operations were taking. XFS resulted in much better local times (160ms vs. 250ms+ for the best EXT4 configuration), as well as lower average wait times. The XFS performance also showed less variability in disk performance.

<a id="operations-hardware-and-os--general-filesystem-notes"></a>

### General Filesystem Notes

For any filesystem used for data directories, on Linux systems, the following options are recommended to be used at mount time:

- noatime: This option disables updating of a file’s atime (last access time) attribute when the file is read. This can eliminate a significant number of filesystem writes, especially in the case of bootstrapping consumers. Kafka does not rely on the atime attributes at all, so it is safe to disable this.

<a id="operations-hardware-and-os--xfs-notes"></a>

### XFS Notes

The XFS filesystem has a significant amount of auto-tuning in place, so it does not require any change in the default settings, either at filesystem creation time or at mount. The only tuning parameters worth considering are:

- largeio: This affects the preferred I/O size reported by the stat call. While this can allow for higher performance on larger disk writes, in practice it had minimal or no effect on performance.
- nobarrier: For underlying devices that have battery-backed cache, this option can provide a little more performance by disabling periodic write flushes. However, if the underlying device is well-behaved, it will report to the filesystem that it does not require flushes, and this option will have no effect.

<a id="operations-hardware-and-os--ext4-notes"></a>

### EXT4 Notes

EXT4 is a serviceable choice of filesystem for the Kafka data directories, however getting the most performance out of it will require adjusting several mount options. In addition, these options are generally unsafe in a failure scenario, and will result in much more data loss and corruption. For a single broker failure, this is not much of a concern as the disk can be wiped and the replicas rebuilt from the cluster. In a multiple-failure scenario, such as a power outage, this can mean underlying filesystem (and therefore data) corruption that is not easily recoverable. The following options can be adjusted:

- data=writeback: Ext4 defaults to data=ordered which puts a strong order on some writes. Kafka does not require this ordering as it does very paranoid data recovery on all unflushed log. This setting removes the ordering constraint and seems to significantly reduce latency.
- Disabling journaling: Journaling is a tradeoff: it makes reboots faster after server crashes but it introduces a great deal of additional locking which adds variance to write performance. Those who don’t care about reboot time and want to reduce a major source of write latency spikes can turn off journaling entirely.
- commit=num\_secs: This tunes the frequency with which ext4 commits to its metadata journal. Setting this to a lower value reduces the loss of unflushed data during a crash. Setting this to a higher value will improve throughput.
- nobh: This setting controls additional ordering guarantees when using data=writeback mode. This should be safe with Kafka as we do not depend on write ordering and improves throughput and latency.
- delalloc: Delayed allocation means that the filesystem avoid allocating any blocks until the physical write occurs. This allows ext4 to allocate a large extent instead of smaller pages and helps ensure the data is written sequentially. This feature is great for throughput. It does seem to involve some locking in the filesystem which adds a bit of latency variance.
- fast\_commit: Added in Linux 5.10, [fast\_commit](https://lwn.net/Articles/842385/) is a lighter-weight journaling method which can be used with data=ordered journaling mode. Enabling it seems to significantly reduce latency.

<a id="operations-hardware-and-os--replace-kraft-controller-disk"></a>

## Replace KRaft Controller Disk

When Kafka is configured to use KRaft, the controllers store the cluster metadata in the directory specified in `metadata.log.dir` -- or the first log directory, if `metadata.log.dir` is not configured. See the documentation for `metadata.log.dir` for details.

If the data in the cluster metadata directory is lost either because of hardware failure or the hardware needs to be replaced, care should be taken when provisioning the new controller node. The new controller node should not be formatted and started until the majority of the controllers have all of the committed data. To determine if the majority of the controllers have the committed data, run the kafka-metadata-quorum.sh tool to describe the replication status:

```bash
$ bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 describe --replication NodeId DirectoryId LogEndOffset Lag LastFetchTimestamp LastCaughtUpTimestamp Status 1 dDo1k_pRSD-VmReEpu383g 966 0 1732367153528 1732367153528 Leader 2 wQWaQMJYpcifUPMBGeRHqg 966 0 1732367153304 1732367153304 Observer... ... ... ... ... ...
```

Check and wait until the `Lag` is small for a majority of the controllers. If the leader’s end offset is not increasing, you can wait until the lag is 0 for a majority; otherwise, you can pick the latest leader end offset and wait until all replicas have reached it. Check and wait until the `LastFetchTimestamp` and `LastCaughtUpTimestamp` are close to each other for the majority of the controllers. At this point it is safer to format the controller’s metadata log directory. This can be done by running the kafka-storage.sh command.

```bash
$ bin/kafka-storage.sh format --cluster-id uuid --config config/server.properties
```

It is possible for the `bin/kafka-storage.sh format` command above to fail with a message like `Log directory ... is already formatted`. This can happen when combined mode is used and only the metadata log directory was lost but not the others. In that case and only in that case, can you run the `bin/kafka-storage.sh format` command with the `--ignore-formatted` option.

Start the KRaft controller after formatting the log directories.

```bash
$ bin/kafka-server-start.sh config/server.properties
```

<a id="operations-monitoring"></a>

<a id="operations-monitoring--monitoring"></a>

# Monitoring

Monitoring

Kafka uses Yammer Metrics for metrics reporting in the server. The Java clients use Kafka Metrics, a built-in metrics registry that minimizes transitive dependencies pulled into client applications. Both expose metrics via JMX and can be configured to report stats using pluggable stats reporters to hook up to your monitoring system.

All Kafka rate metrics have a corresponding cumulative count metric with suffix `-total`. For example, `records-consumed-rate` has a corresponding metric named `records-consumed-total`.

The easiest way to see the available metrics is to fire up jconsole and point it at a running kafka client or server; this will allow browsing all metrics with JMX.

<a id="operations-monitoring--security-considerations-for-remote-monitoring-using-jmx"></a>

<a id="operations-kraft"></a>

<a id="operations-kraft--kraft"></a>

# KRaft

KRaft

<a id="operations-kraft--configuration"></a>

## Configuration

<a id="operations-kraft--process-roles"></a>

### Process Roles

In KRaft mode each Kafka server can be configured as a controller, a broker, or both using the `process.roles` property. This property can have the following values:

- If `process.roles` is set to `broker`, the server acts as a broker.
- If `process.roles` is set to `controller`, the server acts as a controller.
- If `process.roles` is set to `broker,controller`, the server acts as both a broker and a controller.

Kafka servers that act as both brokers and controllers are referred to as “combined” servers. Combined servers are simpler to operate for small use cases like a development environment. The key disadvantage is that the controller will be less isolated from the rest of the system. For example, it is not possible to roll or scale the controllers separately from the brokers in combined mode. Combined mode is not recommended in critical deployment environments.

<a id="operations-kraft--controllers"></a>

### Controllers

In KRaft mode, specific Kafka servers are selected to be controllers. The servers selected to be controllers will participate in the metadata quorum. Each controller is either an active or a hot standby for the current active controller.

A Kafka admin will typically select 3 or 5 servers for this role, depending on factors like cost and the number of concurrent failures your system should withstand without availability impact. A majority of the controllers must be alive in order to maintain availability. With 3 controllers, the cluster can tolerate 1 controller failure; with 5 controllers, the cluster can tolerate 2 controller failures.

All of the servers in a Kafka cluster discover the active controller using the `controller.quorum.bootstrap.servers` property. All the controllers should be enumerated in this property. Each controller is identified with their `host` and `port` information. For example:

```properties
controller.quorum.bootstrap.servers=host1:port1,host2:port2,host3:port3
```

If a Kafka cluster has 3 controllers named controller1, controller2 and controller3, then controller1 may have the following configuration:

```properties
process.roles=controller
node.id=1
listeners=CONTROLLER://controller1.example.com:9093
controller.quorum.bootstrap.servers=controller1.example.com:9093,controller2.example.com:9093,controller3.example.com:9093
controller.listener.names=CONTROLLER
```

Every broker and controller must set the `controller.quorum.bootstrap.servers` property.

<a id="operations-kraft--upgrade"></a>

## Upgrade

Apache Kafka 4.1 added support for upgrading a cluster from a static controller configuration to a dynamic controller configuration. Dynamic controller configuration allows users to add controller to and remove controller from the cluster. See the Controller membership changes section for more details.

This feature upgrade is done by upgrading the KRaft feature version and updating the nodes’ configuration.

<a id="operations-kraft--describe-kraft-version"></a>

### Describe KRaft Version

Dynamic controller cluster was added in `kraft.version=1` or `release-version 4.1`. To determine which kraft feature version the cluster is using you can execute the following CLI command:

```bash
$ bin/kafka-features.sh --bootstrap-controller localhost:9093 describe... Feature: kraft.version SupportedMinVersion: 0 SupportedMaxVersion: 1 FinalizedVersionLevel: 0 Epoch: 7 Feature: metadata.version SupportedMinVersion: 3.3-IV3 SupportedMaxVersion: 4.0-IV3 FinalizedVersionLevel: 4.0-IV3 Epoch: 7
```

If the `FinalizedVersionLevel` for `Feature: kraft.version` is `0`, the version needs to be upgraded to at least `1` to support a dynamic controller cluster.

<a id="operations-kraft--upgrade-kraft-version"></a>

### Upgrade KRaft Version

The KRaft feature version can be upgraded to support dynamic controller clusters by using the `kafka-feature` CLI command. To upgrade all of the feature versions to the latest version:

```bash
$ bin/kafka-features.sh --bootstrap-server localhost:9092 upgrade --release-version 4.1
```

To upgrade just the KRaft feature version:

```bash
$ bin/kafka-features.sh --bootstrap-server localhost:9092 upgrade --feature kraft.version=1
```

<a id="operations-kraft--update-kraft-config"></a>

### Update KRaft Config

```properties
process.roles=...
node.id=...
controller.quorum.bootstrap.servers=controller1.example.com:9093,controller2.example.com:9093,controller3.example.com:9093
controller.listener.names=CONTROLLER
```

<a id="operations-kraft--provisioning-nodes"></a>

## Provisioning Nodes

The `bin/kafka-storage.sh random-uuid` command can be used to generate a cluster ID for your new cluster. This cluster ID must be used when formatting each server in the cluster with the `bin/kafka-storage.sh format` command.

This is different from how Kafka has operated in the past. Previously, Kafka would format blank storage directories automatically, and also generate a new cluster ID automatically. One reason for the change is that auto-formatting can sometimes obscure an error condition. This is particularly important for the metadata log maintained by the controller and broker servers. If a majority of the controllers were able to start with an empty log directory, a leader might be able to be elected with missing committed data.

<a id="operations-kraft--bootstrap-a-standalone-controller"></a>

### Bootstrap a Standalone Controller

The recommended method for creating a new KRaft controller cluster is to bootstrap it with one voter and dynamically add the rest of the controllers. Bootstrapping the first controller can be done with the following CLI command:

```bash
$ bin/kafka-storage.sh format --cluster-id <CLUSTER_ID> --standalone --config config/controller.properties
```

This command will 1) create a meta.properties file in metadata.log.dir with a randomly generated directory.id, 2) create a snapshot at 00000000000000000000-0000000000.checkpoint with the necessary control records (KRaftVersionRecord and VotersRecord) to make this Kafka node the only voter for the quorum.

<a id="operations-kraft--bootstrap-with-multiple-controllers"></a>

### Bootstrap with Multiple Controllers

The KRaft cluster metadata partition can also be bootstrapped with more than one voter. This can be done by using the –initial-controllers flag:

```bash
CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
CONTROLLER_0_UUID="$(bin/kafka-storage.sh random-uuid)"
CONTROLLER_1_UUID="$(bin/kafka-storage.sh random-uuid)"
CONTROLLER_2_UUID="$(bin/kafka-storage.sh random-uuid)"

# In each controller execute bin/kafka-storage.sh format --cluster-id ${CLUSTER_ID} \ --initial-controllers "0@controller-0:1234:${CONTROLLER_0_UUID},1@controller-1:1234:${CONTROLLER_1_UUID},2@controller-2:1234:${CONTROLLER_2_UUID}" \ --config config/controller.properties
```

This command is similar to the standalone version but the snapshot at 00000000000000000000-0000000000.checkpoint will instead contain a VotersRecord that includes information for all of the controllers specified in –initial-controllers. It is important that the value of this flag is the same in all of the controllers with the same cluster id. In the replica description 0@controller-0:1234:3Db5QLSqSZieL3rJBUUegA, 0 is the replica id, 3Db5QLSqSZieL3rJBUUegA is the replica directory id, controller-0 is the replica’s host and 1234 is the replica’s port.

<a id="operations-kraft--formatting-brokers-and-new-controllers"></a>

### Formatting Brokers and New Controllers

When provisioning new broker and controller nodes that we want to add to an existing Kafka cluster, use the `kafka-storage.sh format` command with the –no-initial-controllers flag.

```bash
$ bin/kafka-storage.sh format --cluster-id <CLUSTER_ID> --config config/server.properties --no-initial-controllers
```

<a id="operations-kraft--controller-membership-changes"></a>

## Controller membership changes

<a id="operations-kraft--static-versus-dynamic-kraft-quorums"></a>

### Static versus Dynamic KRaft Quorums

There are two ways to run KRaft: using KIP-853 dynamic controller quorums, or the old way using static controller quorums.

When using a dynamic quorum, `controller.quorum.voters` must not be set and `controller.quorum.bootstrap.servers` is set instead. This configuration key need not contain all the controllers, but it should contain as many as possible so that all the servers can locate the quorum. In other words, its function is much like the `bootstrap.servers` configuration used by Kafka clients.

When using a static quorum, the configuration file for each broker and controller must specify the IDs, hostnames, and ports of all controllers in `controller.quorum.voters`.

If you are not sure whether you are using static or dynamic quorums, you can determine this by running something like the following:

```bash
$ bin/kafka-features.sh --bootstrap-controller localhost:9093 describe
```

If the `kraft.version` field is level 0 or absent, you are using a static quorum. If it is 1 or above, you are using a dynamic quorum. For example, here is an example of a static quorum:

```text
Feature: kraft.version  SupportedMinVersion: 0  SupportedMaxVersion: 1  FinalizedVersionLevel: 0 Epoch: 5
Feature: metadata.version       SupportedMinVersion: 3.3-IV3    SupportedMaxVersion: 3.9-IV0 FinalizedVersionLevel: 3.9-IV0  Epoch: 5
```

Here is another example of a static quorum:

```text
Feature: metadata.version       SupportedMinVersion: 3.3-IV3    SupportedMaxVersion: 3.8-IV0 FinalizedVersionLevel: 3.8-IV0  Epoch: 5
```

Here is an example of a dynamic quorum:

```text
Feature: kraft.version  SupportedMinVersion: 0  SupportedMaxVersion: 1  FinalizedVersionLevel: 1 Epoch: 5
Feature: metadata.version       SupportedMinVersion: 3.3-IV3    SupportedMaxVersion: 3.9-IV0 FinalizedVersionLevel: 3.9-IV0  Epoch: 5
```

The static versus dynamic nature of the quorum is determined at the time of formatting. Specifically, the quorum will be formatted as dynamic if `controller.quorum.voters` is **not** present, and one of –standalone, –initial-controllers, or –no-initial-controllers is set. If you have followed the instructions earlier in this document, you will get a dynamic quorum.

Note: To migrate from static voter set to dynamic voter set, please refer to the Upgrade section.

<a id="operations-kraft--add-new-controller"></a>

### Add New Controller

If a dynamic controller cluster already exists, it can be expanded by first provisioning a new controller using the kafka-storage.sh tool and starting the controller. After starting the controller, the replication to the new controller can be monitored using the `bin/kafka-metadata-quorum.sh describe --replication` command. Once the new controller has caught up to the active controller, it can be added to the cluster using the `bin/kafka-metadata-quorum.sh add-controller` command. When using broker endpoints use the –bootstrap-server flag:

```bash
$ bin/kafka-metadata-quorum.sh --command-config config/controller.properties --bootstrap-server localhost:9092 add-controller
```

When using controller endpoints use the –bootstrap-controller flag:

```bash
$ bin/kafka-metadata-quorum.sh --command-config config/controller.properties --bootstrap-controller localhost:9093 add-controller
```

Note that if there are any configs needed to be passed to the Admin Client, like the authentication configuration, please also include in the “controller.properties”.

<a id="operations-kraft--remove-controller"></a>

### Remove Controller

If the dynamic controller cluster already exists, it can be shrunk using the `bin/kafka-metadata-quorum.sh remove-controller` command. Use the remove-controller command before shutting down the controller to have it removed from the quorum first. When using broker endpoints use the –bootstrap-server flag:

```bash
$ bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 remove-controller --controller-id <id> --controller-directory-id <directory-id>
```

When using controller endpoints use the –bootstrap-controller flag:

```bash
$ bin/kafka-metadata-quorum.sh --bootstrap-controller localhost:9093 remove-controller --controller-id <id> --controller-directory-id <directory-id>
```

<a id="operations-kraft--debugging"></a>

## Debugging

<a id="operations-kraft--metadata-quorum-tool"></a>

### Metadata Quorum Tool

The kafka-metadata-quorum.sh tool can be used to describe the runtime state of the cluster metadata partition. For example, the following command displays a summary of the metadata quorum:

```bash
$ bin/kafka-metadata-quorum.sh --bootstrap-server localhost:9092 describe --status ClusterId: fMCL8kv1SWm87L_Md-I2hg LeaderId: 3002 LeaderEpoch: 2 HighWatermark: 10 MaxFollowerLag: 0 MaxFollowerLagTimeMs: -1 CurrentVoters: [{"id": 3000, "directoryId": "ILZ5MPTeRWakmJu99uBJCA", "endpoints": ["CONTROLLER://localhost:9093"]},{"id": 3001, "directoryId": "b-DwmhtOheTqZzPoh52kfA", "endpoints": ["CONTROLLER://localhost:9094"]},{"id": 3002, "directoryId": "g42deArWBTRM5A1yuVpMCg", "endpoints": ["CONTROLLER://localhost:9095"]}] CurrentObservers: [{"id": 0, "directoryId": "3Db5QLSqSZieL3rJBUUegA"},{"id": 1, "directoryId": "UegA3Db5QLSqSZieL3rJBU"},{"id": 2, "directoryId": "L3rJBUUegA3Db5QLSqSZie"}]
```

<a id="operations-kraft--dump-log-tool"></a>

### Dump Log Tool

The kafka-dump-log.sh tool can be used to debug the log segments and snapshots for the cluster metadata directory. The tool will scan the provided files and decode the metadata records. For example, this command decodes and prints the records in the first log segment:

```bash
$ bin/kafka-dump-log.sh --cluster-metadata-decoder --files metadata_log_dir/__cluster_metadata-0/00000000000000000000.log
```

This command decodes and prints the records in a cluster metadata snapshot:

```bash
$ bin/kafka-dump-log.sh --cluster-metadata-decoder --files metadata_log_dir/__cluster_metadata-0/00000000000000000100-0000000001.checkpoint
```

<a id="operations-kraft--metadata-shell"></a>

### Metadata Shell

The kafka-metadata-shell.sh tool can be used to interactively inspect the state of the cluster metadata partition:

```bash
$ bin/kafka-metadata-shell.sh --snapshot metadata_log_dir/__cluster_metadata-0/00000000000000007228-0000000001.checkpoint >> ls /brokers local metadataQuorum topicIds topics >> ls /topics foo >> cat /topics/foo/0/data {"partitionId" : 0,"topicId" : "5zoAlv-xEh9xRANKXt1Lbg","replicas" : [ 1 ],"isr" : [ 1 ],"removingReplicas" : null,"addingReplicas" : null,"leader" : 1,"leaderEpoch" : 0,"partitionEpoch" : 0} >> exit
```

Note: `00000000000000000000-0000000000.checkpoint` does not contain cluster metadata. Use a valid snapshot file when examining metadata with the `kafka-metadata-shell.sh` tool.

<a id="operations-kraft--deploying-considerations"></a>

## Deploying Considerations

- Kafka server’s `process.roles` should be set to either `broker` or `controller` but not both. Combined mode can be used in development environments, but it should be avoided in critical deployment environments.
- For redundancy, a Kafka cluster should use 3 or more controllers, depending on factors like cost and the number of concurrent failures your system should withstand without availability impact. For the KRaft controller cluster to withstand `N` concurrent failures the controller cluster must include `2N + 1` controllers.
- The Kafka controllers store all the metadata for the cluster in memory and on disk. We believe that for a typical Kafka cluster 5GB of main memory and 5GB of disk space on the metadata log director is sufficient.

<a id="operations-kraft--zookeeper-to-kraft-migration"></a>

## ZooKeeper to KRaft Migration

In order to migrate from ZooKeeper to KRaft you need to use a bridge release. The last bridge release is Kafka 3.9. See the [ZooKeeper to KRaft Migration steps](https://kafka.apache.org/39/operations/kraft/#zookeeper-to-kraft-migration) in the 3.9 documentation.

---

<a id="operations-tiered-storage"></a>

<a id="operations-tiered-storage--tiered-storage"></a>

# Tiered Storage

Tiered Storage

<a id="operations-tiered-storage--tiered-storage-overview"></a>

## Tiered Storage Overview

Kafka data is mostly consumed in a streaming fashion using tail reads. Tail reads leverage OS’s page cache to serve the data instead of disk reads. Older data is typically read from the disk for backfill or failure recovery purposes and is infrequent.

In the tiered storage approach, Kafka cluster is configured with two tiers of storage - local and remote. The local tier is the same as the current Kafka that uses the local disks on the Kafka brokers to store the log segments. The new remote tier uses external storage systems, such as HDFS or S3, to store the completed log segments. Please check [KIP-405](https://cwiki.apache.org/confluence/x/KJDQBQ) for more information.

<a id="operations-tiered-storage--configuration"></a>

## Configuration

<a id="operations-tiered-storage--broker-configurations"></a>

### Broker Configurations

By default, the Kafka server will not enable the tiered storage feature. `remote.log.storage.system.enable` is the property to control whether to enable tiered storage functionality in a broker or not. Setting it to “true” enables this feature.

`RemoteStorageManager` is an interface to provide the lifecycle of remote log segments and indexes. Kafka server doesn’t provide out-of-the-box implementation of RemoteStorageManager. Users must configure `remote.log.storage.manager.class.name` and `remote.log.storage.manager.class.path` to specify the implementation of RemoteStorageManager.

`RemoteLogMetadataManager` is an interface to provide the lifecycle of metadata about remote log segments with strongly consistent semantics. By default, Kafka provides an implementation with storage as an internal topic. This implementation can be changed by configuring `remote.log.metadata.manager.class.name` and `remote.log.metadata.manager.class.path`. When adopting the default kafka internal topic based implementation, `remote.log.metadata.manager.listener.name` is a mandatory property to specify which listener the clients created by the default RemoteLogMetadataManager implementation.

<a id="operations-tiered-storage--topic-configurations"></a>

### Topic Configurations

After correctly configuring broker side configurations for tiered storage feature, there are still configurations in topic level needed to be set. `remote.storage.enable` is the switch to determine if a topic wants to use tiered storage or not. By default it is set to false. After enabling `remote.storage.enable` property, the next thing to consider is the log retention. When tiered storage is enabled for a topic, there are 2 additional log retention configurations to set:

- `local.retention.ms`
- `retention.ms`
- `local.retention.bytes`
- `retention.bytes`

The configuration prefixed with `local` are to specify the time/size the “local” log file can accept before moving to remote storage, and then get deleted. If unset, The value in `retention.ms` and `retention.bytes` will be used.

<a id="operations-tiered-storage--quick-start-example"></a>

## Quick Start Example

Apache Kafka doesn’t provide an out-of-the-box RemoteStorageManager implementation. To have a preview of the tiered storage feature, the [LocalTieredStorage](https://github.com/apache/kafka/blob/trunk/storage/src/test/java/org/apache/kafka/server/log/remote/storage/LocalTieredStorage.java) implemented for integration test can be used, which will create a temporary directory in local storage to simulate the remote storage.

To adopt the `LocalTieredStorage`, the test library needs to be built locally:

```bash
# please checkout to the specific version tag you're using before building it
# ex: `git checkout 4.3.1`
$ ./gradlew clean :storage:testJar
```

After build successfully, there should be a `kafka-storage-x.x.x-test.jar` file under `storage/build/libs`. Next, setting configurations in the broker side to enable tiered storage feature.

```properties
# Sample KRaft broker server.properties listening on PLAINTEXT://:9092
remote.log.storage.system.enable=true

# Setting the listener for the clients in RemoteLogMetadataManager to talk to the brokers.
remote.log.metadata.manager.listener.name=PLAINTEXT

# Please provide the implementation info for remoteStorageManager.
# This is the mandatory configuration for tiered storage.
# Here, we use the `LocalTieredStorage` built above.
remote.log.storage.manager.class.name=org.apache.kafka.server.log.remote.storage.LocalTieredStorage
remote.log.storage.manager.class.path=/PATH/TO/kafka-storage-4.3.1-test.jar

# These 2 prefix are default values, but customizable
remote.log.storage.manager.impl.prefix=rsm.config.
remote.log.metadata.manager.impl.prefix=rlmm.config.

# Configure the directory used for `LocalTieredStorage`
# Note, please make sure the brokers need to have access to this directory
rsm.config.dir=/tmp/kafka-remote-storage

# For single broker cluster, set this to 1. Default is 3 for clusters with 3 or more brokers.
rlmm.config.remote.log.metadata.topic.replication.factor=1

# The minimum number of replicas that must acknowledge a write to remote log metadata topic.
# Default value is 2. For single broker cluster (replication factor = 1), set this to 1.
rlmm.config.remote.log.metadata.topic.min.isr=1

# Try to speed up the log retention check interval for testing
log.retention.check.interval.ms=1000
```

Following quick start guide to start up the kafka environment. Then, create a topic with tiered storage enabled with configs:

```bash
# remote.storage.enable=true -> enables tiered storage on the topic
# local.retention.ms=1000 -> The number of milliseconds to keep the local log segment before it gets deleted.
# Note that a local log segment is eligible for deletion only after it gets uploaded to remote.
# retention.ms=3600000 -> when segments exceed this time, the segments in remote storage will be deleted
# segment.bytes=1048576 -> for test only, to speed up the log segment rolling interval
# file.delete.delay.ms=10000 -> for test only, to speed up the local-log segment file delete delay

$ bin/kafka-topics.sh --create --topic tieredTopic --bootstrap-server localhost:9092 \ --config remote.storage.enable=true --config local.retention.ms=1000 --config retention.ms=3600000 \ --config segment.bytes=1048576 --config file.delete.delay.ms=1000
```

Try to send messages to the `tieredTopic` topic to roll the log segment:

```bash
$ bin/kafka-producer-perf-test.sh --bootstrap-server localhost:9092 --topic tieredTopic --num-records 1200 --record-size 1024 --throughput -1
```

Then, after the active segment is rolled, the old segment should be moved to the remote storage and get deleted. This can be verified by checking the remote log directory configured above. For example:

```bash
$ ls /tmp/kafka-remote-storage/kafka-tiered-storage/tieredTopic-0-jF8s79t9SrG_PNqlwv7bAA 00000000000000000000-knnxbs3FSRyKdPcSAOQC-w.index 00000000000000000000-knnxbs3FSRyKdPcSAOQC-w.snapshot 00000000000000000000-knnxbs3FSRyKdPcSAOQC-w.leader_epoch_checkpoint 00000000000000000000-knnxbs3FSRyKdPcSAOQC-w.timeindex 00000000000000000000-knnxbs3FSRyKdPcSAOQC-w.log
```

Lastly, we can try to consume some data from the beginning and print offset number, to make sure it will successfully fetch offset 0 from the remote storage.

```bash
$ bin/kafka-console-consumer.sh --topic tieredTopic --from-beginning --max-messages 1 --bootstrap-server localhost:9092 --formatter-property print.offset=true
```

In KRaft mode, you can disable tiered storage at the topic level, to make the remote logs as read-only logs, or completely delete all remote logs.

If you want to let the remote logs become read-only and no more local logs copied to the remote storage, you can set `remote.storage.enable=true,remote.log.copy.disable=true` to the topic.

Note: You also need to set `local.retention.ms` and `local.retention.bytes` to the same value as `retention.ms` and `retention.bytes`, or set to “-2”. This is because after disabling remote log copy, the local retention policies will not be applied anymore, and that might confuse users and cause unexpected disk full.

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 \ --alter --entity-type topics --entity-name tieredTopic \ --add-config 'remote.storage.enable=true,remote.log.copy.disable=true,local.retention.ms=-2,local.retention.bytes=-2'
```

If you want to completely disable tiered storage at the topic level with all remote logs deleted, you can set `remote.storage.enable=false,remote.log.delete.on.disable=true` to the topic.

```bash
$ bin/kafka-configs.sh --bootstrap-server localhost:9092 \ --alter --entity-type topics --entity-name tieredTopic \ --add-config 'remote.storage.enable=false,remote.log.delete.on.disable=true'
```

You can also re-enable tiered storage feature at the topic level. Please note, if you want to disable tiered storage at the cluster level, you should delete the tiered storage enabled topics explicitly. Attempting to disable tiered storage at the cluster level without deleting the topics using tiered storage will result in an exception during startup.

```bash
$ bin/kafka-topics.sh --delete --topic tieredTopic --bootstrap-server localhost:9092
```

After topics are deleted, you’re safe to set `remote.log.storage.system.enable=false` in the broker configuration.

<a id="operations-tiered-storage--limitations"></a>

## Limitations

While the Tiered Storage works for most use cases, it is still important to be aware of the following limitations:

- No support for compacted topics
- Disabling tiered storage on all topics where it is enabled is required before disabling tiered storage at the broker level
- Admin actions related to tiered storage feature are only supported on clients from version 3.0 onwards
- No support for log segments missing producer snapshot file. It can happen when topic is created before v2.8.0.

For more information, please check [Kafka Tiered Storage GA Release Notes](https://cwiki.apache.org/confluence/x/9xDOEg).

---

<a id="operations-consumer-rebalance-protocol"></a>

<a id="operations-consumer-rebalance-protocol--consumer-rebalance-protocol"></a>

# Consumer Rebalance Protocol

Consumer Rebalance Protocol

<a id="operations-consumer-rebalance-protocol--overview"></a>

## Overview

Starting from Apache Kafka 4.0, the Next Generation of the Consumer Rebalance Protocol ([KIP-848](https://cwiki.apache.org/confluence/x/HhD1D)) is Generally Available (GA), ready for production workloads.
It improves the scalability of consumer groups while simplifying consumers. It also decreases rebalance times, thanks to its fully incremental design, which no longer relies on a global synchronization barrier.

There are now two types of consumer groups, named depending upon whether the consumers are using the new “consumer” group protocol or the earlier “classic” group protocol.

<a id="operations-consumer-rebalance-protocol--server"></a>

## Server

The new consumer protocol is automatically enabled on the server since Apache Kafka 4.0. Enabling and disabling the protocol on the server side is controlled by the `group.version` feature flag.

The consumer heartbeat interval and the session timeout are controlled by the server now with the following configs:

- `group.consumer.heartbeat.interval.ms`
- `group.consumer.session.timeout.ms`

The assignment strategy is also controlled by the server. The `group.consumer.assignors` configuration can be used to specify the list of available assignors for `Consumer` groups.

- `uniform` and `range` assignors are provided by default
- `uniform` is the default one (first assignor in the list of `group.consumer.assignors`) unless the Consumer selects a different one (via the client config `group.remote.assignor`)
- it is possible to implement custom assignment strategies on the server side, by implementing the `ConsumerGroupPartitionAssignor` interface and specifying the full class name in the `group.consumer.assignors` configuration.

<a id="operations-consumer-rebalance-protocol--migrating-from-client-side-assignors"></a>

### Migrating from Client-side Assignors

The following table shows the mapping from client-side assignors to the new server-side assignors:

| Client-side Assignor | Server-side Assignor |
| --- | --- |
| RangeAssignor | range |
| CooperativeStickyAssignor | uniform |
| StickyAssignor | uniform |
| RoundRobinAssignor | uniform |

<a id="operations-consumer-rebalance-protocol--consumer"></a>

## Consumer

Since Apache Kafka 4.0, the Consumer fully supports the new Consumer rebalance protocol. However, the protocol is not enabled by default. The `group.protocol` configuration must be set to `consumer` to enable it. When enabled, the new consumer protocol is used alongside an improved threading model.

The `subscribe(SubscriptionPattern)` and `subscribe(SubscriptionPattern, ConsumerRebalanceListener)` methods have been added to subscribe to a regular expression with the new Consumer rebalance protocol. With these methods, the regular expression uses the RE2J format and is now evaluated on the server side.

New metrics have been added to the Consumer when using the new rebalance protocol, mainly providing visibility over the improved threading model. See [New Consumer Metrics](https://cwiki.apache.org/confluence/x/lQ_TEg).

When the new rebalance protocol is enabled, the following configurations and APIs are no longer usable:

- `heartbeat.interval.ms`
- `session.timeout.ms`
- `partition.assignment.strategy`
- `enforceRebalance(String)` and `enforceRebalance()`

<a id="operations-consumer-rebalance-protocol--upgrade-downgrade"></a>

## Upgrade & Downgrade

<a id="operations-consumer-rebalance-protocol--offline"></a>

### Offline

Consumer groups are automatically converted from `Classic` to `Consumer` and vice versa when they are empty. Hence, it is possible to change the protocol used by the group by shutting down all the consumers and bringing them back up with the `group.protocol=consumer` configuration. The downside is that it requires taking the consumer group down.

<a id="operations-consumer-rebalance-protocol--online"></a>

### Online

Consumer groups can be upgraded without downtime by rolling out the consumer with the `group.protocol=consumer` configuration. When the first consumer using the new Consumer rebalance protocol joins the group, the group is converted from `Classic` to `Consumer`, and the Classic rebalance protocol is interoperated to work with the new Consumer rebalance protocol. This is only possible when the classic group uses an assignor that does not embed custom metadata.

Consumer groups can be downgraded using the opposite process. In this case, the group is converted from `Consumer` to `Classic` when the last consumer using the new Consumer rebalance protocol leaves the group.

<a id="operations-consumer-rebalance-protocol--evolution-timeline"></a>

## Evolution Timeline

The evolution timeline of the Consumer rebalance protocol is described in [KIP-1274](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1274%3A+Deprecate+and+remove+support+for+Classic+rebalance+protocol+in+KafkaConsumer), and expected to be as follows:

- **Apache Kafka 3.7**: Early Access
- **Apache Kafka 4.0**: GA (production-ready).
- **Apache Kafka 5.0**: `KafkaConsumer` defaults to `Consumer` protocol, while still supporting `Classic`
- **Apache Kafka 6.0**: `KafkaConsumer` only supports `Consumer` as rebalance protocol, while the broker still supports `Classic` for backward compatibility.

<a id="operations-consumer-rebalance-protocol--limitations"></a>

## Limitations

- Client-side assignors are not supported and not in scope at the moment. Use [KAFKA-18327](https://issues.apache.org/jira/browse/KAFKA-18327) to provide feedback if you have custom assignment strategies that may not be covered.
- Rack-aware assignment strategies are not fully supported yet (work is in progress, see [KAFKA-19387](https://issues.apache.org/jira/browse/KAFKA-19387)).

---

<a id="operations-transaction-protocol"></a>

<a id="operations-transaction-protocol--transaction-protocol"></a>

# Transaction Protocol

Transaction Protocol

<a id="operations-transaction-protocol--overview"></a>

## Overview

Starting from Apache Kafka 4.0, Transactions Server Side Defense ([KIP-890](https://cwiki.apache.org/confluence/x/B40ODg)) brings a strengthened transactional protocol. When enabled and using 4.0 producer clients, the producer epoch is bumped on every transaction to ensure every transaction includes the intended messages and duplicates are not written as part of the next transaction.

The protocol is automatically enabled on the server since Apache Kafka 4.0. Enabling and disabling the protocol is controlled by the `transaction.version` feature flag. This flag can be set using the storage tool on new cluster creation, or dynamically to an existing cluster via the features tool. Producer clients starting 4.0 and above will use the new transactional protocol as long as it is enabled on the server.

<a id="operations-transaction-protocol--upgrade-downgrade"></a>

## Upgrade & Downgrade

To enable the new protocol on the server, set `transaction.version=2`. The producer clients do not need to be restarted, and will dynamically upgrade the next time they connect or re-connect to a broker. (Alternatively, the client can be restarted to force this connection). A producer will not upgrade mid-transaction, but on the start of the next transaction after it becomes aware of the server-side upgrade.

Downgrades are safe to perform and work similarly. The older protocol will be used by the clients on the first transaction after the producer becomes aware of the downgraded protocol.

<a id="operations-transaction-protocol--performance"></a>

## Performance

The new transactional protocol improves performance over verification by only sending a single call to add partitions on the server side, rather than one from the client to add and one from the server to verify.

One consequence of this change is that we can no longer use the hardcoded retry backoff introduced by [KAFKA-5477](https://issues.apache.org/jira/browse/KAFKA-5477). Due to the asynchronous nature of the `endTransaction` api, the client can start adding partitions to the next transaction before the markers are written. When this happens, the server will return `CONCURRENT_TRANSACTIONS` until the previous transaction completes. Rather than the default client backoff for these retries, there was a shorter retry backoff of 20ms.

Now with the server-side request, the server will attempt to retry adding the partition a few times when it sees the `CONCURRENT_TRANSACTIONS` error before it returns the error to the client. This can result in higher produce latencies reported on these requests. The transaction end to end latency (measured from the time the client begins the transaction to the time to commit) does not increase overall with this change. The time just shifts from client-side backoff to being calculated as part of the produce latency.

The server-side backoff and total retry time can be configured with the following new configs:

- `add.partitions.to.txn.retry.backoff.ms`
- `add.partitions.to.txn.retry.backoff.max.ms`

---

<a id="operations-eligible-leader-replicas"></a>

<a id="operations-eligible-leader-replicas--eligible-leader-replicas"></a>

# Eligible Leader Replicas

Eligible Leader Replicas

<a id="operations-eligible-leader-replicas--overview"></a>

## Overview

Starting from Apache Kafka 4.0, Eligible Leader Replicas ([KIP-966 Part 1](https://cwiki.apache.org/confluence/x/mpOzDw)) is available for the users to an improvement to Kafka replication (ELR is enabled by default on new clusters starting 4.1). As the “strict min ISR” rule has been generally applied, which means the high watermark for the data partition can’t advance if the size of the ISR is smaller than the min ISR(`min.insync.replicas`), it makes some replicas that are not in the ISR safe to become the leader. The KRaft controller stores such replicas in the PartitionRecord field called `Eligible Leader Replicas`. During the leader election, the controller will select the leaders with the following order:

- If ISR is not empty, select one of them.
- If ELR is not empty, select one that is not fenced.
- Select the last known leader if it is unfenced. This is a similar behavior prior to the 4.0 when all the replicas are offline.

<a id="operations-eligible-leader-replicas--upgrade-downgrade"></a>

## Upgrade & Downgrade

The ELR is not enabled by default for 4.0. To enable the new protocol on the server, set `eligible.leader.replicas.version=1`. After that the upgrade, the KRaft controller will start tracking the ELR.

Downgrades are safe to perform by setting `eligible.leader.replicas.version=0`.

<a id="operations-eligible-leader-replicas--tool"></a>

## Tool

The ELR fields can be checked through the API DescribeTopicPartitions. The admin client can fetch the ELR info by describing the topics.

Note that when the ELR feature is enabled:

- The cluster-level `min.insync.replicas` config will be added if there is not any. The value is the same as the static config in the active controller.
- The removal of `min.insync.replicas` config at the cluster-level is not allowed.
- If the cluster-level `min.insync.replicas` is updated, even if the value is unchanged, all the ELR state will be cleaned.
- The previously set `min.insync.replicas` value at the broker-level config will be removed. Please set at the cluster-level if necessary.
- The alteration of `min.insync.replicas` config at the broker-level is not allowed.
- If `min.insync.replicas` is updated for a topic, the ELR state will be cleaned.

---

<a id="security"></a>

<a id="security--security"></a>

# Security

---

<a id="security--security-overview"></a>

##### [Security Overview](#security-security-overview)

Security Overview

<a id="security--listener-configuration"></a>

##### [Listener Configuration](#security-listener-configuration)

Listener Configuration

<a id="security--encryption-and-authentication-using-ssl"></a>

##### [Encryption and Authentication using SSL](#security-encryption-and-authentication-using-ssl)

Encryption and Authentication using SSL

<a id="security--authentication-using-sasl"></a>

##### [Authentication using SASL](#security-authentication-using-sasl)

Authentication using SASL

<a id="security--authorization-and-acls"></a>

##### [Authorization and ACLs](#security-authorization-and-acls)

Authorization and ACLs

<a id="security--incorporating-security-features-in-a-running-cluster"></a>

##### [Incorporating Security Features in a Running Cluster](#security-incorporating-security-features-in-a-running-cluster)

Incorporating Security Features in a Running Cluster

---

<a id="security-security-overview"></a>

<a id="security-security-overview--security-overview"></a>

# Security Overview

Security Overview

The following security measures are currently supported:

1. Authentication of connections to brokers from clients (producers and consumers), other brokers and tools, using either SSL or SASL. Kafka supports the following SASL mechanisms:

   - SASL/GSSAPI (Kerberos) - starting at version 0.9.0.0
   - SASL/PLAIN - starting at version 0.10.0.0
   - SASL/SCRAM-SHA-256 and SASL/SCRAM-SHA-512 - starting at version 0.10.2.0
   - SASL/OAUTHBEARER - starting at version 2.0
2. Encryption of data transferred between brokers and clients, between brokers, or between brokers and tools using SSL (Note that there is a performance degradation when SSL is enabled, the magnitude of which depends on the CPU type and the JVM implementation.)
3. Authorization of read / write operations by clients
4. Authorization is pluggable and integration with external authorization services is supported

It’s worth noting that security is optional - non-secured clusters are supported, as well as a mix of authenticated, unauthenticated, encrypted and non-encrypted clients. The guides below explain how to configure and use the security features in both clients and brokers.

---

<a id="security-listener-configuration"></a>

<a id="security-listener-configuration--listener-configuration"></a>

# Listener Configuration

Listener Configuration

In order to secure a Kafka cluster, it is necessary to secure the channels that are used to communicate with the servers. Each server must define the set of listeners that are used to receive requests from clients as well as other servers. Each listener may be configured to authenticate clients using various mechanisms and to ensure traffic between the server and the client is encrypted. This section provides a primer for the configuration of listeners.

Kafka servers support listening for connections on multiple ports. This is configured through the `listeners` property in the server configuration, which accepts a comma-separated list of the listeners to enable. At least one listener must be defined on each server. The format of each listener defined in `listeners` is given below:

```
{LISTENER_NAME}://{hostname}:{port}
```

The `LISTENER_NAME` is usually a descriptive name which defines the purpose of the listener. For example, many configurations use a separate listener for client traffic, so they might refer to the corresponding listener as `CLIENT` in the configuration:

```
listeners=CLIENT://localhost:9092
```

The security protocol of each listener is defined in a separate configuration: `listener.security.protocol.map`. The value is a comma-separated list of each listener mapped to its security protocol. For example, the follow value configuration specifies that the `CLIENT` listener will use SSL while the `BROKER` listener will use plaintext.

```
listener.security.protocol.map=CLIENT:SSL,BROKER:PLAINTEXT
```

Possible options (case-insensitive) for the security protocol are given below:

1. PLAINTEXT
2. SSL
3. SASL\_PLAINTEXT
4. SASL\_SSL

The plaintext protocol provides no security and does not require any additional configuration. In the following sections, this document covers how to configure the remaining protocols.

If each required listener uses a separate security protocol, it is also possible to use the security protocol name as the listener name in `listeners`. Using the example above, we could skip the definition of the `CLIENT` and `BROKER` listeners using the following definition:

```
listeners=SSL://localhost:9092,PLAINTEXT://localhost:9093
```

However, we recommend users to provide explicit names for the listeners since it makes the intended usage of each listener clearer.

Among the listeners in this list, it is possible to declare the listener to be used for inter-broker communication by setting the `inter.broker.listener.name` configuration to the name of the listener. The primary purpose of the inter-broker listener is partition replication. If not defined, then the inter-broker listener is determined by the security protocol defined by `security.inter.broker.protocol`, which defaults to `PLAINTEXT`.

In a KRaft cluster, a broker is any server which has the `broker` role enabled in `process.roles` and a controller is any server which has the `controller` role enabled. Listener configuration depends on the role. The listener defined by `inter.broker.listener.name` is used exclusively for requests between brokers. Controllers, on the other hand, must use separate listener which is defined by the `controller.listener.names` configuration. This cannot be set to the same value as the inter-broker listener.

Controllers receive requests both from other controllers and from brokers. For this reason, even if a server does not have the `controller` role enabled (i.e. it is just a broker), it must still define the controller listener along with any security properties that are needed to configure it. For example, we might use the following configuration on a standalone broker:

```
process.roles=broker
listeners=BROKER://localhost:9092
inter.broker.listener.name=BROKER
controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER
listener.security.protocol.map=BROKER:SASL_SSL,CONTROLLER:SASL_SSL
```

The controller listener is still configured in this example to use the `SASL_SSL` security protocol, but it is not included in `listeners` since the broker does not expose the controller listener itself. The port that will be used in this case comes from the `controller.quorum.voters` configuration, which defines the complete list of controllers.

For KRaft servers which have both the broker and controller role enabled, the configuration is similar. The only difference is that the controller listener must be included in `listeners`:

```
process.roles=broker,controller
listeners=BROKER://localhost:9092,CONTROLLER://localhost:9093
inter.broker.listener.name=BROKER
controller.quorum.bootstrap.servers=localhost:9093
controller.listener.names=CONTROLLER
listener.security.protocol.map=BROKER:SASL_SSL,CONTROLLER:SASL_SSL
```

It is a requirement that the host and port defined in `controller.quorum.bootstrap.servers` is routed to the exposed controller listeners. For example, here the `CONTROLLER` listener is bound to localhost:9093. The connection string defined by `controller.quorum.bootstrap.servers` must then also use localhost:9093, as it does here.

The controller will accept requests on all listeners defined by `controller.listener.names`. Typically there would be just one controller listener, but it is possible to have more. For example, this provides a way to change the active listener from one port or security protocol to another through a roll of the cluster (one roll to expose the new listener, and one roll to remove the old listener). When multiple controller listeners are defined, the first one in the list will be used for outbound requests.

It is conventional in Kafka to use a separate listener for clients. This allows the inter-cluster listeners to be isolated at the network level. In the case of the controller listener in KRaft, the listener should be isolated since clients do not work with it anyway. Clients are expected to connect to any other listener configured on a broker. Any requests that are bound for the controller will be forwarded as described below

In the following section, this document covers how to enable SSL on a listener for encryption as well as authentication. The subsequent section will then cover additional authentication mechanisms using SASL.

---

<a id="security-encryption-and-authentication-using-ssl"></a>

<a id="security-encryption-and-authentication-using-ssl--encryption-and-authentication-using-ssl"></a>

# Encryption and Authentication using SSL

Encryption and Authentication using SSL

Apache Kafka allows clients to use SSL for encryption of traffic as well as authentication. By default, SSL is disabled but can be turned on if needed. The following paragraphs explain in detail how to set up your own PKI infrastructure, use it to create certificates and configure Kafka to use these.

<a id="security-encryption-and-authentication-using-ssl--generate-ssl-key-and-certificate-for-each-kafka-broker"></a>

### Generate SSL key and certificate for each Kafka broker

```
     $ keytool -keystore {keystorefile} -alias localhost -validity {validity} -genkey -keyalg RSA -storetype pkcs12
```

You need to specify two parameters in the above command:

1. keystorefile: the keystore file that stores the keys (and later the certificate) for this broker. The keystore file contains the private and public keys of this broker, therefore it needs to be kept safe. Ideally this step is run on the Kafka broker that the key will be used on, as this key should never be transmitted/leave the server that it is intended for.
2. validity: the valid time of the key in days. Please note that this differs from the validity period for the certificate, which will be determined in Signing the certificate. You can use the same key to request multiple certificates: if your key has a validity of 10 years, but your CA will only sign certificates that are valid for one year, you can use the same key with 10 certificates over time.

To obtain a certificate that can be used with the private key that was just created a certificate signing request needs to be created. This signing request, when signed by a trusted CA results in the actual certificate which can then be installed in the keystore and used for authentication purposes. To generate certificate signing requests run the following command for all server keystores created so far.

```
$ keytool -keystore server.keystore.jks -alias localhost -validity {validity} -genkey -keyalg RSA -destkeystoretype pkcs12 -ext SAN=DNS:{FQDN},IP:{IPADDRESS1}
```

This command assumes that you want to add hostname information to the certificate, if this is not the case, you can omit the extension parameter `-ext SAN=DNS:{FQDN},IP:{IPADDRESS1}`. Please see below for more information on this.

<a id="security-encryption-and-authentication-using-ssl--host-name-verification"></a>

### Host Name Verification

Host name verification, when enabled, is the process of checking attributes from the certificate that is presented by the server you are connecting to against the actual hostname or ip address of that server to ensure that you are indeed connecting to the correct server.
The main reason for this check is to prevent man-in-the-middle attacks. For Kafka, this check has been disabled by default for a long time, but as of Kafka 2.0.0 host name verification of servers is enabled by default for client connections as well as inter-broker connections.
Server host name verification may be disabled by setting `ssl.endpoint.identification.algorithm` to an empty string.
For dynamically configured broker listeners, hostname verification may be disabled using `kafka-configs.sh`:

```
$ bin/kafka-configs.sh --bootstrap-server localhost:9093 --entity-type brokers --entity-name 0 --alter --add-config "listener.name.internal.ssl.endpoint.identification.algorithm="
```

**Note:**

Normally there is no good reason to disable hostname verification apart from being the quickest way to “just get it to work” followed by the promise to “fix it later when there is more time”! Getting hostname verification right is not that hard when done at the right time, but gets much harder once the cluster is up and running - do yourself a favor and do it now!

If host name verification is enabled, clients will verify the server’s fully qualified domain name (FQDN) or ip address against one of the following two fields:

1. Common Name (CN)
2. [Subject Alternative Name (SAN)](https://tools.ietf.org/html/rfc5280#section-4.2.1.6)

Another advantage is that if the SAN field is used for hostname verification the common name can be set to a more meaningful value for authorization purposes. Since we need the SAN field to be contained in the signed certificate, it will be specified when generating the signing request. It can also be specified when generating the keypair, but this will not automatically be copied into the signing request.
To add a SAN field append the following argument `-ext SAN=DNS:{FQDN},IP:{IPADDRESS}` to the keytool command:

```
$ keytool -keystore server.keystore.jks -alias localhost -validity {validity} -genkey -keyalg RSA -destkeystoretype pkcs12 -ext SAN=DNS:{FQDN},IP:{IPADDRESS1}
```

<a id="security-encryption-and-authentication-using-ssl--creating-your-own-ca"></a>

### Creating your own CA

After this step each machine in the cluster has a public/private key pair which can already be used to encrypt traffic and a certificate signing request, which is the basis for creating a certificate. To add authentication capabilities this signing request needs to be signed by a trusted authority, which will be created in this step.

A certificate authority (CA) is responsible for signing certificates. CAs works likes a government that issues passports - the government stamps (signs) each passport so that the passport becomes difficult to forge. Other governments verify the stamps to ensure the passport is authentic. Similarly, the CA signs the certificates, and the cryptography guarantees that a signed certificate is computationally difficult to forge. Thus, as long as the CA is a genuine and trusted authority, the clients have a strong assurance that they are connecting to the authentic machines.

For this guide we will be our own Certificate Authority. When setting up a production cluster in a corporate environment these certificates would usually be signed by a corporate CA that is trusted throughout the company. Please see Common Pitfalls in Production for some things to consider for this case.

Due to a [bug](https://www.openssl.org/docs/man1.1.1/man1/x509.html#BUGS) in OpenSSL, the x509 module will not copy requested extension fields from CSRs into the final certificate. Since we want the SAN extension to be present in our certificate to enable hostname verification, we’ll use the *ca* module instead. This requires some additional configuration to be in place before we generate our CA keypair. Save the following listing into a file called openssl-ca.cnf and adjust the values for validity and common attributes as necessary.

```
     HOME            = .
     RANDFILE        = $ENV::HOME/.rnd

     ####################################################################
     [ ca ]
     default_ca    = CA_default      # The default ca section

     [ CA_default ]

     base_dir      = .
     certificate   = $base_dir/cacert.pem   # The CA certificate
     private_key   = $base_dir/cakey.pem    # The CA private key
     new_certs_dir = $base_dir              # Location for new certs after signing
     database      = $base_dir/index.txt    # Database index file
     serial        = $base_dir/serial.txt   # The current serial number

     default_days     = 1000         # How long to certify for
     default_crl_days = 30           # How long before next CRL
     default_md       = sha256       # Use public key default MD
     preserve         = no           # Keep passed DN ordering

     x509_extensions = ca_extensions # The extensions to add to the cert

     email_in_dn     = no            # Don't concat the email in the DN
     copy_extensions = copy          # Required to copy SANs from CSR to cert

     ####################################################################
     [ req ]
     default_bits       = 4096
     default_keyfile    = cakey.pem
     distinguished_name = ca_distinguished_name
     x509_extensions    = ca_extensions
     string_mask        = utf8only

     ####################################################################
     [ ca_distinguished_name ]
     countryName         = Country Name (2 letter code)
     countryName_default = DE

     stateOrProvinceName         = State or Province Name (full name)
     stateOrProvinceName_default = Test Province

     localityName                = Locality Name (eg, city)
     localityName_default        = Test Town

     organizationName            = Organization Name (eg, company)
     organizationName_default    = Test Company

     organizationalUnitName         = Organizational Unit (eg, division)
     organizationalUnitName_default = Test Unit

     commonName         = Common Name (e.g. server FQDN or YOUR name)
     commonName_default = Test Name

     emailAddress         = Email Address
     emailAddress_default = test@test.com

     ####################################################################
     [ ca_extensions ]

     subjectKeyIdentifier   = hash
     authorityKeyIdentifier = keyid:always, issuer
     basicConstraints       = critical, CA:true
     keyUsage               = keyCertSign, cRLSign

     ####################################################################
     [ signing_policy ]
     countryName            = optional
     stateOrProvinceName    = optional
     localityName           = optional
     organizationName       = optional
     organizationalUnitName = optional
     commonName             = supplied
     emailAddress           = optional

     ####################################################################
     [ signing_req ]
     subjectKeyIdentifier   = hash
     authorityKeyIdentifier = keyid,issuer
     basicConstraints       = CA:FALSE
     keyUsage               = digitalSignature, keyEncipherment
```

Then create a database and serial number file, these will be used to keep track of which certificates were signed with this CA. Both of these are simply text files that reside in the same directory as your CA keys.

```
     $ echo 01 > serial.txt
     $ touch index.txt
```

With these steps done you are now ready to generate your CA that will be used to sign certificates later.

```
     $ openssl req -x509 -config openssl-ca.cnf -newkey rsa:4096 -sha256 -nodes -out cacert.pem -outform PEM
```

The CA is simply a public/private key pair and certificate that is signed by itself, and is only intended to sign other certificates. This keypair should be kept very safe, if someone gains access to it, they can create and sign certificates that will be trusted by your infrastructure, which means they will be able to impersonate anybody when connecting to any service that trusts this CA. The next step is to add the generated CA to the **clients’ truststore** so that the clients can trust this CA:

```
     $ keytool -keystore client.truststore.jks -alias CARoot -import -file ca-cert
```

**Note:** If you configure the Kafka brokers to require client authentication by setting ssl.client.auth to be “requested” or “required” in the Kafka brokers config then you must provide a truststore for the Kafka brokers as well and it should have all the CA certificates that clients’ keys were signed by.

```
     $ keytool -keystore server.truststore.jks -alias CARoot -import -file ca-cert
```

In contrast to the keystore in step 1 that stores each machine’s own identity, the truststore of a client stores all the certificates that the client should trust. Importing a certificate into one’s truststore also means trusting all certificates that are signed by that certificate. As the analogy above, trusting the government (CA) also means trusting all passports (certificates) that it has issued. This attribute is called the chain of trust, and it is particularly useful when deploying SSL on a large Kafka cluster. You can sign all certificates in the cluster with a single CA, and have all machines share the same truststore that trusts the CA. That way all machines can authenticate all other machines.

<a id="security-encryption-and-authentication-using-ssl--signing-the-certificate"></a>

### Signing the certificate

Then sign it with the CA:

```
     $ openssl ca -config openssl-ca.cnf -policy signing_policy -extensions signing_req -out {server certificate} -infiles {certificate signing request}
```

Finally, you need to import both the certificate of the CA and the signed certificate into the keystore:

```
     $ keytool -keystore {keystore} -alias CARoot -import -file {CA certificate}
     $ keytool -keystore {keystore} -alias localhost -import -file cert-signed
```

The definitions of the parameters are the following:

1. keystore: the location of the keystore
2. CA certificate: the certificate of the CA
3. certificate signing request: the csr created with the server key
4. server certificate: the file to write the signed certificate of the server to
   This will leave you with one truststore called *truststore.jks* - this can be the same for all clients and brokers and does not contain any sensitive information, so there is no need to secure this. Additionally you will have one *server.keystore.jks* file per node which contains that nodes keys, certificate and your CAs certificate, please refer to Configuring Kafka Brokers and Configuring Kafka Clients for information on how to use these files.

For some tooling assistance on this topic, please check out the [easyRSA](https://github.com/OpenVPN/easy-rsa) project which has extensive scripting in place to help with these steps.

<a id="security-encryption-and-authentication-using-ssl--ssl-key-and-certificates-in-pem-format"></a>

### SSL key and certificates in PEM format

From 2.7.0 onwards, SSL key and trust stores can be configured for Kafka brokers and clients directly in the configuration in PEM format. This avoids the need to store separate files on the file system and benefits from password protection features of Kafka configuration. PEM may also be used as the store type for file-based key and trust stores in addition to JKS and PKCS12. To configure PEM key store directly in the broker or client configuration, private key in PEM format should be provided in `ssl.keystore.key` and the certificate chain in PEM format should be provided in `ssl.keystore.certificate.chain`. To configure trust store, trust certificates, e.g. public certificate of CA, should be provided in `ssl.truststore.certificates`. Since PEM is typically stored as multi-line base-64 strings, the configuration value can be included in Kafka configuration as multi-line strings with lines terminating in backslash (’') for line continuation.

Store password configs `ssl.keystore.password` and `ssl.truststore.password` are not used for PEM. If private key is encrypted using a password, the key password must be provided in `ssl.key.password`. Private keys may be provided in unencrypted form without a password. In production deployments, configs should be encrypted or externalized using password protection feature in Kafka in this case. Note that the default SSL engine factory has limited capabilities for decryption of encrypted private keys when external tools like OpenSSL are used for encryption. Third party libraries like BouncyCastle may be integrated with a custom `SslEngineFactory` to support a wider range of encrypted private keys.

<a id="security-encryption-and-authentication-using-ssl--common-pitfalls-in-production"></a>

### Common Pitfalls in Production

The above paragraphs show the process to create your own CA and use it to sign certificates for your cluster. While very useful for sandbox, dev, test, and similar systems, this is usually not the correct process to create certificates for a production cluster in a corporate environment. Enterprises will normally operate their own CA and users can send in CSRs to be signed with this CA, which has the benefit of users not being responsible to keep the CA secure as well as a central authority that everybody can trust. However it also takes away a lot of control over the process of signing certificates from the user. Quite often the persons operating corporate CAs will apply tight restrictions on certificates that can cause issues when trying to use these certificates with Kafka.

1. **[Extended Key Usage](https://tools.ietf.org/html/rfc5280#section-4.2.1.12)** Certificates may contain an extension field that controls the purpose for which the certificate can be used. If this field is empty, there are no restrictions on the usage, but if any usage is specified in here, valid SSL implementations have to enforce these usages. Relevant usages for Kafka are:

- Client authentication
- Server authentication
  Kafka brokers need both these usages to be allowed, as for intra-cluster communication every broker will behave as both the client and the server towards other brokers. It is not uncommon for corporate CAs to have a signing profile for webservers and use this for Kafka as well, which will only contain the *serverAuth* usage value and cause the SSL handshake to fail.

2. **Intermediate Certificates** Corporate Root CAs are often kept offline for security reasons. To enable day-to-day usage, so called intermediate CAs are created, which are then used to sign the final certificates. When importing a certificate into the keystore that was signed by an intermediate CA it is necessary to provide the entire chain of trust up to the root CA. This can be done by simply *cat* ing the certificate files into one combined certificate file and then importing this with keytool.
3. **Failure to copy extension fields** CA operators are often hesitant to copy and requested extension fields from CSRs and prefer to specify these themselves as this makes it harder for a malicious party to obtain certificates with potentially misleading or fraudulent values. It is advisable to double check signed certificates, whether these contain all requested SAN fields to enable proper hostname verification. The following command can be used to print certificate details to the console, which should be compared with what was originally requested:

```
     $ openssl x509 -in certificate.crt -text -noout
```

<a id="security-encryption-and-authentication-using-ssl--configuring-kafka-brokers"></a>

### Configuring Kafka Brokers

If SSL is not enabled for inter-broker communication (see below for how to enable it), both PLAINTEXT and SSL ports will be necessary.

```
     listeners=PLAINTEXT://host.name:port,SSL://host.name:port
```

Following SSL configs are needed on the broker side

```
     ssl.keystore.location=/var/private/ssl/server.keystore.jks
     ssl.keystore.password=test1234
     ssl.key.password=test1234
     ssl.truststore.location=/var/private/ssl/server.truststore.jks
     ssl.truststore.password=test1234
```

Note: ssl.truststore.password is technically optional but highly recommended. If a password is not set access to the truststore is still available, but integrity checking is disabled. Optional settings that are worth considering:

1. ssl.client.auth=none (“required” => client authentication is required, “requested” => client authentication is requested and client without certs can still connect. The usage of “requested” is discouraged as it provides a false sense of security and misconfigured clients will still connect successfully.)
2. ssl.cipher.suites (Optional). A cipher suite is a named combination of authentication, encryption, MAC and key exchange algorithm used to negotiate the security settings for a network connection using TLS or SSL network protocol. (Default is an empty list)
4. ssl.keystore.type=JKS
5. ssl.truststore.type=JKS
6. ssl.secure.random.implementation=SHA1PRNG
   If you want to enable SSL for inter-broker communication, add the following to the server.properties file (it defaults to PLAINTEXT)

   security.inter.broker.protocol=SSL

Due to import regulations in some countries, the Oracle implementation limits the strength of cryptographic algorithms available by default. If stronger algorithms are needed (for example, AES with 256-bit keys), the [JCE Unlimited Strength Jurisdiction Policy Files](https://www.oracle.com/technetwork/java/javase/downloads/index.html) must be obtained and installed in the JDK/JRE. See the [JCA Providers Documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html) for more information.

The JRE/JDK will have a default pseudo-random number generator (PRNG) that is used for cryptography operations, so it is not required to configure the implementation used with the `ssl.secure.random.implementation`. However, there are performance issues with some implementations (notably, the default chosen on Linux systems, `NativePRNG`, utilizes a global lock). In cases where performance of SSL connections becomes an issue, consider explicitly setting the implementation to be used. The `SHA1PRNG` implementation is non-blocking, and has shown very good performance characteristics under heavy load (50 MB/sec of produced messages, plus replication traffic, per-broker).

Once you start the broker you should be able to see in the server.log

```
with addresses: PLAINTEXT -> EndPoint(192.168.64.1,9092,PLAINTEXT),SSL -> EndPoint(192.168.64.1,9093,SSL)
```

To check quickly if the server keystore and truststore are setup properly you can run the following command

```
$ openssl s_client -debug -connect localhost:9093 -tls1
```

(Note: TLSv1 should be listed under ssl.enabled.protocols) In the output of this command you should see server’s certificate:

```
-----BEGIN CERTIFICATE-----
{variable sized random bytes}
-----END CERTIFICATE-----
subject=/C=US/ST=CA/L=Santa Clara/O=org/OU=org/CN=Sriharsha Chintalapani
issuer=/C=US/ST=CA/L=Santa Clara/O=org/OU=org/CN=kafka/emailAddress=test@test.com
```

If the certificate does not show up or if there are any other error messages then your keystore is not setup properly.

<a id="security-encryption-and-authentication-using-ssl--configuring-kafka-clients"></a>

### Configuring Kafka Clients

SSL is supported only for the new Kafka Producer and Consumer, the older API is not supported. The configs for SSL will be the same for both producer and consumer. If client authentication is not required in the broker, then the following is a minimal configuration example:

```
     security.protocol=SSL
     ssl.truststore.location=/var/private/ssl/client.truststore.jks
     ssl.truststore.password=test1234
```

Note: ssl.truststore.password is technically optional but highly recommended. If a password is not set access to the truststore is still available, but integrity checking is disabled. If client authentication is required, then a keystore must be created like in step 1 and the following must also be configured:

```
     ssl.keystore.location=/var/private/ssl/client.keystore.jks
     ssl.keystore.password=test1234
     ssl.key.password=test1234
```

Other configuration settings that may also be needed depending on our requirements and the broker configuration:

1. ssl.provider (Optional). The name of the security provider used for SSL connections. Default value is the default security provider of the JVM.
2. ssl.cipher.suites (Optional). A cipher suite is a named combination of authentication, encryption, MAC and key exchange algorithm used to negotiate the security settings for a network connection using TLS or SSL network protocol.
3. ssl.enabled.protocols=TLSv1.2,TLSv1.1,TLSv1. It should list at least one of the protocols configured on the broker side
4. ssl.truststore.type=JKS
5. ssl.keystore.type=JKS

Examples using console-producer and console-consumer:

```
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9093 --topic test --command-config client-ssl.properties
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9093 --topic test --command-config client-ssl.properties
```

---

<a id="security-authentication-using-sasl"></a>

<a id="security-authentication-using-sasl--authentication-using-sasl"></a>

# Authentication using SASL

Authentication using SASL

<a id="security-authentication-using-sasl--jaas-configuration"></a>

### JAAS configuration

Kafka uses the Java Authentication and Authorization Service ([JAAS](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASRefGuide.html)) for SASL configuration.

<a id="security-authentication-using-sasl--jaas-configuration-for-kafka-brokers"></a>

#### JAAS configuration for Kafka brokers

`KafkaServer` is the section name in the JAAS file used by each KafkaServer/Broker. This section provides SASL configuration options for the broker including any SASL client connections made by the broker for inter-broker communication. If multiple listeners are configured to use SASL, the section name may be prefixed with the listener name in lower-case followed by a period, e.g. `sasl_ssl.KafkaServer`.

Brokers may also configure JAAS using the broker configuration property `sasl.jaas.config`. The property name must be prefixed with the listener prefix including the SASL mechanism, i.e. `listener.name.{listenerName}.{saslMechanism}.sasl.jaas.config`. Only one login module may be specified in the config value. If multiple mechanisms are configured on a listener, configs must be provided for each mechanism using the listener and mechanism prefix. For example,

```
        listener.name.sasl_ssl.scram-sha-256.sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
            username="admin" \
            password="admin-secret";
        listener.name.sasl_ssl.plain.sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
            username="admin" \
            password="admin-secret" \
            user_admin="admin-secret" \
            user_alice="alice-secret";
```

If JAAS configuration is defined at different levels, the order of precedence used is:

- Broker configuration property `listener.name.{listenerName}.{saslMechanism}.sasl.jaas.config`
- `{listenerName}.KafkaServer` section of static JAAS configuration
- `KafkaServer` section of static JAAS configuration

See GSSAPI (Kerberos), PLAIN, SCRAM, or non-production/production OAUTHBEARER for example broker configurations.

<a id="security-authentication-using-sasl--jaas-configuration-for-kafka-clients"></a>

#### JAAS configuration for Kafka clients

Clients may configure JAAS using the client configuration property sasl.jaas.config or using the static JAAS config file similar to brokers.

<a id="security-authentication-using-sasl--jaas-configuration-using-client-configuration-property"></a>

##### JAAS configuration using client configuration property

Clients may specify JAAS configuration as a producer or consumer property without creating a physical configuration file. This mode also enables different producers and consumers within the same JVM to use different credentials by specifying different properties for each client. If both static JAAS configuration system property `java.security.auth.login.config` and client property `sasl.jaas.config` are specified, the client property will be used.

See GSSAPI (Kerberos), PLAIN, SCRAM, or non-production/production OAUTHBEARER for example client configurations.

<a id="security-authentication-using-sasl--jaas-configuration-using-static-config-file"></a>

##### JAAS configuration using static config file

To configure SASL authentication on the clients using static JAAS config file:

1. Add a JAAS config file with a client login section named `KafkaClient`. Configure a login module in `KafkaClient` for the selected mechanism as described in the examples for setting up GSSAPI (Kerberos), PLAIN, SCRAM, or non-production/production OAUTHBEARER. For example, GSSAPI credentials may be configured as:

```
KafkaClient {
    com.sun.security.auth.module.Krb5LoginModule required
    useKeyTab=true
    storeKey=true
    keyTab="/etc/security/keytabs/kafka_client.keytab"
    principal="kafka-client-1@EXAMPLE.COM";
};
```

2. Pass the JAAS config file location as JVM parameter to each client JVM. For example:

```
-Djava.security.auth.login.config=/etc/kafka/kafka_client_jaas.conf
```

<a id="security-authentication-using-sasl--sasl-configuration"></a>

### SASL configuration

SASL may be used with PLAINTEXT or SSL as the transport layer using the security protocol SASL\_PLAINTEXT or SASL\_SSL respectively. If SASL\_SSL is used, then SSL must also be configured.

<a id="security-authentication-using-sasl--sasl-mechanisms"></a>

#### SASL mechanisms

Kafka supports the following SASL mechanisms:

- GSSAPI (Kerberos)
- PLAIN
- SCRAM-SHA-256
- SCRAM-SHA-512
- OAUTHBEARER

<a id="security-authentication-using-sasl--sasl-configuration-for-kafka-brokers"></a>

#### SASL configuration for Kafka brokers

1. Configure a SASL port in server.properties, by adding at least one of SASL\_PLAINTEXT or SASL\_SSL to the *listeners* parameter, which contains one or more comma-separated values:

```
listeners=SASL_PLAINTEXT://host.name:port
```

   If you are only configuring a SASL port (or if you want the Kafka brokers to authenticate each other using SASL) then make sure you set the same SASL protocol for inter-broker communication:

```
security.inter.broker.protocol=SASL_PLAINTEXT (or SASL_SSL)
```

2. Select one or more supported mechanisms to enable in the broker and follow the steps to configure SASL for the mechanism. To enable multiple mechanisms in the broker, follow the steps here.

<a id="security-authentication-using-sasl--sasl-configuration-for-kafka-clients"></a>

#### SASL configuration for Kafka clients

SASL authentication is only supported for the new Java Kafka producer and consumer, the older API is not supported.

To configure SASL authentication on the clients, select a SASL mechanism that is enabled in the broker for client authentication and follow the steps to configure SASL for the selected mechanism.

Note: When establishing connections to brokers via SASL, clients may perform a reverse DNS lookup of the broker address. Due to how the JRE implements reverse DNS lookups, clients may observe slow SASL handshakes if fully qualified domain names are not used, for both the client’s `bootstrap.servers` and a broker’s `advertised.listeners`.

<a id="security-authentication-using-sasl--authentication-using-saslkerberos"></a>
<a id="security-authentication-using-sasl--authentication-using-sasl-kerberos"></a>

### Authentication using SASL/Kerberos

<a id="security-authentication-using-sasl--prerequisites"></a>

#### Prerequisites

1. **Kerberos**
   If your organization is already using a Kerberos server (for example, by using Active Directory), there is no need to install a new server just for Kafka. Otherwise you will need to install one, your Linux vendor likely has packages for Kerberos and a short guide on how to install and configure it ([Ubuntu](https://help.ubuntu.com/community/Kerberos), [Redhat](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Managing_Smart_Cards/installing-kerberos.html)). Note that if you are using Oracle Java, you will need to download JCE policy files for your Java version and copy them to $JAVA\_HOME/jre/lib/security.
2. **Create Kerberos Principals**
   If you are using the organization’s Kerberos or Active Directory server, ask your Kerberos administrator for a principal for each Kafka broker in your cluster and for every operating system user that will access Kafka with Kerberos authentication (via clients and tools).

   If you have installed your own Kerberos, you will need to create these principals yourself using the following commands:

```
$ sudo /usr/sbin/kadmin.local -q 'addprinc -randkey kafka/{hostname}@{REALM}'
$ sudo /usr/sbin/kadmin.local -q "ktadd -k /etc/security/keytabs/{keytabname}.keytab kafka/{hostname}@{REALM}"
```

3. **Make sure all hosts can be reachable using hostnames** - it is a Kerberos requirement that all your hosts can be resolved with their FQDNs.

<a id="security-authentication-using-sasl--configuring-kafka-brokers"></a>

#### Configuring Kafka Brokers

1. Add a suitably modified JAAS file similar to the one below to each Kafka broker’s config directory, let’s call it kafka\_server\_jaas.conf for this example (note that each broker should have its own keytab):

```
KafkaServer {
    com.sun.security.auth.module.Krb5LoginModule required
    useKeyTab=true
    storeKey=true
    keyTab="/etc/security/keytabs/kafka_server.keytab"
    principal="kafka/kafka1.hostname.com@EXAMPLE.COM";
};
```

   `KafkaServer` section in the JAAS file tells the broker which principal to use and the location of the keytab where this principal is stored. It allows the broker to login using the keytab specified in this section.
2. Pass the JAAS and optionally the krb5 file locations as JVM parameters to each Kafka broker (see [here](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html) for more details):

```
-Djava.security.krb5.conf=/etc/kafka/krb5.conf
-Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
```

3. Make sure the keytabs configured in the JAAS file are readable by the operating system user who is starting kafka broker.
4. Configure SASL port and SASL mechanisms in server.properties as described here. For example:

```
listeners=SASL_PLAINTEXT://host.name:port
security.inter.broker.protocol=SASL_PLAINTEXT
sasl.mechanism.inter.broker.protocol=GSSAPI
sasl.enabled.mechanisms=GSSAPI
```

   We must also configure the service name in server.properties, which should match the principal name of the kafka brokers. In the above example, principal is “[kafka/kafka1.hostname.com@EXAMPLE.com](mailto:kafka/kafka1.hostname.com@EXAMPLE.com)”, so:

```
sasl.kerberos.service.name=kafka
```

<a id="security-authentication-using-sasl--configuring-kafka-clients"></a>

#### Configuring Kafka Clients

To configure SASL authentication on the clients:

1. Clients (producers, consumers, connect workers, etc) will authenticate to the cluster with their own principal (usually with the same name as the user running the client), so obtain or create these principals as needed. Then configure the JAAS configuration property for each client. Different clients within a JVM may run as different users by specifying different principals. The property `sasl.jaas.config` in producer.properties or consumer.properties describes how clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client using a keytab (recommended for long-running processes):

```
        sasl.jaas.config=com.sun.security.auth.module.Krb5LoginModule required \
            useKeyTab=true \
            storeKey=true  \
            keyTab="/etc/security/keytabs/kafka_client.keytab" \
            principal="kafka-client-1@EXAMPLE.COM";
```

For command-line utilities like kafka-console-consumer or kafka-console-producer, kinit can be used along with “useTicketCache=true” as in:

```
           sasl.jaas.config=com.sun.security.auth.module.Krb5LoginModule required \
               useTicketCache=true;
```

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.
2. Make sure the keytabs configured in the JAAS configuration are readable by the operating system user who is starting kafka client.
3. Optionally pass the krb5 file locations as JVM parameters to each client JVM (see [here](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/KerberosReq.html) for more details):

```
           -Djava.security.krb5.conf=/etc/kafka/krb5.conf
```

4. Configure the following properties in producer.properties or consumer.properties:

```
        security.protocol=SASL_PLAINTEXT (or SASL_SSL)
        sasl.mechanism=GSSAPI
        sasl.kerberos.service.name=kafka
```

<a id="security-authentication-using-sasl--authentication-using-saslplain"></a>
<a id="security-authentication-using-sasl--authentication-using-sasl-plain"></a>

### Authentication using SASL/PLAIN

SASL/PLAIN is a simple username/password authentication mechanism that is typically used with TLS for encryption to implement secure authentication. Kafka supports a default implementation for SASL/PLAIN which can be extended for production use as described here.

Under the default implementation of `principal.builder.class`, the username is used as the authenticated `Principal` for configuration of ACLs etc.

<a id="security-authentication-using-sasl--configuring-kafka-brokers-1"></a>
<a id="security-authentication-using-sasl--configuring-kafka-brokers-2"></a>

#### Configuring Kafka Brokers

1. Add a suitably modified JAAS file similar to the one below to each Kafka broker’s config directory, let’s call it kafka\_server\_jaas.conf for this example:

```
        KafkaServer {
            org.apache.kafka.common.security.plain.PlainLoginModule required
            username="admin"
            password="admin-secret"
            user_admin="admin-secret"
            user_alice="alice-secret";
        };
```

This configuration defines two users (*admin* and *alice*). The properties `username` and `password` in the `KafkaServer` section are used by the broker to initiate connections to other brokers. In this example, *admin* is the user for inter-broker communication. The set of properties `user__userName_` defines the passwords for all users that connect to the broker and the broker validates all client connections including those from other brokers using these properties.
2. Pass the JAAS config file location as JVM parameter to each Kafka broker:

```
           -Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
```

3. Configure SASL port and SASL mechanisms in server.properties as described here. For example:

```
        listeners=SASL_SSL://host.name:port
        security.inter.broker.protocol=SASL_SSL
        sasl.mechanism.inter.broker.protocol=PLAIN
        sasl.enabled.mechanisms=PLAIN
```

<a id="security-authentication-using-sasl--configuring-kafka-clients-1"></a>
<a id="security-authentication-using-sasl--configuring-kafka-clients-2"></a>

#### Configuring Kafka Clients

To configure SASL authentication on the clients:

1. Configure the JAAS configuration property for each client in producer.properties or consumer.properties. The login module describes how the clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client for the PLAIN mechanism:

```
        sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required \
            username="alice" \
            password="alice-secret";
```

The options `username` and `password` are used by clients to configure the user for client connections. In this example, clients connect to the broker as user *alice*. Different clients within a JVM may connect as different users by specifying different user names and passwords in `sasl.jaas.config`.

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.

2. Configure the following properties in producer.properties or consumer.properties:

```
        security.protocol=SASL_SSL
        sasl.mechanism=PLAIN
```

<a id="security-authentication-using-sasl--use-of-saslplain-in-production"></a>
<a id="security-authentication-using-sasl--use-of-sasl-plain-in-production"></a>

#### Use of SASL/PLAIN in production

- SASL/PLAIN should be used only with SSL as transport layer to ensure that clear passwords are not transmitted on the wire without encryption.
- The default implementation of SASL/PLAIN in Kafka specifies usernames and passwords in the JAAS configuration file as shown here. From Kafka version 2.0 onwards, you can avoid storing clear passwords on disk by configuring your own callback handlers that obtain username and password from an external source using the configuration options `sasl.server.callback.handler.class` and `sasl.client.callback.handler.class`.
- In production systems, external authentication servers may implement password authentication. From Kafka version 2.0 onwards, you can plug in your own callback handlers that use external authentication servers for password verification by configuring `sasl.server.callback.handler.class`.

<a id="security-authentication-using-sasl--authentication-using-saslscram"></a>
<a id="security-authentication-using-sasl--authentication-using-sasl-scram"></a>

### Authentication using SASL/SCRAM

Salted Challenge Response Authentication Mechanism (SCRAM) is a family of SASL mechanisms that addresses the security concerns with traditional mechanisms that perform username/password authentication like PLAIN and DIGEST-MD5. The mechanism is defined in [RFC 5802](https://tools.ietf.org/html/rfc5802). Kafka supports [SCRAM-SHA-256](https://tools.ietf.org/html/rfc7677) and SCRAM-SHA-512 which can be used with TLS to perform secure authentication. Under the default implementation of `principal.builder.class`, the username is used as the authenticated `Principal` for configuration of ACLs etc. The default SCRAM implementation in Kafka stores SCRAM credentials in the metadata log. Refer to Security Considerations for more details.

<a id="security-authentication-using-sasl--creating-scram-credentials"></a>

#### Creating SCRAM Credentials

The SCRAM implementation in Kafka uses the metadata log as credential store. Credentials can be created in the metadata log using `kafka-storage.sh` or `kafka-configs.sh`. For each SCRAM mechanism enabled, credentials must be created by adding a config with the mechanism name. Credentials for inter-broker communication must be created before Kafka brokers are started. `kafka-storage.sh` can format storage with initial credentials. Client credentials may be created and updated dynamically and updated credentials will be used to authenticate new connections. `kafka-configs.sh` can be used to create and update credentials after Kafka brokers are started.

Create initial SCRAM credentials for user *admin* with password *admin-secret* :

```
        $ bin/kafka-storage.sh format -t $(bin/kafka-storage.sh random-uuid) -c config/server.properties --add-scram 'SCRAM-SHA-256=[name="admin",password="admin-secret"]'
```

Create SCRAM credentials for user *alice* with password *alice-secret* (refer to Configuring Kafka Clients for client configuration):

```
        $ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --add-config 'SCRAM-SHA-256=[iterations=8192,password=alice-secret]' --entity-type users --entity-name alice --command-config client.properties
```

The default iteration count of 4096 is used if iterations are not specified. A random salt is created if it’s not specified. The SCRAM identity consisting of salt, iterations, StoredKey and ServerKey are stored in the metadata log. See [RFC 5802](https://tools.ietf.org/html/rfc5802) for details on SCRAM identity and the individual fields.

Existing credentials may be listed using the *--describe* option:

```
        $ bin/kafka-configs.sh --bootstrap-server localhost:9092 --describe --entity-type users --entity-name alice --command-config client.properties
```

Credentials may be deleted for one or more SCRAM mechanisms using the *--alter –delete-config* option:

```
        $ bin/kafka-configs.sh --bootstrap-server localhost:9092 --alter --delete-config 'SCRAM-SHA-256' --entity-type users --entity-name alice --command-config client.properties
```

<a id="security-authentication-using-sasl--configuring-kafka-brokers-2-2"></a>
<a id="security-authentication-using-sasl--configuring-kafka-brokers-3"></a>

#### Configuring Kafka Brokers

1. Add a suitably modified JAAS file similar to the one below to each Kafka broker’s config directory, let’s call it kafka\_server\_jaas.conf for this example:

```
        KafkaServer {
            org.apache.kafka.common.security.scram.ScramLoginModule required
            username="admin"
            password="admin-secret";
        };
```

The properties `username` and `password` in the `KafkaServer` section are used by the broker to initiate connections to other brokers. In this example, *admin* is the user for inter-broker communication.
2. Pass the JAAS config file location as JVM parameter to each Kafka broker:

```
           -Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
```

3. Configure SASL port and SASL mechanisms in server.properties as described here. For example:

```
        listeners=SASL_SSL://host.name:port
        security.inter.broker.protocol=SASL_SSL
        sasl.mechanism.inter.broker.protocol=SCRAM-SHA-256 (or SCRAM-SHA-512)
        sasl.enabled.mechanisms=SCRAM-SHA-256 (or SCRAM-SHA-512)
```

<a id="security-authentication-using-sasl--configuring-kafka-clients-2-2"></a>
<a id="security-authentication-using-sasl--configuring-kafka-clients-3"></a>

#### Configuring Kafka Clients

To configure SASL authentication on the clients:

1. Configure the JAAS configuration property for each client in producer.properties or consumer.properties. The login module describes how the clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client for the SCRAM mechanisms:

```
        sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
            username="alice" \
            password="alice-secret";
```

The options `username` and `password` are used by clients to configure the user for client connections. In this example, clients connect to the broker as user *alice*. Different clients within a JVM may connect as different users by specifying different user names and passwords in `sasl.jaas.config`.

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.

2. Configure the following properties in producer.properties or consumer.properties:

```
        security.protocol=SASL_SSL
        sasl.mechanism=SCRAM-SHA-256 (or SCRAM-SHA-512)
```

<a id="security-authentication-using-sasl--security-considerations-for-saslscram"></a>
<a id="security-authentication-using-sasl--security-considerations-for-sasl-scram"></a>

#### Security Considerations for SASL/SCRAM

- The default implementation of SASL/SCRAM in Kafka stores SCRAM credentials in the metadata log. This is suitable for production use in installations where KRaft controllers are secure and on a private network.
- Kafka supports only the strong hash functions SHA-256 and SHA-512 with a minimum iteration count of 4096. Strong hash functions combined with strong passwords and high iteration counts protect against brute force attacks if KRaft controllers security is compromised.
- SCRAM should be used only with TLS-encryption to prevent interception of SCRAM exchanges. This protects against dictionary or brute force attacks and against impersonation if KRaft controllers security is compromised.
- From Kafka version 2.0 onwards, the default SASL/SCRAM credential store may be overridden using custom callback handlers by configuring `sasl.server.callback.handler.class` in installations where KRaft controllers are not secure.
- For more details on security considerations, refer to [RFC 5802](https://tools.ietf.org/html/rfc5802#section-9).

<a id="security-authentication-using-sasl--authentication-using-sasloauthbearer"></a>
<a id="security-authentication-using-sasl--authentication-using-sasl-oauthbearer"></a>

### Authentication using SASL/OAUTHBEARER

The [OAuth 2 Authorization Framework](https://tools.ietf.org/html/rfc6749) “enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.” The SASL OAUTHBEARER mechanism enables the use of the framework in a SASL (i.e. a non-HTTP) context; it is defined in [RFC 7628](https://tools.ietf.org/html/rfc7628). The default OAUTHBEARER implementation in Kafka creates and validates [Unsecured JSON Web Tokens](https://tools.ietf.org/html/rfc7515#appendix-A.5) and is only suitable for use in non-production Kafka installations. Refer to Security Considerations for more details. Recent versions of Apache Kafka have added production-ready OAUTHBEARER implementations that support interaction with an OAuth 2.0-standards compliant identity provider. Both modes are described in the following, noted where applicable.

Under the default implementation of `principal.builder.class`, the principalName of OAuthBearerToken is used as the authenticated `Principal` for configuration of ACLs etc.

<a id="security-authentication-using-sasl--configuring-non-production-kafka-brokers"></a>

#### Configuring Non-production Kafka Brokers

The default implementation of SASL/OAUTHBEARER in Kafka creates and validates [Unsecured JSON Web Tokens](https://tools.ietf.org/html/rfc7515#appendix-A.5). While suitable only for non-production use, it does provide the flexibility to create arbitrary tokens in a DEV or TEST environment.

1. Add a suitably modified JAAS file similar to the one below to each Kafka broker’s config directory, let’s call it kafka\_server\_jaas.conf for this example:

```
        KafkaServer {
            org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required
            unsecuredLoginStringClaim_sub="admin";
        };
```

The property `unsecuredLoginStringClaim_sub` in the `KafkaServer` section is used by the broker when it initiates connections to other brokers. In this example, *admin* will appear in the subject (`sub`) claim and will be the user for inter-broker communication.

Here are the various supported JAAS module options on the broker side for [Unsecured JSON Web Token](https://tools.ietf.org/html/rfc7515#appendix-A.5) validation:

| JAAS Module Option for Unsecured Token Validation | Documentation |
| --- | --- |
| `unsecuredValidatorPrincipalClaimName="value"` | Set to a non-empty value if you wish a particular `String` claim holding a principal name to be checked for existence; the default is to check for the existence of the ‘`sub`’ claim. |
| `unsecuredValidatorScopeClaimName="value"` | Set to a custom claim name if you wish the name of the `String` or `String List` claim holding any token scope to be something other than ‘`scope`’. |
| `unsecuredValidatorRequiredScope="value"` | Set to a space-delimited list of scope values if you wish the `String/String List` claim holding the token scope to be checked to make sure it contains certain values. |
| `unsecuredValidatorAllowableClockSkewMs="value"` | Set to a positive integer value if you wish to allow up to some number of positive milliseconds of clock skew (the default is 0). |

2. Pass the JAAS config file location as JVM parameter to each Kafka broker:

```
        -Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
```

3. Configure SASL port and SASL mechanisms in server.properties as described here. For example:

```
        listeners=SASL_SSL://host.name:port (or SASL_PLAINTEXT if non-production)
        security.inter.broker.protocol=SASL_SSL (or SASL_PLAINTEXT if non-production)
        sasl.mechanism.inter.broker.protocol=OAUTHBEARER
        sasl.enabled.mechanisms=OAUTHBEARER
```

<a id="security-authentication-using-sasl--configuring-production-kafka-brokers"></a>

#### Configuring Production Kafka Brokers

1. Add a suitably modified JAAS file similar to the one below to each Kafka broker’s config directory, let’s call it kafka\_server\_jaas.conf for this example:

```
        KafkaServer {
            org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required ;
        };
```

2. Pass the JAAS config file location as JVM parameter to each Kafka broker:

```
        -Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
```

3. Configure SASL port and SASL mechanisms in server.properties as described here. For example:

```
        listeners=SASL_SSL://host.name:port
        security.inter.broker.protocol=SASL_SSL
        sasl.mechanism.inter.broker.protocol=OAUTHBEARER
        sasl.enabled.mechanisms=OAUTHBEARER
        listener.name.<listener name>.oauthbearer.sasl.server.callback.handler.class=org.apache.kafka.common.security.oauthbearer.OAuthBearerValidatorCallbackHandler
        listener.name.<listener name>.oauthbearer.sasl.oauthbearer.jwks.endpoint.url=https://example.com/oauth2/v1/keys
```

The OAUTHBEARER broker configuration includes:

- sasl.oauthbearer.clock.skew.seconds
- sasl.oauthbearer.expected.audience
- sasl.oauthbearer.expected.issuer
- sasl.oauthbearer.jwks.endpoint.refresh.ms
- sasl.oauthbearer.jwks.endpoint.retry.backoff.max.ms
- sasl.oauthbearer.jwks.endpoint.retry.backoff.ms
- sasl.oauthbearer.jwks.endpoint.url
- sasl.oauthbearer.scope.claim.name
- sasl.oauthbearer.sub.claim.name

<a id="security-authentication-using-sasl--configuring-non-production-kafka-clients"></a>

#### Configuring Non-production Kafka Clients

To configure SASL authentication on the clients:

1. Configure the JAAS configuration property for each client in producer.properties or consumer.properties. The login module describes how the clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client for the OAUTHBEARER mechanisms:

```
        sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required \
            unsecuredLoginStringClaim_sub="alice";
```

The option `unsecuredLoginStringClaim_sub` is used by clients to configure the subject (`sub`) claim, which determines the user for client connections. In this example, clients connect to the broker as user *alice*. Different clients within a JVM may connect as different users by specifying different subject (`sub`) claims in `sasl.jaas.config`.

The default implementation of SASL/OAUTHBEARER in Kafka creates and validates [Unsecured JSON Web Tokens](https://tools.ietf.org/html/rfc7515#appendix-A.5). While suitable only for non-production use, it does provide the flexibility to create arbitrary tokens in a DEV or TEST environment.

Here are the various supported JAAS module options on the client side (and on the broker side if OAUTHBEARER is the inter-broker protocol):

| JAAS Module Option for Unsecured Token Creation | Documentation |
| --- | --- |
| `unsecuredLoginStringClaim_<claimname>="value"` | Creates a `String` claim with the given name and value. Any valid claim name can be specified except ‘`iat`’ and ‘`exp`’ (these are automatically generated). |
| `unsecuredLoginNumberClaim_<claimname>="value"` | Creates a `Number` claim with the given name and value. Any valid claim name can be specified except ‘`iat`’ and ‘`exp`’ (these are automatically generated). |
| `unsecuredLoginListClaim_<claimname>="value"` | Creates a `String List` claim with the given name and values parsed from the given value where the first character is taken as the delimiter. For example: `unsecuredLoginListClaim_fubar="\|value1\|value2"`. Any valid claim name can be specified except ‘`iat`’ and ‘`exp`’ (these are automatically generated). |
| `unsecuredLoginExtension_<extensionname>="value"` | Creates a `String` extension with the given name and value. For example: `unsecuredLoginExtension_traceId="123"`. A valid extension name is any sequence of lowercase or uppercase alphabet characters. In addition, the “auth” extension name is reserved. A valid extension value is any combination of characters with ASCII codes 1-127. |
| `unsecuredLoginPrincipalClaimName` | Set to a custom claim name if you wish the name of the `String` claim holding the principal name to be something other than ‘`sub`’. |
| `unsecuredLoginLifetimeSeconds` | Set to an integer value if the token expiration is to be set to something other than the default value of 3600 seconds (which is 1 hour). The ‘`exp`’ claim will be set to reflect the expiration time. |
| `unsecuredLoginScopeClaimName` | Set to a custom claim name if you wish the name of the `String` or `String List` claim holding any token scope to be something other than ‘`scope`’. |

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.

2. Configure the following properties in producer.properties or consumer.properties:

```
        security.protocol=SASL_SSL (or SASL_PLAINTEXT if non-production)
        sasl.mechanism=OAUTHBEARER
```

3. The default implementation of SASL/OAUTHBEARER depends on the jackson-databind library. Since it’s an optional dependency, users have to configure it as a dependency via their build tool.

<a id="security-authentication-using-sasl--configuring-production-kafka-clients"></a>

#### Configuring Production Kafka Clients

To configure SASL authentication on the clients:

1. Configure the JAAS configuration property for each client in producer.properties or consumer.properties. The login module describes how the clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client for the OAUTHBEARER mechanisms:

```
        sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required ;
```

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.

2. Configure the following properties in producer.properties or consumer.properties. The `sasl.oauthbearer.jwt.retriever.class` property defaults to `DefaultJwtRetriever`, which automatically delegates to `ClientCredentialsJwtRetriever` for HTTP/HTTPS token endpoint URLs and `FileJwtRetriever` for `file://` URLs. In most cases, this property does not need to be set explicitly.

For example, if using the OAuth `client_credentials` grant type with a client secret to communicate with the OAuth identity provider, the configuration might look like this:

```
           security.protocol=SASL_SSL
           sasl.mechanism=OAUTHBEARER
           sasl.oauthbearer.client.credentials.client.id=jdoe
           sasl.oauthbearer.client.credentials.client.secret=$3cr3+
           sasl.oauthbearer.scope=my-application-scope
           sasl.oauthbearer.token.endpoint.url=https://example.com/oauth2/v1/token
```

Alternatively, the `client_credentials` grant type also supports client assertion authentication as defined in [RFC 7523](https://tools.ietf.org/html/rfc7523). Instead of sending a client secret, the client authenticates by presenting a signed JWT assertion to the OAuth identity provider. This provides enhanced security since private keys never leave the client and assertions are short-lived. See [KIP-1258](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1258) for details.

When using client assertion with dynamically-generated JWTs (recommended), the configuration might look like this:

```
           security.protocol=SASL_SSL
           sasl.mechanism=OAUTHBEARER
           sasl.oauthbearer.token.endpoint.url=https://example.com/oauth2/v1/token
           sasl.oauthbearer.assertion.private.key.file=/path/to/private-key.pem
           sasl.oauthbearer.assertion.algorithm=RS256
           sasl.oauthbearer.assertion.claim.iss=my-kafka-client
           sasl.oauthbearer.assertion.claim.sub=my-service-account
           sasl.oauthbearer.assertion.claim.aud=https://example.com
           sasl.oauthbearer.assertion.claim.exp.seconds=300
           sasl.oauthbearer.assertion.claim.jti.include=true
           sasl.oauthbearer.scope=my-application-scope
```

Alternatively, a pre-generated JWT assertion can be read from a file. This is useful when assertions are generated by an external process or secrets manager:

```
           security.protocol=SASL_SSL
           sasl.mechanism=OAUTHBEARER
           sasl.oauthbearer.token.endpoint.url=https://example.com/oauth2/v1/token
           sasl.oauthbearer.assertion.file=/path/to/assertion.jwt
           sasl.oauthbearer.scope=my-application-scope
```

For dynamically-generated assertions, additional static claims can be provided via a JSON template file using `sasl.oauthbearer.assertion.template.file`. The template supports `header` and `payload` sections whose values are merged into the generated JWT:

```
           {
             "header": {
               "kid": "my-key-id"
             },
             "payload": {
               "iss": "my-kafka-client",
               "sub": "my-service-account",
               "aud": "https://example.com"
             }
           }
```

When both client assertion and client secret configurations are present, the `ClientCredentialsJwtRetriever` uses a three-tier preference order:

1. **File-based assertion** (`sasl.oauthbearer.assertion.file`) — highest priority
2. **Locally-generated assertion** (`sasl.oauthbearer.assertion.claim.iss` with private key) — second priority
3. **Client secret** (`sasl.oauthbearer.client.credentials.client.secret`) — fallback

This selection is made at configuration time. Once a method is selected, it persists for the client’s lifetime; runtime failures do not cause fallback to an alternative method.

Or, if using the OAuth `urn:ietf:params:oauth:grant-type:jwt-bearer` grant type to communicate with the OAuth identity provider, the `JwtBearerJwtRetriever` must be configured explicitly since the default retriever delegates to `ClientCredentialsJwtRetriever`:

```
           security.protocol=SASL_SSL
           sasl.mechanism=OAUTHBEARER
           sasl.oauthbearer.jwt.retriever.class=org.apache.kafka.common.security.oauthbearer.JwtBearerJwtRetriever
           sasl.oauthbearer.assertion.private.key.file=/path/to/private.key
           sasl.oauthbearer.assertion.algorithm=RS256
           sasl.oauthbearer.assertion.claim.exp.seconds=600
           sasl.oauthbearer.assertion.template.file=/path/to/template.json
           sasl.oauthbearer.scope=my-application-scope
           sasl.oauthbearer.token.endpoint.url=https://example.com/oauth2/v1/token
```

The OAUTHBEARER client configuration includes:

- sasl.oauthbearer.assertion.algorithm
- sasl.oauthbearer.assertion.claim.aud
- sasl.oauthbearer.assertion.claim.exp.seconds
- sasl.oauthbearer.assertion.claim.iss
- sasl.oauthbearer.assertion.claim.jti.include
- sasl.oauthbearer.assertion.claim.nbf.seconds
- sasl.oauthbearer.assertion.claim.sub
- sasl.oauthbearer.assertion.file
- sasl.oauthbearer.assertion.private.key.file
- sasl.oauthbearer.assertion.private.key.passphrase
- sasl.oauthbearer.assertion.template.file
- sasl.oauthbearer.client.credentials.client.id
- sasl.oauthbearer.client.credentials.client.secret
- sasl.oauthbearer.header.urlencode
- sasl.oauthbearer.jwt.retriever.class
- sasl.oauthbearer.jwt.validator.class
- sasl.oauthbearer.scope
- sasl.oauthbearer.token.endpoint.url

3. The default implementation of SASL/OAUTHBEARER depends on the jackson-databind library. Since it’s an optional dependency, users have to configure it as a dependency via their build tool.

<a id="security-authentication-using-sasl--token-refresh-for-sasloauthbearer"></a>
<a id="security-authentication-using-sasl--token-refresh-for-sasl-oauthbearer"></a>

#### Token Refresh for SASL/OAUTHBEARER

Kafka periodically refreshes any token before it expires so that the client can continue to make connections to brokers. The parameters that impact how the refresh algorithm operates are specified as part of the producer/consumer/broker configuration and are as follows. See the documentation for these properties elsewhere for details. The default values are usually reasonable, in which case these configuration parameters would not need to be explicitly set.

Producer/Consumer/Broker Configuration Property

`sasl.login.refresh.window.factor`

`sasl.login.refresh.window.jitter`

`sasl.login.refresh.min.period.seconds`

`sasl.login.refresh.min.buffer.seconds`

#### Secure/Production Use of SASL/OAUTHBEARER

Kafka provides built-in JWT retriever implementations for production use: `ClientCredentialsJwtRetriever` for the `client_credentials` grant type (supporting both client secret and client assertion authentication) and `JwtBearerJwtRetriever` for the `jwt-bearer` grant type. These can be configured via `sasl.oauthbearer.jwt.retriever.class` as shown in the examples above. Alternatively, production use cases may provide a custom implementation of `org.apache.kafka.common.security.auth.AuthenticateCallbackHandler` that can handle an instance of `org.apache.kafka.common.security.oauthbearer.OAuthBearerTokenCallback` and declaring it via either the `sasl.login.callback.handler.class` configuration option for a non-broker client or via the `listener.name.sasl_ssl.oauthbearer.sasl.login.callback.handler.class` configuration option for brokers (when SASL/OAUTHBEARER is the inter-broker protocol).

Production use cases will also require writing an implementation of `org.apache.kafka.common.security.auth.AuthenticateCallbackHandler` that can handle an instance of `org.apache.kafka.common.security.oauthbearer.OAuthBearerValidatorCallback` and declaring it via the `listener.name.sasl_ssl.oauthbearer.sasl.server.callback.handler.class` broker configuration option.

<a id="security-authentication-using-sasl--security-considerations-for-sasloauthbearer"></a>
<a id="security-authentication-using-sasl--security-considerations-for-sasl-oauthbearer"></a>

#### Security Considerations for SASL/OAUTHBEARER

- The default implementation of SASL/OAUTHBEARER in Kafka creates and validates [Unsecured JSON Web Tokens](https://tools.ietf.org/html/rfc7515#appendix-A.5). This is suitable only for non-production use.
- OAUTHBEARER should be used in production environments only with TLS-encryption to prevent interception of tokens.
- The default unsecured SASL/OAUTHBEARER implementation may be overridden (and must be overridden in production environments) using custom login and SASL Server callback handlers or the built-in JWT retriever implementations as described above.
- When using client assertion authentication, private keys never leave the client and are not transmitted over the network, unlike client secrets. Use short assertion expiration times (e.g. 300 seconds via `sasl.oauthbearer.assertion.claim.exp.seconds`) and enable JTI inclusion (`sasl.oauthbearer.assertion.claim.jti.include=true`) to protect against replay attacks.
- For more details on OAuth 2 security considerations in general, refer to [RFC 6749, Section 10](https://tools.ietf.org/html/rfc6749#section-10).

<a id="security-authentication-using-sasl--enabling-multiple-sasl-mechanisms-in-a-broker"></a>

### Enabling multiple SASL mechanisms in a broker

1. Specify configuration for the login modules of all enabled mechanisms in the `KafkaServer` section of the JAAS config file. For example:

```
     KafkaServer {
         com.sun.security.auth.module.Krb5LoginModule required
         useKeyTab=true
         storeKey=true
         keyTab="/etc/security/keytabs/kafka_server.keytab"
         principal="kafka/kafka1.hostname.com@EXAMPLE.COM";

         org.apache.kafka.common.security.plain.PlainLoginModule required
         username="admin"
         password="admin-secret"
         user_admin="admin-secret"
         user_alice="alice-secret";
     };
```

2. Enable the SASL mechanisms in server.properties:

```
     sasl.enabled.mechanisms=GSSAPI,PLAIN,SCRAM-SHA-256,SCRAM-SHA-512,OAUTHBEARER
```

3. Specify the SASL security protocol and mechanism for inter-broker communication in server.properties if required:

```
     security.inter.broker.protocol=SASL_PLAINTEXT (or SASL_SSL)
     sasl.mechanism.inter.broker.protocol=GSSAPI (or one of the other enabled mechanisms)
```

4. Follow the mechanism-specific steps in GSSAPI (Kerberos), PLAIN, SCRAM, and non-production/production OAUTHBEARER to configure SASL for the enabled mechanisms.

<a id="security-authentication-using-sasl--modifying-sasl-mechanism-in-a-running-cluster"></a>

### Modifying SASL mechanism in a Running Cluster

SASL mechanism can be modified in a running cluster using the following sequence:

1. Enable new SASL mechanism by adding the mechanism to `sasl.enabled.mechanisms` in server.properties for each broker. Update JAAS config file to include both mechanisms as described here. Incrementally bounce the cluster nodes.
2. Restart clients using the new mechanism.
3. To change the mechanism of inter-broker communication (if this is required), set `sasl.mechanism.inter.broker.protocol` in server.properties to the new mechanism and incrementally bounce the cluster again.
4. To remove old mechanism (if this is required), remove the old mechanism from `sasl.enabled.mechanisms` in server.properties and remove the entries for the old mechanism from JAAS config file. Incrementally bounce the cluster again.

<a id="security-authentication-using-sasl--authentication-using-delegation-tokens"></a>

### Authentication using Delegation Tokens

Delegation token based authentication is a lightweight authentication mechanism to complement existing SASL/SSL methods. Delegation tokens are shared secrets between kafka brokers and clients. Delegation tokens will help processing frameworks to distribute the workload to available workers in a secure environment without the added cost of distributing Kerberos TGT/keytabs or keystores when 2-way SSL is used. See [KIP-48](https://cwiki.apache.org/confluence/x/tfmnAw) for more details.

Under the default implementation of `principal.builder.class`, the owner of delegation token is used as the authenticated `Principal` for configuration of ACLs etc.

Typical steps for delegation token usage are:

1. User authenticates with the Kafka cluster via SASL or SSL, and obtains a delegation token. This can be done using Admin APIs or using `kafka-delegation-tokens.sh` script.
2. User securely passes the delegation token to Kafka clients for authenticating with the Kafka cluster.
3. Token owner/renewer can renew/expire the delegation tokens.

<a id="security-authentication-using-sasl--token-management"></a>

#### Token Management

A secret is used to generate and verify delegation tokens. This is supplied using config option `delegation.token.secret.key`. The same secret key must be configured across all the brokers. The controllers must also be configured with the secret using the same config option. If the secret is not set or set to empty string, delegation token authentication and API operations will fail.

The token details are stored with the other metadata on the controller nodes and delegation tokens are suitable for use when the controllers are on a private network or when all communications between brokers and controllers is encrypted. Currently, this secret is stored as plain text in the server.properties config file. We intend to make these configurable in a future Kafka release.

A token has a current life, and a maximum renewable life. By default, tokens must be renewed once every 24 hours for up to 7 days. These can be configured using `delegation.token.expiry.time.ms` and `delegation.token.max.lifetime.ms` config options.

Tokens can also be cancelled explicitly. If a token is not renewed by the token’s expiration time or if token is beyond the max life time, it will be deleted from all broker caches.

<a id="security-authentication-using-sasl--creating-delegation-tokens"></a>

#### Creating Delegation Tokens

Tokens can be created by using Admin APIs or using `kafka-delegation-tokens.sh` script. Delegation token requests (create/renew/expire/describe) should be issued only on SASL or SSL authenticated channels. Tokens can not be requests if the initial authentication is done through delegation token. A token can be created by the user for that user or others as well by specifying the `--owner-principal` parameter. Owner/Renewers can renew or expire tokens. Owner/renewers can always describe their own tokens. To describe other tokens, a DESCRIBE\_TOKEN permission needs to be added on the User resource representing the owner of the token. `kafka-delegation-tokens.sh` script examples are given below.

Create a delegation token:

```
        $ bin/kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --create   --max-life-time-period -1 --command-config client.properties --renewer-principal User:user1
```

Create a delegation token for a different owner:

```
        $ bin/kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --create   --max-life-time-period -1 --command-config client.properties --renewer-principal User:user1 --owner-principal User:owner1
```

Renew a delegation token:

```
        $ bin/kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --renew    --renew-time-period -1 --command-config client.properties --hmac ABCDEFGHIJK
```

Expire a delegation token:

```
        $ bin/kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --expire   --expiry-time-period -1   --command-config client.properties  --hmac ABCDEFGHIJK
```

Existing tokens can be described using the –describe option:

```
        $ bin/kafka-delegation-tokens.sh --bootstrap-server localhost:9092 --describe --command-config client.properties  --owner-principal User:user1
```

<a id="security-authentication-using-sasl--token-authentication"></a>

#### Token Authentication

Delegation token authentication piggybacks on the current SASL/SCRAM authentication mechanism. We must enable SASL/SCRAM mechanism on Kafka cluster as described in here.

Configuring Kafka Clients:

1. Configure the JAAS configuration property for each client in producer.properties or consumer.properties. The login module describes how the clients like producer and consumer can connect to the Kafka Broker. The following is an example configuration for a client for the token authentication:

```
        sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
            username="tokenID123" \
            password="lAYYSFmLs4bTjf+lTZ1LCHR/ZZFNA==" \
            tokenauth="true";
```

The options `username` and `password` are used by clients to configure the token id and token HMAC. And the option `tokenauth` is used to indicate the server about token authentication. In this example, clients connect to the broker using token id: *tokenID123*. Different clients within a JVM may connect using different tokens by specifying different token details in `sasl.jaas.config`.

JAAS configuration for clients may alternatively be specified as a JVM parameter similar to brokers as described here. Clients use the login section named `KafkaClient`. This option allows only one user for all client connections from a JVM.

<a id="security-authentication-using-sasl--procedure-to-manually-rotate-the-secret"></a>
<a id="security-authentication-using-sasl--procedure-to-manually-rotate-the-secret:"></a>

#### Procedure to manually rotate the secret:

We require a re-deployment when the secret needs to be rotated. During this process, already connected clients will continue to work. But any new connection requests and renew/expire requests with old tokens can fail. Steps are given below.

1. Expire all existing tokens.
2. Rotate the secret by rolling upgrade, and
3. Generate new tokens

We intend to automate this in a future Kafka release.

---

<a id="security-authorization-and-acls"></a>

<a id="security-authorization-and-acls--authorization-and-acls"></a>

# Authorization and ACLs

Authorization and ACLs

Kafka ships with a pluggable authorization framework, which is configured with the `authorizer.class.name` property in the server configuration. Configured implementations must extend `org.apache.kafka.server.authorizer.Authorizer`. Kafka provides a default implementation which store ACLs in the cluster metadata (KRaft metadata log). For KRaft clusters, use the following configuration on all nodes (brokers, controllers, or combined broker/controller nodes):

```
authorizer.class.name=org.apache.kafka.metadata.authorizer.StandardAuthorizer
```

Kafka ACLs are defined in the general format of “Principal {P} is [Allowed|Denied] Operation {O} From Host {H} on any Resource {R} matching ResourcePattern {RP}”. You can read more about the ACL structure in [KIP-11](https://cwiki.apache.org/confluence/x/XIUWAw) and resource patterns in [KIP-290](https://cwiki.apache.org/confluence/x/QpvLB). In order to add, remove, or list ACLs, you can use the Kafka ACL CLI `kafka-acls.sh`.

<a id="security-authorization-and-acls--_behavior-without-acls_"></a>
<a id="security-authorization-and-acls--behavior-without-acls:"></a>

### *Behavior Without ACLs:*

If a resource (R) does not have any ACLs defined, meaning that no ACL matches the resource, Kafka will restrict access to that resource. In this situation, only super users are allowed to access it.

<a id="security-authorization-and-acls--_changing-the-default-behavior_"></a>
<a id="security-authorization-and-acls--changing-the-default-behavior:"></a>

### *Changing the Default Behavior:*

If you prefer that resources without any ACLs be accessible by all users (instead of just super users), you can change the default behavior. To do this, add the following line to your server.properties file:

```
allow.everyone.if.no.acl.found=true
```

With this setting enabled, if a resource does not have any ACLs defined, Kafka will allow access to everyone. If a resource has one or more ACLs defined, those ACL rules will be enforced as usual, regardless of the setting. One can also add super users in server.properties like the following (note that the delimiter is semicolon since SSL user names may contain comma). Default PrincipalType string “User” is case sensitive.

```
super.users=User:Bob;User:Alice
```

<a id="security-authorization-and-acls--kraft-principal-forwarding"></a>

### KRaft Principal Forwarding

In KRaft clusters, admin requests such as `CreateTopics` and `DeleteTopics` are sent to the broker listeners by the client. The broker then forwards the request to the active controller through the first listener configured in `controller.listener.names`. Authorization of these requests is done on the controller node. This is achieved by way of an `Envelope` request which packages both the underlying request from the client as well as the client principal. When the controller receives the forwarded `Envelope` request from the broker, it first authorizes the `Envelope` request using the authenticated broker principal. Then it authorizes the underlying request using the forwarded principal.
All of this implies that Kafka must understand how to serialize and deserialize the client principal. The authentication framework allows for customized principals by overriding the `principal.builder.class` configuration. In order for customized principals to work with KRaft, the configured class must implement `org.apache.kafka.common.security.auth.KafkaPrincipalSerde` so that Kafka knows how to serialize and deserialize the principals. The default implementation `org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalBuilder` uses the Kafka RPC format defined in the source code: `clients/src/main/resources/common/message/DefaultPrincipalData.json`.

<a id="security-authorization-and-acls--customizing-ssl-user-name"></a>

### Customizing SSL User Name

By default, the SSL user name will be of the form “CN=writeuser,OU=Unknown,O=Unknown,L=Unknown,ST=Unknown,C=Unknown”. One can change that by setting `ssl.principal.mapping.rules` to a customized rule in server.properties. This config allows a list of rules for mapping X.500 distinguished name to short name. The rules are evaluated in order and the first rule that matches a distinguished name is used to map it to a short name. Any later rules in the list are ignored.
The format of `ssl.principal.mapping.rules` is a list where each rule starts with “RULE:” and contains an expression as the following formats. Default rule will return string representation of the X.500 certificate distinguished name. If the distinguished name matches the pattern, then the replacement command will be run over the name. This also supports lowercase/uppercase options, to force the translated result to be all lower/uppercase case. This is done by adding a “/L” or “/U’ to the end of the rule.

```
RULE:pattern/replacement/
RULE:pattern/replacement/[LU]
```

Example `ssl.principal.mapping.rules` values are:

```
RULE:^CN=(.*?),OU=ServiceUsers.*$/$1/,
RULE:^CN=(.*?),OU=(.*?),O=(.*?),L=(.*?),ST=(.*?),C=(.*?)$/$1@$2/L,
RULE:^.*[Cc][Nn]=([a-zA-Z0-9.]*).*$/$1/L,
DEFAULT
```

Above rules translate distinguished name “CN=serviceuser,OU=ServiceUsers,O=Unknown,L=Unknown,ST=Unknown,C=Unknown” to “serviceuser” and “CN=adminUser,OU=Admin,O=Unknown,L=Unknown,ST=Unknown,C=Unknown” to “adminuser@admin”. For advanced use cases, one can customize the name by setting a customized PrincipalBuilder in server.properties like the following.

```
principal.builder.class=CustomizedPrincipalBuilderClass
```

<a id="security-authorization-and-acls--customizing-sasl-user-name"></a>

### Customizing SASL User Name

By default, the SASL user name will be the primary part of the Kerberos principal. One can change that by setting `sasl.kerberos.principal.to.local.rules` to a customized rule in server.properties. The format of `sasl.kerberos.principal.to.local.rules` is a list where each rule works in the same way as the auth\_to\_local in [Kerberos configuration file (krb5.conf)](https://web.mit.edu/Kerberos/krb5-latest/doc/admin/conf_files/krb5_conf.html). This also support additional lowercase/uppercase rule, to force the translated result to be all lowercase/uppercase. This is done by adding a “/L” or “/U” to the end of the rule. check below formats for syntax. Each rules starts with RULE: and contains an expression as the following formats. See the kerberos documentation for more details.

```
RULE:[n:string](regexp)s/pattern/replacement/
RULE:[n:string](regexp)s/pattern/replacement/g
RULE:[n:string](regexp)s/pattern/replacement//L
RULE:[n:string](regexp)s/pattern/replacement/g/L
RULE:[n:string](regexp)s/pattern/replacement//U
RULE:[n:string](regexp)s/pattern/replacement/g/U
```

An example of adding a rule to properly translate [user@MYDOMAIN.COM](mailto:user@MYDOMAIN.COM) to user while also keeping the default rule in place is:

```
sasl.kerberos.principal.to.local.rules=RULE:[1:$1@$0](.*@MYDOMAIN.COM)s/@.*//,DEFAULT
```

<a id="security-authorization-and-acls--command-line-interface"></a>

## Command Line Interface

Kafka Authorization management CLI can be found under bin directory with all the other CLIs. The CLI script is called **kafka-acls.sh**. Following lists all the options that the script supports:

<table><tr><th><p>Option</p></th><th><p>Description</p></th><th><p>Default</p></th><th><p>Option type</p></th></tr><tr><td><p>--add</p></td><td><p>Indicates to the script that user is trying to add an acl.</p></td><td></td><td><p>Action</p></td></tr><tr><td><p>--remove</p></td><td><p>Indicates to the script that user is trying to remove an acl.</p></td><td></td><td><p>Action</p></td></tr><tr><td><p>--list</p></td><td><p>Indicates to the script that user is trying to list acls.</p></td><td></td><td><p>Action</p></td></tr><tr><td><p>--bootstrap-server</p></td><td><p>A list of host/port pairs to use for establishing the connection to the Kafka cluster broker. Only one of –bootstrap-server or –bootstrap-controller option must be specified.</p></td><td></td><td><p>Configuration</p></td></tr><tr><td><p>--bootstrap-controller</p></td><td><p>A list of host/port pairs to use for establishing the connection to the Kafka cluster controller. Only one of –bootstrap-server or –bootstrap-controller option must be specified.</p></td><td></td><td><p>Configuration</p></td></tr><tr><td><p>--command-config</p></td><td><p>A property file containing configs to be passed to Admin Client. This option can only be used with –bootstrap-server option.</p></td><td></td><td><p>Configuration</p></td></tr><tr><td><p>--cluster</p></td><td><p>Indicates to the script that the user is trying to interact with acls on the singular cluster resource.</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--topic [topic-name]</p></td><td><p>Indicates to the script that the user is trying to interact with acls on topic resource pattern(s).</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--group [group-name]</p></td><td><p>Indicates to the script that the user is trying to interact with acls on consumer-group resource pattern(s)</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--transactional-id [transactional-id]</p></td><td><p>The transactionalId to which ACLs should be added or removed. A value of * indicates the ACLs should apply to all transactionalIds.</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--delegation-token [delegation-token]</p></td><td><p>Delegation token to which ACLs should be added or removed. A value of * indicates ACL should apply to all tokens.</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--user-principal [user-principal]</p></td><td><p>A user resource to which ACLs should be added or removed. This is currently supported in relation with delegation tokens. A value of * indicates ACL should apply to all users.</p></td><td></td><td><p>ResourcePattern</p></td></tr><tr><td><p>--resource-pattern-type [pattern-type]</p></td><td><p>Indicates to the script the type of resource pattern, (for –add), or resource pattern filter, (for –list and –remove), the user wishes to use. When adding acls, this should be a specific pattern type, e.g. ’literal’ or ‘prefixed’. When listing or removing acls, a specific pattern type filter can be used to list or remove acls from a specific type of resource pattern, or the filter values of ‘any’ or ‘match’ can be used, where ‘any’ will match any pattern type, but will match the resource name exactly, and ‘match’ will perform pattern matching to list or remove all acls that affect the supplied resource(s). WARNING: ‘match’, when used in combination with the ‘–remove’ switch, should be used with care.</p></td><td><p>literal</p></td><td><p>Configuration</p></td></tr><tr><td><p>--allow-principal</p></td><td><p>Principal is in PrincipalType:name format that will be added to ACL with Allow permission. Default PrincipalType string “User” is case sensitive. You can specify multiple –allow-principal in a single command.</p></td><td></td><td><p>Principal</p></td></tr><tr><td><p>--deny-principal</p></td><td><p>Principal is in PrincipalType:name format that will be added to ACL with Deny permission. Default PrincipalType string “User” is case sensitive. You can specify multiple –deny-principal in a single command.</p></td><td></td><td><p>Principal</p></td></tr><tr><td><p>--principal</p></td><td><p>Principal is in PrincipalType:name format that will be used along with –list option. Default PrincipalType string “User” is case sensitive. This will list the ACLs for the specified principal. You can specify multiple –principal in a single command.</p></td><td></td><td><p>Principal</p></td></tr><tr><td><p>--allow-host</p></td><td><p>IP address from which principals listed in –allow-principal will have access.</p></td><td><p>if –allow-principal is specified defaults to * which translates to “all hosts”</p></td><td><p>Host</p></td></tr><tr><td><p>--deny-host</p></td><td><p>IP address from which principals listed in –deny-principal will be denied access.</p></td><td><p>if –deny-principal is specified defaults to * which translates to “all hosts”</p></td><td><p>Host</p></td></tr><tr><td><p>--operation</p></td><td><p>Operation that will be allowed or denied. Valid values are:</p><ul><li>Read</li><li>Write</li><li>Create</li><li>Delete</li><li>Alter</li><li>Describe</li><li>ClusterAction</li><li>DescribeConfigs</li><li>AlterConfigs</li><li>IdempotentWrite</li><li>CreateTokens</li><li>DescribeTokens</li><li>All</li></ul></td><td><p>All</p></td><td><p>Operation</p></td></tr><tr><td><p>--producer</p></td><td><p>Convenience option to add/remove acls for producer role. This will generate acls that allows WRITE, DESCRIBE and CREATE on topic.</p></td><td></td><td><p>Convenience</p></td></tr><tr><td><p>--consumer</p></td><td><p>Convenience option to add/remove acls for consumer role. This will generate acls that allows READ, DESCRIBE on topic and READ on consumer-group.</p></td><td></td><td><p>Convenience</p></td></tr><tr><td><p>--idempotent</p></td><td><p>Enable idempotence for the producer. This should be used in combination with the –producer option. Note that idempotence is enabled automatically if the producer is authorized to a particular transactional-id.</p></td><td></td><td><p>Convenience</p></td></tr><tr><td><p>--force</p></td><td><p>Convenience option to assume yes to all queries and do not prompt.</p></td><td></td><td><p>Convenience</p></td></tr></table>

<a id="security-authorization-and-acls--examples"></a>

## Examples

- **Adding Acls** Suppose you want to add an acl “Principals User:Bob and User:Alice are allowed to perform Operation Read and Write on Topic Test-Topic from IP 198.51.100.0 and IP 198.51.100.1”. You can do that by executing the CLI with following options:

```
$ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Bob --allow-principal User:Alice --allow-host 198.51.100.0 --allow-host 198.51.100.1 --operation Read --operation Write --topic Test-topic
```

By default, all principals that don’t have an explicit acl that allows access for an operation to a resource are denied. In rare cases where an allow acl is defined that allows access to all but some principal we will have to use the –deny-principal and –deny-host option. For example, if we want to allow all users to Read from Test-topic but only deny User:BadBob from IP 198.51.100.3 we can do so using following commands:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:'*' --allow-host '*' --deny-principal User:BadBob --deny-host 198.51.100.3 --operation Read --topic Test-topic
```

Note that `--allow-host` and `--deny-host` only support IP addresses (hostnames are not supported). Above examples add acls to a topic by specifying –topic [topic-name] as the resource pattern option. Similarly user can add acls to cluster by specifying –cluster and to a consumer group by specifying –group [group-name]. You can add acls on any resource of a certain type, e.g. suppose you wanted to add an acl “Principal User:Peter is allowed to produce to any Topic from IP 198.51.200.0” You can do that by using the wildcard resource ‘\*’, e.g. by executing the CLI with following options:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Peter --allow-host 198.51.200.1 --producer --topic '*'
```

You can add acls on prefixed resource patterns, e.g. suppose you want to add an acl “Principal User:Jane is allowed to produce to any Topic whose name starts with ‘Test-’ from any host”. You can do that by executing the CLI with following options:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Jane --producer --topic Test- --resource-pattern-type prefixed
```

Note, –resource-pattern-type defaults to ’literal’, which only affects resources with the exact same name or, in the case of the wildcard resource name ‘\*’, a resource with any name.

- **Removing Acls** Removing acls is pretty much the same. The only difference is instead of –add option users will have to specify –remove option. To remove the acls added by the first example above we can execute the CLI with following options:

```
$ bin/kafka-acls.sh --bootstrap-server localhost:9092 --remove --allow-principal User:Bob --allow-principal User:Alice --allow-host 198.51.100.0 --allow-host 198.51.100.1 --operation Read --operation Write --topic Test-topic
```

If you want to remove the acl added to the prefixed resource pattern above we can execute the CLI with following options:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --remove --allow-principal User:Jane --producer --topic Test- --resource-pattern-type Prefixed
```

- **List Acls** We can list acls for any resource by specifying the –list option with the resource. To list all acls on the literal resource pattern Test-topic, we can execute the CLI with following options:

```
$ bin/kafka-acls.sh --bootstrap-server localhost:9092 --list --topic Test-topic
```

However, this will only return the acls that have been added to this exact resource pattern. Other acls can exist that affect access to the topic, e.g. any acls on the topic wildcard ‘\*’, or any acls on prefixed resource patterns. Acls on the wildcard resource pattern can be queried explicitly:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --list --topic '*'
```

However, it is not necessarily possible to explicitly query for acls on prefixed resource patterns that match Test-topic as the name of such patterns may not be known. We can list *all* acls affecting Test-topic by using ‘–resource-pattern-type match’, e.g.

```
    > bin/kafka-acls.sh --bootstrap-server localhost:9092 --list --topic Test-topic --resource-pattern-type match
```

This will list acls on all matching literal, wildcard and prefixed resource patterns.

- **Adding or removing a principal as producer or consumer** The most common use case for acl management are adding/removing a principal as producer or consumer so we added convenience options to handle these cases. In order to add User:Bob as a producer of Test-topic we can execute the following command:

```
$ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Bob --producer --topic Test-topic
```

Similarly to add Alice as a consumer of Test-topic with consumer group Group-1 we just have to pass –consumer option:

```
    $ bin/kafka-acls.sh --bootstrap-server localhost:9092 --add --allow-principal User:Bob --consumer --topic Test-topic --group Group-1
```

Note that for consumer option we must also specify the consumer group. In order to remove a principal from producer or consumer role we just need to pass –remove option.

<a id="security-authorization-and-acls--authorization-primitives"></a>

## Authorization Primitives

Protocol calls are usually performing some operations on certain resources in Kafka. It is required to know the operations and resources to set up effective protection. In this section we’ll list these operations and resources, then list the combination of these with the protocols to see the valid scenarios.

<a id="security-authorization-and-acls--operations-in-kafka"></a>

### Operations in Kafka

There are a few operation primitives that can be used to build up privileges. These can be matched up with certain resources to allow specific protocol calls for a given user. These are:

- Read
- Write
- Create
- Delete
- Alter
- Describe
- ClusterAction
- DescribeConfigs
- AlterConfigs
- IdempotentWrite
- CreateTokens
- DescribeTokens
- All

<a id="security-authorization-and-acls--resources-in-kafka"></a>

### Resources in Kafka

The operations above can be applied on certain resources which are described below.

- **Topic:** this simply represents a Topic. All protocol calls that are acting on topics (such as reading, writing them) require the corresponding privilege to be added. If there is an authorization error with a topic resource, then a TOPIC\_AUTHORIZATION\_FAILED (error code: 29) will be returned.
- **Group:** this represents the consumer groups in the brokers. All protocol calls that are working with consumer groups, like joining a group must have privileges with the group in subject. If the privilege is not given then a GROUP\_AUTHORIZATION\_FAILED (error code: 30) will be returned in the protocol response.
- **Cluster:** this resource represents the cluster. Operations that are affecting the whole cluster, like controlled shutdown are protected by privileges on the Cluster resource. If there is an authorization problem on a cluster resource, then a CLUSTER\_AUTHORIZATION\_FAILED (error code: 31) will be returned.
- **TransactionalId:** this resource represents actions related to transactions, such as committing. If any error occurs, then a TRANSACTIONAL\_ID\_AUTHORIZATION\_FAILED (error code: 53) will be returned by brokers.
- **DelegationToken:** this represents the delegation tokens in the cluster. Actions, such as describing delegation tokens could be protected by a privilege on the DelegationToken resource. Since these objects have a little special behavior in Kafka it is recommended to read [KIP-48](https://cwiki.apache.org/confluence/x/tfmnAw) and the related upstream documentation at Authentication using Delegation Tokens.
- **User:** CreateToken and DescribeToken operations can be granted to User resources to allow creating and describing tokens for other users. More info can be found in [KIP-373](https://cwiki.apache.org/confluence/x/cwOQBQ).

<a id="security-authorization-and-acls--operations-and-resources-on-protocols"></a>

### Operations and Resources on Protocols

In the below table we’ll list the valid operations on resources that are executed by the Kafka API protocols.

| Protocol (API key) | Operation | Resource | Note |
| --- | --- | --- | --- |
| PRODUCE (0) | Write | TransactionalId | A transactional producer which has its transactional.id set requires this privilege. |
| PRODUCE (0) | IdempotentWrite | Cluster | An idempotent produce action requires this privilege. |
| PRODUCE (0) | Write | Topic | This applies to a normal produce action. |
| FETCH (1) | ClusterAction | Cluster | A follower must have ClusterAction on the Cluster resource in order to fetch partition data. |
| FETCH (1) | Read | Topic | Regular Kafka consumers need READ permission on each partition they are fetching. |
| LIST\_OFFSETS (2) | Describe | Topic |  |
| METADATA (3) | Describe | Topic |  |
| METADATA (3) | Create | Cluster | If topic auto-creation is enabled, then the broker-side API will check for the existence of a Cluster level privilege. If it’s found then it’ll allow creating the topic, otherwise it’ll iterate through the Topic level privileges (see the next one). |
| METADATA (3) | Create | Topic | This authorizes auto topic creation if enabled but the given user doesn’t have a cluster level permission (above). |
| LEADER\_AND\_ISR (4) | ClusterAction | Cluster |  |
| STOP\_REPLICA (5) | ClusterAction | Cluster |  |
| UPDATE\_METADATA (6) | ClusterAction | Cluster |  |
| CONTROLLED\_SHUTDOWN (7) | ClusterAction | Cluster |  |
| OFFSET\_COMMIT (8) | Read | Group | An offset can only be committed if it’s authorized to the given group and the topic too (see below). Group access is checked first, then Topic access. |
| OFFSET\_COMMIT (8) | Read | Topic | Since offset commit is part of the consuming process, it needs privileges for the read action. |
| OFFSET\_FETCH (9) | Describe | Group | Similarly to OFFSET\_COMMIT, the application must have privileges on group and topic level too to be able to fetch. However in this case it requires describe access instead of read. Group access is checked first, then Topic access. |
| OFFSET\_FETCH (9) | Describe | Topic |  |
| FIND\_COORDINATOR (10) | Describe | Group | The FIND\_COORDINATOR request can be of “Group” type in which case it is looking for consumergroup coordinators. This privilege would represent the Group mode. |
| FIND\_COORDINATOR (10) | Describe | TransactionalId | This applies only on transactional producers and checked when a producer tries to find the transaction coordinator. |
| JOIN\_GROUP (11) | Read | Group |  |
| HEARTBEAT (12) | Read | Group |  |
| LEAVE\_GROUP (13) | Read | Group |  |
| SYNC\_GROUP (14) | Read | Group |  |
| DESCRIBE\_GROUPS (15) | Describe | Group |  |
| LIST\_GROUPS (16) | Describe | Cluster | When the broker checks to authorize a list\_groups request it first checks for this cluster level authorization. If none found then it proceeds to check the groups individually. This operation doesn’t return CLUSTER\_AUTHORIZATION\_FAILED. |
| LIST\_GROUPS (16) | Describe | Group | If none of the groups are authorized, then just an empty response will be sent back instead of an error. This operation doesn’t return CLUSTER\_AUTHORIZATION\_FAILED. This is applicable from the 2.1 release. |
| SASL\_HANDSHAKE (17) |  |  | The SASL handshake is part of the authentication process and therefore it’s not possible to apply any kind of authorization here. |
| API\_VERSIONS (18) |  |  | The API\_VERSIONS request is part of the Kafka protocol handshake and happens on connection and before any authentication. Therefore it’s not possible to control this with authorization. |
| CREATE\_TOPICS (19) | Create | Cluster | If there is no cluster level authorization then it won’t return CLUSTER\_AUTHORIZATION\_FAILED but fall back to use topic level, which is just below. That’ll throw error if there is a problem. |
| CREATE\_TOPICS (19) | Create | Topic | This is applicable from the 2.0 release. |
| DELETE\_TOPICS (20) | Delete | Topic |  |
| DELETE\_RECORDS (21) | Delete | Topic |  |
| INIT\_PRODUCER\_ID (22) | Write | TransactionalId |  |
| INIT\_PRODUCER\_ID (22) | IdempotentWrite | Cluster |  |
| OFFSET\_FOR\_LEADER\_EPOCH (23) | ClusterAction | Cluster | If there is no cluster level privilege for this operation, then it’ll check for topic level one. |
| OFFSET\_FOR\_LEADER\_EPOCH (23) | Describe | Topic | This is applicable from the 2.1 release. |
| ADD\_PARTITIONS\_TO\_TXN (24) | Write | TransactionalId | This API is only applicable to transactional requests. It first checks for the Write action on the TransactionalId resource, then it checks the Topic in subject (below). |
| ADD\_PARTITIONS\_TO\_TXN (24) | Write | Topic |  |
| ADD\_OFFSETS\_TO\_TXN (25) | Write | TransactionalId | Similarly to ADD\_PARTITIONS\_TO\_TXN this is only applicable to transactional requests. It first checks for Write action on the TransactionalId resource, then it checks whether it can Read on the given group (below). |
| ADD\_OFFSETS\_TO\_TXN (25) | Read | Group |  |
| END\_TXN (26) | Write | TransactionalId |  |
| WRITE\_TXN\_MARKERS (27) | Alter | Cluster |  |
| WRITE\_TXN\_MARKERS (27) | ClusterAction | Cluster |  |
| TXN\_OFFSET\_COMMIT (28) | Write | TransactionalId |  |
| TXN\_OFFSET\_COMMIT (28) | Read | Group |  |
| TXN\_OFFSET\_COMMIT (28) | Read | Topic |  |
| DESCRIBE\_ACLS (29) | Describe | Cluster |  |
| CREATE\_ACLS (30) | Alter | Cluster |  |
| DELETE\_ACLS (31) | Alter | Cluster |  |
| DESCRIBE\_CONFIGS (32) | DescribeConfigs | Cluster | If broker configs are requested, then the broker will check cluster level privileges. |
| DESCRIBE\_CONFIGS (32) | DescribeConfigs | Topic | If topic configs are requested, then the broker will check topic level privileges. |
| ALTER\_CONFIGS (33) | AlterConfigs | Cluster | If broker configs are altered, then the broker will check cluster level privileges. |
| ALTER\_CONFIGS (33) | AlterConfigs | Topic | If topic configs are altered, then the broker will check topic level privileges. |
| ALTER\_REPLICA\_LOG\_DIRS (34) | Alter | Cluster |  |
| DESCRIBE\_LOG\_DIRS (35) | Describe | Cluster | An empty response will be returned on authorization failure. |
| SASL\_AUTHENTICATE (36) |  |  | SASL\_AUTHENTICATE is part of the authentication process and therefore it’s not possible to apply any kind of authorization here. |
| CREATE\_PARTITIONS (37) | Alter | Topic |  |
| CREATE\_DELEGATION\_TOKEN (38) |  |  | Creating delegation tokens has special rules, for this please see the Authentication using Delegation Tokens section. |
| CREATE\_DELEGATION\_TOKEN (38) | CreateTokens | User | Allows creating delegation tokens for the User resource. |
| RENEW\_DELEGATION\_TOKEN (39) |  |  | Renewing delegation tokens has special rules, for this please see the Authentication using Delegation Tokens section. |
| EXPIRE\_DELEGATION\_TOKEN (40) |  |  | Expiring delegation tokens has special rules, for this please see the Authentication using Delegation Tokens section. |
| DESCRIBE\_DELEGATION\_TOKEN (41) | Describe | DelegationToken | Describing delegation tokens has special rules, for this please see the Authentication using Delegation Tokens section. |
| DESCRIBE\_DELEGATION\_TOKEN (41) | DescribeTokens | User | Allows describing delegation tokens of the User resource. |
| DELETE\_GROUPS (42) | Delete | Group |  |
| ELECT\_PREFERRED\_LEADERS (43) | ClusterAction | Cluster |  |
| INCREMENTAL\_ALTER\_CONFIGS (44) | AlterConfigs | Cluster | If broker configs are altered, then the broker will check cluster level privileges. |
| INCREMENTAL\_ALTER\_CONFIGS (44) | AlterConfigs | Topic | If topic configs are altered, then the broker will check topic level privileges. |
| ALTER\_PARTITION\_REASSIGNMENTS (45) | Alter | Cluster |  |
| LIST\_PARTITION\_REASSIGNMENTS (46) | Describe | Cluster |  |
| OFFSET\_DELETE (47) | Delete | Group |  |
| OFFSET\_DELETE (47) | Read | Topic |  |
| DESCRIBE\_CLIENT\_QUOTAS (48) | DescribeConfigs | Cluster |  |
| ALTER\_CLIENT\_QUOTAS (49) | AlterConfigs | Cluster |  |
| DESCRIBE\_USER\_SCRAM\_CREDENTIALS (50) | Describe | Cluster |  |
| ALTER\_USER\_SCRAM\_CREDENTIALS (51) | Alter | Cluster |  |
| VOTE (52) | ClusterAction | Cluster |  |
| BEGIN\_QUORUM\_EPOCH (53) | ClusterAction | Cluster |  |
| END\_QUORUM\_EPOCH (54) | ClusterAction | Cluster |  |
| DESCRIBE\_QUORUM (55) | Describe | Cluster |  |
| ALTER\_PARTITION (56) | ClusterAction | Cluster |  |
| UPDATE\_FEATURES (57) | Alter | Cluster |  |
| ENVELOPE (58) | ClusterAction | Cluster |  |
| FETCH\_SNAPSHOT (59) | ClusterAction | Cluster |  |
| DESCRIBE\_CLUSTER (60) | Describe | Cluster |  |
| DESCRIBE\_PRODUCERS (61) | Read | Topic |  |
| BROKER\_REGISTRATION (62) | ClusterAction | Cluster |  |
| BROKER\_HEARTBEAT (63) | ClusterAction | Cluster |  |
| UNREGISTER\_BROKER (64) | Alter | Cluster |  |
| DESCRIBE\_TRANSACTIONS (65) | Describe | TransactionalId |  |
| LIST\_TRANSACTIONS (66) | Describe | TransactionalId |  |
| ALLOCATE\_PRODUCER\_IDS (67) | ClusterAction | Cluster |  |
| CONSUMER\_GROUP\_HEARTBEAT (68) | Read | Group |  |
| CONSUMER\_GROUP\_DESCRIBE (69) | Read | Group |  |
| CONTROLLER\_REGISTRATION (70) | ClusterAction | Cluster |  |
| GET\_TELEMETRY\_SUBSCRIPTIONS (71) |  |  | No authorization check is performed for this request. |
| PUSH\_TELEMETRY (72) |  |  | No authorization check is performed for this request. |
| ASSIGN\_REPLICAS\_TO\_DIRS (73) | ClusterAction | Cluster |  |
| LIST\_CONFIG\_RESOURCES (74) | DescribeConfigs | Cluster |  |
| DESCRIBE\_TOPIC\_PARTITIONS (75) | Describe | Topic |  |
| SHARE\_GROUP\_HEARTBEAT (76) | Read | Group |  |
| SHARE\_GROUP\_DESCRIBE (77) | Describe | Group |  |
| SHARE\_FETCH (78) | Read | Group |  |
| SHARE\_FETCH (78) | Read | Topic |  |
| SHARE\_ACKNOWLEDGE (79) | Read | Group |  |
| SHARE\_ACKNOWLEDGE (79) | Read | Topic |  |
| INITIALIZE\_SHARE\_GROUP\_STATE (83) | ClusterAction | Cluster |  |
| READ\_SHARE\_GROUP\_STATE (84) | ClusterAction | Cluster |  |
| WRITE\_SHARE\_GROUP\_STATE (85) | ClusterAction | Cluster |  |
| DELETE\_SHARE\_GROUP\_STATE (86) | ClusterAction | Cluster |  |
| READ\_SHARE\_GROUP\_STATE\_SUMMARY (87) | ClusterAction | Cluster |  |
| STREAMS\_GROUP\_HEARTBEAT (88) | Read | Group |  |
| STREAMS\_GROUP\_HEARTBEAT (88) | Describe | Topic | Required for all source topics and internal topics used in the topology of the group. |
| STREAMS\_GROUP\_HEARTBEAT (88) | Create | Topic | Required for all internal topics, for the broker to automatically create internal topics. Not required if internal topics exist. |
| STREAMS\_GROUP\_DESCRIBE (89) | Describe | Group |  |
| STREAMS\_GROUP\_DESCRIBE (89) | Describe | Topic | Required for all source topics and internal topics used in the topology of the group. |
| DESCRIBE\_SHARE\_GROUP\_OFFSETS (90) | Describe | Group | To describe the offset information for a partition in a share group, the application must have privileges on the group and the topic. Group access is checked first, then topic access. |
| DESCRIBE\_SHARE\_GROUP\_OFFSETS (90) | Describe | Topic |  |
| ALTER\_SHARE\_GROUP\_OFFSETS (91) | Read | Group | To alter the offset information for a partition in a share group, the application must have privileges on the group and the topic. Group access is checked first, then topic access. |
| ALTER\_SHARE\_GROUP\_OFFSETS (91) | Read | Topic |  |
| DELETE\_SHARE\_GROUP\_OFFSETS (92) | Delete | Group | To delete the offset information for a topic in a share group, the application must have privileges on the group and the topic. Group access is checked first, then topic access. |
| DELETE\_SHARE\_GROUP\_OFFSETS (92) | Read | Topic |  |

---

<a id="security-incorporating-security-features-in-a-running-cluster"></a>

<a id="security-incorporating-security-features-in-a-running-cluster--incorporating-security-features-in-a-running-cluster"></a>

# Incorporating Security Features in a Running Cluster

Incorporating Security Features in a Running Cluster

You can secure a running cluster via one or more of the supported protocols discussed previously. This is done in phases:

- Incrementally bounce the cluster nodes to open additional secured port(s).
- Restart clients using the secured rather than PLAINTEXT port (assuming you are securing the client-broker connection).
- Incrementally bounce the cluster again to enable broker-to-broker security (if this is required)
- A final incremental bounce to close the PLAINTEXT port.

The specific steps for configuring SSL and SASL are described in sections 7.3 and 7.4. Follow these steps to enable security for your desired protocol(s).

The security implementation lets you configure different protocols for both broker-client and broker-broker communication. These must be enabled in separate bounces. A PLAINTEXT port must be left open throughout so brokers and/or clients can continue to communicate.

When performing an incremental bounce stop the brokers cleanly via a SIGTERM. It’s also good practice to wait for restarted replicas to return to the ISR list before moving onto the next node.

As an example, say we wish to encrypt both broker-client and broker-broker communication with SSL. In the first incremental bounce, an SSL port is opened on each node:

```
listeners=PLAINTEXT://broker1:9091,SSL://broker1:9092
```

We then restart the clients, changing their config to point at the newly opened, secured port:

```
bootstrap.servers = [broker1:9092,...]
security.protocol = SSL
...etc
```

In the second incremental server bounce we instruct Kafka to use SSL as the broker-broker protocol (which will use the same SSL port):

```
listeners=PLAINTEXT://broker1:9091,SSL://broker1:9092
security.inter.broker.protocol=SSL
```

In the final bounce we secure the cluster by closing the PLAINTEXT port:

```
listeners=SSL://broker1:9092
security.inter.broker.protocol=SSL
```

Alternatively we might choose to open multiple ports so that different protocols can be used for broker-broker and broker-client communication. Say we wished to use SSL encryption throughout (i.e. for broker-broker and broker-client communication) but we’d like to add SASL authentication to the broker-client connection also. We would achieve this by opening two additional ports during the first bounce:

```
listeners=PLAINTEXT://broker1:9091,SSL://broker1:9092,SASL_SSL://broker1:9093
```

We would then restart the clients, changing their config to point at the newly opened, SASL & SSL secured port:

```
bootstrap.servers = [broker1:9093,...]
security.protocol = SASL_SSL
...etc
```

The second server bounce would switch the cluster to use encrypted broker-broker communication via the SSL port we previously opened on port 9092:

```
listeners=PLAINTEXT://broker1:9091,SSL://broker1:9092,SASL_SSL://broker1:9093
security.inter.broker.protocol=SSL
```

The final bounce secures the cluster by closing the PLAINTEXT port.

```
listeners=SSL://broker1:9092,SASL_SSL://broker1:9093
security.inter.broker.protocol=SSL
```

---

<a id="kafka-connect"></a>

<a id="kafka-connect--kafka-connect"></a>

# Kafka Connect

---

<a id="kafka-connect--overview"></a>

##### [Overview](#kafka-connect-overview)

Overview

<a id="kafka-connect--user-guide"></a>

##### [User Guide](#kafka-connect-user-guide)

User Guide

<a id="kafka-connect--connector-development-guide"></a>

##### [Connector Development Guide](#kafka-connect-connector-development-guide)

Connector Development Guide

<a id="kafka-connect--administration"></a>

##### [Administration](#kafka-connect-administration)

Administration

---

<a id="kafka-connect-overview"></a>

<a id="kafka-connect-overview--overview"></a>

# Overview

Overview

Kafka Connect is a tool for scalably and reliably streaming data between Apache Kafka and other systems. It makes it simple to quickly define *connectors* that move large collections of data into and out of Kafka. Kafka Connect can ingest entire databases or collect metrics from all your application servers into Kafka topics, making the data available for stream processing with low latency. An export job can deliver data from Kafka topics into secondary storage and query systems or into batch systems for offline analysis.

Kafka Connect features include:

- **A common framework for Kafka connectors** - Kafka Connect standardizes integration of other data systems with Kafka, simplifying connector development, deployment, and management
- **Distributed and standalone modes** - scale up to a large, centrally managed service supporting an entire organization or scale down to development, testing, and small production deployments
- **REST interface** - submit and manage connectors to your Kafka Connect cluster via an easy to use REST API
- **Automatic offset management** - with just a little information from connectors, Kafka Connect can manage the offset commit process automatically so connector developers do not need to worry about this error prone part of connector development
- **Distributed and scalable by default** - Kafka Connect builds on the existing group management protocol. More workers can be added to scale up a Kafka Connect cluster.
- **Streaming/batch integration** - leveraging Kafka’s existing capabilities, Kafka Connect is an ideal solution for bridging streaming and batch data systems

---

<a id="kafka-connect-user-guide"></a>

<a id="kafka-connect-user-guide--user-guide"></a>

# User Guide

User Guide

The [quickstart](https://kafka.apache.org/43/kafka-connect/getting-started/quickstart) provides a brief example of how to run a standalone version of Kafka Connect. This section describes how to configure, run, and manage Kafka Connect in more detail.

<a id="kafka-connect-user-guide--running-kafka-connect"></a>

## Running Kafka Connect

Kafka Connect currently supports two modes of execution: standalone (single process) and distributed.

In standalone mode all work is performed in a single process. This configuration is simpler to setup and get started with and may be useful in situations where only one worker makes sense (e.g. collecting log files), but it does not benefit from some of the features of Kafka Connect such as fault tolerance. You can start a standalone process with the following command:

```bash
$ bin/connect-standalone.sh config/connect-standalone.properties [connector1.properties connector2.json …]
```

The first parameter is the configuration for the worker. This includes settings such as the Kafka connection parameters, serialization format, and how frequently to commit offsets. The provided example should work well with a local cluster running with the default configuration provided by `config/server.properties`. It will require tweaking to use with a different configuration or production deployment. All workers (both standalone and distributed) require a few configs:

- `bootstrap.servers` - List of Kafka servers used to bootstrap connections to Kafka
- `key.converter` - Converter class used to convert between Kafka Connect format and the serialized form that is written to Kafka. This controls the format of the keys in messages written to or read from Kafka, and since this is independent of connectors it allows any connector to work with any serialization format. Examples of common formats include JSON and Avro.
- `value.converter` - Converter class used to convert between Kafka Connect format and the serialized form that is written to Kafka. This controls the format of the values in messages written to or read from Kafka, and since this is independent of connectors it allows any connector to work with any serialization format. Examples of common formats include JSON and Avro.
- `plugin.path` (default `null`) - a list of paths that contain Connect plugins (connectors, converters, transformations). Before running quick starts, users must add the absolute path that contains the example FileStreamSourceConnector and FileStreamSinkConnector packaged in `connect-file-4.3.1.jar`, because these connectors are not included by default to the `CLASSPATH` or the `plugin.path` of the Connect worker (see plugin.path property for examples).

The important configuration options specific to standalone mode are:

- `offset.storage.file.filename` - File to store source connector offsets

The parameters that are configured here are intended for producers and consumers used by Kafka Connect to access the configuration, offset and status topics. For configuration of the producers used by Kafka source tasks and the consumers used by Kafka sink tasks, the same parameters can be used but need to be prefixed with `producer.` and `consumer.` respectively. The only Kafka client parameter that is inherited without a prefix from the worker configuration is `bootstrap.servers`, which in most cases will be sufficient, since the same cluster is often used for all purposes. A notable exception is a secured cluster, which requires extra parameters to allow connections. These parameters will need to be set up to three times in the worker configuration, once for management access, once for Kafka sources and once for Kafka sinks.

Client configuration overrides can be configured individually per connector by using the prefixes `producer.override.` and `consumer.override.` for Kafka sources or Kafka sinks respectively. These overrides are included with the rest of the connector’s configuration properties.

The remaining parameters are connector configuration files. Each file may either be a Java Properties file or a JSON file containing an object with the same structure as the request body of either the `POST /connectors` endpoint or the `PUT /connectors/{name}/config` endpoint (see the [OpenAPI documentation](assets/files/connect-rest_bb879b8e08035384.yaml)). You may include as many as you want, but all will execute within the same process (on different threads). You can also choose not to specify any connector configuration files on the command line, and instead use the REST API to create connectors at runtime after your standalone worker starts.

Distributed mode handles automatic balancing of work, allows you to scale up (or down) dynamically, and offers fault tolerance both in the active tasks and for configuration and offset commit data. Execution is very similar to standalone mode:

```bash
$ bin/connect-distributed.sh config/connect-distributed.properties
```

The difference is in the class which is started and the configuration parameters which change how the Kafka Connect process decides where to store configurations, how to assign work, and where to store offsets and task statues. In the distributed mode, Kafka Connect stores the offsets, configs and task statuses in Kafka topics. It is recommended to manually create the topics for offset, configs and statuses in order to achieve the desired the number of partitions and replication factors. If the topics are not yet created when starting Kafka Connect, the topics will be auto created with default number of partitions and replication factor, which may not be best suited for its usage.

In particular, the following configuration parameters, in addition to the common settings mentioned above, are critical to set before starting your cluster:

- `group.id` - Unique name for the cluster, used in forming the Connect cluster group; note that this **must not conflict** with consumer group IDs
- `config.storage.topic` - Name for the topic to use for storing connector and task configurations; this topic should have a single partition, be replicated, and be configured for compaction
- `offset.storage.topic` - Name for the topic to use for storing offsets; this topic should have many partitions, be replicated, and be configured for compaction
- `status.storage.topic` - Name for the topic to use for storing statuses; this topic can have multiple partitions, be replicated, and be configured for compaction

Note that in distributed mode the connector configurations are not passed on the command line. Instead, use the REST API described below to create, modify, and destroy connectors.

<a id="kafka-connect-user-guide--configuring-connectors"></a>

## Configuring Connectors

Connector configurations are simple key-value mappings. In both standalone and distributed mode, they are included in the JSON payload for the REST request that creates (or modifies) the connector. In standalone mode these can also be defined in a properties file and passed to the Connect process on the command line.

Most configurations are connector dependent, so they can’t be outlined here. However, there are a few common options:

- `name` - Unique name for the connector. Attempting to register again with the same name will fail.
- `connector.class` - The Java class for the connector
- `tasks.max` - The maximum number of tasks that should be created for this connector. The connector may create fewer tasks if it cannot achieve this level of parallelism.
- `key.converter` - (optional) Override the default key converter set by the worker.
- `value.converter` - (optional) Override the default value converter set by the worker.

The `connector.class` config supports several formats: the full name or alias of the class for this connector. If the connector is org.apache.kafka.connect.file.FileStreamSinkConnector, you can either specify this full name or use FileStreamSink or FileStreamSinkConnector to make the configuration a bit shorter.

Sink connectors also have a few additional options to control their input. Each sink connector must set one of the following:

- `topics` - A comma-separated list of topics to use as input for this connector
- `topics.regex` - A Java regular expression of topics to use as input for this connector

For any other options, you should consult the documentation for the connector.

<a id="kafka-connect-user-guide--transformations"></a>

## Transformations

Connectors can be configured with transformations to make lightweight message-at-a-time modifications. They can be convenient for data massaging and event routing.

A transformation chain can be specified in the connector configuration.

- `transforms` - List of aliases for the transformation, specifying the order in which the transformations will be applied.
- `transforms.$alias.type` - Fully qualified class name for the transformation.
- `transforms.$alias.$transformationSpecificConfig` Configuration properties for the transformation

For example, lets take the built-in file source connector and use a transformation to add a static field.

Throughout the example we’ll use schemaless JSON data format. To use schemaless format, we changed the following two lines in `connect-standalone.properties` from true to false:

```properties
key.converter.schemas.enable
value.converter.schemas.enable
```

The file source connector reads each line as a String. We will wrap each line in a Map and then add a second field to identify the origin of the event. To do this, we use two transformations:

- **HoistField** to place the input line inside a Map
- **InsertField** to add the static field. In this example we’ll indicate that the record came from a file connector

After adding the transformations, `connect-file-source.properties` file looks as following:

```properties
name=local-file-source
connector.class=FileStreamSource
tasks.max=1
file=test.txt
topic=connect-test
transforms=MakeMap, InsertSource
transforms.MakeMap.type=org.apache.kafka.connect.transforms.HoistField$Value
transforms.MakeMap.field=line
transforms.InsertSource.type=org.apache.kafka.connect.transforms.InsertField$Value
transforms.InsertSource.static.field=data_source
transforms.InsertSource.static.value=test-file-source
```

All the lines starting with `transforms` were added for the transformations. You can see the two transformations we created: “InsertSource” and “MakeMap” are aliases that we chose to give the transformations. The transformation types are based on the list of built-in transformations you can see below. Each transformation type has additional configuration: HoistField requires a configuration called “field”, which is the name of the field in the map that will include the original String from the file. InsertField transformation lets us specify the field name and the value that we are adding.

When we ran the file source connector on my sample file without the transformations, and then read them using `kafka-console-consumer.sh`, the results were:

```text
"foo"
"bar"
"hello world"
```

We then create a new file connector, this time after adding the transformations to the configuration file. This time, the results will be:

```json
{"line":"foo","data_source":"test-file-source"}
{"line":"bar","data_source":"test-file-source"}
{"line":"hello world","data_source":"test-file-source"}
```

You can see that the lines we’ve read are now part of a JSON map, and there is an extra field with the static value we specified. This is just one example of what you can do with transformations.

<a id="kafka-connect-user-guide--included-transformations"></a>

### Included transformations

Several widely-applicable data and routing transformations are included with Kafka Connect:

- Cast - Cast fields or the entire key or value to a specific type
- DropHeaders - Remove headers by name
- ExtractField - Extract a specific field from Struct and Map and include only this field in results
- Filter - Removes messages from all further processing. This is used with a predicate to selectively filter certain messages
- Flatten - Flatten a nested data structure
- HeaderFrom - Copy or move fields in the key or value to the record headers
- HoistField - Wrap the entire event as a single field inside a Struct or a Map
- InsertField - Add a field using either static data or record metadata
- InsertHeader - Add a header using static data
- MaskField - Replace field with valid null value for the type (0, empty string, etc) or custom replacement (non-empty string or numeric value only)
- RegexRouter - modify the topic of a record based on original topic, replacement string and a regular expression
- ReplaceField - Filter or rename fields
- SetSchemaMetadata - modify the schema name or version
- TimestampConverter - Convert timestamps between different formats
- TimestampRouter - Modify the topic of a record based on original topic and timestamp. Useful when using a sink that needs to write to different tables or indexes based on timestamps
- ValueToKey - Replace the record key with a new key formed from a subset of fields in the record value

Details on how to configure each transformation are listed below:

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.cast"></a>

##### [org.apache.kafka.connect.transforms.Cast](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.cast)

Cast fields or the entire key or value to a specific type, e.g. to force an integer field to a smaller width. Cast from integers, floats, boolean and string to any other type, and cast binary to string (base64 encoded).

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.Cast$Key`) or value (`org.apache.kafka.connect.transforms.Cast$Value`).

-

<a id="kafka-connect-user-guide--spec"></a>

  ###### [spec](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.cast_spec)

  List of fields and the type to cast them to of the form field1:type,field2:type to cast fields of Maps or Structs. A single type to cast the entire value. Valid types are int8, int16, int32, int64, float32, float64, boolean, and string. Note that binary fields can only be cast to string.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: | list of colon-delimited pairs, e.g. `foo:bar,abc:xyz` |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.cast_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.dropheaders"></a>

##### [org.apache.kafka.connect.transforms.DropHeaders](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.dropheaders)

Removes one or more headers from each record.

-

<a id="kafka-connect-user-guide--headers"></a>

  ###### [headers](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.dropheaders_headers)

  The name of the headers to be removed.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.extractfield"></a>

##### [org.apache.kafka.connect.transforms.ExtractField](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.extractfield)

Extract the specified field from a Struct when schema present, or a Map in the case of schemaless data. Any null values are passed through unmodified.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.ExtractField$Key`) or value (`org.apache.kafka.connect.transforms.ExtractField$Value`).

-

<a id="kafka-connect-user-guide--field"></a>

  ###### [field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.extractfield_field)

  Field name to extract.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--field.syntax.version"></a>

  ###### [field.syntax.version](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.extractfield_field.syntax.version)

  Defines the version of the syntax to access fields. If set to `V1`, then the field paths are limited to access the elements at the root level of the struct or map. If set to `V2`, the syntax will support accessing nested elements. To access nested elements, dotted notation is used. If dots are already included in the field name, then backtick pairs can be used to wrap field names containing dots. E.g. to access the subfield `baz` from a field named "foo.bar" in a struct/map the following format can be used to access its elements: "`foo.bar`.baz".

| Type: | string |
| --- | --- |
| Default: | V1 |
| Valid Values: | (case insensitive) [V1, V2] |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default-2"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.extractfield_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.filter"></a>

##### [org.apache.kafka.connect.transforms.Filter](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.filter)

Drops all records, filtering them from subsequent transformations in the chain. This is intended to be used conditionally to filter out records matching (or not matching) a particular Predicate.

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.flatten"></a>

##### [org.apache.kafka.connect.transforms.Flatten](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.flatten)

Flatten a nested data structure, generating names for each field by concatenating the field names at each level with a configurable delimiter character. Applies to Struct when schema present, or a Map in the case of schemaless data. Array fields and their contents are not modified. The default delimiter is '.'.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.Flatten$Key`) or value (`org.apache.kafka.connect.transforms.Flatten$Value`).

-

<a id="kafka-connect-user-guide--delimiter"></a>

  ###### [delimiter](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.flatten_delimiter)

  Delimiter to insert between field names from the input record when generating field names for the output record

| Type: | string |
| --- | --- |
| Default: | . |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom"></a>

##### [org.apache.kafka.connect.transforms.HeaderFrom](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom)

Moves or copies fields in the key/value of a record into that record's headers. Corresponding elements of `fields` and `headers` together identify a field and the header it should be moved or copied to. Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.HeaderFrom$Key`) or value (`org.apache.kafka.connect.transforms.HeaderFrom$Value`).

-

<a id="kafka-connect-user-guide--fields"></a>

  ###### [fields](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom_fields)

  Field names in the record whose values are to be copied or moved to headers.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: | non-empty list |
| Importance: | high |

-

<a id="kafka-connect-user-guide--headers-2"></a>

  ###### [headers](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom_headers)

  Header names, in the same order as the field names listed in the fields configuration property.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: | non-empty list |
| Importance: | high |

-

<a id="kafka-connect-user-guide--operation"></a>

  ###### [operation](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom_operation)

  Either `move` if the fields are to be moved to the headers (removed from the key/value), or `copy` if the fields are to be copied to the headers (retained in the key/value).

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | [move, copy] |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default-3"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.headerfrom_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.hoistfield"></a>

##### [org.apache.kafka.connect.transforms.HoistField](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.hoistfield)

Wrap data using the specified field name in a Struct when schema present, or a Map in the case of schemaless data.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.HoistField$Key`) or value (`org.apache.kafka.connect.transforms.HoistField$Value`).

-

<a id="kafka-connect-user-guide--field-2"></a>

  ###### [field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.hoistfield_field)

  Field name for the single field that will be created in the resulting Struct or Map.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield"></a>

##### [org.apache.kafka.connect.transforms.InsertField](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield)

Insert field(s) using attributes from the record metadata or a configured static value.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.InsertField$Key`) or value (`org.apache.kafka.connect.transforms.InsertField$Value`).

-

<a id="kafka-connect-user-guide--offset.field"></a>

  ###### [offset.field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_offset.field)

  Field name for Kafka offset - only applicable to sink connectors.
  Suffix with `!` to make this a required field, or `?` to keep it optional (the default).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--partition.field"></a>

  ###### [partition.field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_partition.field)

  Field name for Kafka partition. Suffix with `!` to make this a required field, or `?` to keep it optional (the default).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--replace.null.with.default-4"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--static.field"></a>

  ###### [static.field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_static.field)

  Field name for static data field. Suffix with `!` to make this a required field, or `?` to keep it optional (the default).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--static.value"></a>

  ###### [static.value](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_static.value)

  Static field value, if field name configured.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--timestamp.field"></a>

  ###### [timestamp.field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_timestamp.field)

  Field name for record timestamp. Suffix with `!` to make this a required field, or `?` to keep it optional (the default).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--topic.field"></a>

  ###### [topic.field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertfield_topic.field)

  Field name for Kafka topic. Suffix with `!` to make this a required field, or `?` to keep it optional (the default).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertheader"></a>

##### [org.apache.kafka.connect.transforms.InsertHeader](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertheader)

Add a header to each record.

-

<a id="kafka-connect-user-guide--header"></a>

  ###### [header](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertheader_header)

  The name of the header.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | non-null string |
| Importance: | high |

-

<a id="kafka-connect-user-guide--value.literal"></a>

  ###### [value.literal](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.insertheader_value.literal)

  The literal value that is to be set as the header value on all records.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | non-null string |
| Importance: | high |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.maskfield"></a>

##### [org.apache.kafka.connect.transforms.MaskField](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.maskfield)

Mask specified fields with a valid null value for the field type (i.e. 0, false, empty string, and so on).

For numeric and string fields, an optional replacement value can be specified that is converted to the correct type.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.MaskField$Key`) or value (`org.apache.kafka.connect.transforms.MaskField$Value`).

-

<a id="kafka-connect-user-guide--fields-2"></a>

  ###### [fields](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.maskfield_fields)

  Names of fields to mask.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default-5"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.maskfield_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--replacement"></a>

  ###### [replacement](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.maskfield_replacement)

  Custom value replacement, that will be applied to all 'fields' values (numeric or non-empty string values only).

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: | non-empty string |
| Importance: | low |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.regexrouter"></a>

##### [org.apache.kafka.connect.transforms.RegexRouter](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.regexrouter)

Update the record topic using the configured regular expression and replacement string.

Under the hood, the regex is compiled to a `java.util.regex.Pattern`. If the pattern matches the input topic, `java.util.regex.Matcher#replaceFirst()` is used with the replacement string to obtain the new topic.

-

<a id="kafka-connect-user-guide--regex"></a>

  ###### [regex](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.regexrouter_regex)

  Regular expression to use for matching.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | valid regex |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replacement-2"></a>

  ###### [replacement](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.regexrouter_replacement)

  Replacement string.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield"></a>

##### [org.apache.kafka.connect.transforms.ReplaceField](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield)

Filter or rename fields.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.ReplaceField$Key`) or value (`org.apache.kafka.connect.transforms.ReplaceField$Value`).

-

<a id="kafka-connect-user-guide--exclude"></a>

  ###### [exclude](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield_exclude)

  Fields to exclude. This takes precedence over the fields to include.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--include"></a>

  ###### [include](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield_include)

  Fields to include. If specified, only these fields will be used.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--renames"></a>

  ###### [renames](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield_renames)

  Field rename mappings.

| Type: | list |
| --- | --- |
| Default: | "" |
| Valid Values: | list of colon-delimited pairs, e.g. `foo:bar,abc:xyz` |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--replace.null.with.default-6"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.replacefield_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.setschemametadata"></a>

##### [org.apache.kafka.connect.transforms.SetSchemaMetadata](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.setschemametadata)

Set the schema name, version or both on the record's key (`org.apache.kafka.connect.transforms.SetSchemaMetadata$Key`) or value (`org.apache.kafka.connect.transforms.SetSchemaMetadata$Value`) schema.

-

<a id="kafka-connect-user-guide--schema.name"></a>

  ###### [schema.name](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.setschemametadata_schema.name)

  Schema name to set.

| Type: | string |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--schema.version"></a>

  ###### [schema.version](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.setschemametadata_schema.version)

  Schema version to set.

| Type: | int |
| --- | --- |
| Default: | null |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default-7"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.setschemametadata_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter"></a>

##### [org.apache.kafka.connect.transforms.TimestampConverter](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter)

Convert timestamps between different formats such as Unix epoch, strings, and Connect Date/Timestamp types.Applies to individual fields or to the entire value.

Use the concrete transformation type designed for the record key (`org.apache.kafka.connect.transforms.TimestampConverter$Key`) or value (`org.apache.kafka.connect.transforms.TimestampConverter$Value`).

-

<a id="kafka-connect-user-guide--target.type"></a>

  ###### [target.type](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter_target.type)

  The desired timestamp representation: string, unix, Date, Time, or Timestamp

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | [string, unix, Date, Time, Timestamp] |
| Importance: | high |

-

<a id="kafka-connect-user-guide--field-3"></a>

  ###### [field](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter_field)

  The field containing the timestamp, or empty if the entire value is a timestamp

| Type: | string |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--format"></a>

  ###### [format](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter_format)

  A SimpleDateFormat-compatible format for the timestamp. Used to generate the output when type=string or used to parse the input if the input is a string.

| Type: | string |
| --- | --- |
| Default: | "" |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--replace.null.with.default-8"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

-

<a id="kafka-connect-user-guide--unix.precision"></a>

  ###### [unix.precision](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestampconverter_unix.precision)

  The desired Unix precision for the timestamp: seconds, milliseconds, microseconds, or nanoseconds. Used to generate the output when type=unix or used to parse the input if the input is a Long.Note: This SMT will cause precision loss during conversions from, and to, values with sub-millisecond components.

| Type: | string |
| --- | --- |
| Default: | milliseconds |
| Valid Values: | [nanoseconds, microseconds, milliseconds, seconds] |
| Importance: | low |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestamprouter"></a>

##### [org.apache.kafka.connect.transforms.TimestampRouter](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestamprouter)

Update the record's topic field as a function of the original topic value and the record timestamp.

This is mainly useful for sink connectors, since the topic field is often used to determine the equivalent entity name in the destination system(e.g. database table or search index name).

-

<a id="kafka-connect-user-guide--timestamp.format"></a>

  ###### [timestamp.format](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestamprouter_timestamp.format)

  Format string for the timestamp that is compatible with `java.text.SimpleDateFormat`.

| Type: | string |
| --- | --- |
| Default: | yyyyMMdd |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--topic.format"></a>

  ###### [topic.format](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.timestamprouter_topic.format)

  Format string which can contain `${topic}` and `${timestamp}` as placeholders for the topic and timestamp, respectively.

| Type: | string |
| --- | --- |
| Default: | ${topic}-${timestamp} |
| Valid Values: |  |
| Importance: | high |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.valuetokey"></a>

##### [org.apache.kafka.connect.transforms.ValueToKey](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.valuetokey)

Replace the record key with a new key formed from a subset of fields in the record value.

-

<a id="kafka-connect-user-guide--fields-3"></a>

  ###### [fields](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.valuetokey_fields)

  Field names on the record value to extract as the record key.

| Type: | list |
| --- | --- |
| Default: |  |
| Valid Values: |  |
| Importance: | high |

-

<a id="kafka-connect-user-guide--replace.null.with.default-9"></a>

  ###### [replace.null.with.default](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.valuetokey_replace.null.with.default)

  Whether to replace fields that have a default value and that are null to the default value. When set to true, the default value is used, otherwise null is used.

| Type: | boolean |
| --- | --- |
| Default: | true |
| Valid Values: |  |
| Importance: | medium |

<a id="kafka-connect-user-guide--predicates"></a>

### Predicates

Transformations can be configured with predicates so that the transformation is applied only to messages which satisfy some condition. In particular, when combined with the **Filter** transformation predicates can be used to selectively filter out certain messages.

Predicates are specified in the connector configuration.

- `predicates` - Set of aliases for the predicates to be applied to some of the transformations.
- `predicates.$alias.type` - Fully qualified class name for the predicate.
- `predicates.$alias.$predicateSpecificConfig` - Configuration properties for the predicate.

All transformations have the implicit config properties `predicate` and `negate`. A particular predicate is associated with a transformation by setting the transformation’s `predicate` config to the predicate’s alias. The predicate’s value can be reversed using the `negate` configuration property.

For example, suppose you have a source connector which produces messages to many different topics and you want to:

- filter out the messages in the ‘foo’ topic entirely
- apply the ExtractField transformation with the field name ‘other\_field’ to records in all topics *except* the topic ‘bar’

To do this we need first to filter out the records destined for the topic ‘foo’. The Filter transformation removes records from further processing, and can use the TopicNameMatches predicate to apply the transformation only to records in topics which match a certain regular expression. TopicNameMatches’s only configuration property is `pattern` which is a Java regular expression for matching against the topic name. The configuration would look like this:

```properties
transforms=Filter
transforms.Filter.type=org.apache.kafka.connect.transforms.Filter
transforms.Filter.predicate=IsFoo

predicates=IsFoo
predicates.IsFoo.type=org.apache.kafka.connect.transforms.predicates.TopicNameMatches
predicates.IsFoo.pattern=foo
```

Next we need to apply ExtractField only when the topic name of the record is not ‘bar’. We can’t just use TopicNameMatches directly, because that would apply the transformation to matching topic names, not topic names which do *not* match. The transformation’s implicit `negate` config properties allows us to invert the set of records which a predicate matches. Adding the configuration for this to the previous example we arrive at:

```properties
transforms=Filter,Extract
transforms.Filter.type=org.apache.kafka.connect.transforms.Filter
transforms.Filter.predicate=IsFoo

transforms.Extract.type=org.apache.kafka.connect.transforms.ExtractField$Key
transforms.Extract.field=other_field
transforms.Extract.predicate=IsBar
transforms.Extract.negate=true

predicates=IsFoo,IsBar
predicates.IsFoo.type=org.apache.kafka.connect.transforms.predicates.TopicNameMatches
predicates.IsFoo.pattern=foo

predicates.IsBar.type=org.apache.kafka.connect.transforms.predicates.TopicNameMatches
predicates.IsBar.pattern=bar
```

Kafka Connect includes the following predicates:

- `TopicNameMatches` - matches records in a topic with a name matching a particular Java regular expression.
- `HasHeaderKey` - matches records which have a header with the given key.
- `RecordIsTombstone` - matches tombstone records, that is records with a null value.

Details on how to configure each predicate are listed below:

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.hasheaderkey"></a>

##### [org.apache.kafka.connect.transforms.predicates.HasHeaderKey](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.hasheaderkey)

A predicate which is true for records with at least one header with the configured name.

-

<a id="kafka-connect-user-guide--name"></a>

  ###### [name](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.hasheaderkey_name)

  The header name.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | non-empty string |
| Importance: | medium |

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.recordistombstone"></a>

##### [org.apache.kafka.connect.transforms.predicates.RecordIsTombstone](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.recordistombstone)

A predicate which is true for records which are tombstones (i.e. have null value).

<a id="kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.topicnamematches"></a>

##### [org.apache.kafka.connect.transforms.predicates.TopicNameMatches](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.topicnamematches)

A predicate which is true for records with a topic name that matches the configured regular expression.

-

<a id="kafka-connect-user-guide--pattern"></a>

  ###### [pattern](#kafka-connect-user-guide--org.apache.kafka.connect.transforms.predicates.topicnamematches_pattern)

  A Java regular expression for matching against the name of a record's topic.

| Type: | string |
| --- | --- |
| Default: |  |
| Valid Values: | non-empty string, valid regex |
| Importance: | medium |

<a id="kafka-connect-user-guide--rest-api"></a>

## REST API

Since Kafka Connect is intended to be run as a service, it also provides a REST API for managing connectors. This REST API is available in both standalone and distributed mode. The REST API server can be configured using the `listeners` configuration option. This field should contain a list of listeners in the following format: `protocol://host:port,protocol2://host2:port2`. Currently supported protocols are `http` and `https`. For example:

```properties
listeners=http://localhost:8080,https://localhost:8443
```

By default, if no `listeners` are specified, the REST server runs on port 8083 using the HTTP protocol. When using HTTPS, the configuration has to include the SSL configuration. By default, it will use the `ssl.*` settings. In case it is needed to use different configuration for the REST API than for connecting to Kafka brokers, the fields can be prefixed with `listeners.https`. When using the prefix, only the prefixed options will be used and the `ssl.*` options without the prefix will be ignored. Following fields can be used to configure HTTPS for the REST API:

- `ssl.keystore.location`
- `ssl.keystore.password`
- `ssl.keystore.type`
- `ssl.key.password`
- `ssl.truststore.location`
- `ssl.truststore.password`
- `ssl.truststore.type`
- `ssl.enabled.protocols`
- `ssl.provider`
- `ssl.protocol`
- `ssl.cipher.suites`
- `ssl.keymanager.algorithm`
- `ssl.secure.random.implementation`
- `ssl.trustmanager.algorithm`
- `ssl.endpoint.identification.algorithm`
- `ssl.client.auth`

The REST API is used not only by users to monitor / manage Kafka Connect. In distributed mode, it is also used for the Kafka Connect cross-cluster communication. Some requests received on the follower nodes REST API will be forwarded to the leader node REST API. In case the URI under which is given host reachable is different from the URI which it listens on, the configuration options `rest.advertised.host.name`, `rest.advertised.port` and `rest.advertised.listener` can be used to change the URI which will be used by the follower nodes to connect with the leader. When using both HTTP and HTTPS listeners, the `rest.advertised.listener` option can be also used to define which listener will be used for the cross-cluster communication. When using HTTPS for communication between nodes, the same `ssl.*` or `listeners.https` options will be used to configure the HTTPS client.

The following are the currently supported REST API endpoints:

- `GET /connectors` - return a list of active connectors
- `POST /connectors` - create a new connector; the request body should be a JSON object containing a string `name` field and an object `config` field with the connector configuration parameters. The JSON object may also optionally contain a string `initial_state` field which can take the following values - `STOPPED`, `PAUSED` or `RUNNING` (the default value)
- `GET /connectors/{name}` - get information about a specific connector
- `GET /connectors/{name}/config` - get the configuration parameters for a specific connector
- `PUT /connectors/{name}/config` - update the configuration parameters for a specific connector
- `PATCH /connectors/{name}/config` - patch the configuration parameters for a specific connector, where `null` values in the JSON body indicates removing of the key from the final configuration
- `GET /connectors/{name}/status` - get current status of the connector, including if it is running, failed, paused, etc., which worker it is assigned to, error information if it has failed, and the state of all its tasks
- `GET /connectors/{name}/tasks` - get a list of tasks currently running for a connector along with their configurations
- `GET /connectors/{name}/tasks/{taskid}/status` - get current status of the task, including if it is running, failed, paused, etc., which worker it is assigned to, and error information if it has failed
- `PUT /connectors/{name}/pause` - pause the connector and its tasks, which stops message processing until the connector is resumed. Any resources claimed by its tasks are left allocated, which allows the connector to begin processing data quickly once it is resumed.
- `PUT /connectors/{name}/stop` - stop the connector and shut down its tasks, deallocating any resources claimed by its tasks. This is more efficient from a resource usage standpoint than pausing the connector, but can cause it to take longer to begin processing data once resumed. Note that the offsets for a connector can be only modified via the offsets management endpoints if it is in the stopped state
- `PUT /connectors/{name}/resume` - resume a paused or stopped connector (or do nothing if the connector is not paused or stopped)
- `POST /connectors/{name}/restart?includeTasks=<true|false>&onlyFailed=<true|false>` - restart a connector and its tasks instances.
  - the “includeTasks” parameter specifies whether to restart the connector instance and task instances (“includeTasks=true”) or just the connector instance (“includeTasks=false”), with the default (“false”) preserving the same behavior as earlier versions.
  - the “onlyFailed” parameter specifies whether to restart just the instances with a FAILED status (“onlyFailed=true”) or all instances (“onlyFailed=false”), with the default (“false”) preserving the same behavior as earlier versions.
- `POST /connectors/{name}/tasks/{taskId}/restart` - restart an individual task (typically because it has failed)
- `DELETE /connectors/{name}` - delete a connector, halting all tasks and deleting its configuration
- `GET /connectors/{name}/topics` - get the set of topics that a specific connector is using since the connector was created or since a request to reset its set of active topics was issued
- `PUT /connectors/{name}/topics/reset` - send a request to empty the set of active topics of a connector
- Offsets management endpoints (see [KIP-875](https://cwiki.apache.org/confluence/x/Io3GDQ) for more details):
  - `GET /connectors/{name}/offsets` - get the current offsets for a connector
  - `DELETE /connectors/{name}/offsets` - reset the offsets for a connector. The connector must exist and must be in the stopped state (see `PUT /connectors/{name}/stop`)
  - `PATCH /connectors/{name}/offsets` - alter the offsets for a connector. The connector must exist and must be in the stopped state (see `PUT /connectors/{name}/stop`). The request body should be a JSON object containing a JSON array `offsets` field, similar to the response body of the `GET /connectors/{name}/offsets` endpoint. An example request body for the `FileStreamSourceConnector`:

```json
{"offsets": [{"partition": {"filename": "test.txt" },"offset": {"position": 30}}]}
```

An example request body for the `FileStreamSinkConnector`:

```json
{"offsets": [{"partition": {"kafka_topic": "test","kafka_partition": 0 },"offset": {"kafka_offset": 5} },{"partition": {"kafka_topic": "test","kafka_partition": 1 },"offset": null}]}
```

The “offset” field may be null to reset the offset for a specific partition (applicable to both source and sink connectors). Note that the request body format depends on the connector implementation in the case of source connectors, whereas there is a common format across all sink connectors.

Kafka Connect also provides a REST API for getting information about connector plugins:

- `GET /connector-plugins`- return a list of connector plugins installed in the Kafka Connect cluster. Note that the API only checks for connectors on the worker that handles the request, which means you may see inconsistent results, especially during a rolling upgrade if you add new connector jars
- `GET /connector-plugins/{plugin-type}/config` - get the configuration definition for the specified plugin.
- `PUT /connector-plugins/{connector-type}/config/validate` - validate the provided configuration values against the configuration definition. This API performs per config validation, returns suggested values and error messages during validation.

The following is a supported REST request at the top-level (root) endpoint:

- `GET /`- return basic information about the Kafka Connect cluster such as the version of the Connect worker that serves the REST request (including git commit ID of the source code) and the Kafka cluster ID that is connected to.

The `admin.listeners` configuration can be used to configure admin REST APIs on Kafka Connect’s REST API server. Similar to the `listeners` configuration, this field should contain a list of listeners in the following format: `protocol://host:port,protocol2://host2:port2`. Currently supported protocols are `http` and `https`. For example:

```properties
admin.listeners=http://localhost:8080,https://localhost:8443
```

By default, if `admin.listeners` is not configured, the admin REST APIs will be available on the regular listeners.

The following are the currently supported admin REST API endpoints:

- `GET /admin/loggers` - list the current loggers that have their levels explicitly set and their log levels
- `GET /admin/loggers/{name}` - get the log level for the specified logger
- `PUT /admin/loggers/{name}` - set the log level for the specified logger

See [KIP-495](https://cwiki.apache.org/confluence/x/-4tTBw) for more details about the admin logger REST APIs.

For the complete specification of the Kafka Connect REST API, see the [OpenAPI documentation](assets/files/connect-rest_bb879b8e08035384.yaml)

<a id="kafka-connect-user-guide--error-reporting-in-connect"></a>

## Error Reporting in Connect

Kafka Connect provides error reporting to handle errors encountered along various stages of processing. By default, any error encountered during conversion or within transformations will cause the connector to fail. Each connector configuration can also enable tolerating such errors by skipping them, optionally writing each error and the details of the failed operation and problematic record (with various levels of detail) to the Connect application log. These mechanisms also capture errors when a sink connector is processing the messages consumed from its Kafka topics, and all of the errors can be written to a configurable “dead letter queue” (DLQ) Kafka topic.

To report errors within a connector’s converter, transforms, or within the sink connector itself to the log, set `errors.log.enable=true` in the connector configuration to log details of each error and problem record’s topic, partition, and offset. For additional debugging purposes, set `errors.log.include.messages=true` to also log the problem record key, value, and headers to the log (note this may log sensitive information).

To report errors within a connector’s converter, transforms, or within the sink connector itself to a dead letter queue topic, set `errors.deadletterqueue.topic.name`, and optionally `errors.deadletterqueue.context.headers.enable=true`.

By default connectors exhibit “fail fast” behavior immediately upon an error or exception. This is equivalent to adding the following configuration properties with their defaults to a connector configuration:

```properties
# disable retries on failure
errors.retry.timeout=0

# do not log the error and their contexts
errors.log.enable=false

# do not record errors in a dead letter queue topic
errors.deadletterqueue.topic.name=

# Fail on first error
errors.tolerance=none
```

These and other related connector configuration properties can be changed to provide different behavior. For example, the following configuration properties can be added to a connector configuration to setup error handling with multiple retries, logging to the application logs and the `my-connector-errors` Kafka topic, and tolerating all errors by reporting them rather than failing the connector task:

```properties
# retry for at most 10 minutes times waiting up to 30 seconds between consecutive failures
errors.retry.timeout=600000
errors.retry.delay.max.ms=30000

# log error context along with application logs, but do not include configs and messages
errors.log.enable=true
errors.log.include.messages=false

# produce error context into the Kafka topic
errors.deadletterqueue.topic.name=my-connector-errors

# Tolerate all errors.
errors.tolerance=all
```

<a id="kafka-connect-user-guide--exactly-once-support"></a>

## Exactly-once support

Kafka Connect is capable of providing exactly-once semantics for sink connectors (as of version 0.11.0) and source connectors (as of version 3.3.0). Please note that **support for exactly-once semantics is highly dependent on the type of connector you run.** Even if you set all the correct worker properties in the configuration for each node in a cluster, if a connector is not designed to, or cannot take advantage of the capabilities of the Kafka Connect framework, exactly-once may not be possible.

<a id="kafka-connect-user-guide--sink-connectors"></a>

### Sink connectors

If a sink connector supports exactly-once semantics, to enable exactly-once at the Connect worker level, you must ensure its consumer group is configured to ignore records in aborted transactions. You can do this by setting the worker property `consumer.isolation.level` to `read_committed` or, if running a version of Kafka Connect that supports it, using a connector client config override policy that allows the `consumer.override.isolation.level` property to be set to `read_committed` in individual connector configs.

<a id="kafka-connect-user-guide--source-connectors"></a>

### Source connectors

If a source connector supports exactly-once semantics, you must configure your Connect cluster to enable framework-level support for exactly-once source connectors. Additional ACLs may be necessary if running against a secured Kafka cluster. Note that exactly-once support for source connectors is currently only available in distributed mode; standalone Connect workers cannot provide exactly-once semantics.

<a id="kafka-connect-user-guide--worker-configuration"></a>

#### Worker configuration

For new Connect clusters, set the `exactly.once.source.support` property to `enabled` in the worker config for each node in the cluster. For existing clusters, two rolling upgrades are necessary. During the first upgrade, the `exactly.once.source.support` property should be set to `preparing`, and during the second, it should be set to `enabled`.

<a id="kafka-connect-user-guide--plugin-discovery"></a>

## Plugin Discovery

Plugin discovery is the name for the strategy which the Connect worker uses to find plugin classes and make them accessible to configure and run in connectors. This is controlled by the plugin.discovery worker configuration, and has a significant impact on worker startup time. `service_load` is the fastest strategy, but care should be taken to verify that plugins are compatible before setting this configuration to `service_load`.

Prior to version 3.6, this strategy was not configurable, and behaved like the `only_scan` mode which is compatible with all plugins. For version 3.6 and later, this mode defaults to `hybrid_warn` which is also compatible with all plugins, but logs a warning for plugins which are incompatible with `service_load`. The `hybrid_fail` strategy stops the worker with an error if a plugin incompatible with `service_load` is detected, asserting that all plugins are compatible. Finally, the `service_load` strategy disables the slow legacy scanning mechanism used in all other modes, and instead uses the faster `ServiceLoader` mechanism. Plugins which are incompatible with that mechanism may be unusable.

<a id="kafka-connect-user-guide--verifying-plugin-compatibility"></a>

### Verifying Plugin Compatibility

To verify if all of your plugins are compatible with `service_load`, first ensure that you are using version 3.6 or later of Kafka Connect. You can then perform one of the following checks:

- Start your worker with the default `hybrid_warn`strategy, and WARN logs enabled for the `org.apache.kafka.connect` package. At least one WARN log message mentioning the `plugin.discovery` configuration should be printed. This log message will explicitly say that all plugins are compatible, or list the incompatible plugins.
- Start your worker in a test environment with `hybrid_fail`. If all plugins are compatible, startup will succeed. If at least one plugin is not compatible the worker will fail to start up, and all incompatible plugins will be listed in the exception.

If the verification step succeeds, then your current set of installed plugins is compatible, and it should be safe to change the `plugin.discovery` configuration to `service_load`. If the verification fails, you cannot use `service_load` strategy and should take note of the list of incompatible plugins. All plugins must be addressed before using the `service_load` strategy. It is recommended to perform this verification after installing or changing plugin versions, and the verification can be done automatically in a Continuous Integration environment.

<a id="kafka-connect-user-guide--operators-artifact-migration"></a>
<a id="kafka-connect-user-guide--operators:-artifact-migration"></a>

### Operators: Artifact Migration

As an operator of Connect, if you discover incompatible plugins, there are multiple ways to resolve the incompatibility. They are listed below from most to least preferable.

1. Check the latest release from your plugin provider, and if it is compatible, upgrade.
2. Contact your plugin provider and request that they migrate the plugin to be compatible, following the source migration instructions, and then upgrade to the compatible version.
3. Migrate the plugin artifacts yourself using the included migration script.

The migration script is located in `bin/connect-plugin-path.sh` and `bin\windows\connect-plugin-path.bat` of your Kafka installation. The script can migrate incompatible plugin artifacts already installed on your Connect worker’s `plugin.path` by adding or modifying JAR or resource files. This is not suitable for environments using code-signing, as this can change artifacts such that they will fail signature verification. View the built-in help with `--help`.

To perform a migration, first use the `list` subcommand to get an overview of the plugins available to the script. You must tell the script where to find plugins, which can be done with the repeatable `--worker-config`, `--plugin-path`, and `--plugin-location` arguments. The script will ignore plugins on the classpath, so any custom plugins on your classpath should be moved to the plugin path in order to be used with this migration script, or migrated manually. Be sure to compare the output of `list` with the worker startup warning or error message to ensure that all of your affected plugins are found by the script.

Once you see that all incompatible plugins are included in the listing, you can proceed to dry-run the migration with `sync-manifests --dry-run`. This will perform all parts of the migration, except for writing the results of the migration to disk. Note that the `sync-manifests` command requires all specified paths to be writable, and may alter the contents of the directories. Make a backup of your plugins in the specified paths, or copy them to a writable directory.

Ensure that you have a backup of your plugins and the dry-run succeeds before removing the `--dry-run` flag and actually running the migration. If the migration fails without the `--dry-run` flag, then the partially migrated artifacts should be discarded. The migration is idempotent, so running it multiple times and on already-migrated plugins is safe. After the script finishes, you should verify the migration is complete. The migration script is suitable for use in a Continuous Integration environment for automatic migration.

<a id="kafka-connect-user-guide--developers-source-migration"></a>
<a id="kafka-connect-user-guide--developers:-source-migration"></a>

### Developers: Source Migration

To make plugins compatible with `service_load`, it is necessary to add [ServiceLoader](https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html) manifests to your source code, which should then be packaged in the release artifact. Manifests are resource files in `META-INF/services/` named after their superclass type, and contain a list of fully-qualified subclass names, one on each line.

In order for a plugin to be compatible, it must appear as a line in a manifest corresponding to the plugin superclass it extends. If a single plugin implements multiple plugin interfaces, then it should appear in a manifest for each interface it implements. If you have no classes for a certain type of plugin, you do not need to include a manifest file for that type. If you have classes which should not be visible as plugins, they should be marked abstract. The following types are expected to have manifests:

- `org.apache.kafka.connect.sink.SinkConnector`
- `org.apache.kafka.connect.source.SourceConnector`
- `org.apache.kafka.connect.storage.Converter`
- `org.apache.kafka.connect.storage.HeaderConverter`
- `org.apache.kafka.connect.transforms.Transformation`
- `org.apache.kafka.connect.transforms.predicates.Predicate`
- `org.apache.kafka.common.config.provider.ConfigProvider`
- `org.apache.kafka.connect.rest.ConnectRestExtension`
- `org.apache.kafka.connect.connector.policy.ConnectorClientConfigOverridePolicy`

For example, if you only have one connector with the fully-qualified name `com.example.MySinkConnector`, then only one manifest file must be added to resources in `META-INF/services/org.apache.kafka.connect.sink.SinkConnector`, and the contents should be similar to the following:

```text
# license header or comment
com.example.MySinkConnector
```

You should then verify that your manifests are correct by using the verification steps with a pre-release artifact. If the verification succeeds, you can then release the plugin normally, and operators can upgrade to the compatible version.

<a id="kafka-connect-user-guide--security"></a>

## Security

It’s important to understand the security concerns inherent to Connect. First, Connect allows running custom plugins. These plugins can run arbitrary code, so you must trust them before installing them in your Connect clusters. By default, the REST API is unsecured and allows anyone that can access it to start and stop connectors. You should only directly expose the REST API to trusted users, otherwise it’s easy to gain arbitrary code execution on Connect workers. By default, connectors can also override the configurations of the Kafka clients that Connect uses internally. Since Kafka 4.2.0, it’s recommended to set `connector.client.config.override.policy` to `Allowlist`, this will be the default from Kafka 5.0.0, and explicitly only allow configurations that you need to override. Keep in mind that configurations that can load classes such as `sasl.jaas.config` or `sasl.login.class` should only be allowed if only trusted users can access the REST API as they, by design, enable executing code on the Connect worker.

<a id="kafka-connect-user-guide--acl-requirements"></a>

### ACL requirements

The principal for each Connect worker requires the following ACLs:

| Operation | Resource Type | Resource Name | Note |
| --- | --- | --- | --- |
| Read | Group | `group.id` of the Connect cluster |  |
| Read | Topic | `config.storage.topic` of the Connect cluster |  |
| Write | Topic | `config.storage.topic` of the Connect cluster |  |
| Create | Topic | `config.storage.topic` of the Connect cluster | Only necessary if the config topic for Connect does not exist yet |
| Read | Topic | `offset.storage.topic` of the Connect cluster |  |
| Write | Topic | `offset.storage.topic` of the Connect cluster |  |
| Create | Topic | `offset.storage.topic` of the Connect cluster | Only necessary if the offsets topic for Connect does not exist yet |
| Read | Topic | `status.storage.topic` of the Connect cluster |  |
| Write | Topic | `status.storage.topic` of the Connect cluster |  |
| Create | Topic | `status.storage.topic` of the Connect cluster | Only necessary if the status topic for Connect does not exist yet |
| Write | TransactionalId | `connect-cluster-${groupId}` where `${groupId}` is the `group.id` of the cluster | Only necessary if [exactly-once support](#kafka-connect-user-guide--exactly-once-support) is enabled or if `exactly.once.source.support` is set to `preparing`. |
| Describe | TransactionalId | `connect-cluster-${groupId}` where `${groupId}` is the `group.id` of the cluster | Only necessary if [exactly-once support](#kafka-connect-user-guide--exactly-once-support) is enabled or if `exactly.once.source.support` is set to `preparing`. |

To support Source connectors, the principal for each individual connector will require the following ACLs:

| Operation | Resource Type | Resource Name | Note |
| --- | --- | --- | --- |
| Write | Topic | topic(s) used as the destination |  |
| Create | Topic | topic(s) used as the destination | Only necessary if `topic.creation.enable` is `true` and the topic(s) do not exist yet |
| Describe | Topic | Offsets topic used by the connector This is the value of the `offsets.storage.topic` property in the connector’s configuration if provided, or the value of the `offsets.storage.topic` property in the worker’s configuration if not. | Only necessary if [exactly-once support](#kafka-connect-user-guide--exactly-once-support) is enabled. |
| Write | TransactionalId | `${groupId}-${connector}-${taskId}` for each task that the connector will create, where `${groupId}` is the `group.id` of the Connect cluster `${connector}` is the name of the connector `${taskId}` is the ID of the task (starting from zero) | Only necessary if [exactly-once support](#kafka-connect-user-guide--exactly-once-support) is enabled. A wildcard prefix of `${groupId}-${connector}*` can be used for convenience if there is no risk of conflict with other transactional IDs or if conflicts are acceptable to the user. |
| Describe | TransactionalId | `${groupId}-${connector}-${taskId}` for each task that the connector will create, where `${groupId}` is the `group.id` of the Connect cluster `${connector}` is the name of the connector `${taskId}` is the ID of the task (starting from zero) | Only necessary if [exactly-once support](#kafka-connect-user-guide--exactly-once-support) is enabled. A wildcard prefix of `${groupId}-${connector}*` can be used for convenience if there is no risk of conflict with other transactional IDs or if conflicts are acceptable to the user. |

To support Sink connectors, the principal for each individual connector will require the following ACLs:

| Operation | Resource Type | Resource Name | Note |
| --- | --- | --- | --- |
| Read | Group | `connect-${connector}` where `${connector}` is the name of the connector or the value of `consumer.group.id` if present in the Connect configuration, or the value of `consumer.overrides.group.id` if present in the Connector configuration |  |
| Read | Topic | sink topic(s) that the connector will consume from | These will be identified by the `topics` or `topics.regex` option of the connector |
| Write | Topic | `errors.deadletterqueue.topic.name` of the connector | Only necessary if `errors.deadletterqueue.topic.name` is set to a non-empty value |

Some connectors make additional use of Kafka topics that is not managed by the Kafka Connect framework (for example, change data capture connectors may use additional topics to store schema history). Refer to Connector documentation for details of any additional ACLs that are required. These can be added to the principal for the individual connector.

---

<a id="kafka-connect-connector-development-guide"></a>

<a id="kafka-connect-connector-development-guide--connector-development-guide"></a>

# Connector Development Guide

Connector Development Guide

This guide describes how developers can write new connectors for Kafka Connect to move data between Kafka and other systems. It briefly reviews a few key concepts and then describes how to create a simple connector.

<a id="kafka-connect-connector-development-guide--core-concepts-and-apis"></a>

## Core Concepts and APIs

<a id="kafka-connect-connector-development-guide--connectors-and-tasks"></a>

### Connectors and Tasks

To copy data between Kafka and another system, users create a `Connector` for the system they want to pull data from or push data to. Connectors come in two flavors: `SourceConnectors` import data from another system (e.g. `JDBCSourceConnector` would import a relational database into Kafka) and `SinkConnectors` export data (e.g. `HDFSSinkConnector` would export the contents of a Kafka topic to an HDFS file).

`Connectors` do not perform any data copying themselves: their configuration describes the data to be copied, and the `Connector` is responsible for breaking that job into a set of `Tasks` that can be distributed to workers. These `Tasks` also come in two corresponding flavors: `SourceTask` and `SinkTask`.

With an assignment in hand, each `Task` must copy its subset of the data to or from Kafka. In Kafka Connect, it should always be possible to frame these assignments as a set of input and output streams consisting of records with consistent schemas. Sometimes this mapping is obvious: each file in a set of log files can be considered a stream with each parsed line forming a record using the same schema and offsets stored as byte offsets in the file. In other cases it may require more effort to map to this model: a JDBC connector can map each table to a stream, but the offset is less clear. One possible mapping uses a timestamp column to generate queries incrementally returning new data, and the last queried timestamp can be used as the offset.

<a id="kafka-connect-connector-development-guide--streams-and-records"></a>

### Streams and Records

Each stream should be a sequence of key-value records. Both the keys and values can have complex structure – many primitive types are provided, but arrays, objects, and nested data structures can be represented as well. The runtime data format does not assume any particular serialization format; this conversion is handled internally by the framework.

In addition to the key and value, records (both those generated by sources and those delivered to sinks) have associated stream IDs and offsets. These are used by the framework to periodically commit the offsets of data that have been processed so that in the event of failures, processing can resume from the last committed offsets, avoiding unnecessary reprocessing and duplication of events.

<a id="kafka-connect-connector-development-guide--dynamic-connectors"></a>

### Dynamic Connectors

Not all jobs are static, so `Connector` implementations are also responsible for monitoring the external system for any changes that might require reconfiguration. For example, in the `JDBCSourceConnector` example, the `Connector` might assign a set of tables to each `Task`. When a new table is created, it must discover this so it can assign the new table to one of the `Tasks` by updating its configuration. When it notices a change that requires reconfiguration (or a change in the number of `Tasks`), it notifies the framework and the framework updates any corresponding `Tasks`.

<a id="kafka-connect-connector-development-guide--developing-a-simple-connector"></a>

## Developing a Simple Connector

Developing a connector only requires implementing two interfaces, the `Connector` and `Task`. A simple example is included with the source code for Kafka in the `file` package. This connector is meant for use in standalone mode and has implementations of a `SourceConnector`/`SourceTask` to read each line of a file and emit it as a record and a `SinkConnector`/`SinkTask` that writes each record to a file.

The rest of this section will walk through some code to demonstrate the key steps in creating a connector, but developers should also refer to the full example source code as many details are omitted for brevity.

<a id="kafka-connect-connector-development-guide--connector-example"></a>

### Connector Example

We’ll cover the `SourceConnector` as a simple example. `SinkConnector` implementations are very similar. Pick a package and class name, these examples will use the `FileStreamSourceConnector` but substitute your own class name where appropriate. In order to make the plugin discoverable at runtime, add a ServiceLoader manifest to your resources in `META-INF/services/org.apache.kafka.connect.source.SourceConnector` with your fully-qualified class name on a single line:

```text
com.example.FileStreamSourceConnector
```

Create a class that inherits from `SourceConnector` and add a field that will store the configuration information to be propagated to the task(s) (the topic to send data to, and optionally - the filename to read from and the maximum batch size):

```java
package com.example;

public class FileStreamSourceConnector extends SourceConnector {
    private Map<String, String> props;
```

The easiest method to fill in is `taskClass()`, which defines the class that should be instantiated in worker processes to actually read the data:

```java
@Override
public Class<? extends Task> taskClass() {
    return FileStreamSourceTask.class;
}
```

We will define the `FileStreamSourceTask` class below. Next, we add some standard lifecycle methods, `start()` and `stop()`:

```java
@Override
public void start(Map<String, String> props) {
    // Initialization logic and setting up of resources can take place in this method.
    // This connector doesn't need to do any of that, but we do log a helpful message to the user.

    this.props = props;
    AbstractConfig config = new AbstractConfig(CONFIG_DEF, props);
    String filename = config.getString(FILE_CONFIG);
    filename = (filename == null || filename.isEmpty()) ? "standard input" : config.getString(FILE_CONFIG);
    log.info("Starting file source connector reading from {}", filename);
}

@Override
public void stop() {
    // Nothing to do since no background monitoring is required.
}
```

Finally, the real core of the implementation is in `taskConfigs()`. In this case we are only handling a single file, so even though we may be permitted to generate more tasks as per the `maxTasks` argument, we return a list with only one entry:

```java
@Override
public List<Map<String, String>> taskConfigs(int maxTasks) {
    // Note that the task configs could contain configs additional to or different from the connector configs if needed. For instance,
    // if different tasks have different responsibilities, or if different tasks are meant to process different subsets of the source data stream).
    ArrayList<Map<String, String>> configs = new ArrayList<>();
    // Only one input stream makes sense.
    configs.add(props);
    return configs;
}
```

Even with multiple tasks, this method implementation is usually pretty simple. It just has to determine the number of input tasks, which may require contacting the remote service it is pulling data from, and then divvy them up. Because some patterns for splitting work among tasks are so common, some utilities are provided in `ConnectorUtils` to simplify these cases.

Note that this simple example does not include dynamic input. See the discussion in the next section for how to trigger updates to task configs.

<a id="kafka-connect-connector-development-guide--task-example-source-task"></a>

### Task Example - Source Task

Next we’ll describe the implementation of the corresponding `SourceTask`. The implementation is short, but too long to cover completely in this guide. We’ll use pseudo-code to describe most of the implementation, but you can refer to the source code for the full example.

Just as with the connector, we need to create a class inheriting from the appropriate base `Task` class. It also has some standard lifecycle methods:

```java
public class FileStreamSourceTask extends SourceTask {
    private String filename;
    private InputStream stream;
    private String topic;
    private int batchSize;

    @Override
    public void start(Map<String, String> props) {
        filename = props.get(FileStreamSourceConnector.FILE_CONFIG);
        stream = openOrThrowError(filename);
        topic = props.get(FileStreamSourceConnector.TOPIC_CONFIG);
        batchSize = props.get(FileStreamSourceConnector.TASK_BATCH_SIZE_CONFIG);
    }

    @Override
    public synchronized void stop() {
        stream.close();
    }
}
```

These are slightly simplified versions, but show that these methods should be relatively simple and the only work they should perform is allocating or freeing resources. There are two points to note about this implementation. First, the `start()` method does not yet handle resuming from a previous offset, which will be addressed in a later section. Second, the `stop()` method is synchronized. This will be necessary because `SourceTasks` are given a dedicated thread which they can block indefinitely, so they need to be stopped with a call from a different thread in the Worker.

Next, we implement the main functionality of the task, the `poll()` method which gets events from the input system and returns a `List<SourceRecord>`:

```java
@Override public List<SourceRecord> poll() throws InterruptedException {try {ArrayList<SourceRecord> records = new ArrayList<>(); while (streamValid(stream) && records.isEmpty()) {LineAndOffset line = readToNextLine(stream); if (line != null) {Map<String, Object> sourcePartition = Collections.singletonMap("filename", filename); Map<String, Object> sourceOffset = Collections.singletonMap("position", streamOffset); records.add(new SourceRecord(sourcePartition, sourceOffset, topic, Schema.STRING_SCHEMA, line)); if (records.size() >= batchSize) {return records;} } else {Thread.sleep(1);}} return records; } catch (IOException e) {// Underlying stream was killed, probably as a result of calling stop. Allow to return // null, and driving thread will handle any shutdown if necessary.} return null;}
```

Again, we’ve omitted some details, but we can see the important steps: the `poll()` method is going to be called repeatedly, and for each call it will loop trying to read records from the file. For each line it reads, it also tracks the file offset. It uses this information to create an output `SourceRecord` with four pieces of information: the source partition (there is only one, the single file being read), source offset (byte offset in the file), output topic name, and output value (the line, and we include a schema indicating this value will always be a string). Other variants of the `SourceRecord` constructor can also include a specific output partition, a key, and headers.

Note that this implementation uses the normal Java `InputStream` interface and may sleep if data is not available. This is acceptable because Kafka Connect provides each task with a dedicated thread. While task implementations have to conform to the basic `poll()` interface, they have a lot of flexibility in how they are implemented. In this case, an NIO-based implementation would be more efficient, but this simple approach works, is quick to implement, and is compatible with older versions of Java.

Although not used in the example, `SourceTask` also provides two APIs to commit offsets in the source system: `commit` and `commitRecord`. The APIs are provided for source systems which have an acknowledgement mechanism for messages. Overriding these methods allows the source connector to acknowledge messages in the source system, either in bulk or individually, once they have been written to Kafka. The `commit` API stores the offsets in the source system, up to the offsets that have been returned by `poll`. The implementation of this API should block until the commit is complete. The `commitRecord` API saves the offset in the source system for each `SourceRecord` after it is written to Kafka. As Kafka Connect will record offsets automatically, `SourceTask`s are not required to implement them. In cases where a connector does need to acknowledge messages in the source system, only one of the APIs is typically required.

<a id="kafka-connect-connector-development-guide--sink-tasks"></a>

### Sink Tasks

The previous section described how to implement a simple `SourceTask`. Unlike `SourceConnector` and `SinkConnector`, `SourceTask` and `SinkTask` have very different interfaces because `SourceTask` uses a pull interface and `SinkTask` uses a push interface. Both share the common lifecycle methods, but the `SinkTask` interface is quite different:

```java
public abstract class SinkTask implements Task {public void initialize(SinkTaskContext context) {this.context = context;}
public abstract void put(Collection<SinkRecord> records);
public void flush(Map<TopicPartition, OffsetAndMetadata> currentOffsets) {}}
```

The `SinkTask` documentation contains full details, but this interface is nearly as simple as the `SourceTask`. The `put()` method should contain most of the implementation, accepting sets of `SinkRecords`, performing any required translation, and storing them in the destination system. This method does not need to ensure the data has been fully written to the destination system before returning. In fact, in many cases internal buffering will be useful so an entire batch of records can be sent at once, reducing the overhead of inserting events into the downstream data store. The `SinkRecords` contain essentially the same information as `SourceRecords`: Kafka topic, partition, offset, the event key and value, and optional headers.

The `flush()` method is used during the offset commit process, which allows tasks to recover from failures and resume from a safe point such that no events will be missed. The method should push any outstanding data to the destination system and then block until the write has been acknowledged. The `offsets` parameter can often be ignored, but is useful in some cases where implementations want to store offset information in the destination store to provide exactly-once delivery. For example, an HDFS connector could do this and use atomic move operations to make sure the `flush()` operation atomically commits the data and offsets to a final location in HDFS.

<a id="kafka-connect-connector-development-guide--errant-record-reporter"></a>

### Errant Record Reporter

When error reporting is enabled for a connector, the connector can use an `ErrantRecordReporter` to report problems with individual records sent to a sink connector. The following example shows how a connector’s `SinkTask` subclass might obtain and use the `ErrantRecordReporter`, safely handling a null reporter when the DLQ is not enabled or when the connector is installed in an older Connect runtime that doesn’t have this reporter feature:

```java
private ErrantRecordReporter reporter;
@Override public void start(Map<String, String> props) {...try {reporter = context.errantRecordReporter(); // may be null if DLQ not enabled } catch (NoSuchMethodException | NoClassDefFoundError e) {// Will occur in Connect runtimes earlier than 2.6 reporter = null;}}
@Override public void put(Collection<SinkRecord> records) {for (SinkRecord record: records) {try {// attempt to process and send record to data sink process(record); } catch(Exception e) {if (reporter != null) {// Send errant record to error reporter reporter.report(record, e); } else {// There's no error reporter, so fail throw new ConnectException("Failed on record", e);}}}}
```

<a id="kafka-connect-connector-development-guide--resuming-from-previous-offsets"></a>

### Resuming from Previous Offsets

The `SourceTask` implementation included a stream ID (the input filename) and offset (position in the file) with each record. The framework uses this to commit offsets periodically so that in the case of a failure, the task can recover and minimize the number of events that are reprocessed and possibly duplicated (or to resume from the most recent offset if Kafka Connect was stopped gracefully, e.g. in standalone mode or due to a job reconfiguration). This commit process is completely automated by the framework, but only the connector knows how to seek back to the right position in the input stream to resume from that location.

To correctly resume upon startup, the task can use the `SourceContext` passed into its `initialize()` method to access the offset data. In `initialize()`, we would add a bit more code to read the offset (if it exists) and seek to that position:

```java
stream = new FileInputStream(filename);
Map<String, Object> offset = context.offsetStorageReader().offset(Collections.singletonMap(FILENAME_FIELD, filename));
if (offset != null) {
    Long lastRecordedOffset = (Long) offset.get("position");
    if (lastRecordedOffset != null)
        seekToOffset(stream, lastRecordedOffset);
}
```

Of course, you might need to read many keys for each of the input streams. The `OffsetStorageReader` interface also allows you to issue bulk reads to efficiently load all offsets, then apply them by seeking each input stream to the appropriate position.

<a id="kafka-connect-connector-development-guide--exactly-once-source-connectors"></a>

### Exactly-once source connectors

<a id="kafka-connect-connector-development-guide--supporting-exactly-once"></a>

#### Supporting exactly-once

With the passing of [KIP-618](https://cwiki.apache.org/confluence/x/Vg0rCQ), Kafka Connect supports exactly-once source connectors as of version 3.3.0. In order for a source connector to take advantage of this support, it must be able to provide meaningful source offsets for each record that it emits, and resume consumption from the external system at the exact position corresponding to any of those offsets without dropping or duplicating messages.

<a id="kafka-connect-connector-development-guide--defining-transaction-boundaries"></a>

#### Defining transaction boundaries

By default, the Kafka Connect framework will create and commit a new Kafka transaction for each batch of records that a source task returns from its `poll` method. However, connectors can also define their own transaction boundaries, which can be enabled by users by setting the `transaction.boundary` property to `connector` in the config for the connector.

If enabled, the connector’s tasks will have access to a `TransactionContext` from their `SourceTaskContext`, which they can use to control when transactions are aborted and committed.

For example, to commit a transaction at least every ten records:

```java
private int recordsSent;
@Override public void start(Map<String, String> props) {this.recordsSent = 0;}
@Override public List<SourceRecord> poll() {List<SourceRecord> records = fetchRecords(); boolean shouldCommit = false; for (SourceRecord record : records) {if (++this.recordsSent >= 10) {shouldCommit = true;}} if (shouldCommit) {this.recordsSent = 0; this.context.transactionContext().commitTransaction();} return records;}
```

Or to commit a transaction for exactly every tenth record:

```java
private int recordsSent;
@Override public void start(Map<String, String> props) {this.recordsSent = 0;}
@Override public List<SourceRecord> poll() {List<SourceRecord> records = fetchRecords(); for (SourceRecord record : records) {if (++this.recordsSent % 10 == 0) {this.context.transactionContext().commitTransaction(record);}} return records;}
```

Most connectors do not need to define their own transaction boundaries. However, it may be useful if files or objects in the source system are broken up into multiple source records, but should be delivered atomically. Additionally, it may be useful if it is impossible to give each source record a unique source offset, if every record with a given offset is delivered within a single transaction.

Note that if the user has not enabled connector-defined transaction boundaries in the connector configuration, the `TransactionContext` returned by `context.transactionContext()` will be `null`.

<a id="kafka-connect-connector-development-guide--validation-apis"></a>

#### Validation APIs

A few additional preflight validation APIs can be implemented by source connector developers.

Some users may require exactly-once semantics from a connector. In this case, they may set the `exactly.once.support` property to `required` in the configuration for the connector. When this happens, the Kafka Connect framework will ask the connector whether it can provide exactly-once semantics with the specified configuration. This is done by invoking the `exactlyOnceSupport` method on the connector.

If a connector doesn’t support exactly-once semantics, it should still implement this method to let users know for certain that it cannot provide exactly-once semantics:

```java
@Override
public ExactlyOnceSupport exactlyOnceSupport(Map<String, String> props) {
    // This connector cannot provide exactly-once semantics under any conditions
    return ExactlyOnceSupport.UNSUPPORTED;
}
```

Otherwise, a connector should examine the configuration, and return `ExactlyOnceSupport.SUPPORTED` if it can provide exactly-once semantics:

```java
@Override
public ExactlyOnceSupport exactlyOnceSupport(Map<String, String> props) {
    // This connector can always provide exactly-once semantics
    return ExactlyOnceSupport.SUPPORTED;
}
```

Additionally, if the user has configured the connector to define its own transaction boundaries, the Kafka Connect framework will ask the connector whether it can define its own transaction boundaries with the specified configuration, using the `canDefineTransactionBoundaries` method:

```java
@Override
public ConnectorTransactionBoundaries canDefineTransactionBoundaries(Map<String, String> props) {
    // This connector can always define its own transaction boundaries
    return ConnectorTransactionBoundaries.SUPPORTED;
}
```

This method should only be implemented for connectors that can define their own transaction boundaries in some cases. If a connector is never able to define its own transaction boundaries, it does not need to implement this method.

<a id="kafka-connect-connector-development-guide--dynamic-inputoutput-streams"></a>
<a id="kafka-connect-connector-development-guide--dynamic-input-output-streams"></a>

## Dynamic Input/Output Streams

Kafka Connect is intended to define bulk data copying jobs, such as copying an entire database rather than creating many jobs to copy each table individually. One consequence of this design is that the set of input or output streams for a connector can vary over time.

Source connectors need to monitor the source system for changes, e.g. table additions/deletions in a database. When they pick up changes, they should notify the framework via the `ConnectorContext` object that reconfiguration is necessary. For example, in a `SourceConnector`:

```java
if (inputsChanged())
    this.context.requestTaskReconfiguration();
```

The framework will promptly request new configuration information and update the tasks, allowing them to gracefully commit their progress before reconfiguring them. Note that in the `SourceConnector` this monitoring is currently left up to the connector implementation. If an extra thread is required to perform this monitoring, the connector must allocate it itself.

Ideally this code for monitoring changes would be isolated to the `Connector` and tasks would not need to worry about them. However, changes can also affect tasks, most commonly when one of their input streams is destroyed in the input system, e.g. if a table is dropped from a database. If the `Task` encounters the issue before the `Connector`, which will be common if the `Connector` needs to poll for changes, the `Task` will need to handle the subsequent error. Thankfully, this can usually be handled simply by catching and handling the appropriate exception.

`SinkConnectors` usually only have to handle the addition of streams, which may translate to new entries in their outputs (e.g., a new database table). The framework manages any changes to the Kafka input, such as when the set of input topics changes because of a regex subscription. `SinkTasks` should expect new input streams, which may require creating new resources in the downstream system, such as a new table in a database. The trickiest situation to handle in these cases may be conflicts between multiple `SinkTasks` seeing a new input stream for the first time and simultaneously trying to create the new resource. `SinkConnectors`, on the other hand, will generally require no special code for handling a dynamic set of streams.

<a id="kafka-connect-connector-development-guide--configuration-validation"></a>

## Configuration Validation

Kafka Connect allows you to validate connector configurations before submitting a connector to be executed and can provide feedback about errors and recommended values. To take advantage of this, connector developers need to provide an implementation of `config()` to expose the configuration definition to the framework.

The following code in `FileStreamSourceConnector` defines the configuration and exposes it to the framework.

```java
static final ConfigDef CONFIG_DEF = new ConfigDef()
    .define(FILE_CONFIG, Type.STRING, null, Importance.HIGH, "Source filename. If not specified, the standard input will be used")
    .define(TOPIC_CONFIG, Type.STRING, ConfigDef.NO_DEFAULT_VALUE, new ConfigDef.NonEmptyString(), Importance.HIGH, "The topic to publish data to")
    .define(TASK_BATCH_SIZE_CONFIG, Type.INT, DEFAULT_TASK_BATCH_SIZE, Importance.LOW,
        "The maximum number of records the source task can read from the file each time it is polled");

public ConfigDef config() {
    return CONFIG_DEF;
}
```

`ConfigDef` class is used for specifying the set of expected configurations. For each configuration, you can specify the name, the type, the default value, the documentation, the group information, the order in the group, the width of the configuration value and the name suitable for display in the UI. Plus, you can provide special validation logic used for single configuration validation by overriding the `Validator` class. Moreover, as there may be dependencies between configurations, for example, the valid values and visibility of a configuration may change according to the values of other configurations. To handle this, `ConfigDef` allows you to specify the dependents of a configuration and to provide an implementation of `Recommender` to get valid values and set visibility of a configuration given the current configuration values.

Also, the `validate()` method in `Connector` provides a default validation implementation which returns a list of allowed configurations together with configuration errors and recommended values for each configuration. However, it does not use the recommended values for configuration validation. You may provide an override of the default implementation for customized configuration validation, which may use the recommended values.

<a id="kafka-connect-connector-development-guide--working-with-schemas"></a>

## Working with Schemas

The FileStream connectors are good examples because they are simple, but they also have trivially structured data – each line is just a string. Almost all practical connectors will need schemas with more complex data formats.

To create more complex data, you’ll need to work with the Kafka Connect `data` API. Most structured records will need to interact with two classes in addition to primitive types: `Schema` and `Struct`.

The API documentation provides a complete reference, but here is a simple example creating a `Schema` and `Struct`:

```java
Schema schema = SchemaBuilder.struct().name(NAME)
    .field("name", Schema.STRING_SCHEMA)
    .field("age", Schema.INT_SCHEMA)
    .field("admin", SchemaBuilder.bool().defaultValue(false).build())
    .build();

Struct struct = new Struct(schema)
    .put("name", "Barbara Liskov")
    .put("age", 75);
```

If you are implementing a source connector, you’ll need to decide when and how to create schemas. Where possible, you should avoid recomputing them as much as possible. For example, if your connector is guaranteed to have a fixed schema, create it statically and reuse a single instance.

However, many connectors will have dynamic schemas. One simple example of this is a database connector. Considering even just a single table, the schema will not be predefined for the entire connector (as it varies from table to table). But it also may not be fixed for a single table over the lifetime of the connector since the user may execute an `ALTER TABLE` command. The connector must be able to detect these changes and react appropriately.

Sink connectors are usually simpler because they are consuming data and therefore do not need to create schemas. However, they should take just as much care to validate that the schemas they receive have the expected format. When the schema does not match – usually indicating the upstream producer is generating invalid data that cannot be correctly translated to the destination system – sink connectors should throw an exception to indicate this error to the system.

---

<a id="kafka-connect-administration"></a>

<a id="kafka-connect-administration--administration"></a>

# Administration

Administration

Kafka Connect’s REST layer provides a set of APIs to enable administration of the cluster. This includes APIs to view the configuration of connectors and the status of their tasks, as well as to alter their current behavior (e.g. changing configuration and restarting tasks).

When a connector is first submitted to the cluster, a rebalance is triggered between the Connect workers in order to distribute the load that consists of the tasks of the new connector. This same rebalancing procedure is also used when connectors increase or decrease the number of tasks they require, when a connector’s configuration is changed, or when a worker is added or removed from the group as part of an intentional upgrade of the Connect cluster or due to a failure.

In versions prior to 2.3.0, the Connect workers would rebalance the full set of connectors and their tasks in the cluster as a simple way to make sure that each worker has approximately the same amount of work. This behavior can be still enabled by setting `connect.protocol=eager`.

Starting with 2.3.0, Kafka Connect is using by default a protocol that performs [incremental cooperative rebalancing](https://cwiki.apache.org/confluence/x/Y4MCBg) that incrementally balances the connectors and tasks across the Connect workers, affecting only tasks that are new, to be removed, or need to move from one worker to another. Other tasks are not stopped and restarted during the rebalance, as they would have been with the old protocol.

If a Connect worker leaves the group, intentionally or due to a failure, Connect waits for `scheduled.rebalance.max.delay.ms` before triggering a rebalance. This delay defaults to five minutes (`300000ms`) to tolerate failures or upgrades of workers without immediately redistributing the load of a departing worker. If this worker returns within the configured delay, it gets its previously assigned tasks in full. However, this means that the tasks will remain unassigned until the time specified by `scheduled.rebalance.max.delay.ms` elapses. If a worker does not return within that time limit, Connect will reassign those tasks among the remaining workers in the Connect cluster.

The new Connect protocol is enabled when all the workers that form the Connect cluster are configured with `connect.protocol=compatible`, which is also the default value when this property is missing. Therefore, upgrading to the new Connect protocol happens automatically when all the workers upgrade to 2.3.0. A rolling upgrade of the Connect cluster will activate incremental cooperative rebalancing when the last worker joins on version 2.3.0.

You can use the REST API to view the current status of a connector and its tasks, including the ID of the worker to which each was assigned. For example, the `GET /connectors/file-source/status` request shows the status of a connector named `file-source`:

```json
{"name": "file-source","connector": {"state": "RUNNING","worker_id": "192.168.1.208:8083" },"tasks": [{"id": 0,"state": "RUNNING","worker_id": "192.168.1.209:8083"}]}
```

Connectors and their tasks publish status updates to a shared topic (configured with `status.storage.topic`) which all workers in the cluster monitor. Because the workers consume this topic asynchronously, there is typically a (short) delay before a state change is visible through the status API. The following states are possible for a connector or one of its tasks:

- **UNASSIGNED:** The connector/task has not yet been assigned to a worker.
- **RUNNING:** The connector/task is running.
- **PAUSED:** The connector/task has been administratively paused.
- **STOPPED:** The connector has been stopped. Note that this state is not applicable to tasks because the tasks for a stopped connector are shut down and won’t be visible in the status API.
- **FAILED:** The connector/task has failed (usually by raising an exception, which is reported in the status output).
- **RESTARTING:** The connector/task is either actively restarting or is expected to restart soon

In most cases, connector and task states will match, though they may be different for short periods of time when changes are occurring or if tasks have failed. For example, when a connector is first started, there may be a noticeable delay before the connector and its tasks have all transitioned to the RUNNING state. States will also diverge when tasks fail since Connect does not automatically restart failed tasks. To restart a connector/task manually, you can use the restart APIs listed above. Note that if you try to restart a task while a rebalance is taking place, Connect will return a 409 (Conflict) status code. You can retry after the rebalance completes, but it might not be necessary since rebalances effectively restart all the connectors and tasks in the cluster.

Starting with 2.5.0, Kafka Connect uses the `status.storage.topic` to also store information related to the topics that each connector is using. Connect Workers use these per-connector topic status updates to respond to requests to the REST endpoint `GET /connectors/{name}/topics` by returning the set of topic names that a connector is using. A request to the REST endpoint `PUT /connectors/{name}/topics/reset` resets the set of active topics for a connector and allows a new set to be populated, based on the connector’s latest pattern of topic usage. Upon connector deletion, the set of the connector’s active topics is also deleted. Topic tracking is enabled by default but can be disabled by setting `topic.tracking.enable=false`. If you want to disallow requests to reset the active topics of connectors during runtime, set the Worker property `topic.tracking.allow.reset=false`.

It’s sometimes useful to temporarily stop the message processing of a connector. For example, if the remote system is undergoing maintenance, it would be preferable for source connectors to stop polling it for new data instead of filling logs with exception spam. For this use case, Connect offers a pause/resume API. While a source connector is paused, Connect will stop polling it for additional records. While a sink connector is paused, Connect will stop pushing new messages to it. The pause state is persistent, so even if you restart the cluster, the connector will not begin message processing again until the task has been resumed. Note that there may be a delay before all of a connector’s tasks have transitioned to the PAUSED state since it may take time for them to finish whatever processing they were in the middle of when being paused. Additionally, failed tasks will not transition to the PAUSED state until they have been restarted.

In 3.5.0, Connect introduced a stop API that completely shuts down the tasks for a connector and deallocates any resources claimed by them. This is different from pausing a connector where tasks are left idling and any resources claimed by them are left allocated (which allows the connector to begin processing data quickly once it is resumed). Stopping a connector is more efficient from a resource usage standpoint than pausing it, but can cause it to take longer to begin processing data once resumed. Note that the offsets for a connector can be only modified via the offsets management endpoints if it is in the stopped state.

<a id="streams"></a>

<a id="streams--kafka-streams"></a>

# Kafka Streams

---

<a id="streams--introduction"></a>

##### [Introduction](#streams-introduction)

<a id="streams--quick-start"></a>

##### [Quick Start](#streams-quickstart)

<a id="streams--write-a-streams-app"></a>

##### [Write a streams app](#streams-tutorial)

<a id="streams--core-concepts"></a>

##### [Core Concepts](#streams-core-concepts)

<a id="streams--architecture"></a>

##### [Architecture](#streams-architecture)

<a id="streams--upgrade-guide"></a>

##### [Upgrade Guide](#streams-upgrade-guide)

<a id="streams--streams-developer-guide"></a>

##### [Streams Developer Guide](#streams-developer-guide)

---

<a id="streams-introduction"></a>

<a id="streams-introduction--introduction"></a>

# Introduction

<a id="streams-introduction--kafka-streams"></a>

# Kafka Streams

<a id="streams-introduction--the-easiest-way-to-write-mission-critical-real-time-applications-and-microservices"></a>

## The easiest way to write mission-critical real-time applications and microservices

Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in Kafka clusters. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology.

<a id="streams-introduction--tour-of-the-streams-api"></a>

## Tour of the Streams API

<a id="streams-introduction--1.-intro-to-streams"></a>

#### 1. Intro to Streams

<a id="streams-introduction--2.-creating-a-streams-application"></a>

#### 2. Creating a Streams Application

<a id="streams-introduction--3.-transforming-data-pt.-1"></a>

#### 3. Transforming Data Pt. 1

<a id="streams-introduction--4.-transforming-data-pt.-2"></a>

#### 4. Transforming Data Pt. 2

---

<a id="streams-introduction--why-youll-love-using-kafka-streams"></a>
<a id="streams-introduction--why-you-ll-love-using-kafka-streams"></a>

## Why you’ll love using Kafka Streams!

- Elastic, highly scalable, fault-tolerant
- Deploy to containers, VMs, bare metal, cloud
- Equally viable for small, medium, & large use cases
- Fully integrated with Kafka security
- Write standard Java and Scala applications
- Exactly-once processing semantics
- No separate processing cluster required
- Develop on Mac, Linux, Windows

[Write your first app](#documentation-streams-tutorial)

---

<a id="streams-introduction--kafka-streams-use-cases"></a>

## Kafka Streams use cases

[The New York Times uses Apache Kafka](https://open.nytimes.com/publishing-with-apache-kafka-at-the-new-york-times-7f0e3b7d2077) and the Kafka Streams API to store and distribute, in real-time, published content to the various applications and systems that make it available to the readers.

[Pinterest uses Apache Kafka and the Kafka Streams API](https://medium.com/@Pinterest_Engineering/using-kafka-streams-api-for-predictive-budgeting-9f58d206c996) at large scale to power the real-time, predictive budgeting system of their advertising infrastructure. With Kafka Streams, spend predictions are more accurate than ever.

As the leading online fashion retailer in Europe, Zalando uses Kafka as an ESB (Enterprise Service Bus), which helps us in transitioning from a monolithic to a micro services architecture. Using Kafka for processing event streams enables our technical team to do near-real time business intelligence.

LINE uses Apache Kafka as a central datahub for our services to communicate to one another. Hundreds of billions of messages are produced daily and are used to execute various business logic, threat detection, search indexing and data analysis. LINE leverages Kafka Streams to reliably transform and filter topics enabling sub topics consumers can efficiently consume, meanwhile retaining easy maintainability thanks to its sophisticated yet minimal code base.

Rabobank is one of the 3 largest banks in the Netherlands. Its digital nervous system, the Business Event Bus, is powered by Apache Kafka. It is used by an increasing amount of financial processes and services, one which is Rabo Alerts. This service alerts customers in real-time upon financial events and is built using Kafka Streams.

We use Apache Kafka (and Kafka Streams) to collect and ingest all of our game service logs (including analytics, server, or access logs). Apache Kafka has been one of the core components of our data pipeline from early 2015.

ironSource powers the growth of the world's top games, using Apache Kafka as the backbone infrastructure for the async messaging of millions of events per second that run through their industry-leading game growth platform. In addition ironSource uses the Kafka Streams API to handle multiple real-time use cases, such as budget management, monitoring and alerting.

Kpow is an enterprise-grade toolkit that provides a rich, data-oriented UI and secure API for Apache Kafka. It's designed to give engineers deep visibility and control over their Kafka clusters, Schema Registry, Kafka Connect, and Kafka Streams applications. Offering multiple deployment options for cloud or on-premise environments, Kpow works with any Kafka distribution and integrates with enterprise security systems for authentication and role-based access.

Ksolves delivers end-to-end [Apache Kafka services](https://www.ksolves.com/apache-kafka-development-company), including seamless Kafka implementation, cluster setup, and configuration tailored to your business needs. Our expert team ensures real-time data streaming with Kafka Streams, high-throughput message processing, and fault-tolerant architecture. From Kafka integration with existing systems to performance tuning and ongoing support, Ksolves empowers businesses to build scalable, reliable, and efficient data pipelines effortlessly.

La Redoute, the digital platform for families, uses Kafka as a central nervous system to decouple its application through business events. It enables a decentralized, event-driven architecture bringing near-real-time data reporting, analytics and emerging AI-pipelines combining Kafka Connect, Kafka Streams and KSQL.

Nuuly, a clothing rental subscription from the Urban Outfitters family of brands, uses Kafka as a central nervous system to integrate our front-end customer experience with real-time inventory management and operations at our distribution center. Nuuly relies on Kafka Streams and Kafka Connect, coupled with data science and machine learning to provide in-the-moment business intelligence and to tailor a personalized rental experience to our customers.

Recursion uses Kafka Streams to power its data pipeline for its drug discovery efforts. Kafka is used to to coordinate various services across the company. For more information about the use case see [this Kafka Summit talk](https://www.confluent.io/kafka-summit-san-francisco-2019/discovering-drugs-with-kafka-streams).

Salesforce adopted Apache Kafka to implement a [pub/sub architecture system](https://engineering.salesforce.com/expanding-visibility-with-apache-kafka-e305b12c4aba) and to securely add an enterprise-ready, [event-driven layer](https://engineering.salesforce.com/how-apache-kafka-inspired-our-platform-events-architecture-2f351fe4cf63) to our multi-tenant system. With Kafka as the central nervous system of our microservices architecture, [Kafka Streams applications](https://engineering.salesforce.com/real-time-einstein-insights-using-kafka-streams-ca94008c2c6f) perform a variety of operations to generate useful real-time insights for our customers.

At Schrödinger, Kafka powers our physics-based computational platform by feeding data into our predictive modeling, data analytics, and collaboration services thus enabling rapid exploration of chemical space. More specifically, Kafka is used as a distributed high speed event bus while Kafka Connect and Kafka Streams are the basic components of our streaming Change Data Capture framework used by LiveDesign, our enterprise informatics solution. Currently, Schrödinger processes billions of molecules per week and our Kafka-powered data pipeline enables us to scale our architecture easily and push this even further.

<a id="streams-introduction--hello-kafka-streams"></a>

## Hello Kafka Streams

The code example below implements a WordCount application that is elastic, highly scalable, fault-tolerant, stateful, and ready to run in production at large scale

```java
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.utils.Bytes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.KTable;
import org.apache.kafka.streams.kstream.Materialized;
import org.apache.kafka.streams.kstream.Produced;
import org.apache.kafka.streams.state.KeyValueStore;

import java.util.Arrays;
import java.util.Properties;

public class WordCountApplication {

   public static void main(final String[] args) throws Exception {
       Properties props = new Properties();
       props.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount-application");
       props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-broker1:9092");
       props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
       props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

       StreamsBuilder builder = new StreamsBuilder();
       KStream<String, String> textLines = builder.stream("TextLinesTopic");
       KTable<String, Long> wordCounts = textLines
           .flatMapValues(textLine -> Arrays.asList(textLine.toLowerCase().split("\W+")))
           .groupBy((key, word) -> word)
           .count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("counts-store"));
       wordCounts.toStream().to("WordsWithCountsTopic", Produced.with(Serdes.String(), Serdes.Long()));

       KafkaStreams streams = new KafkaStreams(builder.build(), props);
       streams.start();
   }

}
```

```scala
import java.util.Properties
import java.util.concurrent.TimeUnit

import org.apache.kafka.streams.kstream.Materialized
import org.apache.kafka.streams.scala.ImplicitConversions._
import org.apache.kafka.streams.scala._
import org.apache.kafka.streams.scala.kstream._
import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}

object WordCountApplication extends App {
  import Serdes._

  val props: Properties = {
    val p = new Properties()
    p.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount-application")
    p.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-broker1:9092")
    p
  }

  val builder: StreamsBuilder = new StreamsBuilder
  val textLines: KStream[String, String] = builder.stream[String, String]("TextLinesTopic")
  val wordCounts: KTable[String, Long] = textLines
    .flatMapValues(textLine => textLine.toLowerCase.split("\W+"))
    .groupBy((_, word) => word)
    .count()(Materialized.as("counts-store"))
  wordCounts.toStream.to("WordsWithCountsTopic")

  val streams: KafkaStreams = new KafkaStreams(builder.build(), props)
  streams.start()

  sys.ShutdownHookThread {
     streams.close(10, TimeUnit.SECONDS)
  }
}
```

---

<a id="streams-quickstart"></a>

<a id="streams-quickstart--quick-start"></a>

# Quick Start

<a id="streams-quickstart--run-kafka-streams-demo-application"></a>

# Run Kafka Streams Demo Application

This tutorial assumes you are starting fresh and have no existing Kafka data. However, if you have already started Kafka, feel free to skip the first two steps.

Kafka Streams is a client library for building mission-critical real-time applications and microservices, where the input and/or output data is stored in Kafka clusters. Kafka Streams combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology to make these applications highly scalable, elastic, fault-tolerant, distributed, and much more.

This quickstart example will demonstrate how to run a streaming application coded in this library. Here is the gist of the `[WordCountDemo](https://github.com/apache/kafka/blob/4.3/streams/examples/src/main/java/org/apache/kafka/streams/examples/wordcount/WordCountDemo.java)` example code.

```
// Serializers/deserializers (serde) for String and Long types
final Serde<String> stringSerde = Serdes.String();
final Serde<Long> longSerde = Serdes.Long();

// Construct a `KStream` from the input topic "streams-plaintext-input", where message values
// represent lines of text (for the sake of this example, we ignore whatever may be stored
// in the message keys).
KStream<String, String> textLines = builder.stream(
      "streams-plaintext-input",
      Consumed.with(stringSerde, stringSerde)
    );

KTable<String, Long> wordCounts = textLines
    // Split each text line, by whitespace, into words.
    .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\W+")))

    // Group the text words as message keys
    .groupBy((key, value) -> value)

    // Count the occurrences of each word (message key).
    .count();

// Store the running counts as a changelog stream to the output topic.
wordCounts.toStream().to("streams-wordcount-output", Produced.with(Serdes.String(), Serdes.Long()));
```

It implements the WordCount algorithm, which computes a word occurrence histogram from the input text. However, unlike other WordCount examples you might have seen before that operate on bounded data, the WordCount demo application behaves slightly differently because it is designed to operate on an **infinite, unbounded stream** of data. Similar to the bounded variant, it is a stateful algorithm that tracks and updates the counts of words. However, since it must assume potentially unbounded input data, it will periodically output its current state and results while continuing to process more data because it cannot know when it has processed “all” the input data.

As the first step, we will start Kafka (unless you already have it started) and then we will prepare input data to a Kafka topic, which will subsequently be processed by a Kafka Streams application.

<a id="streams-quickstart--step-1-download-the-code"></a>
<a id="streams-quickstart--step-1:-download-the-code"></a>

### Step 1: Download the code

[Download](https://www.apache.org/dyn/closer.cgi?path=/kafka/4.3.1/kafka_2.13-4.3.1.tgz "Kafka downloads") the 4.3.1 release and un-tar it. Note that there are multiple downloadable Scala versions and we choose to use the recommended version (2.13) here:

```
$ tar -xzf kafka_2.13-4.3.1.tgz
$ cd kafka_2.13-4.3.1
```

<a id="streams-quickstart--step-2-start-the-kafka-server"></a>
<a id="streams-quickstart--step-2:-start-the-kafka-server"></a>

### Step 2: Start the Kafka server

Generate a Cluster UUID

```
$ KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

Format Log Directories

```
$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
```

Start the Kafka Server

```
$ bin/kafka-server-start.sh config/server.properties
```

<a id="streams-quickstart--step-3-prepare-input-topic-and-start-kafka-producer"></a>
<a id="streams-quickstart--step-3:-prepare-input-topic-and-start-kafka-producer"></a>

### Step 3: Prepare input topic and start Kafka producer

Next, we create the input topic named **streams-plaintext-input** and the output topic named **streams-wordcount-output** :

```
$ bin/kafka-topics.sh --create \ --bootstrap-server localhost:9092 \ --replication-factor 1 \ --partitions 1 \ --topic streams-plaintext-input Created topic "streams-plaintext-input".
```

Note: we create the output topic with compaction enabled because the output stream is a changelog stream (cf. explanation of application output below).

```
$ bin/kafka-topics.sh --create \ --bootstrap-server localhost:9092 \ --replication-factor 1 \ --partitions 1 \ --topic streams-wordcount-output \ --config cleanup.policy=compact Created topic "streams-wordcount-output".
```

The created topic can be described with the same **kafka-topics** tool:

```
$ bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --exclude-internal Topic:streams-wordcount-output PartitionCount:1 ReplicationFactor:1 Configs:cleanup.policy=compact,segment.bytes=1073741824 Topic: streams-wordcount-output Partition: 0 Leader: 0 Replicas: 0 Isr: 0 Topic:streams-plaintext-input PartitionCount:1 ReplicationFactor:1 Configs:segment.bytes=1073741824 Topic: streams-plaintext-input Partition: 0 Leader: 0 Replicas: 0 Isr: 0
```

<a id="streams-quickstart--step-4-start-the-wordcount-application"></a>
<a id="streams-quickstart--step-4:-start-the-wordcount-application"></a>

### Step 4: Start the Wordcount Application

The following command starts the WordCount demo application:

```
$ bin/kafka-run-class.sh org.apache.kafka.streams.examples.wordcount.WordCountDemo
```

The demo application will read from the input topic **streams-plaintext-input** , perform the computations of the WordCount algorithm on each of the read messages, and continuously write its current results to the output topic **streams-wordcount-output**. Hence there won’t be any STDOUT output except log entries as the results are written back into in Kafka.

Optionally, use `group.protocol=streams` to enable the new rebalancing protocol introduced in KIP-1071. This shifts task assignment logic from the client to the broker, reducing rebalance times and eliminating stop-the-world rebalances.

```
$ echo "group.protocol=streams" > streams.properties
$ bin/kafka-run-class.sh org.apache.kafka.streams.examples.wordcount.WordCountDemo streams.properties
```

Now we can start the console producer in a separate terminal to write some input data to this topic:

```
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic streams-plaintext-input
```

and inspect the output of the WordCount demo application by reading from its output topic with the console consumer in a separate terminal:

```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \ --topic streams-wordcount-output \ --from-beginning \ --formatter-property print.key=true \ --formatter-property print.value=true \ --formatter-property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \ --formatter-property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer
```

<a id="streams-quickstart--step-5-process-some-data"></a>
<a id="streams-quickstart--step-5:-process-some-data"></a>

### Step 5: Process some data

Now let’s write some message with the console producer into the input topic **streams-plaintext-input** by entering a single line of text and then hit . This will send a new message to the input topic, where the message key is null and the message value is the string encoded text line that you just entered (in practice, input data for applications will typically be streaming continuously into Kafka, rather than being manually entered as we do in this quickstart):

```
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic streams-plaintext-input >all streams lead to kafka
```

This message will be processed by the Wordcount application and the following output data will be written to the **streams-wordcount-output** topic and printed by the console consumer:

```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \ --topic streams-wordcount-output \ --from-beginning \ --formatter-property print.key=true \ --formatter-property print.value=true \ --formatter-property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \ --formatter-property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer

all	    1
streams	1
lead	1
to	    1
kafka	1
```

Here, the first column is the Kafka message key in `java.lang.String` format and represents a word that is being counted, and the second column is the message value in `java.lang.Long`format, representing the word’s latest count.

Now let’s continue writing one more message with the console producer into the input topic **streams-plaintext-input**. Enter the text line “hello kafka streams” and hit . Your terminal should look as follows:

```
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic streams-plaintext-input >all streams lead to kafka >hello kafka streams
```

In your other terminal in which the console consumer is running, you will observe that the WordCount application wrote new output data:

```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \ --topic streams-wordcount-output \ --from-beginning \ --formatter-property print.key=true \ --formatter-property print.value=true \ --formatter-property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \ --formatter-property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer

all	    1
streams	1
lead	1
to	    1
kafka	1
hello	1
kafka	2
streams	2
```

Here the last printed lines **kafka 2** and **streams 2** indicate updates to the keys **kafka** and **streams** whose counts have been incremented from **1** to **2**. Whenever you write further input messages to the input topic, you will observe new messages being added to the **streams-wordcount-output** topic, representing the most recent word counts as computed by the WordCount application. Let’s enter one final input text line “join kafka summit” and hit in the console producer to the input topic **streams-plaintext-input** before we wrap up this quickstart:

```
$ bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic streams-plaintext-input >all streams lead to kafka >hello kafka streams >join kafka summit
```

The **streams-wordcount-output** topic will subsequently show the corresponding updated word counts (see last three lines):

```
$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 \ --topic streams-wordcount-output \ --from-beginning \ --formatter-property print.key=true \ --formatter-property print.value=true \ --formatter-property key.deserializer=org.apache.kafka.common.serialization.StringDeserializer \ --formatter-property value.deserializer=org.apache.kafka.common.serialization.LongDeserializer

all	    1
streams	1
lead	1
to	    1
kafka	1
hello	1
kafka	2
streams	2
join	1
kafka	3
summit	1
```

As one can see, outputs of the Wordcount application is actually a continuous stream of updates, where each output record (i.e. each line in the original output above) is an updated count of a single word, aka record key such as “kafka”. For multiple records with the same key, each later record is an update of the previous one.

The two diagrams below illustrate what is essentially happening behind the scenes. The first column shows the evolution of the current state of the `KTable<String, Long>` that is counting word occurrences for `count`. The second column shows the change records that result from state updates to the KTable and that are being sent to the output Kafka topic **streams-wordcount-output**.

First the text line “all streams lead to kafka” is being processed. The `KTable` is being built up as each new word results in a new table entry (highlighted with a green background), and a corresponding change record is sent to the downstream `KStream`.

When the second text line “hello kafka streams” is processed, we observe, for the first time, that existing entries in the `KTable` are being updated (here: for the words “kafka” and for “streams”). And again, change records are being sent to the output topic.

And so on (we skip the illustration of how the third line is being processed). This explains why the output topic has the contents we showed above, because it contains the full record of changes.

Looking beyond the scope of this concrete example, what Kafka Streams is doing here is to leverage the duality between a table and a changelog stream (here: table = the KTable, changelog stream = the downstream KStream): you can publish every change of the table to a stream, and if you consume the entire changelog stream from beginning to end, you can reconstruct the contents of the table.

<a id="streams-quickstart--step-6-teardown-the-application"></a>
<a id="streams-quickstart--step-6:-teardown-the-application"></a>

### Step 6: Teardown the application

You can now stop the console consumer, the console producer, the Wordcount application, the Kafka broker in order via **Ctrl-C**.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)

---

<a id="streams-tutorial"></a>

<a id="streams-tutorial--write-a-streams-app"></a>

# Write a streams app

<a id="streams-tutorial--tutorial-write-a-kafka-streams-application"></a>
<a id="streams-tutorial--tutorial:-write-a-kafka-streams-application"></a>

# Tutorial: Write a Kafka Streams Application

In this guide we will start from scratch on setting up your own project to write a stream processing application using Kafka Streams. It is highly recommended to read the [quickstart](#documentation-streams-quickstart) first on how to run a Streams application written in Kafka Streams if you have not done so.

<a id="streams-tutorial--setting-up-a-maven-project"></a>

### Setting up a Maven Project

We are going to use a Kafka Streams Maven Archetype for creating a Streams project structure with the following commands:

```
$ mvn archetype:generate \
-DarchetypeGroupId=org.apache.kafka \
-DarchetypeArtifactId=streams-quickstart-java \
-DarchetypeVersion=4.3.1 \
-DgroupId=streams.examples \
-DartifactId=streams-quickstart \
-Dversion=0.1 \
-Dpackage=myapps
```

You can use a different value for `groupId`, `artifactId` and `package` parameters if you like. Assuming the above parameter values are used, this command will create a project structure that looks like this:

```
$ tree streams-quickstart streams-quickstart |-- pom.xml |-- src |-- main |-- java | |-- myapps | |-- LineSplit.java | |-- Pipe.java | |-- WordCount.java |-- resources |-- log4j.properties
```

The `pom.xml` file included in the project already has the Streams dependency defined. Note, that the generated `pom.xml` targets Java 11.

There are already several example programs written with Streams library under `src/main/java`. Since we are going to start writing such programs from scratch, we can now delete these examples:

```
$ cd streams-quickstart
$ rm src/main/java/myapps/*.java
```

<a id="streams-tutorial--writing-a-first-streams-application-pipe"></a>
<a id="streams-tutorial--writing-a-first-streams-application:-pipe"></a>

### Writing a first Streams application: Pipe

It’s coding time now! Feel free to open your favorite IDE and import this Maven project, or simply open a text editor and create a java file under `src/main/java/myapps`. Let’s name it `Pipe.java`:

```
package myapps;
public class Pipe {
public static void main(String[] args) throws Exception {
}}
```

We are going to fill in the `main` function to write this pipe program. Note that we will not list the import statements as we go since IDEs can usually add them automatically. However if you are using a text editor you need to manually add the imports, and at the end of this section we’ll show the complete code snippet with import statement for you.

The first step to write a Streams application is to create a `java.util.Properties` map to specify different Streams execution configuration values as defined in `StreamsConfig`. A couple of important configuration values you need to set are: `StreamsConfig.BOOTSTRAP_SERVERS_CONFIG`, which specifies a list of host/port pairs to use for establishing the initial connection to the Kafka cluster, and `StreamsConfig.APPLICATION_ID_CONFIG`, which gives the unique identifier of your Streams application to distinguish itself with other applications talking to the same Kafka cluster:

```
Properties props = new Properties();
props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-pipe");
props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");    // assuming that the Kafka broker this application is talking to runs on local machine with port 9092
```

In addition, you can customize other configurations in the same map, for example, default serialization and deserialization libraries for the record key-value pairs:

```
props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
```

For a full list of configurations of Kafka Streams please refer to this [table](#documentation--streamsconfigs).

Next we will define the computational logic of our Streams application. In Kafka Streams this computational logic is defined as a `topology` of connected processor nodes. We can use a topology builder to construct such a topology,

```
final StreamsBuilder builder = new StreamsBuilder();
```

And then create a source stream from a Kafka topic named `streams-plaintext-input` using this topology builder:

```
KStream<String, String> source = builder.stream("streams-plaintext-input");
```

Now we get a `KStream` that is continuously generating records from its source Kafka topic `streams-plaintext-input`. The records are organized as `String` typed key-value pairs. The simplest thing we can do with this stream is to write it into another Kafka topic, say it’s named `streams-pipe-output`:

```
source.to("streams-pipe-output");
```

Note that we can also concatenate the above two lines into a single line as:

```
builder.stream("streams-plaintext-input").to("streams-pipe-output");
```

We can inspect what kind of `topology` is created from this builder by doing the following:

```
final Topology topology = builder.build();
```

And print its description to standard output as:

```
System.out.println(topology.describe());
```

If we just stop here, compile and run the program, it will output the following information:

```
$ mvn clean package
$ mvn exec:java -Dexec.mainClass=myapps.Pipe Sub-topologies:Sub-topology: 0 Source: KSTREAM-SOURCE-0000000000(topics: streams-plaintext-input) --> KSTREAM-SINK-0000000001 Sink: KSTREAM-SINK-0000000001(topic: streams-pipe-output) <-- KSTREAM-SOURCE-0000000000 Global Stores:none
```

As shown above, it illustrates that the constructed topology has two processor nodes, a source node `KSTREAM-SOURCE-0000000000` and a sink node `KSTREAM-SINK-0000000001`. `KSTREAM-SOURCE-0000000000` continuously read records from Kafka topic `streams-plaintext-input` and pipe them to its downstream node `KSTREAM-SINK-0000000001`; `KSTREAM-SINK-0000000001` will write each of its received record in order to another Kafka topic `streams-pipe-output` (the `-->` and `<--` arrows dictates the downstream and upstream processor nodes of this node, i.e. “children” and “parents” within the topology graph). It also illustrates that this simple topology has no global state stores associated with it (we will talk about state stores more in the following sections).

Note that we can always describe the topology as we did above at any given point while we are building it in the code, so as a user you can interactively “try and taste” your computational logic defined in the topology until you are happy with it. Suppose we are already done with this simple topology that just pipes data from one Kafka topic to another in an endless streaming manner, we can now construct the Streams client with the two components we have just constructed above: the configuration map specified in a `java.util.Properties` instance and the `Topology` object.

```
final KafkaStreams streams = new KafkaStreams(topology, props);
```

By calling its `start()` function we can trigger the execution of this client. The execution won’t stop until `close()` is called on this client. We can, for example, add a shutdown hook with a countdown latch to capture a user interrupt and close the client upon terminating this program:

```
final CountDownLatch latch = new CountDownLatch(1);

// attach shutdown handler to catch control-c
Runtime.getRuntime().addShutdownHook(new Thread("streams-shutdown-hook") {
    @Override
    public void run() {
        streams.close();
        latch.countDown();
    }
});

try {
    streams.start();
    latch.await();
} catch (Throwable e) {
    System.exit(1);
}
System.exit(0);
```

The complete code so far looks like this:

```
package myapps;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;

import java.util.Properties;
import java.util.concurrent.CountDownLatch;

public class Pipe {

    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-pipe");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        final StreamsBuilder builder = new StreamsBuilder();

        builder.stream("streams-plaintext-input").to("streams-pipe-output");

        final Topology topology = builder.build();

        final KafkaStreams streams = new KafkaStreams(topology, props);
        final CountDownLatch latch = new CountDownLatch(1);

        // attach shutdown handler to catch control-c
        Runtime.getRuntime().addShutdownHook(new Thread("streams-shutdown-hook") {
            @Override
            public void run() {
                streams.close();
                latch.countDown();
            }
        });

        try {
            streams.start();
            latch.await();
        } catch (Throwable e) {
            System.exit(1);
        }
        System.exit(0);
    }
}
```

If you already have the Kafka broker up and running at `localhost:9092`, and the topics `streams-plaintext-input` and `streams-pipe-output` created on that broker, you can run this code in your IDE or on the command line, using Maven:

```
$ mvn clean package
$ mvn exec:java -Dexec.mainClass=myapps.Pipe
```

For detailed instructions on how to run a Streams application and observe its computing results, please read the [Play with a Streams Application](#documentation-streams-quickstart) section. We will not talk about this in the rest of this section.

<a id="streams-tutorial--writing-a-second-streams-application-line-split"></a>
<a id="streams-tutorial--writing-a-second-streams-application:-line-split"></a>

### Writing a second Streams application: Line Split

We have learned how to construct a Streams client with its two key components: the `StreamsConfig` and `Topology`. Now let’s move on to add some real processing logic by augmenting the current topology. We can first create another program by first copy the existing `Pipe.java` class:

```
$ cp src/main/java/myapps/Pipe.java src/main/java/myapps/LineSplit.java
```

And change its class name as well as the application id config to distinguish with the original program:

```
public class LineSplit {
public static void main(String[] args) throws Exception {Properties props = new Properties(); props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-linesplit"); // ...}}
```

Since each of the source stream’s record is a `String` typed key-value pair, let’s treat the value string as a text line and split it into words with a `FlatMapValues` operator:

```
KStream<String, String> source = builder.stream("streams-plaintext-input");
KStream<String, String> words = source.flatMapValues(new ValueMapper<String, Iterable<String>>() {
            @Override
            public Iterable<String> apply(String value) {
                return Arrays.asList(value.split("\W+"));
            }
        });
```

The operator will take the `source` stream as its input, and generate a new stream named `words` by processing each record from its source stream in order and breaking its value string into a list of words, and producing each word as a new record to the output `words` stream. This is a stateless operator that does not need to keep track of any previously received records or processed results. Note if you are using JDK 8 you can use lambda expression and simplify the above code as:

```
KStream<String, String> source = builder.stream("streams-plaintext-input");
KStream<String, String> words = source.flatMapValues(value -> Arrays.asList(value.split("\W+")));
```

And finally we can write the word stream back into another Kafka topic, say `streams-linesplit-output`. Again, these two steps can be concatenated as the following (assuming lambda expression is used):

```
KStream<String, String> source = builder.stream("streams-plaintext-input");
source.flatMapValues(value -> Arrays.asList(value.split("\W+")))
      .to("streams-linesplit-output");
```

If we now describe this augmented topology as `System.out.println(topology.describe())`, we will get the following:

```
$ mvn clean package
$ mvn exec:java -Dexec.mainClass=myapps.LineSplit Sub-topologies:Sub-topology: 0 Source: KSTREAM-SOURCE-0000000000(topics: streams-plaintext-input) --> KSTREAM-FLATMAPVALUES-0000000001 Processor: KSTREAM-FLATMAPVALUES-0000000001(stores: []) --> KSTREAM-SINK-0000000002 <-- KSTREAM-SOURCE-0000000000 Sink: KSTREAM-SINK-0000000002(topic: streams-linesplit-output) <-- KSTREAM-FLATMAPVALUES-0000000001 Global Stores:none
```

As we can see above, a new processor node `KSTREAM-FLATMAPVALUES-0000000001` is injected into the topology between the original source and sink nodes. It takes the source node as its parent and the sink node as its child. In other words, each record fetched by the source node will first traverse to the newly added `KSTREAM-FLATMAPVALUES-0000000001` node to be processed, and one or more new records will be generated as a result. They will continue traverse down to the sink node to be written back to Kafka. Note this processor node is “stateless” as it is not associated with any stores (i.e. `(stores: [])`).

The complete code looks like this (assuming lambda expression is used):

```
package myapps;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KStream;

import java.util.Arrays;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

public class LineSplit {

    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-linesplit");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        final StreamsBuilder builder = new StreamsBuilder();

        KStream<String, String> source = builder.stream("streams-plaintext-input");
        source.flatMapValues(value -> Arrays.asList(value.split("\W+")))
              .to("streams-linesplit-output");

        final Topology topology = builder.build();
        final KafkaStreams streams = new KafkaStreams(topology, props);
        final CountDownLatch latch = new CountDownLatch(1);

        // ... same as Pipe.java above
    }
}
```

<a id="streams-tutorial--writing-a-third-streams-application-wordcount"></a>
<a id="streams-tutorial--writing-a-third-streams-application:-wordcount"></a>

### Writing a third Streams application: Wordcount

Let’s now take a step further to add some “stateful” computations to the topology by counting the occurrence of the words split from the source text stream. Following similar steps let’s create another program based on the `LineSplit.java` class:

```
public class WordCount {
public static void main(String[] args) throws Exception {Properties props = new Properties(); props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-wordcount"); // ...}}
```

In order to count the words we can first modify the `flatMapValues` operator to treat all of them as lower case (assuming lambda expression is used):

```
source.flatMapValues(new ValueMapper<String, Iterable<String>>() {
    @Override
    public Iterable<String> apply(String value) {
        return Arrays.asList(value.toLowerCase(Locale.getDefault()).split("\W+"));
    }
});
```

In order to do the counting aggregation we have to first specify that we want to key the stream on the value string, i.e. the lower cased word, with a `groupBy` operator. This operator generate a new grouped stream, which can then be aggregated by a `count` operator, which generates a running count on each of the grouped keys:

```
KTable<String, Long> counts =source.flatMapValues(new ValueMapper<String, Iterable<String>>() {@Override public Iterable<String> apply(String value) {return Arrays.asList(value.toLowerCase(Locale.getDefault()).split("\W+"));} }) .groupBy(new KeyValueMapper<String, String, String>() {@Override public String apply(String key, String value) {return value;} }) // Materialize the result into a KeyValueStore named "counts-store".// The Materialized store is always of type <Bytes, byte[]> as this is the format of the inner most store..count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>> as("counts-store"));
```

Note that the `count` operator has a `Materialized` parameter that specifies that the running count should be stored in a state store named `counts-store`. This `counts-store` store can be queried in real-time, with details described in the [Developer Manual](#documentation-streams-developer-guide--streams_interactive_queries).

We can also write the `counts` KTable’s changelog stream back into another Kafka topic, say `streams-wordcount-output`. Because the result is a changelog stream, the output topic `streams-wordcount-output` should be configured with log compaction enabled. Note that this time the value type is no longer `String` but `Long`, so the default serialization classes are not viable for writing it to Kafka anymore. We need to provide overridden serialization methods for `Long` types, otherwise a runtime exception will be thrown:

```
counts.toStream().to("streams-wordcount-output", Produced.with(Serdes.String(), Serdes.Long()));
```

Note that in order to read the changelog stream from topic `streams-wordcount-output`, one needs to set the value deserialization as `org.apache.kafka.common.serialization.LongDeserializer`. Details of this can be found in the [Play with a Streams Application](#documentation-streams-quickstart) section. Assuming lambda expression from JDK 8 can be used, the above code can be simplified as:

```
KStream<String, String> source = builder.stream("streams-plaintext-input");
source.flatMapValues(value -> Arrays.asList(value.toLowerCase(Locale.getDefault()).split("\W+")))
      .groupBy((key, value) -> value)
      .count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("counts-store"))
      .toStream()
      .to("streams-wordcount-output", Produced.with(Serdes.String(), Serdes.Long()));
```

If we again describe this augmented topology as `System.out.println(topology.describe())`, we will get the following:

```
$ mvn clean package
$ mvn exec:java -Dexec.mainClass=myapps.WordCount Sub-topologies:Sub-topology: 0 Source: KSTREAM-SOURCE-0000000000(topics: streams-plaintext-input) --> KSTREAM-FLATMAPVALUES-0000000001 Processor: KSTREAM-FLATMAPVALUES-0000000001(stores: []) --> KSTREAM-KEY-SELECT-0000000002 <-- KSTREAM-SOURCE-0000000000 Processor: KSTREAM-KEY-SELECT-0000000002(stores: []) --> KSTREAM-FILTER-0000000005 <-- KSTREAM-FLATMAPVALUES-0000000001 Processor: KSTREAM-FILTER-0000000005(stores: []) --> KSTREAM-SINK-0000000004 <-- KSTREAM-KEY-SELECT-0000000002 Sink: KSTREAM-SINK-0000000004(topic: counts-store-repartition) <-- KSTREAM-FILTER-0000000005 Sub-topology: 1 Source: KSTREAM-SOURCE-0000000006(topics: counts-store-repartition) --> KSTREAM-AGGREGATE-0000000003 Processor: KSTREAM-AGGREGATE-0000000003(stores: [counts-store]) --> KTABLE-TOSTREAM-0000000007 <-- KSTREAM-SOURCE-0000000006 Processor: KTABLE-TOSTREAM-0000000007(stores: []) --> KSTREAM-SINK-0000000008 <-- KSTREAM-AGGREGATE-0000000003 Sink: KSTREAM-SINK-0000000008(topic: streams-wordcount-output) <-- KTABLE-TOSTREAM-0000000007 Global Stores:none
```

As we can see above, the topology now contains two disconnected sub-topologies. The first sub-topology’s sink node `KSTREAM-SINK-0000000004` will write to a repartition topic `counts-store-repartition`, which will be read by the second sub-topology’s source node `KSTREAM-SOURCE-0000000006`. The repartition topic is used to “shuffle” the source stream by its aggregation key, which is in this case the value string. In addition, inside the first sub-topology a stateless `KSTREAM-FILTER-0000000005` node is injected between the grouping `KSTREAM-KEY-SELECT-0000000002` node and the sink node to filter out any intermediate record whose aggregate key is empty.

In the second sub-topology, the aggregation node `KSTREAM-AGGREGATE-0000000003` is associated with a state store named `counts-store` (the name is specified by the user in the `count` operator). Upon receiving each record from its upcoming stream source node, the aggregation processor will first query its associated `counts-store` store to get the current count for that key, augment by one, and then write the new count back to the store. Each updated count for the key will also be piped downstream to the `KTABLE-TOSTREAM-0000000007` node, which interpret this update stream as a record stream before further piping to the sink node `KSTREAM-SINK-0000000008` for writing back to Kafka.

The complete code looks like this (assuming lambda expression is used):

```
package myapps;

import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.common.utils.Bytes;
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.Materialized;
import org.apache.kafka.streams.kstream.Produced;
import org.apache.kafka.streams.state.KeyValueStore;

import java.util.Arrays;
import java.util.Locale;
import java.util.Properties;
import java.util.concurrent.CountDownLatch;

public class WordCount {

    public static void main(String[] args) throws Exception {
        Properties props = new Properties();
        props.put(StreamsConfig.APPLICATION_ID_CONFIG, "streams-wordcount");
        props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());

        final StreamsBuilder builder = new StreamsBuilder();

        KStream<String, String> source = builder.stream("streams-plaintext-input");
        source.flatMapValues(value -> Arrays.asList(value.toLowerCase(Locale.getDefault()).split("\W+")))
              .groupBy((key, value) -> value)
              .count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("counts-store"))
              .toStream()
              .to("streams-wordcount-output", Produced.with(Serdes.String(), Serdes.Long()));

        final Topology topology = builder.build();
        final KafkaStreams streams = new KafkaStreams(topology, props);
        final CountDownLatch latch = new CountDownLatch(1);

        // ... same as Pipe.java above
    }
}
```

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)

---

<a id="streams-core-concepts"></a>

<a id="streams-core-concepts--core-concepts"></a>

# Core Concepts

Kafka Streams is a client library for processing and analyzing data stored in Kafka. It builds upon important stream processing concepts such as properly distinguishing between event time and processing time, windowing support, and simple yet efficient management and real-time querying of application state.

Kafka Streams has a **low barrier to entry** : You can quickly write and run a small-scale proof-of-concept on a single machine; and you only need to run additional instances of your application on multiple machines to scale up to high-volume production workloads. Kafka Streams transparently handles the load balancing of multiple instances of the same application by leveraging Kafka’s parallelism model.

Some highlights of Kafka Streams:

- Designed as a **simple and lightweight client library** , which can be easily embedded in any Java application and integrated with any existing packaging, deployment and operational tools that users have for their streaming applications.
- Has **no external dependencies on systems other than Apache Kafka itself** as the internal messaging layer; notably, it uses Kafka’s partitioning model to horizontally scale processing while maintaining strong ordering guarantees.
- Supports **fault-tolerant local state** , which enables very fast and efficient stateful operations like windowed joins and aggregations.
- Supports **exactly-once** processing semantics to guarantee that each record will be processed once and only once even when there is a failure on either Streams clients or Kafka brokers in the middle of processing.
- Employs **one-record-at-a-time processing** to achieve millisecond processing latency, and supports **event-time based windowing operations** with out-of-order arrival of records.
- Offers necessary stream processing primitives, along with a **high-level Streams DSL** and a **low-level Processor API**.

We first summarize the key concepts of Kafka Streams.

<a id="streams-core-concepts--stream-processing-topology"></a>

## Stream Processing Topology

- A **stream** is the most important abstraction provided by Kafka Streams: it represents an unbounded, continuously updating data set. A stream is an ordered, replayable, and fault-tolerant sequence of immutable data records, where a **data record** is defined as a key-value pair.
- A **stream processing application** is any program that makes use of the Kafka Streams library. It defines its computational logic through one or more **processor topologies** , where a processor topology is a graph of stream processors (nodes) that are connected by streams (edges).
- A [**stream processor**](#documentation-streams-developer-guide-processor-api--defining-a-stream-processor) is a node in the processor topology; it represents a processing step to transform data in streams by receiving one input record at a time from its upstream processors in the topology, applying its operation to it, and may subsequently produce one or more output records to its downstream processors.

There are two special processors in the topology:

- **Source Processor** : A source processor is a special type of stream processor that does not have any upstream processors. It produces an input stream to its topology from one or multiple Kafka topics by consuming records from these topics and forwarding them to its down-stream processors.
- **Sink Processor** : A sink processor is a special type of stream processor that does not have down-stream processors. It sends any received records from its up-stream processors to a specified Kafka topic.

Note that in normal processor nodes other remote systems can also be accessed while processing the current record. Therefore the processed results can either be streamed back into Kafka or written to an external system. ![](assets/images/streams-architecture-topology_f2caedd33ebb3f22.jpg)

Kafka Streams offers two ways to define the stream processing topology: the [**Kafka Streams DSL**](#documentation-streams-developer-guide-dsl-api) provides the most common data transformation operations such as `map`, `filter`, `join` and `aggregations` out of the box; the lower-level [**Processor API**](#documentation-streams-developer-guide-processor-api) allows developers define and connect custom processors as well as to interact with state stores.

A processor topology is merely a logical abstraction for your stream processing code. At runtime, the logical topology is instantiated and replicated inside the application for parallel processing (see [**Stream Partitions and Tasks**](#documentation-streams-architecture--streams_architecture_tasks) for details).

<a id="streams-core-concepts--time"></a>

## Time

A critical aspect in stream processing is the notion of **time** , and how it is modeled and integrated. For example, some operations such as **windowing** are defined based on time boundaries.

Common notions of time in streams are:

- **Event time** - The point in time when an event or data record occurred, i.e. was originally created “at the source”. **Example:** If the event is a geo-location change reported by a GPS sensor in a car, then the associated event-time would be the time when the GPS sensor captured the location change.
- **Processing time** - The point in time when the event or data record happens to be processed by the stream processing application, i.e. when the record is being consumed. The processing time may be milliseconds, hours, or days etc. later than the original event time. **Example:** Imagine an analytics application that reads and processes the geo-location data reported from car sensors to present it to a fleet management dashboard. Here, processing-time in the analytics application might be milliseconds or seconds (e.g. for real-time pipelines based on Apache Kafka and Kafka Streams) or hours (e.g. for batch pipelines based on Apache Hadoop or Apache Spark) after event-time.
- **Ingestion time** - The point in time when an event or data record is stored in a topic partition by a Kafka broker. The difference to event time is that this ingestion timestamp is generated when the record is appended to the target topic by the Kafka broker, not when the record is created “at the source”. The difference to processing time is that processing time is when the stream processing application processes the record. **For example,** if a record is never processed, there is no notion of processing time for it, but it still has an ingestion time.

The choice between event-time and ingestion-time is actually done through the configuration of Kafka (not Kafka Streams): From Kafka 0.10.x onwards, timestamps are automatically embedded into Kafka messages. Depending on Kafka’s configuration these timestamps represent event-time or ingestion-time. The respective Kafka configuration setting can be specified on the broker level or per topic. The default timestamp extractor in Kafka Streams will retrieve these embedded timestamps as-is. Hence, the effective time semantics of your application depend on the effective Kafka configuration for these embedded timestamps.

Kafka Streams assigns a **timestamp** to every data record via the `TimestampExtractor` interface. These per-record timestamps describe the progress of a stream with regards to time and are leveraged by time-dependent operations such as window operations. As a result, this time will only advance when a new record arrives at the processor. We call this data-driven time the **stream time** of the application to differentiate with the **wall-clock time** when this application is actually executing. Concrete implementations of the `TimestampExtractor` interface will then provide different semantics to the stream time definition. For example retrieving or computing timestamps based on the actual contents of data records such as an embedded timestamp field to provide event time semantics, and returning the current wall-clock time thereby yield processing time semantics to stream time. Developers can thus enforce different notions of time depending on their business needs.

Finally, whenever a Kafka Streams application writes records to Kafka, then it will also assign timestamps to these new records. The way the timestamps are assigned depends on the context:

- When new output records are generated via processing some input record, for example, `context.forward()` triggered in the `process()` function call, output record timestamps are inherited from input record timestamps directly.
- When new output records are generated via periodic functions such as `Punctuator#punctuate()`, the output record timestamp is defined as the current internal time (obtained through `context.timestamp()`) of the stream task.
- For aggregations, the timestamp of a result update record will be the maximum timestamp of all input records contributing to the result.

You can change the default behavior in the Processor API by assigning timestamps to output records explicitly when calling `#forward()`.

For aggregations and joins, timestamps are computed by using the following rules.

- For joins (stream-stream, table-table) that have left and right input records, the timestamp of the output record is assigned `max(left.ts, right.ts)`.
- For stream-table joins, the output record is assigned the timestamp from the stream record.
- For aggregations, Kafka Streams also computes the `max` timestamp over all records, per key, either globally (for non-windowed) or per-window.
- For stateless operations, the input record timestamp is passed through. For `flatMap` and siblings that emit multiple records, all output records inherit the timestamp from the corresponding input record.

<a id="streams-core-concepts--duality-of-streams-and-tables"></a>

## Duality of Streams and Tables

When implementing stream processing use cases in practice, you typically need both **streams** and also **databases**. An example use case that is very common in practice is an e-commerce application that enriches an incoming *stream* of customer transactions with the latest customer information from a *database table*. In other words, streams are everywhere, but databases are everywhere, too.

Any stream processing technology must therefore provide **first-class support for streams and tables**. Kafka’s Streams API provides such functionality through its core abstractions for [streams](#documentation-streams-developer-guide-dsl-api--streams_concepts_kstream) and [tables](#documentation-streams-developer-guide-dsl-api--streams_concepts_ktable), which we will talk about in a minute. Now, an interesting observation is that there is actually a **close relationship between streams and tables** , the so-called stream-table duality. And Kafka exploits this duality in many ways: for example, to make your applications [elastic](#documentation-streams-developer-guide-running-app--elastic-scaling-of-your-application), to support [fault-tolerant stateful processing](#documentation-streams-architecture--streams_architecture_recovery), or to run [interactive queries](#documentation-streams-developer-guide-interactive-queries--interactive-queries) against your application’s latest processing results. And, beyond its internal usage, the Kafka Streams API also allows developers to exploit this duality in their own applications.

Before we discuss concepts such as [aggregations](#documentation-streams-developer-guide-dsl-api--aggregating) in Kafka Streams, we must first introduce **tables** in more detail, and talk about the aforementioned stream-table duality. Essentially, this duality means that a stream can be viewed as a table, and a table can be viewed as a stream. Kafka’s log compaction feature, for example, exploits this duality.

A simple form of a table is a collection of key-value pairs, also called a map or associative array. Such a table may look as follows:

- **Stream as Table** : A stream can be considered a changelog of a table, where each data record in the stream captures a state change of the table. A stream is thus a table in disguise, and it can be easily turned into a “real” table by replaying the changelog from beginning to end to reconstruct the table. Similarly, in a more general analogy, aggregating data records in a stream - such as computing the total number of pageviews by user from a stream of pageview events - will return a table (here with the key and the value being the user and its corresponding pageview count, respectively).
- **Table as Stream** : A table can be considered a snapshot, at a point in time, of the latest value for each key in a stream (a stream’s data records are key-value pairs). A table is thus a stream in disguise, and it can be easily turned into a “real” stream by iterating over each key-value entry in the table.

Let’s illustrate this with an example. Imagine a table that tracks the total number of pageviews by user (first column of diagram below). Over time, whenever a new pageview event is processed, the state of the table is updated accordingly. Here, the state changes between different points in time - and different revisions of the table - can be represented as a changelog stream (second column).

Interestingly, because of the stream-table duality, the same stream can be used to reconstruct the original table (third column):

The same mechanism is used, for example, to replicate databases via change data capture (CDC) and, within Kafka Streams, to replicate its so-called state stores across machines for fault-tolerance. The stream-table duality is such an important concept that Kafka Streams models it explicitly via the KStream, KTable, and GlobalKTable interfaces.

<a id="streams-core-concepts--aggregations"></a>

## Aggregations

An **aggregation** operation takes one input stream or table, and yields a new table by combining multiple input records into a single output record. Examples of aggregations are computing counts or sum.

In the `Kafka Streams DSL`, an input stream of an `aggregation` can be a KStream or a KTable, but the output stream will always be a KTable. This allows Kafka Streams to update an aggregate value upon the out-of-order arrival of further records after the value was produced and emitted. When such out-of-order arrival happens, the aggregating KStream or KTable emits a new aggregate value. Because the output is a KTable, the new value is considered to overwrite the old value with the same key in subsequent processing steps.

<a id="streams-core-concepts--windowing"></a>

## Windowing

Windowing lets you control how to *group records that have the same key* for stateful operations such as `aggregations` or `joins` into so-called *windows*. Windows are tracked per record key.

`Windowing operations` are available in the `Kafka Streams DSL`. When working with windows, you can specify a **grace period** for the window. This grace period controls how long Kafka Streams will wait for **out-of-order** data records for a given window. If a record arrives after the grace period of a window has passed, the record is discarded and will not be processed in that window. Specifically, a record is discarded if its timestamp dictates it belongs to a window, but the current stream time is greater than the end of the window plus the grace period.

Out-of-order records are always possible in the real world and should be properly accounted for in your applications. It depends on the effective `time semantics` how out-of-order records are handled. In the case of processing-time, the semantics are “when the record is being processed”, which means that the notion of out-of-order records is not applicable as, by definition, no record can be out-of-order. Hence, out-of-order records can only be considered as such for event-time. In both cases, Kafka Streams is able to properly handle out-of-order records.

<a id="streams-core-concepts--states"></a>

## States

Some stream processing applications don’t require state, which means the processing of a message is independent from the processing of all other messages. However, being able to maintain state opens up many possibilities for sophisticated stream processing applications: you can join input streams, or group and aggregate data records. Many such stateful operators are provided by the [**Kafka Streams DSL**](#documentation-streams-developer-guide-dsl-api).

Kafka Streams provides so-called **state stores** , which can be used by stream processing applications to store and query data. This is an important capability when implementing stateful operations. Every task in Kafka Streams embeds one or more state stores that can be accessed via APIs to store and query data required for processing. These state stores can either be a persistent key-value store, an in-memory hashmap, or another convenient data structure. Kafka Streams offers fault-tolerance and automatic recovery for local state stores.

Kafka Streams allows direct read-only queries of the state stores by methods, threads, processes or applications external to the stream processing application that created the state stores. This is provided through a feature called **Interactive Queries**. All stores are named and Interactive Queries exposes only the read operations of the underlying implementation.

<a id="streams-core-concepts--processing-guarantees"></a>

# Processing Guarantees

In stream processing, one of the most frequently asked question is “does my stream processing system guarantee that each record is processed once and only once, even if some failures are encountered in the middle of processing?” Failing to guarantee exactly-once stream processing is a deal-breaker for many applications that cannot tolerate any data-loss or data duplicates, and in that case a batch-oriented framework is usually used in addition to the stream processing pipeline, known as the [Lambda Architecture](https://en.wikipedia.org/wiki/Lambda_architecture). Prior to 0.11.0.0, Kafka only provides at-least-once delivery guarantees and hence any stream processing systems that leverage it as the backend storage could not guarantee end-to-end exactly-once semantics. In fact, even for those stream processing systems that claim to support exactly-once processing, as long as they are reading from / writing to Kafka as the source / sink, their applications cannot actually guarantee that no duplicates will be generated throughout the pipeline.
Since the 0.11.0.0 release, Kafka has added support to allow its producers to send messages to different topic partitions in a [transactional and idempotent manner](https://kafka.apache.org/documentation/#semantics), and Kafka Streams has hence added the end-to-end exactly-once processing semantics by leveraging these features. More specifically, it guarantees that for any record read from the source Kafka topics, its processing results will be reflected exactly once in the output Kafka topic as well as in the state stores for stateful operations. Note the key difference between Kafka Streams end-to-end exactly-once guarantee with other stream processing frameworks’ claimed guarantees is that Kafka Streams tightly integrates with the underlying Kafka storage system and ensure that commits on the input topic offsets, updates on the state stores, and writes to the output topics will be completed atomically instead of treating Kafka as an external system that may have side-effects. For more information on how this is done inside Kafka Streams, see [KIP-129](https://cwiki.apache.org/confluence/x/0okYB).
To enable exactly-once semantics when running Kafka Streams applications, set the `processing.guarantee` config value (default value is **at\_least\_once**) to **StreamsConfig.EXACTLY\_ONCE\_V2** (requires brokers version 2.5 or newer). For more information, see the [Kafka Streams Configs](https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams.html) section.

<a id="streams-core-concepts--out-of-order-handling"></a>

## Out-of-Order Handling

Besides the guarantee that each record will be processed exactly-once, another issue that many stream processing applications will face is how to handle [out-of-order data](https://dl.acm.org/citation.cfm?id=3242155) that may impact their business logic. In Kafka Streams, there are two causes that could potentially result in out-of-order data arrivals with respect to their timestamps:

- Within a topic-partition, a record’s timestamp may not be monotonically increasing along with their offsets. Since Kafka Streams will always try to process records within a topic-partition to follow the offset order, it can cause records with larger timestamps (but smaller offsets) to be processed earlier than records with smaller timestamps (but larger offsets) in the same topic-partition.
- Within a [stream task](#documentation-streams-architecture--streams_architecture_tasks) that may be processing multiple topic-partitions, if users configure the application to not wait for all partitions to contain some buffered data and pick from the partition with the smallest timestamp to process the next record, then later on when some records are fetched for other topic-partitions, their timestamps may be smaller than those processed records fetched from another topic-partition.

For stateless operations, out-of-order data will not impact processing logic since only one record is considered at a time, without looking into the history of past processed records; for stateful operations such as aggregations and joins, however, out-of-order data could cause the processing logic to be incorrect. If users want to handle such out-of-order data, generally they need to allow their applications to wait for longer time while bookkeeping their states during the wait time, i.e. making trade-off decisions between latency, cost, and correctness. In Kafka Streams specifically, users can configure their window operators for windowed aggregations to achieve such trade-offs (details can be found in [**Developer Guide**](#documentation-streams-developer-guide)). As for Joins, users may use [versioned state stores](#documentation-streams-developer-guide-dsl-api--versioned-state-stores) to address concerns with out-of-order data, but out-of-order data will not be handled by default:

- For Stream-Stream joins, all three types (inner, outer, left) handle out-of-order records correctly.
- For Stream-Table joins, if not using versioned stores, then out-of-order records are not handled (i.e., Streams applications don’t check for out-of-order records and just process all records in offset order), and hence it may produce unpredictable results. With versioned stores, stream-side out-of-order data will be properly handled by performing a timestamp-based lookup in the table. Table-side out-of-order data is still not handled.
- For Table-Table joins, if not using versioned stores, then out-of-order records are not handled (i.e., Streams applications don’t check for out-of-order records and just process all records in offset order). However, the join result is a changelog stream and hence will be eventually consistent. With versioned stores, table-table join semantics change from offset-based semantics to [timestamp-based semantics](#documentation-streams-developer-guide-dsl-api--versioned-state-stores) and out-of-order records are handled accordingly.
- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)

---

<a id="streams-architecture"></a>

<a id="streams-architecture--architecture"></a>

# Architecture

Kafka Streams simplifies application development by building on the Kafka producer and consumer libraries and leveraging the native capabilities of Kafka to offer data parallelism, distributed coordination, fault tolerance, and operational simplicity. In this section, we describe how Kafka Streams works underneath the covers.

The picture below shows the anatomy of an application that uses the Kafka Streams library. Let’s walk through some details.

<a id="streams-architecture--stream-partitions-and-tasks"></a>

## Stream Partitions and Tasks

The messaging layer of Kafka partitions data for storing and transporting it. Kafka Streams partitions data for processing it. In both cases, this partitioning is what enables data locality, elasticity, scalability, high performance, and fault tolerance. Kafka Streams uses the concepts of **partitions** and **tasks** as logical units of its parallelism model based on Kafka topic partitions. There are close links between Kafka Streams and Kafka in the context of parallelism:

- Each **stream partition** is a totally ordered sequence of data records and maps to a Kafka **topic partition**.
- A **data record** in the stream maps to a Kafka **message** from that topic.
- The **keys** of data records determine the partitioning of data in both Kafka and Kafka Streams, i.e., how data is routed to specific partitions within topics.

An application’s processor topology is scaled by breaking it into multiple tasks. More specifically, Kafka Streams creates a fixed number of tasks based on the input stream partitions for the application, with each task assigned a list of partitions from the input streams (i.e., Kafka topics). The assignment of partitions to tasks never changes so that each task is a fixed unit of parallelism of the application. Tasks can then instantiate their own processor topology based on the assigned partitions; they also maintain a buffer for each of its assigned partitions and process messages one-at-a-time from these record buffers. As a result stream tasks can be processed independently and in parallel without manual intervention.

Slightly simplified, the maximum parallelism at which your application may run is bounded by the maximum number of stream tasks, which itself is determined by maximum number of partitions of the input topic(s) the application is reading from. For example, if your input topic has 5 partitions, then you can run up to 5 applications instances. These instances will collaboratively process the topic’s data. If you run a larger number of app instances than partitions of the input topic, the “excess” app instances will launch but remain idle; however, if one of the busy instances goes down, one of the idle instances will resume the former’s work.

It is important to understand that Kafka Streams is not a resource manager, but a library that “runs” anywhere its stream processing application runs. Multiple instances of the application are executed either on the same machine, or spread across multiple machines and tasks can be distributed automatically by the library to those running application instances. The assignment of partitions to tasks never changes; if an application instance fails, all its assigned tasks will be automatically restarted on other instances and continue to consume from the same stream partitions.

**NOTE:** Topic partitions are assigned to tasks, and tasks are assigned to all threads over all instances, in a best-effort attempt to trade off load-balancing and stickiness of stateful tasks. For this assignment, Kafka Streams uses the [StreamsPartitionAssignor](https://github.com/apache/kafka/blob/trunk/streams/src/main/java/org/apache/kafka/streams/processor/internals/StreamsPartitionAssignor.java) class and doesn’t let you change to a different assignor. If you try to use a different assignor, Kafka Streams ignores it.

The following diagram shows two tasks each assigned with one partition of the input streams.

<a id="streams-architecture--threading-model"></a>

## Threading Model

Kafka Streams allows the user to configure the number of **threads** that the library can use to parallelize processing within an application instance. Each thread can execute one or more tasks with their processor topologies independently. For example, the following diagram shows one stream thread running two stream tasks.

Starting more stream threads or more instances of the application merely amounts to replicating the topology and having it process a different subset of Kafka partitions, effectively parallelizing processing. It is worth noting that there is no shared state amongst the threads, so no inter-thread coordination is necessary. This makes it very simple to run topologies in parallel across the application instances and threads. The assignment of Kafka topic partitions amongst the various stream threads is transparently handled by Kafka Streams leveraging [Kafka’s coordination](https://cwiki.apache.org/confluence/x/foynAw) functionality.

As we described above, scaling your stream processing application with Kafka Streams is easy: you merely need to start additional instances of your application, and Kafka Streams takes care of distributing partitions amongst tasks that run in the application instances. You can start as many threads of the application as there are input Kafka topic partitions so that, across all running instances of an application, every thread (or rather, the tasks it runs) has at least one input partition to process.

As of Kafka 2.8 you can scale stream threads much in the same way you can scale your Kafka Stream clients. Simply add or remove stream threads and Kafka Streams will take care of redistributing the partitions. You may also add threads to replace stream threads that have died removing the need to restart clients to recover the number of thread running.

<a id="streams-architecture--local-state-stores"></a>

## Local State Stores

Kafka Streams provides so-called **state stores** , which can be used by stream processing applications to store and query data, which is an important capability when implementing stateful operations. The [Kafka Streams DSL](#documentation-streams-developer-guide-dsl-api), for example, automatically creates and manages such state stores when you are calling stateful operators such as `join()` or `aggregate()`, or when you are windowing a stream.

Every stream task in a Kafka Streams application may embed one or more local state stores that can be accessed via APIs to store and query data required for processing. Kafka Streams offers fault-tolerance and automatic recovery for such local state stores.

The following diagram shows two stream tasks with their dedicated local state stores.

<a id="streams-architecture--fault-tolerance"></a>

## Fault Tolerance

Kafka Streams builds on fault-tolerance capabilities integrated natively within Kafka. Kafka partitions are highly available and replicated; so when stream data is persisted to Kafka it is available even if the application fails and needs to re-process it. Tasks in Kafka Streams leverage the fault-tolerance capability offered by the Kafka consumer client to handle failures. If a task runs on a machine that fails, Kafka Streams automatically restarts the task in one of the remaining running instances of the application.

In addition, Kafka Streams makes sure that the local state stores are robust to failures, too. For each state store, it maintains a replicated changelog Kafka topic in which it tracks any state updates. These changelog topics are partitioned as well so that each local state store instance, and hence the task accessing the store, has its own dedicated changelog topic partition. [Log compaction](#documentation--compaction) is enabled on the changelog topics so that old data can be purged safely to prevent the topics from growing indefinitely. If tasks run on a machine that fails and are restarted on another machine, Kafka Streams guarantees to restore their associated state stores to the content before the failure by replaying the corresponding changelog topics prior to resuming the processing on the newly started tasks. As a result, failure handling is completely transparent to the end user.

Note that the cost of task (re)initialization typically depends primarily on the time for restoring the state by replaying the state stores’ associated changelog topics. To minimize this restoration time, users can configure their applications to have **standby replicas** of local states (i.e. fully replicated copies of the state). When a task migration happens, Kafka Streams will assign a task to an application instance where such a standby replica already exists in order to minimize the task (re)initialization cost. See `num.standby.replicas` in the [**Kafka Streams Configs**](#documentation--streamsconfigs) section. Starting in 2.6, Kafka Streams will guarantee that a task is only ever assigned to an instance with a fully caught-up local copy of the state, if such an instance exists. Standby tasks will increase the likelihood that a caught-up instance exists in the case of a failure.

You can also configure standby replicas with rack awareness. When configured, Kafka Streams will attempt to distribute a standby task on a different “rack” than the active one, thus having a faster recovery time when the rack of the active tasks fails. See `rack.aware.assignment.tags` in the [**Kafka Streams Developer Guide**](https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams.html#rack-aware-assignment-tags) section.

There is also a client config `client.rack` which can set the rack for a Kafka consumer. If brokers also have their rack set via `broker.rack`, then rack aware task assignment can be enabled via `rack.aware.assignment.strategy` (cf. [**Kafka Streams Developer Guide**](https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams.html#rack-aware-assignment-strategy)) to compute a task assignment which can reduce cross rack traffic by trying to assign tasks to clients with the same rack. Note that `client.rack` can also be used to distribute standby tasks to different racks from the active ones, which has a similar functionality as `rack.aware.assignment.tags`. Currently, `rack.aware.assignment.tag` takes precedence in distributing standby tasks which means if both configs present, `rack.aware.assignment.tag` will be used for distributing standby tasks on different racks from the active ones because it can configure more tag keys.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)

---

<a id="streams-upgrade-guide"></a>

<a id="streams-upgrade-guide--upgrade-guide"></a>

# Upgrade Guide

<a id="streams-upgrade-guide--upgrade-guide-and-api-changes"></a>

# Upgrade Guide and API Changes

Upgrading from any older version to 4.3.0 is possible: if upgrading from 3.4 or below, you will need to do two rolling bounces, where during the first rolling bounce phase you set the config `upgrade.from="older version"` (possible values are `"2.4" - "3.4"`) and during the second you remove it. This is required to safely handle 2 changes. The first is a change in foreign-key join serialization format. The second is a change in the serialization format for an internal repartition topic. For more details, please refer to [KIP-904](https://cwiki.apache.org/confluence/x/P5VbDg):

- prepare your application instances for a rolling bounce and make sure that config `upgrade.from` is set to the version from which it is being upgrade.
- bounce each instance of your application once
- prepare your newly deployed 4.3.0 application instances for a second round of rolling bounces; make sure to remove the value for config `upgrade.from`
- bounce each instance of your application once more to complete the upgrade

As an alternative, an offline upgrade is also possible. Upgrading from any versions as old as 0.11.0.x to 4.3.0 in offline mode require the following steps:

- stop all old (e.g., 0.11.0.x) application instances
- update your code and swap old code and jar file with new code and new jar file
- restart all new (4.3.0) application instances

For a table that shows Streams API compatibility with Kafka broker versions, see Broker Compatibility.

<a id="streams-upgrade-guide--notable-compatibility-changes-in-past-releases"></a>

## Notable compatibility changes in past releases

Starting in version 4.0.0, Kafka Streams will only be compatible when running against brokers on version 2.1 or higher. Additionally, exactly-once semantics (EOS) will require brokers to be at least version 2.5.

Downgrading from 3.5.x or newer version to 3.4.x or older version needs special attention: Since 3.5.0 release, Kafka Streams uses a new serialization format for repartition topics. This means that older versions of Kafka Streams would not be able to recognize the bytes written by newer versions, and hence it is harder to downgrade Kafka Streams with version 3.5.0 or newer to older versions in-flight. For more details, please refer to [KIP-904](https://cwiki.apache.org/confluence/x/P5VbDg). For a downgrade, first switch the config from `"upgrade.from"` to the version you are downgrading to. This disables writing of the new serialization format in your application. It’s important to wait in this state long enough to make sure that the application has finished processing any “in-flight” messages written into the repartition topics in the new serialization format. Afterwards, you can downgrade your application to a pre-3.5.x version.

Downgrading from 3.0.x or newer version to 2.8.x or older version needs special attention: Since 3.0.0 release, Kafka Streams uses a newer RocksDB version whose on-disk format changed. This means that old versioned RocksDB would not be able to recognize the bytes written by that newer versioned RocksDB, and hence it is harder to downgrade Kafka Streams with version 3.0.0 or newer to older versions in-flight. Users need to first delete the local RocksDB state stores written by the new versioned Kafka Streams before swapping in the older versioned Kafka Streams bytecode, which would then restore the state stores with the old on-disk format from the changelogs.

Downgrading from 4.0.x or newer version to older than 4.0.0 needs special attention: Since 4.0.0 release, Kafka Streams upgraded RocksDB from version 7.9.2 to 9.7.3. This upgrade introduces a RocksDB file format version change from version 5 to version 6 (introduced in RocksDB 8.6). While the newer RocksDB version (9.7.3) can read state stores written in the old format (version 5), the older RocksDB versions cannot read state stores written in the new format (version 6). This means that downgrading from Kafka Streams 4.0.x or newer to versions older than 4.0.0 in-flight is not possible out-of-the-box. Users must first delete the local RocksDB state stores written by Kafka Streams 4.0.x or newer before downgrading to versions older than 4.0.0, which will then restore the state stores from the changelogs using the old file format.

Downgrading from 4.3.x or newer version to 4.2.x or older version needs special attention: Since 4.3.0 release, Kafka Streams persists state store changelog offsets inside each state store rather than in a per-task `.checkpoint` file (see [KIP-1035](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1035%3A+StateStore+managed+changelog+offsets)). For built-in RocksDB stores, offsets are written into a dedicated `offsets` column family inside each RocksDB instance. Older Kafka Streams versions do not declare this column family when opening RocksDB, so they will fail to open the store and the application will crash on startup. In-flight downgrade is therefore not supported. To downgrade to 4.2.x or older, stop each application instance, delete the local state directory (`state.dir`), then start the older version — Kafka Streams will restore all state stores from their changelog topics using the older on-disk format.

Kafka Streams does not support running multiple instances of the same application as different processes on the same physical state directory. Starting in 2.8.0 (as well as 2.7.1 and 2.6.2), this restriction will be enforced. If you wish to run more than one instance of Kafka Streams, you must configure them with different values for `state.dir`.

Starting in Kafka Streams 2.6.x, a new processing mode is available, named EOS version 2. This can be configured by setting `"processing.guarantee"` to `"exactly_once_v2"` for application versions 3.0+, or setting it to `"exactly_once_beta"` for versions between 2.6 and 2.8. To use this new feature, your brokers must be on version 2.5.x or newer. If you want to upgrade your EOS application from an older version and enable this feature in version 3.0+, you first need to upgrade your application to version 3.0.x, staying on `"exactly_once"`, and then do second round of rolling bounces to switch to `"exactly_once_v2"`. If you are upgrading an EOS application from an older (pre-2.6) version to a version between 2.6 and 2.8, follow these same steps but with the config `"exactly_once_beta"` instead. No special steps are required to upgrade an application using `"exactly_once_beta"` from version 2.6+ to 3.0 or higher: you can just change the config from `"exactly_once_beta"` to `"exactly_once_v2"` during the rolling upgrade. For a downgrade, do the reverse: first switch the config from `"exactly_once_v2"` to `"exactly_once"` to disable the feature in your 2.6.x application. Afterward, you can downgrade your application to a pre-2.6.x version.

Since 2.6.0 release, Kafka Streams depends on a RocksDB version that requires MacOS 10.14 or higher.

<a id="streams-upgrade-guide--streams-api-changes-in-430"></a>
<a id="streams-upgrade-guide--streams-api-changes-in-4.3.0"></a>

## Streams API changes in 4.3.0

**Note:** Kafka Streams 4.3.0 contains a critical native memory leak in the RocksDB state store layer ([KAFKA-20616](https://issues.apache.org/jira/browse/KAFKA-20616)). The `ColumnFamilyOptions` for the offsets column family is not closed, and column family handles can leak on close-path exceptions, which under cascading task closes (e.g., rebalances or error-triggered recoveries) leads to unbounded off-heap memory growth and eventual OOM. Users running Kafka Streams should consider upgrading directly to 4.3.1, which includes the fix for it.

Kafka Streams now supports `ProcessingExceptionHandler` for global store/KTable processing via [KIP-1270](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1270%3A+Extend+ProcessExceptionalHandler+for+GlobalThread). Previously, the `ProcessingExceptionHandler` only applied to regular stream tasks. With this release, you can now configure exception handling for global store/KTables by setting the new config `processing.exception.handler.global.enabled` to `true` (recommended). When enabled, the configured `ProcessingExceptionHandler` will be invoked for exceptions occurring during global store/KTable processing. Note that Dead Letter Queue (DLQ) support is not yet available for global store/KTable and will be added in an upcoming release. More details can be found in [KIP-1270](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1270%3A+Extend+ProcessExceptionalHandler+for+GlobalThread).

The streams thread metrics `commit-ratio`, `process-ratio`, `punctuate-ratio`, and `poll-ratio`, along with streams state updater metrics `active-restore-ratio`, `standby-restore-ratio`, `idle-ratio`, and `checkpoint-ratio` have been updated. Each metric now reports, over a rolling measurement window, the ratio of time this thread spends performing the given action (`{action}`) to the total elapsed time in that window. The effective window duration is determined by the metrics configuration: `metrics.sample.window.ms` (per-sample window length) and `metrics.num.samples` (number of rolling windows).

Kafka Streams now allows to purge local state directories and checkpoint files during application startup if they have not been modified for a certain period of time. This can be configured via the new `state.cleanup.dir.max.age.ms` config. More details can be found in [KIP-1259](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1259%3A+Add+configuration+to+wipe+Kafka+Streams+local+state+on+startup)

Kafka Streams now persists state store changelog offsets inside each state store rather than in a single per-task `.checkpoint` file ([KIP-1035](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1035%3A+StateStore+managed+changelog+offsets)). This is an internal infrastructure change and is transparent to most users — existing per-task `.checkpoint` files are migrated automatically on first startup, and no application or operator action is required. EOS crash behavior is unchanged in 4.3: state stores are still wiped and fully restored from the changelog. KIP-1035 is a prerequisite for [KIP-892: Transactional Semantics for StateStores](https://cwiki.apache.org/confluence/display/KAFKA/KIP-892%3A+Transactional+Semantics+for+StateStores), which will use these per-store offsets to make EOS state writes transactional and skip the full restore. Authors of custom `StateStore` implementations may opt-in to managing their own offsets via `managesOffsets()`, `commit(Map<TopicPartition, Long>)`, and `committedOffset(TopicPartition)`; see KIP-1035 for the API. For downgrade implications, see [Notable compatibility changes in past releases](#streams-upgrade-guide--notable-compatibility-changes-in-past-releases).

As part of KIP-1035, the per-store changelog offset is written into RocksDB on each commit and is made durable on disk only when RocksDB flushes its memtable to an SST file — either organically once the memtable fills `write_buffer_size` (16 MB by default), or on a clean store close. Earlier releases force-flushed RocksDB on every commit. A consequence is that for a **low-traffic store** whose memtable rarely fills, the on-disk offset can lag the store’s actual position until the next clean shutdown. For the durability model and guidance on tuning flush frequency for low-traffic stores, see [Memory Management: RocksDB](https://kafka.apache.org/%7b43%7d/documentation/streams/developer-guide/memory-mgmt.html#rocksdb-offset-durability). If the process then exits uncleanly (for example SIGKILL/OOM-kill, or a KafkaStreams#close that does not complete within the shutdown grace period) and changelog retention or compaction has since advanced the changelog’s log-start offset past that stale offset, the restore consumer seeks out of range on restart — logged as OffsetOutOfRangeException/TaskCorruptedException — and the task is automatically re-initialized from the changelog (no data loss, but a full re-restore).

<a id="streams-upgrade-guide--kip-1271-headers-aware-stores"></a>
<a id="streams-upgrade-guide--header-aware-state-stores-for-the-processor-api-kip-1271"></a>

### Header-aware state stores for the Processor API (KIP-1271)

Kafka Streams adds **header-aware** state stores. Opt in with the new `Stores` suppliers whose names end with `WithHeaders` and the matching `StoreBuilder` factories. For example:

- `persistentTimestampedKeyValueStoreWithHeaders` with `timestampedKeyValueStoreWithHeadersBuilder`
- `persistentTimestampedWindowStoreWithHeaders` with `timestampedWindowStoreWithHeadersBuilder`
- `persistentSessionStoreWithHeaders` with `sessionStoreWithHeadersBuilder`

See the [Processor API state store documentation](#streams-developer-guide-processor-api--headers-in-state-stores).

Existing applications that keep using the same headerless `Stores` suppliers and builders are unaffected: storage format, changelogs, and performance stay as before.

For stores that adopt the header-aware format, KIP-1271 defines a single rolling-bounce upgrade: the changelog topic format is unchanged, legacy rows are read with empty header sets until rewritten, and RocksDB-backed stores migrate data lazily on access. Downgrading in place after migration is not supported except by clearing local store data and restoring from the changelog.

Storing headers increases disk and serialization cost versus headerless stores; the KIP discusses lazy header parsing and other performance considerations.

`TopologyTestDriver` and Interactive Queries support the new store types. The existing `store()` facades continue to return values (or `ValueAndTimestamp`) without exposing record headers. See the [interactive queries guide](#streams-developer-guide-interactive-queries--header-aware-stores-interactive-queries).

<a id="streams-upgrade-guide--headers-aware-state-stores-for-dsl-operators-kip-1285"></a>

### Headers-Aware State Stores for DSL Operators (KIP-1285)

[KIP-1285](https://cwiki.apache.org/confluence/x/4ow8G) lets DSL operators use the headers-aware state stores introduced by [KIP-1271](#streams-upgrade-guide--kip-1271-headers-aware-stores). Set [`dsl.store.format=HEADERS`](#streams-developer-guide-config-streams--dsl-store-format) to use headers-aware stores for supported DSL operators. These stores can keep record headers together with the value and timestamp.

The config only chooses the state store format. It does not define how DSL operators create headers for output records; see [Current limitations](#streams-upgrade-guide--current-limitations) below.

```java
// Enable headers-aware stores globally for all DSL operators
Properties props = new Properties();
props.put(StreamsConfig.DSL_STORE_FORMAT_CONFIG, "HEADERS");
```

<a id="streams-upgrade-guide--current-limitations"></a>

#### Current limitations

Today, DSL result headers behave as follows:

- Aggregations (`count`, `reduce`, `aggregate`, including their windowed and session-windowed variants), KTable-KTable joins (inner / left / outer), materialized `KTable.mapValues`, `KStream.toTable()`, and `StreamsBuilder.table()` write empty headers to their materialized stores.
- KStream-KStream join window stores keep source-record headers, but join result records do not get computed or merged headers. They may carry the headers from the record that triggered the result.
- `suppress()` and left/outer stream-stream joins use non-headers-aware buffer stores. Records that pass through those buffers lose their headers.

A follow-up KIP will give users explicit control over how DSL result headers are computed. See [Stateful transformations](#streams-developer-guide-dsl-api--stateful-transformations) for more details.

<a id="streams-upgrade-guide--changelog-migration-and-performance"></a>

#### Changelog, migration, and performance

KIP-1285 does not change the changelog wire format, the migration procedure, or the per-store overhead — those are properties of the underlying KIP-1271 stores. See the [KIP-1271 section](#streams-upgrade-guide--kip-1271-headers-aware-stores) above for the full description of changelog compatibility, the lazy per-key RocksDB migration on `DEFAULT`→`HEADERS`, the restore behavior, and the per-record size impact. The DSL config `dsl.store.format` only controls which operators participate; once an operator is using a headers-aware store, the store runtime behavior is identical to the Processor API case.

<a id="streams-upgrade-guide--deprecation-of-streams-scala-module-kip-1244"></a>

### Deprecation of streams-scala module (KIP-1244)

For a detailed migration guide with code examples, see [Migrating from Streams Scala to Java API](#streams-developer-guide-scala-migration).

<a id="streams-upgrade-guide--streams-api-changes-in-420"></a>
<a id="streams-upgrade-guide--streams-api-changes-in-4.2.0"></a>

## Streams API changes in 4.2.0

<a id="streams-upgrade-guide--general-availability-for-a-core-feature-set-of-the-streams-rebalance-protocol-kip-1071"></a>

### General Availability for a core feature set of the Streams Rebalance Protocol (KIP-1071)

The Streams Rebalance Protocol is a broker-driven rebalancing system designed specifically for Kafka Streams applications.
This release marks the General Availability for the core functionality detailed in [KIP-1071](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1071%3A+Streams+Rebalance+Protocol).
For more information about the feature set, design, usage and migration, please refer to the [developer guide](#streams-developer-guide-streams-rebalance-protocol).

**Note:** Due to a critical broker-side bug in the offline migration code ([KAFKA-20254](https://issues.apache.org/jira/browse/KAFKA-20254)), we recommend against doing migrations from classic to streams groups in 4.2.0. Newly created streams groups are not impacted. The fix is available in 4.2.1.

<a id="streams-upgrade-guide--other-changes"></a>

### Other changes

Kafka Streams now allows to enable state store directories created by Kafka Streams to have write access for the OS group, via the newly added config `allow.os.group.write.access`. More details can be found in [KIP-1230](https://cwiki.apache.org/confluence/x/jgl3Fw).

Kafka Streams now provides rebalance listener metrics for “streams” groups to monitor the latency of rebalance callbacks. The following metrics are available at the thread level: `tasks-revoked-latency-avg`, `tasks-revoked-latency-max`, `tasks-assigned-latency-avg`, `tasks-assigned-latency-max`, `tasks-lost-latency-avg`, and `tasks-lost-latency-max`. Note that these metrics are only populated when the Streams Rebalance Protocol (KIP-1071) is enabled. Users migrating from the consumer rebalance listener metrics should update their monitoring dashboards and alerts to use these new streams-specific metrics. More details can be found in [KIP-1216](https://cwiki.apache.org/confluence/x/ywnxFg).

The `application-id` tag is now available for the Kafka Streams client state metric (`client-state`). More details can be found in [KIP-1221](https://cwiki.apache.org/confluence/x/jQobFw).

<a id="streams-developer-guide"></a>

<a id="streams-developer-guide--streams-developer-guide"></a>

# Streams Developer Guide

---

<a id="streams-developer-guide--writing-a-streams-application"></a>

##### [Writing a Streams Application](#streams-developer-guide-write-streams-app)

<a id="streams-developer-guide--configuring-a-streams-application"></a>

##### [Configuring a Streams Application](#streams-developer-guide-config-streams)

<a id="streams-developer-guide--streams-dsl"></a>

##### [Streams DSL](#streams-developer-guide-dsl-api)

<a id="streams-developer-guide--processor-api"></a>

##### [Processor API](#streams-developer-guide-processor-api)

<a id="streams-developer-guide--naming-operators-in-a-streams-dsl-application"></a>

##### [Naming Operators in a Streams DSL application](#streams-developer-guide-dsl-topology-naming)

<a id="streams-developer-guide--data-types-and-serialization"></a>

##### [Data Types and Serialization](#streams-developer-guide-datatypes)

<a id="streams-developer-guide--testing-a-streams-application"></a>

##### [Testing a Streams Application](#streams-developer-guide-testing)

<a id="streams-developer-guide--interactive-queries"></a>

##### [Interactive Queries](#streams-developer-guide-interactive-queries)

<a id="streams-developer-guide--memory-management"></a>

##### [Memory Management](#streams-developer-guide-memory-mgmt)

<a id="streams-developer-guide--running-streams-applications"></a>

##### [Running Streams Applications](#streams-developer-guide-running-app)

<a id="streams-developer-guide--managing-streams-application-topics"></a>

##### [Managing Streams Application Topics](#streams-developer-guide-manage-topics)

<a id="streams-developer-guide--streams-security"></a>

##### [Streams Security](#streams-developer-guide-security)

<a id="streams-developer-guide--application-reset-tool"></a>

##### [Application Reset Tool](#streams-developer-guide-app-reset-tool)

<a id="streams-developer-guide--streams-rebalance-protocol"></a>

##### [Streams Rebalance Protocol](#streams-developer-guide-streams-rebalance-protocol)

<a id="streams-developer-guide--kafka-streams-groups-tool"></a>

##### [Kafka Streams Groups Tool](#streams-developer-guide-kafka-streams-group-sh)

<a id="streams-developer-guide--migrating-from-streams-scala-to-java-api"></a>

##### [Migrating from Streams Scala to Java API](#streams-developer-guide-scala-migration)

---

<a id="streams-developer-guide-write-streams-app"></a>

<a id="streams-developer-guide-write-streams-app--writing-a-streams-application"></a>

# Writing a Streams Application

Any Java or Scala application that makes use of the Kafka Streams library is considered a Kafka Streams application. The computational logic of a Kafka Streams application is defined as a [processor topology](https://kafka.apache.org/43/streams/developer-guide/core-concepts#streams_topology), which is a graph of stream processors (nodes) and streams (edges).

You can define the processor topology with the Kafka Streams APIs:

[Kafka Streams DSL](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/dsl-api.html#streams-developer-guide-dsl)
A high-level API that provides the most common data transformation operations such as `map`, `filter`, `join`, and `aggregations` out of the box. The DSL is the recommended starting point for developers new to Kafka Streams, and should cover many use cases and stream processing needs. If you’re writing a Scala application then you can use the [Kafka Streams DSL for Scala](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/dsl-api.html#scala-dsl) library which removes much of the Java/Scala interoperability boilerplate as opposed to working directly with the Java DSL.
[Processor API](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/processor-api.html#streams-developer-guide-processor-api)
A low-level API that lets you add and connect processors as well as interact directly with state stores. The Processor API provides you with even more flexibility than the DSL but at the expense of requiring more manual work on the side of the application developer (e.g., more lines of code).

<a id="streams-developer-guide-write-streams-app--libraries-and-maven-artifacts"></a>

# Libraries and Maven artifacts

This section lists the Kafka Streams related libraries that are available for writing your Kafka Streams applications.

You can define dependencies on the following libraries for your Kafka Streams applications.

| Group ID | Artifact ID | Version | Description |
| --- | --- | --- | --- |
| `org.apache.kafka` | `kafka-streams` | `4.3.1` | (Required) Base library for Kafka Streams. |
| `org.apache.kafka` | `kafka-clients` | `4.3.1` | (Required) Kafka client library. Contains built-in serializers/deserializers. |
| `org.apache.kafka` | `kafka-streams-scala` | `4.3.1` | (Optional) Kafka Streams DSL for Scala library to write Scala Kafka Streams applications. When not using SBT you will need to suffix the artifact ID with the correct version of Scala your application is using (`_2.12`, `_2.13`) |

> [!TIP]
>

See the section [Data Types and Serialization](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/datatypes.html#streams-developer-guide-serdes) for more information about Serializers/Deserializers.

Example `pom.xml` snippet when using Maven:

```
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
    <version>4.3.1</version>
</dependency>
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>4.3.1</version>
</dependency>
    <dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams-scala_2.13</artifactId>
    <version>4.3.1</version>
</dependency>
```

<a id="streams-developer-guide-write-streams-app--using-kafka-streams-within-your-application-code"></a>

# Using Kafka Streams within your application code

You can call Kafka Streams from anywhere in your application code, but usually these calls are made within the `main()` method of your application, or some variant thereof. The basic elements of defining a processing topology within your application are described below.

First, you must create an instance of `KafkaStreams`.

- The first argument of the `KafkaStreams` constructor takes a topology (either `StreamsBuilder#build()` for the [DSL](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/dsl-api.html#streams-developer-guide-dsl) or `Topology` for the [Processor API](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/processor-api.html#streams-developer-guide-processor-api)) that is used to define a topology.
- The second argument is an instance of `java.util.Properties`, which defines the configuration for this specific topology.

Code example:

```
import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.kstream.StreamsBuilder;
import org.apache.kafka.streams.processor.Topology;

// Use the builders to define the actual processing topology, e.g. to specify
// from which input topics to read, which stream operations (filter, map, etc.)
// should be called, and so on.  We will cover this in detail in the subsequent
// sections of this Developer Guide.

StreamsBuilder builder = ...;  // when using the DSL
Topology topology = builder.build();
//
// OR
//
Topology topology = ...; // when using the Processor API

// Use the configuration to tell your application where the Kafka cluster is,
// which Serializers/Deserializers to use by default, to specify security settings,
// and so on.
Properties props = ...;

KafkaStreams streams = new KafkaStreams(topology, props);
```

At this point, internal structures are initialized, but the processing is not started yet. You have to explicitly start the Kafka Streams thread by calling the `KafkaStreams#start()` method:

```
// Start the Kafka Streams threads
streams.start();
```

If there are other instances of this stream processing application running elsewhere (e.g., on another machine), Kafka Streams transparently re-assigns tasks from the existing instances to the new instance that you just started. For more information, see [Stream Partitions and Tasks](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams_architecture_tasks) and [Threading Model](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams_architecture_threads).

To catch any unexpected exceptions, you can set an `java.lang.Thread.UncaughtExceptionHandler` before you start the application. This handler is called whenever a stream thread is terminated by an unexpected exception:

```
streams.setUncaughtExceptionHandler((Thread thread, Throwable throwable) -> {
  // here you should examine the throwable/exception and perform an appropriate action!
});
```

To stop the application instance, call the `KafkaStreams#close()` method:

```
// Stop the Kafka Streams threads
streams.close();
```

To allow your application to gracefully shutdown in response to SIGTERM, it is recommended that you add a shutdown hook and call `KafkaStreams#close`.

Here is a shutdown hook example in Java:

```
// Add shutdown hook to stop the Kafka Streams threads.
// You can optionally provide a timeout to `close`.
Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
```

After an application is stopped, Kafka Streams will migrate any tasks that had been running in this instance to available remaining instances.

<a id="streams-developer-guide-write-streams-app--testing-a-streams-application"></a>

# Testing a Streams application

Kafka Streams comes with a `test-utils` module to help you test your application [here](https://kafka.apache.org/43/streams/developer-guide/write-streams-app/testing.html).

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-config-streams"></a>

<a id="streams-developer-guide-config-streams--configuring-a-streams-application"></a>

# Configuring a Streams Application

Kafka and Kafka Streams configuration options must be configured before using Streams. You can configure Kafka Streams by specifying parameters in a `java.util.Properties` instance.

1. Create a `java.util.Properties` instance.
2. Set the parameters. For example:

```
import java.util.Properties;
import org.apache.kafka.streams.StreamsConfig;

Properties settings = new Properties();
// Set a few key parameters
settings.put(StreamsConfig.APPLICATION_ID_CONFIG, "my-first-streams-application");
settings.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-broker1:9092");
// Any further settings
settings.put(... , ...);
```

<a id="streams-developer-guide-config-streams--configuration-parameter-reference"></a>

# Configuration parameter reference

- Required configuration parameters
  - application.id
  - bootstrap.servers
- Recommended configuration parameters for resiliency
  - acks
  - replication.factor
  - min.insync.replicas
  - num.standby.replicas
- Optional configuration parameters
  - acceptable.recovery.lag
  - default.key.serde
  - default.timestamp.extractor
  - default.value.serde
  - deserialization.exception.handler
  - dsl.store.format
  - enable.metrics.push
  - ensure.explicit.internal.resource.naming
  - group.protocol
  - log.summary.interval.ms
  - max.task.idle.ms
  - max.warmup.replicas
  - num.standby.replicas
  - num.stream.threads
  - probing.rebalance.interval.ms
  - processing.exception.handler
  - processing.guarantee
  - processor.wrapper.class
  - production.exception.handler
  - rack.aware.assignment.non\_overlap\_cost
  - rack.aware.assignment.strategy
  - rack.aware.assignment.tags
  - rack.aware.assignment.traffic\_cost
  - replication.factor
  - rocksdb.config.setter
  - state.dir
  - task.assignor.class
  - topology.optimization
- Kafka consumers and producer configuration parameters
  - Naming
  - Default Values
  - Parameters controlled by Kafka Streams
  - enable.auto.commit

<a id="streams-developer-guide-config-streams--required-configuration-parameters"></a>

## Required configuration parameters

Here are the required Streams configuration parameters.

| Parameter Name | Importance | Description | Default Value |
| --- | --- | --- | --- |
| application.id | Required | An identifier for the stream processing application. Must be unique within the Kafka cluster. | None |
| bootstrap.servers | Required | A list of host/port pairs to use for establishing the initial connection to the Kafka cluster. | None |

<a id="streams-developer-guide-config-streams--applicationid"></a>
<a id="streams-developer-guide-config-streams--application.id"></a>

### application.id

> (Required) The application ID. Each stream processing application must have a unique ID. The same ID must be given to all instances of the application. It is recommended to use only alphanumeric characters, `.` (dot), `-` (hyphen), and `_` (underscore). Examples: `"hello_world"`, `"hello_world-v1.0.0"`
>
> This ID is used in the following places to isolate resources used by the application from others:
>
> - As the default Kafka consumer and producer `client.id` prefix
> - As the Kafka consumer `group.id` for coordination
> - As the name of the subdirectory in the state directory (cf. `state.dir`)
> - As the prefix of internal Kafka topic names

> Tip:
> When an application is updated, the `application.id` should be changed unless you want to reuse the existing data in internal topics and state stores. For example, you could embed the version information within `application.id`, as `my-app-v1.0.0` and `my-app-v1.0.2`.

<a id="streams-developer-guide-config-streams--bootstrapservers"></a>
<a id="streams-developer-guide-config-streams--bootstrap.servers"></a>

### bootstrap.servers

> (Required) The Kafka bootstrap servers. This is the same [setting](#documentation--producerconfigs) that is used by the underlying producer and consumer clients to connect to the Kafka cluster. Example: `"kafka-broker1:9092,kafka-broker2:9092"`.

<a id="streams-developer-guide-config-streams--recommended-configuration-parameters-for-resiliency"></a>

## Recommended configuration parameters for resiliency

There are several Kafka and Kafka Streams configuration options that need to be configured explicitly for resiliency in face of broker failures:

| Parameter Name | Corresponding Client | Default value | Consider setting to |
| --- | --- | --- | --- |
| acks | Producer (for version <=2.8) | `acks="1")` | `acks="all"` |
| replication.factor (for broker version 2.3 or older) | Streams | `-1` | `3` (broker 2.4+: ensure broker config `default.replication.factor=3`) |
| min.insync.replicas | Broker | `1` | `2` |
| num.standby.replicas | Streams | `0` | `1` |

Increasing the replication factor to 3 ensures that the internal Kafka Streams topic can tolerate up to 2 broker failures. The tradeoff from moving to the default values to the recommended ones is that some performance and more storage space (3x with the replication factor of 3) are sacrificed for more resiliency.

<a id="streams-developer-guide-config-streams--acks"></a>

### acks

> The number of acknowledgments that the leader must have received before considering a request complete. This controls the durability of records that are sent. The possible values are:
>
> - `acks="0"` The producer does not wait for acknowledgment from the server and the record is immediately added to the socket buffer and considered sent. No guarantee can be made that the server has received the record in this case, and the producer won’t generally know of any failures. The offset returned for each record will always be set to `-1`.
> - `acks="1"` The leader writes the record to its local log and responds without waiting for full acknowledgement from all followers. If the leader immediately fails after acknowledging the record, but before the followers have replicated it, then the record will be lost.
> - `acks="all"` (default since 3.0 release) The leader waits for the full set of in-sync replicas to acknowledge the record. This guarantees that the record will not be lost if there is at least one in-sync replica alive. This is the strongest available guarantee.

> For more information, see the [Kafka Producer documentation](https://kafka.apache.org/documentation/#producerconfigs).

<a id="streams-developer-guide-config-streams--replicationfactor"></a>
<a id="streams-developer-guide-config-streams--replication.factor"></a>

### replication.factor

> See the description here.

<a id="streams-developer-guide-config-streams--mininsyncreplicas"></a>
<a id="streams-developer-guide-config-streams--min.insync.replicas"></a>

### min.insync.replicas

The minimum number of in-sync replicas available for replication if the producer is configured with `acks="all"` (see [topic configs](#documentation--topicconfigs_min.insync.replicas)).

<a id="streams-developer-guide-config-streams--numstandbyreplicas"></a>
<a id="streams-developer-guide-config-streams--num.standby.replicas"></a>

### num.standby.replicas

> See the description here.

```
Properties streamsSettings = new Properties();
// for broker version 2.3 or older
//streamsSettings.put(StreamsConfig.REPLICATION_FACTOR_CONFIG, 3);
// for version 2.8 or older
//streamsSettings.put(StreamsConfig.producerPrefix(ProducerConfig.ACKS_CONFIG), "all");
streamsSettings.put(StreamsConfig.topicPrefix(TopicConfig.MIN_IN_SYNC_REPLICAS_CONFIG), 2);
streamsSettings.put(StreamsConfig.NUM_STANDBY_REPLICAS_CONFIG, 1);
```

<a id="streams-developer-guide-config-streams--optional-configuration-parameters"></a>

---

<a id="streams-developer-guide-dsl-api"></a>

# Streams DSL

---

<a id="streams-developer-guide-processor-api"></a>

# Processor API

> [!TIP]
>

<a id="streams-developer-guide-processor-api--processor-api"></a>

>
> # Processor API
>
> The Processor API allows developers to define and connect custom processors and to interact with state stores. With the Processor API, you can define arbitrary stream processors that process one received record at a time, and connect these processors with their associated state stores to compose the processor topology that represents a customized processing logic.
>
>

<a id="streams-developer-guide-processor-api--overview"></a>

>
> # Overview
>
> The Processor API can be used to implement both **stateless** as well as **stateful** operations, where the latter is achieved through the use of state stores.
>
> **Combining the DSL and the Processor API:** You can combine the convenience of the DSL with the power and flexibility of the Processor API as described in the section [Applying processors (Processor API integration)](https://kafka.apache.org/43/streams/developer-guide/processor-api/dsl-api.html#streams-developer-guide-dsl-process).
>
>
>

<a id="streams-developer-guide-processor-api--defining-a-stream-processor"></a>

>
> # Defining a Stream Processor
>
> A [stream processor](https://kafka.apache.org/43/streams/developer-guide/core-concepts.html#streams_processor_node) is a node in the processor topology that represents a single processing step. With the Processor API, you can define arbitrary stream processors that processes one received record at a time, and connect these processors with their associated state stores to compose the processor topology.
>
> You can define a customized stream processor by implementing the `Processor` interface, which provides the `process()` API method. The `process()` method is called on each of the received records.
>
> The `Processor` interface also has an `init()` method, which is called by the Kafka Streams library during task construction phase. Processor instances should perform any required initialization in this method. The `init()` method passes in a `ProcessorContext` instance, which provides access to the metadata of the currently processed record, including its source Kafka topic and partition, its corresponding message offset, and further such information. You can also use this context instance to schedule a punctuation function (via `ProcessorContext#schedule()`), to forward a new record to the downstream processors (via `ProcessorContext#forward()`), and to request a commit of the current processing progress (via `ProcessorContext#commit()`). Any resources you set up in `init()` can be cleaned up in the `close()` method. Note that Kafka Streams may re-use a single `Processor` object by calling `init()` on it again after `close()`.
>
> The `Processor` interface takes four generic parameters: `KIn, VIn, KOut, VOut`. These define the input and output types that the processor implementation can handle. `KIn` and `VIn` define the key and value types of the `Record` that will be passed to `process()`. Likewise, `KOut` and `VOut` define the forwarded key and value types for the result `Record` that `ProcessorContext#forward()` will accept. If your processor does not forward any records at all (or if it only forwards `null` keys or values), a best practice is to set the output generic type argument to `Void`. If it needs to forward multiple types that don’t share a common superclass, you will have to set the output generic type argument to `Object`.
>
> Both the `Processor#process()` and the `ProcessorContext#forward()` methods handle records in the form of the `Record<K, V>` data class. This class gives you access to the main components of a Kafka record: the key, value, timestamp and headers. When forwarding records, you can use the constructor to create a new `Record` from scratch, or you can use the convenience builder methods to replace one of the `Record`’s properties and copy over the rest. For example, `inputRecord.withValue(newValue)` would copy the key, timestamp, and headers from `inputRecord` while setting the output record’s value to `newValue`. Note that this does not mutate `inputRecord`, but instead creates a shallow copy. Beware that this is only a shallow copy, so if you plan to mutate the key, value, or headers elsewhere in the program, you will want to create a deep copy of those fields yourself.
>
> In addition to handling incoming records via `Processor#process()`, you have the option to schedule periodic invocation (called “punctuation”) in your processor’s `init()` method by calling `ProcessorContext#schedule()` and passing it a `Punctuator`. The `PunctuationType` determines what notion of time is used for the punctuation scheduling: either [stream-time](https://kafka.apache.org/43/streams/developer-guide/core-concepts.html#streams_time) or wall-clock-time (by default, stream-time is configured to represent event-time via `TimestampExtractor`). When stream-time is used, `punctuate()` is triggered purely by data because stream-time is determined (and advanced forward) by the timestamps derived from the input data. When there is no new input data arriving, stream-time is not advanced and thus `punctuate()` is not called.
>
> For example, if you schedule a `Punctuator` function every 10 seconds based on `PunctuationType.STREAM_TIME` and if you process a stream of 60 records with consecutive timestamps from 1 (first record) to 60 seconds (last record), then `punctuate()` would be called 6 times. This happens regardless of the time required to actually process those records. `punctuate()` would be called 6 times regardless of whether processing these 60 records takes a second, a minute, or an hour.
>
> When wall-clock-time (i.e. `PunctuationType.WALL_CLOCK_TIME`) is used, `punctuate()` is triggered purely by the wall-clock time. Reusing the example above, if the `Punctuator` function is scheduled based on `PunctuationType.WALL_CLOCK_TIME`, and if these 60 records were processed within 20 seconds, `punctuate()` is called 2 times (one time every 10 seconds). If these 60 records were processed within 5 seconds, then no `punctuate()` is called at all. Note that you can schedule multiple `Punctuator` callbacks with different `PunctuationType` types within the same processor by calling `ProcessorContext#schedule()` multiple times inside `init()` method.
>
> **Attention**
>
> Stream-time is only advanced when Streams processes records. If there are no records to process, or if Streams is waiting for new records due to the [Task Idling](https://kafka.apache.org/documentation/#streamsconfigs_max.task.idle.ms) configuration, then the stream time will not advance and `punctuate()` will not be triggered if `PunctuationType.STREAM_TIME` was specified. This behavior is independent of the configured timestamp extractor, i.e., using `WallclockTimestampExtractor` does not enable wall-clock triggering of `punctuate()`.
>
> **Example**
>
> The following example `Processor` defines a simple word-count algorithm and the following actions are performed:
>
> - In the `init()` method, schedule the punctuation every 1000 time units (the time unit is normally milliseconds, which in this example would translate to punctuation every 1 second) and retrieve the local state store by its name “Counts”.
> - In the `process()` method, upon each received record, split the value string into words, and update their counts into the state store (we will talk about this later in this section).
> - In the `punctuate()` method, iterate the local state store and send the aggregated counts to the downstream processor (we will talk about downstream processors later in this section), and commit the current stream state.
>
>   public class WordCountProcessor implements Processor<String, String, String, String> {
>   private KeyValueStore<String, Integer> kvStore;
>
> ```
> @Override public void init(final ProcessorContext<String, String> context) {context.schedule(Duration.ofSeconds(1), PunctuationType.STREAM_TIME, timestamp -> {try (final KeyValueIterator<String, Integer> iter = kvStore.all()) {while (iter.hasNext()) {final KeyValue<String, Integer> entry = iter.next(); context.forward(new Record<>(entry.key, entry.value.toString(), timestamp));}} }); kvStore = context.getStateStore("Counts");}
> @Override public void process(final Record<String, String> record) {final String[] words = record.value().toLowerCase(Locale.getDefault()).split("\W+");
> for (final String word : words) {final Integer oldValue = kvStore.get(word);
> if (oldValue == null) {kvStore.put(word, 1); } else {kvStore.put(word, oldValue + 1);}}}
> @Override public void close() {// close any resources managed by this processor // Note: Do not close any StateStores as these are managed by the library}
> ```
>
>   }
>
> > [!NOTE]
> >
>
> **Stateful processing with state stores:** The `WordCountProcessor` defined above can access the currently received record in its `process()` method, and it can leverage state stores to maintain processing states to, for example, remember recently arrived records for stateful processing needs like aggregations and joins. For more information, see the state stores documentation.
>
>

<a id="streams-developer-guide-processor-api--unit-testing-processors"></a>

>
> # Unit Testing Processors
>
> Kafka Streams comes with a `test-utils` module to help you write unit tests for your processors [here](https://kafka.apache.org/43/streams/developer-guide/processor-api/testing.html#unit-testing-processors).
>
>

<a id="streams-developer-guide-processor-api--state-stores"></a>

>
> # State Stores
>
> To implement a **stateful** `Processor`, you must provide one or more state stores to the processor (*stateless* processors do not need state stores). State stores can be used to remember recently received input records, to track rolling aggregates, to de-duplicate input records, and more. Another feature of state stores is that they can be [interactively queried](https://kafka.apache.org/43/streams/developer-guide/processor-api/interactive-queries.html#streams-developer-guide-interactive-queries) from other applications, such as a NodeJS-based dashboard or a microservice implemented in Scala or Go.
>
> The available state store types in Kafka Streams have fault tolerance enabled by default.
>
>

<a id="streams-developer-guide-processor-api--defining-and-creating-a-state-store"></a>

>
> ## Defining and creating a State Store
>
> You can either use one of the available store types or implement your own custom store type. It’s common practice to leverage an existing store type via the `Stores` factory.
>
> Note that, when using Kafka Streams, you normally don’t create or instantiate state stores directly in your code. Rather, you define state stores indirectly by creating a so-called `StoreBuilder`. This builder is used by Kafka Streams as a factory to instantiate the actual state stores locally in application instances when and where needed.
>
> The following store types are available out of the box.
>
> // here, we create a <code>KeyValueStore&lt;String, Long&gt;</code> named “inmemory-counts”.
> import org.apache.kafka.streams.state.StoreBuilder;
> import org.apache.kafka.streams.state.Stores;</p><p>// Using a <code>KeyValueStoreBuilder</code> to build a <code>KeyValueStore</code>.
> StoreBuilder&lt;KeyValueStore&lt;String, Long» countStoreSupplier =
> Stores.keyValueStoreBuilder(
> Stores.inMemoryKeyValueStore(“inmemory-counts”), Serdes.String(), Serdes.Long());
> KeyValueStore&lt;String, Long&gt; countStore = countStoreSupplier.build();</p></li></ul></td></tr></table>
>
>

<a id="streams-developer-guide-processor-api--fault-tolerant-state-stores"></a>

>
> ## Fault-tolerant State Stores
>
> To make state stores fault-tolerant and to allow for state store migration without data loss, a state store can be continuously backed up to a Kafka topic behind the scenes. For example, to migrate a stateful stream task from one machine to another when [elastically adding or removing capacity from your application](https://kafka.apache.org/43/streams/developer-guide/processor-api/running-app.html#streams-developer-guide-execution-scaling). This topic is sometimes referred to as the state store’s associated *changelog topic* , or its *changelog*. For example, if you experience machine failure, the state store and the application’s state can be fully restored from its changelog. You can enable or disable this backup feature for a state store.
>
> Fault-tolerant state stores are backed by a [compacted](https://kafka.apache.org/documentation.html#compaction) changelog topic. The purpose of compacting this topic is to prevent the topic from growing indefinitely, to reduce the storage consumed in the associated Kafka cluster, and to minimize recovery time if a state store needs to be restored from its changelog topic.
>
> Fault-tolerant windowed state stores are backed by a topic that uses both compaction and deletion. Because of the structure of the message keys that are being sent to the changelog topics, this combination of deletion and compaction is required for the changelog topics of window stores. For window stores, the message keys are composite keys that include the “normal” key and window timestamps. For these types of composite keys it would not be sufficient to only enable compaction to prevent a changelog topic from growing out of bounds. With deletion enabled, old windows that have expired will be cleaned up by Kafka’s log cleaner as the log segments expire. The default retention setting is `Windows#maintainMs()` + 1 day. You can override this setting by specifying `StreamsConfig.WINDOW_STORE_CHANGE_LOG_ADDITIONAL_RETENTION_MS_CONFIG` in the `StreamsConfig`.
>
> When you open an `Iterator` from a state store you must call `close()` on the iterator when you are done working with it to reclaim resources; or you can use the iterator from within a try-with-resources statement. If you do not close an iterator, you may encounter an OOM error.
>
>

<a id="streams-developer-guide-processor-api--enable-or-disable-fault-tolerance-of-state-stores-store-changelogs"></a>

>
> ## Enable or Disable Fault Tolerance of State Stores (Store Changelogs)
>
> You can enable or disable fault tolerance for a state store by enabling or disabling the change logging of the store through `enableLogging()` and `disableLogging()`. You can also fine-tune the associated topic’s configuration if needed.
>
> Example for disabling fault-tolerance:
>
> ```
> import org.apache.kafka.streams.state.StoreBuilder;
> import org.apache.kafka.streams.state.Stores;
>
> StoreBuilder<KeyValueStore<String, Long>> countStoreSupplier = Stores.keyValueStoreBuilder(
>   Stores.persistentKeyValueStore("Counts"),
>     Serdes.String(),
>     Serdes.Long())
>   .withLoggingDisabled(); // disable backing up the store to a changelog topic
> ```
>
> Attention
>
> If the changelog is disabled then the attached state store is no longer fault tolerant and it can’t have any [standby replicas](https://kafka.apache.org/43/streams/developer-guide/processor-api/config-streams.html#streams-developer-guide-standby-replicas).
>
> Here is an example for enabling fault tolerance, with additional changelog-topic configuration: You can add any log config from [kafka.log.LogConfig](https://github.com/apache/kafka/blob/trunk/core/src/main/scala/kafka/log/LogConfig.scala). Unrecognized configs will be ignored.
>
> ```
> import org.apache.kafka.streams.state.StoreBuilder;
> import org.apache.kafka.streams.state.Stores;
>
> Map<String, String> changelogConfig = new HashMap();
> // override min.insync.replicas
> changelogConfig.put(TopicConfig.MIN_IN_SYNC_REPLICAS_CONFIG, "1")
>
> StoreBuilder<KeyValueStore<String, Long>> countStoreSupplier = Stores.keyValueStoreBuilder(
>   Stores.persistentKeyValueStore("Counts"),
>     Serdes.String(),
>     Serdes.Long())
>   .withLoggingEnabled(changelogConfig); // enable changelogging, with custom changelog settings
> ```
>
>

<a id="streams-developer-guide-processor-api--timestamped-state-stores"></a>

>
> ## Timestamped State Stores
>
> KTables always store timestamps by default. A timestamped state store improves stream processing semantics and enables handling out-of-order data in source KTables, detecting out-of-order joins and aggregations, and getting the timestamp of the latest update in an Interactive Query.
>
> You can query timestamped state stores both with and without a timestamp.
>
> **Upgrade note:** All users upgrade with a single rolling bounce per instance.
>
> - For Processor API users, nothing changes in existing applications, and you have the option of using the timestamped stores.
> - For DSL operators, store data is upgraded lazily in the background.
>
>

<a id="streams-developer-guide-processor-api--headers-in-state-stores"></a>

>
> ## Headers in State Stores
>
>
> Only persistent, RocksDB-backed suppliers exist for header-aware stores (the `Stores` factory names start with `persistent` and end with `WithHeaders`).
>
>
>
> **Upgrade note:** Rolling bounce, changelog compatibility, lazy on-disk migration, performance trade-offs, and downgrade constraints are covered in the [Kafka Streams upgrade guide](#streams-upgrade-guide--kip-1271-headers-aware-stores).
>
>

<a id="streams-developer-guide-processor-api--versioned-key-value-state-stores"></a>

>
> ## Versioned Key-Value State Stores
>
> Versioned key-value state stores are available since Kafka Streams 3.5. Rather than storing a single record version (value and timestamp) per key, versioned state stores may store multiple record versions per key. This allows versioned state stores to support timestamped retrieval operations to return the latest record (per key) as of a specified timestamp.
>
>
> Each versioned store has an associated, fixed-duration *history retention* parameter which specifies long old record versions should be kept for. In particular, a versioned store guarantees to return accurate results for timestamped retrieval operations where the timestamp being queried is within history retention of the current observed stream time.
>
> History retention also doubles as its *grace period* , which determines how far back in time out-of-order writes to the store will be accepted. A versioned store will not accept writes (inserts, updates, or deletions) if the timestamp associated with the write is older than the current observed stream time by more than the grace period. Stream time in this context is tracked per-partition, rather than per-key, which means it’s important that grace period (i.e., history retention) be set high enough to accommodate a record with one key arriving out-of-order relative to a record for another key.
>
> Because the memory footprint of versioned key-value stores is higher than that of non-versioned key-value stores, you may want to adjust your [RocksDB memory settings](https://kafka.apache.org/43/streams/developer-guide/processor-api/memory-mgmt.html#streams-developer-guide-memory-management-rocksdb) accordingly. Benchmarking your application with versioned stores is also advised as performance is expected to be worse than when using non-versioned stores.
>
> Versioned stores do not support caching or interactive queries at this time. Also, window stores and global tables may not be versioned.
>
> **Upgrade note:** Versioned state stores are opt-in only; no automatic upgrades from non-versioned to versioned stores will take place.
>
>
> If you wish to upgrade an application using persistent, non-versioned key-value stores to use persistent, versioned key-value stores instead, you can perform the following procedure:
>
> - Stop all application instances, and [clear any local state directories](https://kafka.apache.org/43/streams/developer-guide/processor-api/app-reset-tool.html#streams-developer-guide-reset-local-environment) for the store(s) being upgraded.
> - Update your application code to use versioned stores where desired.
> - Update your changelog topic configs, for the relevant state stores, to set the value of `min.compaction.lag.ms` to be at least your desired history retention. History retention plus one day is recommended as buffer for the use of broker wall clock time during compaction.
> - Restart your application instances and allow time for the versioned stores to rebuild state from changelog.
>
>

<a id="streams-developer-guide-processor-api--readonly-state-stores"></a>

>
> ## ReadOnly State Stores
>
> A read-only state store materialized the data from its input topic. It also uses the input topic for fault-tolerance, and thus does not have an additional changelog topic (the input topic is re-used as changelog). Thus, the input topic should be configured with [log compaction](https://kafka.apache.org/documentation.html#compaction). Note that no other processor should modify the content of the state store, and the only writer should be the associated “state update processor”; other processors may read the content of the read-only store.
>
> **note:** beware of the partitioning requirements when using read-only state stores for lookups during processing. You might want to make sure the original changelog topic is co-partitioned with the processors reading the read-only statestore.
>
>

<a id="streams-developer-guide-processor-api--implementing-custom-state-stores"></a>

>
> ## Implementing Custom State Stores
>
> You can use the built-in state store types or implement your own. The primary interface to implement for the store is `org.apache.kafka.streams.processor.StateStore`. Kafka Streams also has a few extended interfaces such as `KeyValueStore` and `VersionedKeyValueStore`.
>
>
> You also need to provide a “builder” for the store by implementing the `org.apache.kafka.streams.state.StoreBuilder` interface, which Kafka Streams uses to create instances of your store.
>
>

<a id="streams-developer-guide-processor-api--accessing-processor-context"></a>

>
> # Accessing Processor Context
>
> As we have mentioned in the Defining a Stream Processor section, a `ProcessorContext` control the processing workflow, such as scheduling a punctuation function, and committing the current processed state.
>
> This object can also be used to access the metadata related with the application like `applicationId`, `taskId`, and `stateDir`, and also `RecordMetadata` such as `topic`, `partition`, and `offset`.
>
>

<a id="streams-developer-guide-processor-api--connecting-processors-and-state-stores"></a>

>
> # Connecting Processors and State Stores
>
> Now that a processor (WordCountProcessor) and the state stores have been defined, you can construct the processor topology by connecting these processors and state stores together by using the `Topology` instance. In addition, you can add source processors with the specified Kafka topics to generate input data streams into the topology, and sink processors with the specified Kafka topics to generate output data streams out of the topology.
>
> Here is an example implementation:
>
> ```
> Topology builder = new Topology();
> // add the source processor node that takes Kafka topic "source-topic" as input
> builder.addSource("Source", "source-topic")
>     // add the WordCountProcessor node which takes the source processor as its upstream processor
>     .addProcessor("Process", () -> new WordCountProcessor(), "Source")
>     // add the count store associated with the WordCountProcessor processor
>     .addStateStore(countStoreBuilder, "Process")
>     // add the sink processor node that takes Kafka topic "sink-topic" as output
>     // and the WordCountProcessor node as its upstream processor
>     .addSink("Sink", "sink-topic", "Process");
> ```
>
> Here is a quick explanation of this example:
>
> - A source processor node named `"Source"` is added to the topology using the `addSource` method, with one Kafka topic `"source-topic"` fed to it.
> - A processor node named `"Process"` with the pre-defined `WordCountProcessor` logic is then added as the downstream processor of the `"Source"` node using the `addProcessor` method.
> - A predefined persistent key-value state store is created and associated with the `"Process"` node, using `countStoreBuilder`.
> - A sink processor node is then added to complete the topology using the `addSink` method, taking the `"Process"` node as its upstream processor and writing to a separate `"sink-topic"` Kafka topic (note that users can also use another overloaded variant of `addSink` to dynamically determine the Kafka topic to write to for each received record from the upstream processor).
>
> In some cases, it may be more convenient to add and connect a state store at the same time as you add the processor to the topology. This can be done by implementing `ConnectedStoreProvider#stores()` on the `ProcessorSupplier` instead of calling `Topology#addStateStore()`, like this:
>
> ```
> Topology builder = new Topology();
> // add the source processor node that takes Kafka "source-topic" as input
> builder.addSource("Source", "source-topic")
>     // add the WordCountProcessor node which takes the source processor as its upstream processor.
>     // the ProcessorSupplier provides the count store associated with the WordCountProcessor
>     .addProcessor("Process", new ProcessorSupplier<String, String, String, String>() {
>         public Processor<String, String, String, String> get() {
>             return new WordCountProcessor();
>         }
>
>         public Set<StoreBuilder<?>> stores() {
>             final StoreBuilder<KeyValueStore<String, Long>> countsStoreBuilder =
>                 Stores
>                     .keyValueStoreBuilder(
>                         Stores.persistentKeyValueStore("Counts"),
>                         Serdes.String(),
>                         Serdes.Long()
>                     );
>             return Collections.singleton(countsStoreBuilder);
>         }
>     }, "Source")
>     // add the sink processor node that takes Kafka topic "sink-topic" as output
>     // and the WordCountProcessor node as its upstream processor
>     .addSink("Sink", "sink-topic", "Process");
> ```
>
> This allows for a processor to “own” state stores, effectively encapsulating their usage from the user wiring the topology. Multiple processors that share a state store may provide the same store with this technique, as long as the `StoreBuilder` is the same `instance`.
>
> In these topologies, the `"Process"` stream processor node is considered a downstream processor of the `"Source"` node, and an upstream processor of the `"Sink"` node. As a result, whenever the `"Source"` node forwards a newly fetched record from Kafka to its downstream `"Process"` node, the `WordCountProcessor#process()` method is triggered to process the record and update the associated state store. Whenever `context#forward()` is called in the `WordCountProcessor#punctuate()` method, the aggregate records will be sent via the `"Sink"` processor node to the Kafka topic `"sink-topic"`. Note that in the `WordCountProcessor` implementation, you must refer to the same store name `"Counts"` when accessing the key-value store, otherwise an exception will be thrown at runtime, indicating that the state store cannot be found. If the state store is not associated with the processor in the `Topology` code, accessing it in the processor’s `init()` method will also throw an exception at runtime, indicating the state store is not accessible from this processor.
>
> Note that the `Topology#addProcessor` function takes a `ProcessorSupplier` as argument, and that the supplier pattern requires that a new `Processor` instance is returned each time `ProcessorSupplier#get()` is called. Creating a single `Processor` object and returning the same object reference in `ProcessorSupplier#get()` would be a violation of the supplier pattern and leads to runtime exceptions. So remember not to provide a singleton `Processor` instance to `Topology`. The `ProcessorSupplier` should always generate a new instance each time `ProcessorSupplier#get()` gets called.
>
> Now that you have fully defined your processor topology in your application, you can proceed to [running the Kafka Streams application](https://kafka.apache.org/43/streams/developer-guide/processor-api/running-app.html#streams-developer-guide-execution).
>
> - [Documentation](https://kafka.apache.org/documentation)
> - [Kafka Streams](https://kafka.apache.org/documentation/streams)
> - [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)
>

---

<a id="streams-developer-guide-dsl-topology-naming"></a>

<a id="streams-developer-guide-dsl-topology-naming--naming-operators-in-a-streams-dsl-application"></a>

# Naming Operators in a Streams DSL application

<a id="streams-developer-guide-dsl-topology-naming--developer-guide-for-kafka-streams"></a>

# Developer Guide for Kafka Streams

<a id="streams-developer-guide-dsl-topology-naming--naming-operators-in-a-kafka-streams-dsl-application"></a>

# Naming Operators in a Kafka Streams DSL Application

You now can give names to processors when using the Kafka Streams DSL. In the PAPI there are `Processors` and `State Stores` and you are required to explicitly name each one.

At the DSL layer, there are operators. A single DSL operator may compile down to multiple `Processors` and `State Stores`, and if required `repartition topics`. But with the Kafka Streams DSL, all these names are generated for you. There is a relationship between the generated processor name state store names (hence changelog topic names) and repartition topic names. Note, that the names of state stores and changelog/repartition topics are “stateful” while processor names are “stateless”.

This distinction of stateful vs. stateless names has important implications when updating your topology. While the internal naming makes creating a topology with the DSL much more straightforward, there are a couple of trade-offs. The first trade-off is what we could consider a readability issue. The other more severe trade-off is the shifting of names due to the relationship between the DSL operator and the generated `Processors`, `State Stores` changelog topics and repartition topics.

<a id="streams-developer-guide-dsl-topology-naming--readability-issues"></a>

# Readability Issues

By saying there is a readability trade-off, we are referring to viewing a description of the topology. When you render the string description of your topology via the `Topology#describe()` method, you can see what the processor is, but you don’t have any context for its business purpose. For example, consider the following simple topology:

```
KStream<String,String> stream = builder.stream("input");
stream.filter((k,v) -> !v.equals("invalid_txn"))
	  .mapValues((v) -> v.substring(0,5))
	  .to("output");
```

Running `Topology#describe()` yields this string:

```
Topologies:
   Sub-topology: 0
	Source: KSTREAM-SOURCE-0000000000 (topics: [input])
	  --> KSTREAM-FILTER-0000000001
	Processor: KSTREAM-FILTER-0000000001 (stores: [])
	  --> KSTREAM-MAPVALUES-0000000002
	  <-- KSTREAM-SOURCE-0000000000
	Processor: KSTREAM-MAPVALUES-0000000002 (stores: [])
	  --> KSTREAM-SINK-0000000003
	  <-- KSTREAM-FILTER-0000000001
	Sink: KSTREAM-SINK-0000000003 (topic: output)
	  <-- KSTREAM-MAPVALUES-0000000002
```

From this report, you can see what the different operators are, but what is the broader context here? For example, consider `KSTREAM-FILTER-0000000001`, we can see that it’s a filter operation, which means that records are dropped that don’t match the given predicate. But what is the meaning of the predicate? Additionally, you can see the topic names of the source and sink nodes, but what if the topics aren’t named in a meaningful way? Then you’re left to guess the business purpose behind these topics.

Also notice the numbering here: the source node is suffixed with `0000000000` indicating it’s the first processor in the topology. The filter is suffixed with `0000000001`, indicating it’s the second processor in the topology. In Kafka Streams, there are now overloaded methods for both `KStream` and `KTable` that accept a new parameter `Named`. By using the `Named` class DSL users can provide meaningful names to the processors in their topology.

Now let’s take a look at your topology with all the processors named:

```
KStream<String,String> stream =
builder.stream("input", Consumed.as("Customer_transactions_input_topic"));
stream.filter((k,v) -> !v.equals("invalid_txn"), Named.as("filter_out_invalid_txns"))
	  .mapValues((v) -> v.substring(0,5), Named.as("Map_values_to_first_6_characters"))
	  .to("output", Produced.as("Mapped_transactions_output_topic"));

Topologies:
   Sub-topology: 0
	Source: Customer_transactions_input_topic (topics: [input])
	  --> filter_out_invalid_txns
	Processor: filter_out_invalid_txns (stores: [])
	  --> Map_values_to_first_6_characters
	  <-- Customer_transactions_input_topic
	Processor: Map_values_to_first_6_characters (stores: [])
	  --> Mapped_transactions_output_topic
	  <-- filter_out_invalid_txns
	Sink: Mapped_transactions_output_topic (topic: output)
	  <-- Map_values_to_first_6_characters
```

Now you can look at the topology description and easily understand what role each processor plays in the topology. But there’s another reason for naming your processor nodes when you have stateful operators that remain between restarts of your Kafka Streams applications, state stores, changelog topics, and repartition topics.

<a id="streams-developer-guide-dsl-topology-naming--changing-names"></a>

# Changing Names

Generated names are numbered where they are built in the topology. The name generation strategy is `KSTREAM|KTABLE->operator name<->number suffix<`. The number is a globally incrementing number that represents the operator’s order in the topology. The generated number is prefixed with a varying number of “0"s to create a string that is consistently 10 characters long. This means that if you add/remove or shift the order of operations, the position of the processor shifts, which shifts the name of the processor. Since **most** processors exist in memory only, this name shifting presents no issue for many topologies. But the name shifting does have implications for topologies with stateful operators or repartition topics. Here’s a different topology with some state:

```
KStream<String,String> stream = builder.stream("input");
 stream.groupByKey()
	   .count()
	   .toStream()
	   .to("output");
```

This topology description yields the following:

```
Topologies:
   Sub-topology: 0
	Source: KSTREAM-SOURCE-0000000000 (topics: [input])
	 --> KSTREAM-AGGREGATE-0000000002
	Processor: KSTREAM-AGGREGATE-0000000002 (stores: [KSTREAM-AGGREGATE-STATE-STORE-0000000001])
	 --> KTABLE-TOSTREAM-0000000003
	 <-- KSTREAM-SOURCE-0000000000
	Processor: KTABLE-TOSTREAM-0000000003 (stores: [])
	 --> KSTREAM-SINK-0000000004
	 <-- KSTREAM-AGGREGATE-0000000002
	Sink: KSTREAM-SINK-0000000004 (topic: output)
	 <-- KTABLE-TOSTREAM-0000000003
```

You can see from the topology description above that the state store is named `KSTREAM-AGGREGATE-STATE-STORE-0000000002`. Here’s what happens when you add a filter to keep some of the records out of the aggregation:

```
KStream<String,String> stream = builder.stream("input");
stream.filter((k,v)-> v !=null && v.length() >= 6 )
      .groupByKey()
      .count()
      .toStream()
      .to("output");
```

And the corresponding topology:

```
Topologies:
	Sub-topology: 0
	 Source: KSTREAM-SOURCE-0000000000 (topics: [input])
	  --> KSTREAM-FILTER-0000000001
	 Processor: KSTREAM-FILTER-0000000001 (stores: [])
	   --> KSTREAM-AGGREGATE-0000000003
	   <-- KSTREAM-SOURCE-0000000000
	 Processor: KSTREAM-AGGREGATE-0000000003 (stores: [KSTREAM-AGGREGATE-STATE-STORE-0000000002])
	   --> KTABLE-TOSTREAM-0000000004
	   <-- KSTREAM-FILTER-0000000001
	 Processor: KTABLE-TOSTREAM-0000000004 (stores: [])
	   --> KSTREAM-SINK-0000000005
	   <-- KSTREAM-AGGREGATE-0000000003
	  Sink: KSTREAM-SINK-0000000005 (topic: output)
	   <-- KTABLE-TOSTREAM-0000000004
```

Notice that since you’ve added an operation *before* the `count` operation, the state store (and the changelog topic) names have changed. This name change means you can’t do a rolling re-deployment of your updated topology. Also, you must use the [Streams Reset Tool](#documentation-streams-developer-guide-app-reset-tool) to re-calculate the aggregations, because the changelog topic has changed on start-up and the new changelog topic contains no data. Fortunately, there’s an easy solution to remedy this situation. Give the state store a user-defined name instead of relying on the generated one, so you don’t have to worry about topology changes shifting the name of the state store. You’ve had the ability to name repartition topics with the `Joined`, `StreamJoined`, and`Grouped` classes, and name state store and changelog topics with `Materialized`. But it’s worth reiterating the importance of naming these DSL topology operations again. Here’s how your DSL code looks now giving a specific name to your state store:

```
KStream<String,String> stream = builder.stream("input");
stream.filter((k, v) -> v != null && v.length() >= 6)
	  .groupByKey()
	  .count(Materialized.as("Purchase_count_store"))
	  .toStream()
	  .to("output");
```

And here’s the topology

```
Topologies:
   Sub-topology: 0
	Source: KSTREAM-SOURCE-0000000000 (topics: [input])
	  --> KSTREAM-FILTER-0000000001
	Processor: KSTREAM-FILTER-0000000001 (stores: [])
	  --> KSTREAM-AGGREGATE-0000000002
	  <-- KSTREAM-SOURCE-0000000000
	Processor: KSTREAM-AGGREGATE-0000000002 (stores: [Purchase_count_store])
	  --> KTABLE-TOSTREAM-0000000003
	  <-- KSTREAM-FILTER-0000000001
	Processor: KTABLE-TOSTREAM-0000000003 (stores: [])
	  --> KSTREAM-SINK-0000000004
	  <-- KSTREAM-AGGREGATE-0000000002
	Sink: KSTREAM-SINK-0000000004 (topic: output)
	  <-- KTABLE-TOSTREAM-0000000003
```

Now, even though you’ve added processors before your state store, the store name and its changelog topic names don’t change. This makes your topology more robust and resilient to changes made by adding or removing processors.

<a id="streams-developer-guide-dsl-topology-naming--conclusion"></a>

# Conclusion

It’s a good practice to name your processing nodes when using the DSL, and it’s even more important to do this when you have “stateful” processors your application such as repartition topics and state stores (and the accompanying changelog topics).

Here are a couple of points to remember when naming your DSL topology:

1. If you have an *existing topology* and you *haven’t* named your state stores (and changelog topics) and repartition topics, we recommended that you do so. But this will be a topology breaking change, so you’ll need to shut down all application instances, make the changes, and run the [Streams Reset Tool](#documentation-streams-developer-guide-app-reset-tool). Although this may be inconvenient at first, it’s worth the effort to protect your application from unexpected errors due to topology changes.
2. If you have a *new topology* , make sure you name the persistent parts of your topology: state stores (changelog topics) and repartition topics. This way, when you deploy your application, you’re protected from topology changes that otherwise would break your Kafka Streams application. If you don’t want to add names to stateless processors at first, that’s fine as you can always go back and add the names later.

Here’s a quick reference on naming the critical parts of your Kafka Streams application to prevent topology name changes from breaking your application:

| Operation | Naming Class |
| --- | --- |
| Aggregation repartition topics | Grouped |
| KStream-KStream Join repartition topics | StreamJoined |
| KStream-KTable Join repartition topic | Joined |
| KStream-KStream Join state stores | StreamJoined |
| State Stores (for aggregations and KTable-KTable joins) | Materialized |
| Stream/Table non-stateful operations | Named |

To further enforce best practices, Kafka Streams provides a configuration option, `ensure.explicit.internal.resource.naming`:

```
/
            Properties props = new Properties();
            props.put(StreamsConfig.ENSURE_EXPLICIT_INTERNAL_RESOURCE_NAMING_CONFIG, true);
```

This parameter ensures that all internal topics, state stores, and changelog topics have explicitly defined names. When this configuration is enabled, a Kafka Streams application will not start if any of these components rely on auto-generated names. This guarantees stability across topology updates, as manually defined names remain unchanged even when new processors or transformations are added. Enforcing explicit naming is particularly important in production environments, where consistency and backward compatibility are essential for maintaining reliable stream processing applications.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-datatypes"></a>

<a id="streams-developer-guide-datatypes--data-types-and-serialization"></a>

# Data Types and Serialization

Every Kafka Streams application must provide Serdes (Serializer/Deserializer) for the data types of record keys and record values (e.g. `java.lang.String`) to materialize the data when necessary. Operations that require such Serdes information include: `stream()`, `table()`, `to()`, `repartition()`, `groupByKey()`, `groupBy()`.

You can provide Serdes by using either of these methods, but you must use at least one:

- By setting default Serdes in the `java.util.Properties` config instance.
- By specifying explicit Serdes when calling the appropriate API methods, thus overriding the defaults.

<a id="streams-developer-guide-datatypes--configuring-serdes"></a>

# Configuring Serdes

Serdes specified in the Streams configuration are used as the default in your Kafka Streams application. Because this config’s default is null, you must either set a default Serde by using this configuration or pass in Serdes explicitly, as described below.

```
import org.apache.kafka.common.serialization.Serdes;
import org.apache.kafka.streams.StreamsConfig;

Properties settings = new Properties();
// Default serde for keys of data records (here: built-in serde for String type)
settings.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
// Default serde for values of data records (here: built-in serde for Long type)
settings.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Long().getClass().getName());
```

<a id="streams-developer-guide-datatypes--overriding-default-serdes"></a>

# Overriding default Serdes

You can also specify Serdes explicitly by passing them to the appropriate API methods, which overrides the default serde settings:

```
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;

final Serde<String> stringSerde = Serdes.String();
final Serde<Long> longSerde = Serdes.Long();

// The stream userCountByRegion has type `String` for record keys (for region)
// and type `Long` for record values (for user counts).
KStream<String, Long> userCountByRegion = ...;
userCountByRegion.to("RegionCountsTopic", Produced.with(stringSerde, longSerde));
```

If you want to override serdes selectively, i.e., keep the defaults for some fields, then don’t specify the serde whenever you want to leverage the default settings:

```
import org.apache.kafka.common.serialization.Serde;
import org.apache.kafka.common.serialization.Serdes;

// Use the default serializer for record keys (here: region as String) by not specifying the key serde,
// but override the default serializer for record values (here: userCount as Long).
final Serde<Long> longSerde = Serdes.Long();
KStream<String, Long> userCountByRegion = ...;
userCountByRegion.to("RegionCountsTopic", Produced.valueSerde(Serdes.Long()));
```

If some of your incoming records are corrupted or ill-formatted, they will cause the deserializer class to report an error. Since 1.0.x we have introduced an `DeserializationExceptionHandler` interface which allows you to customize how to handle such records. The customized implementation of the interface can be specified via the `StreamsConfig`. For more details, please feel free to read the [Configuring a Streams Application](https://kafka.apache.org/43/streams/developer-guide/datatypes/config-streams.html#default-deserialization-exception-handler) section.

<a id="streams-developer-guide-datatypes--available-serdes"></a>

# Available Serdes

<a id="streams-developer-guide-datatypes--primitive-and-basic-types"></a>

## Primitive and basic types

Apache Kafka includes several built-in serde implementations for Java primitives and basic types such as `byte[]` in its `kafka-clients` Maven artifact:

```
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-clients</artifactId>
    <version>4.3.1</version>
</dependency>
```

This artifact provides the following serde implementations under the package [org.apache.kafka.common.serialization](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/serialization), which you can leverage when e.g., defining default serializers in your Streams configuration.

| Data type | Serde |
| --- | --- |
| byte[] | `Serdes.ByteArray()`, `Serdes.Bytes()` (see tip below) |
| ByteBuffer | `Serdes.ByteBuffer()` |
| Double | `Serdes.Double()` |
| Integer | `Serdes.Integer()` |
| Long | `Serdes.Long()` |
| String | `Serdes.String()` |
| UUID | `Serdes.UUID()` |
| Void | `Serdes.Void()` |
| List | `Serdes.ListSerde()` |
| Boolean | `Serdes.Boolean()` |

> [!TIP]
>

[Bytes](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/utils/Bytes.java) is a wrapper for Java’s `byte[]` (byte array) that supports proper equality and ordering semantics. You may want to consider using `Bytes` instead of `byte[]` in your applications.

<a id="streams-developer-guide-datatypes--json"></a>

## JSON

The Kafka Streams code examples also include a basic serde implementation for JSON:

- [PageViewTypedDemo](https://github.com/apache/kafka/blob/4.3/streams/examples/src/main/java/org/apache/kafka/streams/examples/pageview/PageViewTypedDemo.java#L83)

As shown in the example, you can use JSONSerdes inner classes `Serdes.serdeFrom(<serializerInstance>, <deserializerInstance>)` to construct JSON compatible serializers and deserializers.

<a id="streams-developer-guide-datatypes--window-serdes"></a>

## Window Serdes

Apache Kafka Streams includes serde implementations for windowed types in its `kafka-streams` Maven artifact:

```
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams</artifactId>
    <version>4.3.1</version>
</dependency>
```

This artifact provides the following windowed serde implementations under the package [org.apache.kafka.streams.kstream](https://github.com/apache/kafka/blob/4.3/streams/src/main/java/org/apache/kafka/streams/kstream):

**Serdes:**

- `WindowedSerdes.TimeWindowedSerde<T>`
- `WindowedSerdes.SessionWindowedSerde<T>`

**Serializers:**

- `TimeWindowedSerializer<T>`
- `SessionWindowedSerializer<T>`

**Deserializers:**

- `TimeWindowedDeserializer<T>`
- `SessionWindowedDeserializer<T>`

<a id="streams-developer-guide-datatypes--usage-in-code"></a>

### Usage in Code

When using windowed serdes in your application code, you typically create instances via constructors or factory methods:

```
// Time windowed serde - using factory method
Serde<Windowed<String>> timeWindowedSerde =
    WindowedSerdes.timeWindowedSerdeFrom(String.class, 500L);

// Time windowed serde - using constructor
Serde<Windowed<String>> timeWindowedSerde2 =
    new WindowedSerdes.TimeWindowedSerde<>(Serdes.String(), 500L);

// Session windowed serde - using factory method
Serde<Windowed<String>> sessionWindowedSerde =
    WindowedSerdes.sessionWindowedSerdeFrom(String.class);

// Session windowed serde - using constructor
Serde<Windowed<String>> sessionWindowedSerde2 =
    new WindowedSerdes.SessionWindowedSerde<>(Serdes.String());

// Using individual serializers/deserializers
TimeWindowedSerializer<String> serializer = new TimeWindowedSerializer<>(Serdes.String().serializer());
TimeWindowedDeserializer<String> deserializer = new TimeWindowedDeserializer<>(Serdes.String().deserializer(), 500L);
```

<a id="streams-developer-guide-datatypes--usage-in-command-line"></a>

### Usage in Command Line

When using command-line tools (like `bin/kafka-console-consumer.sh`), you can configure windowed deserializers by passing the inner class and window size via configuration properties. The property names use a prefix pattern:

```
# Time windowed deserializer configuration --formatter-property print.key=true \ --formatter-property key.deserializer=org.apache.kafka.streams.kstream.TimeWindowedDeserializer \ --formatter-property key.deserializer.windowed.inner.deserializer.class=org.apache.kafka.common.serialization.StringDeserializer \ --formatter-property key.deserializer.window.size.ms=500

# Session windowed deserializer configuration --formatter-property print.key=true \ --formatter-property key.deserializer=org.apache.kafka.streams.kstream.SessionWindowedDeserializer \ --formatter-property key.deserializer.windowed.inner.deserializer.class=org.apache.kafka.common.serialization.StringDeserializer
```

<a id="streams-developer-guide-datatypes--implementing-custom-serdes"></a>

# Implementing custom Serdes

If you need to implement custom Serdes, your best starting point is to take a look at the source code references of existing Serdes (see previous section). Typically, your workflow will be similar to:

1. Write a *serializer* for your data type `T` by implementing [org.apache.kafka.common.serialization.Serializer](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/serialization/Serializer.java).
2. Write a *deserializer* for `T` by implementing [org.apache.kafka.common.serialization.Deserializer](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/serialization/Deserializer.java).
3. Write a *serde* for `T` by implementing [org.apache.kafka.common.serialization.Serde](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/serialization/Serde.java), which you either do manually (see existing Serdes in the previous section) or by leveraging helper functions in [Serdes](https://github.com/apache/kafka/blob/4.3/clients/src/main/java/org/apache/kafka/common/serialization/Serdes.java) such as `Serdes.serdeFrom(Serializer<T>, Deserializer<T>)`. Note that you will need to implement your own class (that has no generic types) if you want to use your custom serde in the configuration provided to `KafkaStreams`. If your serde class has generic types or you use `Serdes.serdeFrom(Serializer<T>, Deserializer<T>)`, you can pass your serde only via methods calls (for example `builder.stream("topicName", Consumed.with(...))`).

<a id="streams-developer-guide-datatypes--kafka-streams-dsl-for-scala-implicit-serdesscala-dsl-serdes-permalink-to-this-headline"></a>
<a id="streams-developer-guide-datatypes--kafka-streams-dsl-for-scala-implicit-serdes"></a>

# Kafka Streams DSL for Scala Implicit Serdes

When using the [Kafka Streams DSL for Scala](https://kafka.apache.org/43/streams/developer-guide/datatypes/dsl-api.html#scala-dsl) you’re not required to configure a default Serdes. In fact, it’s not supported. Serdes are instead provided implicitly by default implementations for common primitive datatypes. See the [Implicit Serdes](https://kafka.apache.org/43/streams/developer-guide/datatypes/dsl-api.html#scala-dsl-implicit-serdes) and [User-Defined Serdes](https://kafka.apache.org/43/streams/developer-guide/datatypes/dsl-api.html#scala-dsl-user-defined-serdes) sections in the DSL API documentation for details

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-testing"></a>

<a id="streams-developer-guide-testing--testing-a-streams-application"></a>

# Testing a Streams Application

<a id="streams-developer-guide-testing--testing-kafka-streams"></a>

# Testing Kafka Streams

<a id="streams-developer-guide-testing--importing-the-test-utilities"></a>

# Importing the test utilities

To test a Kafka Streams application, Kafka provides a test-utils artifact that can be added as regular dependency to your test code base. Example `pom.xml` snippet when using Maven:

```
<dependency>
    <groupId>org.apache.kafka</groupId>
    <artifactId>kafka-streams-test-utils</artifactId>
    <version>4.3.1</version>
    <scope>test</scope>
</dependency>
```

<a id="streams-developer-guide-testing--testing-a-streams-application-2"></a>

# Testing a Streams application

The test-utils package provides a `TopologyTestDriver` that can be used pipe data through a `Topology` that is either assembled manually using Processor API or via the DSL using `StreamsBuilder`. The test driver simulates the library runtime that continuously fetches records from input topics and processes them by traversing the topology. You can use the test driver to verify that your specified processor topology computes the correct result with the manually piped in data records. The test driver captures the results records and allows to query its embedded state stores.

```
// Processor API
Topology topology = new Topology();
topology.addSource("sourceProcessor", "input-topic");
topology.addProcessor("processor", ..., "sourceProcessor");
topology.addSink("sinkProcessor", "output-topic", "processor");
// or
// using DSL
StreamsBuilder builder = new StreamsBuilder();
builder.stream("input-topic").filter(...).to("output-topic");
Topology topology = builder.build();

// create test driver
TopologyTestDriver testDriver = new TopologyTestDriver(topology);
```

With the test driver you can create `TestInputTopic` giving topic name and the corresponding serializers. `TestInputTopic` provides various methods to pipe new message values, keys and values, or list of KeyValue objects.

```
TestInputTopic<String, Long> inputTopic = testDriver.createInputTopic("input-topic", stringSerde.serializer(), longSerde.serializer());
inputTopic.pipeInput("key", 42L);
```

To verify the output, you can use `TestOutputTopic` where you configure the topic and the corresponding deserializers during initialization. It offers helper methods to read only certain parts of the result records or the collection of records. For example, you can validate returned `KeyValue` with standard assertions if you only care about the key and value, but not the timestamp of the result record.

```
TestOutputTopic<String, Long> outputTopic = testDriver.createOutputTopic("output-topic", stringSerde.deserializer(), longSerde.deserializer());
assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("key", 42L)));
```

`TopologyTestDriver` supports punctuations, too. Event-time punctuations are triggered automatically based on the processed records’ timestamps. Wall-clock-time punctuations can also be triggered by advancing the test driver’s wall-clock-time (the driver mocks wall-clock-time internally to give users control over it).

```
testDriver.advanceWallClockTime(Duration.ofSeconds(20));
```

Additionally, you can access state stores via the test driver before or after a test. Accessing stores before a test is useful to pre-populate a store with some initial values. After data was processed, expected updates to the store can be verified.

```
KeyValueStore store = testDriver.getKeyValueStore("store-name");
```

Note, that you should always close the test driver at the end to make sure all resources are release properly.

```
testDriver.close();
```

<a id="streams-developer-guide-testing--example"></a>

## Example

The following example demonstrates how to use the test driver and helper classes. The example creates a topology that computes the maximum value per key using a key-value-store. While processing, no output is generated, but only the store is updated. Output is only sent downstream based on event-time and wall-clock punctuations.

```
private TopologyTestDriver testDriver;
private TestInputTopic<String, Long> inputTopic;
private TestOutputTopic<String, Long> outputTopic;
private KeyValueStore<String, Long> store;

private Serde<String> stringSerde = new Serdes.StringSerde();
private Serde<Long> longSerde = new Serdes.LongSerde();

@Before
public void setup() {
    Topology topology = new Topology();
    topology.addSource("sourceProcessor", "input-topic");
    topology.addProcessor("aggregator", new CustomMaxAggregatorSupplier(), "sourceProcessor");
    topology.addStateStore(
        Stores.keyValueStoreBuilder(
            Stores.inMemoryKeyValueStore("aggStore"),
            Serdes.String(),
            Serdes.Long()).withLoggingDisabled(), // need to disable logging to allow store pre-populating
        "aggregator");
    topology.addSink("sinkProcessor", "result-topic", "aggregator");

    // setup test driver
    Properties props = new Properties();
    props.setProperty(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass().getName());
    props.setProperty(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Long().getClass().getName());
    testDriver = new TopologyTestDriver(topology, props);

    // setup test topics
    inputTopic = testDriver.createInputTopic("input-topic", stringSerde.serializer(), longSerde.serializer());
    outputTopic = testDriver.createOutputTopic("result-topic", stringSerde.deserializer(), longSerde.deserializer());

    // pre-populate store
    store = testDriver.getKeyValueStore("aggStore");
    store.put("a", 21L);
}

@After
public void tearDown() {
    testDriver.close();
}

@Test
public void shouldFlushStoreForFirstInput() {
    inputTopic.pipeInput("a", 1L);
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

@Test
public void shouldNotUpdateStoreForSmallerValue() {
    inputTopic.pipeInput("a", 1L);
    assertThat(store.get("a"), equalTo(21L));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

@Test
public void shouldNotUpdateStoreForLargerValue() {
    inputTopic.pipeInput("a", 42L);
    assertThat(store.get("a"), equalTo(42L));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 42L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

@Test
public void shouldUpdateStoreForNewKey() {
    inputTopic.pipeInput("b", 21L);
    assertThat(store.get("b"), equalTo(21L));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("b", 21L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

@Test
public void shouldPunctuateIfEvenTimeAdvances() {
    final Instant recordTime = Instant.now();
    inputTopic.pipeInput("a", 1L,  recordTime);
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));

    inputTopic.pipeInput("a", 1L,  recordTime);
    assertThat(outputTopic.isEmpty(), is(true));

    inputTopic.pipeInput("a", 1L, recordTime.plusSeconds(10L));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

@Test
public void shouldPunctuateIfWallClockTimeAdvances() {
    testDriver.advanceWallClockTime(Duration.ofSeconds(60));
    assertThat(outputTopic.readKeyValue(), equalTo(new KeyValue<>("a", 21L)));
    assertThat(outputTopic.isEmpty(), is(true));
}

public class CustomMaxAggregatorSupplier implements ProcessorSupplier<String, Long> {
    @Override
    public Processor<String, Long> get() {
        return new CustomMaxAggregator();
    }
}

public class CustomMaxAggregator implements Processor<String, Long> {
    ProcessorContext context;
    private KeyValueStore<String, Long> store;

    @SuppressWarnings("unchecked")
    @Override
    public void init(ProcessorContext context) {
        this.context = context;
        context.schedule(Duration.ofSeconds(60), PunctuationType.WALL_CLOCK_TIME, time -> flushStore());
        context.schedule(Duration.ofSeconds(10), PunctuationType.STREAM_TIME, time -> flushStore());
        store = (KeyValueStore<String, Long>) context.getStateStore("aggStore");
    }

    @Override
    public void process(String key, Long value) {
        Long oldValue = store.get(key);
        if (oldValue == null || value > oldValue) {
            store.put(key, value);
        }
    }

    private void flushStore() {
        KeyValueIterator<String, Long> it = store.all();
        while (it.hasNext()) {
            KeyValue<String, Long> next = it.next();
            context.forward(next.key, next.value);
        }
    }

    @Override
    public void close() {}
}
```

<a id="streams-developer-guide-testing--unit-testing-processors"></a>

# Unit Testing Processors

If you [write a Processor](https://kafka.apache.org/43/streams/developer-guide/testing/processor-api.html), you will want to test it.

Because the `Processor` forwards its results to the context rather than returning them, Unit testing requires a mocked context capable of capturing forwarded data for inspection. For this reason, we provide a `MockProcessorContext` in `test-utils`.

**Construction**

To begin with, instantiate your processor and initialize it with the mock context:

```
final Processor processorUnderTest = ...;
final MockProcessorContext<String, Long> context = new MockProcessorContext<>();
processorUnderTest.init(context);
```

If you need to pass configuration to your processor or set the default serdes, you can create the mock with config:

```
final Properties props = new Properties();
props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Long().getClass());
props.put("some.other.config", "some config value");
final MockProcessorContext<String, Long> context = new MockProcessorContext<>(props);
```

**Captured data**

The mock will capture any values that your processor forwards. You can make assertions on them:

```
processorUnderTest.process("key", "value");

final Iterator<CapturedForward<? extends String, ? extends Long>> forwarded = context.forwarded().iterator();
assertEquals(forwarded.next().record(), new Record<>(..., ...));
assertFalse(forwarded.hasNext());

// you can reset forwards to clear the captured data. This may be helpful in constructing longer scenarios.
context.resetForwards();

assertEquals(context.forwarded().size(), 0);
```

If your processor forwards to specific child processors, you can query the context for captured data by child name:

```
final List<CapturedForward<? extends String, ? extends Long>> captures = context.forwarded("childProcessorName");
```

The mock also captures whether your processor has called `commit()` on the context:

```
assertTrue(context.committed());

// commit captures can also be reset.
context.resetCommit();

assertFalse(context.committed());
```

**Setting record metadata**

In case your processor logic depends on the record metadata (topic, partition, offset), you can set them on the context:

```
context.setRecordMetadata("topicName", /*partition*/ 0, /*offset*/ 0L);
```

Once these are set, the context will continue returning the same values, until you set new ones.

**State stores**

In case your punctuator is stateful, the mock context allows you to register state stores. You’re encouraged to use a simple in-memory store of the appropriate type (KeyValue, Windowed, or Session), since the mock context does *not* manage changelogs, state directories, etc.

```
final KeyValueStore<String, Integer> store =
    Stores.keyValueStoreBuilder(
            Stores.inMemoryKeyValueStore("myStore"),
            Serdes.String(),
            Serdes.Integer()
        )
        .withLoggingDisabled() // Changelog is not supported by MockProcessorContext.
        .build();
store.init(context, store);
```

**Verifying punctuators**

Processors can schedule punctuators to handle periodic tasks. The mock context does *not* automatically execute punctuators, but it does capture them to allow you to unit test them as well:

```
final MockProcessorContext.CapturedPunctuator capturedPunctuator = context.scheduledPunctuators().get(0);
final long interval = capturedPunctuator.getIntervalMs();
final PunctuationType type = capturedPunctuator.getType();
final boolean cancelled = capturedPunctuator.cancelled();
final Punctuator punctuator = capturedPunctuator.getPunctuator();
punctuator.punctuate(/*timestamp*/ 0L);
```

If you need to write tests involving automatic firing of scheduled punctuators, we recommend creating a simple topology with your processor and using the [`TopologyTestDriver`](https://kafka.apache.org/43/streams/developer-guide/testing/testing.html#testing-topologytestdriver).

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-interactive-queries"></a>

<a id="streams-developer-guide-interactive-queries--interactive-queries"></a>

# Interactive Queries

Interactive queries allow you to leverage the state of your application from outside your application. The Kafka Streams enables your applications to be queryable.

The full state of your application is typically [split across many distributed instances of your application](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams_architecture_state), and across many state stores that are managed locally by these application instances.

There are local and remote components to interactively querying the state of your application.

Local state
An application instance can query the locally managed portion of the state and directly query its own local state stores. You can use the corresponding local data in other parts of your application code, as long as it doesn’t require calling the Kafka Streams API. Querying state stores is always read-only to guarantee that the underlying state stores will never be mutated out-of-band (e.g., you cannot add new entries). State stores should only be mutated by the corresponding processor topology and the input data it operates on. For more information, see Querying local state stores for an app instance.
Remote state

To query the full state of your application, you must connect the various fragments of the state, including:

- query local state stores
- discover all running instances of your application in the network and their state stores
- communicate with these instances over the network (e.g., an RPC layer)

Connecting these fragments enables communication between instances of the same app and communication from other applications for interactive queries. For more information, see Querying remote state stores for the entire app.

Kafka Streams natively provides all of the required functionality for interactively querying the state of your application, except if you want to expose the full state of your application via interactive queries. To allow application instances to communicate over the network, you must add a Remote Procedure Call (RPC) layer to your application (e.g., REST API).

This table shows the Kafka Streams native communication support for various procedures.

| Procedure | Application instance | Entire application |
| --- | --- | --- |
| Query local state stores of an app instance | Supported | Supported |
| Make an app instance discoverable to others | Supported | Supported |
| Discover all running app instances and their state stores | Supported | Supported |
| Communicate with app instances over the network (RPC) | Supported | Not supported (you must configure) |

<a id="streams-developer-guide-interactive-queries--querying-local-state-stores-for-an-app-instance"></a>

# Querying local state stores for an app instance

A Kafka Streams application typically runs on multiple instances. The state that is locally available on any given instance is only a subset of the [application’s entire state](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams-architecture-state). Querying the local stores on an instance will only return data locally available on that particular instance.

The method `KafkaStreams#store(...)` finds an application instance’s local state stores by name and type. Note that interactive queries are not supported for [versioned state stores](#streams-developer-guide-processor-api--versioned-key-value-state-stores) at this time.

Every application instance can directly query any of its local state stores.

The *name* of a state store is defined when you create the store. You can create the store explicitly by using the Processor API or implicitly by using stateful operations in the DSL.

- **`QueryableStoreTypes#keyValueStore()`** — see [Querying local key-value stores](#streams-developer-guide-interactive-queries--querying-local-key-value-stores).
- **`QueryableStoreTypes#timestampedKeyValueStore()`** — see [Querying local key-value stores](#streams-developer-guide-interactive-queries--querying-local-key-value-stores).
- **`QueryableStoreTypes#timestampedKeyValueStoreWithHeaders()`** — see [Header-aware stores and interactive queries](#streams-developer-guide-interactive-queries--header-aware-stores-interactive-queries).
- **`QueryableStoreTypes#windowStore()`** — see [Querying local window stores](#streams-developer-guide-interactive-queries--querying-local-window-stores).
- **`QueryableStoreTypes#timestampedWindowStore()`** — see [Querying local window stores](#streams-developer-guide-interactive-queries--querying-local-window-stores).
- **`QueryableStoreTypes#timestampedWindowStoreWithHeaders()`** — see [Header-aware stores and interactive queries](#streams-developer-guide-interactive-queries--header-aware-stores-interactive-queries).
- **`QueryableStoreTypes#sessionStore()`** — see [Querying local window stores](#streams-developer-guide-interactive-queries--querying-local-window-stores).
- **`QueryableStoreTypes#sessionStoreWithHeaders()`** — see [Header-aware stores and interactive queries](#streams-developer-guide-interactive-queries--header-aware-stores-interactive-queries).

You can also implement your own QueryableStoreType as described in section Querying local custom state stores.

> [!NOTE]
>

Kafka Streams materializes one state store per stream partition. This means your application will potentially manage many underlying state stores. The API enables you to query all of the underlying stores without having to know which partition the data is in.

**Note:** For a [header-aware store](#streams-developer-guide-processor-api--headers-in-state-stores), use the **`*WithHeaders()`** entry from the list above that corresponds to your store type when interactive query results must include record headers.

<a id="streams-developer-guide-interactive-queries--querying-local-key-value-stores"></a>

## Querying local key-value stores

To query key-value state, you first build a topology that includes a state store. This example uses the DSL `count()` operator on a grouped stream, which creates a timestamped key-value store named `CountsKeyValueStore`. That store holds the latest count for each word from the topic `word-count-input`.

Note: These examples use `QueryableStoreTypes.keyValueStore()` and `ReadOnlyKeyValueStore<String, Long>`, so interactive queries return values only (the counts). The materialized store also retains timestamps; use `QueryableStoreTypes.timestampedKeyValueStore()` and `ReadOnlyKeyValueStore<String, ValueAndTimestamp<Long>>` if you need timestamps in query results.

```
Properties  props = ...;
StreamsBuilder builder = ...;
KStream<String, String> textLines = ...;

// Define the processing topology (here: WordCount)
KGroupedStream<String, String> groupedByWord = textLines
  .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\W+")))
  .groupBy((key, word) -> word, Grouped.with(stringSerde, stringSerde));

// Create a key-value store named "CountsKeyValueStore" for the all-time word counts
groupedByWord.count(Materialized.<String, String, KeyValueStore<Bytes, byte[]>as("CountsKeyValueStore"));

// Start an instance of the topology
KafkaStreams streams = new KafkaStreams(builder, props);
streams.start();
```

After the application has started, you can get access to “CountsKeyValueStore” and then query it via the [ReadOnlyKeyValueStore](https://github.com/apache/kafka/blob/4.3/streams/src/main/java/org/apache/kafka/streams/state/ReadOnlyKeyValueStore.java) API:

```
// Get the key-value store CountsKeyValueStore
ReadOnlyKeyValueStore<String, Long> keyValueStore =
    streams.store("CountsKeyValueStore", QueryableStoreTypes.keyValueStore());

// Get value by key
System.out.println("count for hello:" + keyValueStore.get("hello"));

// Get the values for a range of keys available in this application instance
KeyValueIterator<String, Long> range = keyValueStore.range("all", "streams");
while (range.hasNext()) {
  KeyValue<String, Long> next = range.next();
  System.out.println("count for " + next.key + ": " + next.value);
}

// Get the values for all of the keys available in this application instance
KeyValueIterator<String, Long> range = keyValueStore.all();
while (range.hasNext()) {
  KeyValue<String, Long> next = range.next();
  System.out.println("count for " + next.key + ": " + next.value);
}
```

You can also materialize the results of stateless operators by using the overloaded methods that take a `queryableStoreName` as shown in the example below:

```
StreamsBuilder builder = ...;
KTable<String, Integer> regionCounts = ...;

// materialize the result of filtering corresponding to odd numbers
// the "queryableStoreName" can be subsequently queried.
KTable<String, Integer> oddCounts = numberLines.filter((region, count) -> (count % 2 != 0),
  Materialized.<String, Integer, KeyValueStore<Bytes, byte[]>as("queryableStoreName"));

// do not materialize the result of filtering corresponding to even numbers
// this means that these results will not be materialized and cannot be queried.
KTable<String, Integer> oddCounts = numberLines.filter((region, count) -> (count % 2 == 0));
```

<a id="streams-developer-guide-interactive-queries--querying-local-window-stores"></a>

## Querying local window stores

A window store will potentially have many results for any given key because the key can be present in multiple windows. However, there is only one result per window for a given key.

To query a windowed store, you first build a topology with a windowed aggregation (for example, using `windowedBy` followed by `count()`). This example uses `count()` to create a timestamped window store named `CountsWindowStore` with 1-minute windows for per-word counts.

Note: These examples use `QueryableStoreTypes.windowStore()` and `ReadOnlyWindowStore<String, Long>`, so interactive queries return values only per window. The materialized store also retains timestamps; use `QueryableStoreTypes.timestampedWindowStore()` and `ReadOnlyWindowStore<String, ValueAndTimestamp<Long>>` if you need timestamps in query results.

```
StreamsBuilder builder = ...;
KStream<String, String> textLines = ...;

// Define the processing topology (here: WordCount)
KGroupedStream<String, String> groupedByWord = textLines
  .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\W+")))
  .groupBy((key, word) -> word, Grouped.with(stringSerde, stringSerde));

// Create a window state store named "CountsWindowStore" that contains the word counts for every minute
groupedByWord.windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofSeconds(60)))
  .count(Materialized.<String, Long, WindowStore<Bytes, byte[]>as("CountsWindowStore"));
```

After the application has started, you can get access to “CountsWindowStore” and then query it via the [ReadOnlyWindowStore](https://github.com/apache/kafka/blob/4.3/streams/src/main/java/org/apache/kafka/streams/state/ReadOnlyWindowStore.java) API:

```
// Get the window store named "CountsWindowStore"
ReadOnlyWindowStore<String, Long> windowStore =
    streams.store("CountsWindowStore", QueryableStoreTypes.windowStore());

// Fetch values for the key "world" for all of the windows available in this application instance.
// To get *all* available windows we fetch windows from the beginning of time until now.
Instant timeFrom = Instant.ofEpochMilli(0); // beginning of time = oldest available
Instant timeTo = Instant.now(); // now (in processing-time)
WindowStoreIterator<Long> iterator = windowStore.fetch("world", timeFrom, timeTo);
while (iterator.hasNext()) {
  KeyValue<Long, Long> next = iterator.next();
  long windowTimestamp = next.key;
  System.out.println("Count of 'world' @ time " + windowTimestamp + " is " + next.value);
}
```

<a id="streams-developer-guide-interactive-queries--querying-local-custom-state-stores"></a>

## Querying local custom state stores

> [!NOTE]
>

Only the [Processor API](#streams-developer-guide-processor-api--implementing-custom-state-stores) supports custom state stores.

Before querying the custom state stores you must implement these interfaces:

- Your custom state store must implement `StateStore`.
- You must have an interface to represent the operations available on the store.
- You must provide an implementation of `StoreBuilder` for creating instances of your store.
- It is recommended that you provide an interface that restricts access to read-only operations. This prevents users of this API from mutating the state of your running Kafka Streams application out-of-band.

The class/interface hierarchy for your custom store might look something like:

```
public class MyCustomStore<K,V> implements StateStore, MyWriteableCustomStore<K,V> {// implementation of the actual store}
// Read-write interface for MyCustomStore public interface MyWriteableCustomStore<K,V> extends MyReadableCustomStore<K,V> {void write(K Key, V value);}
// Read-only interface for MyCustomStore public interface MyReadableCustomStore<K,V> {V read(K key);}
public class MyCustomStoreBuilder implements StoreBuilder {// implementation of the supplier for MyCustomStore}
```

To make this store queryable you must:

- Provide an implementation of [QueryableStoreType](https://github.com/apache/kafka/blob/4.3/streams/src/main/java/org/apache/kafka/streams/state/QueryableStoreType.java).
- Provide a wrapper class that has access to all of the underlying instances of the store and is used for querying.

Here is how to implement `QueryableStoreType`:

```
public class MyCustomStoreType<K,V> implements QueryableStoreType<MyReadableCustomStore<K,V>> {
// Only accept StateStores that are of type MyCustomStore public boolean accepts(final StateStore stateStore) {return stateStore instanceOf MyCustomStore;}
public MyReadableCustomStore<K,V> create(final StateStoreProvider storeProvider, final String storeName) {return new MyCustomStoreTypeWrapper(storeProvider, storeName, this);}
}
```

A wrapper class is required because each instance of a Kafka Streams application may run multiple stream tasks and manage multiple local instances of a particular state store. The wrapper class hides this complexity and lets you query a “logical” state store by name without having to know about all of the underlying local instances of that state store.

When implementing your wrapper class you must use the [StateStoreProvider](https://github.com/apache/kafka/blob/4.3/streams/src/main/java/org/apache/kafka/streams/state/internals/StateStoreProvider.java) interface to get access to the underlying instances of your store. `StateStoreProvider#stores(String storeName, QueryableStoreType<T> queryableStoreType)` returns a `List` of state stores with the given storeName and of the type as defined by `queryableStoreType`.

Here is an example implementation of the wrapper:

```
// We strongly recommended implementing a read-only interface
// to restrict usage of the store to safe read operations!
public class MyCustomStoreTypeWrapper<K,V> implements MyReadableCustomStore<K,V> {

  private final QueryableStoreType<MyReadableCustomStore<K, V>> customStoreType;
  private final String storeName;
  private final StateStoreProvider provider;

  public CustomStoreTypeWrapper(final StateStoreProvider provider,
                              final String storeName,
                              final QueryableStoreType<MyReadableCustomStore<K, V>> customStoreType) {

    // ... assign fields ...
  }

  // Implement a safe read method
  @Override
  public V read(final K key) {
    // Get all the stores with storeName and of customStoreType
    final List<MyReadableCustomStore<K, V>> stores = provider.getStores(storeName, customStoreType);
    // Try and find the value for the given key
    final Optional<V> value = stores.stream().filter(store -> store.read(key) != null).findFirst();
    // Return the value if it exists
    return value.orElse(null);
  }

}
```

You can now find and query your custom store:

```
Topology topology = ...;
ProcessorSupplier processorSuppler = ...;

// Create CustomStoreSupplier for store name the-custom-store
MyCustomStoreBuilder customStoreBuilder = new MyCustomStoreBuilder("the-custom-store") //...;
// Add the source topic
topology.addSource("input", "inputTopic");
// Add a custom processor that reads from the source topic
topology.addProcessor("the-processor", processorSupplier, "input");
// Connect your custom state store to the custom processor above
topology.addStateStore(customStoreBuilder, "the-processor");

KafkaStreams streams = new KafkaStreams(topology, config);
streams.start();

// Get access to the custom store
MyReadableCustomStore<String,String> store = streams.store("the-custom-store", new MyCustomStoreType<String,String>());
// Query the store
String value = store.read("key");
```

<a id="streams-developer-guide-interactive-queries--querying-remote-state-stores-for-the-entire-app"></a>

# Querying remote state stores for the entire app

To query remote states for the entire app, you must expose the application’s full state to other applications, including applications that are running on different machines.

For example, you have a Kafka Streams application that processes user events in a multi-player video game, and you want to retrieve the latest status of each user directly and display it in a mobile app. Here are the required steps to make the full state of your application queryable:

1. Add an RPC layer to your application so that the instances of your application can be interacted with via the network (e.g., a REST API, Thrift, a custom protocol, and so on). The instances must respond to interactive queries. You can follow the reference examples provided to get started.
2. Expose the RPC endpoints of your application’s instances via the `application.server` configuration setting of Kafka Streams. Because RPC endpoints must be unique within a network, each instance has its own value for this configuration setting. This makes an application instance discoverable by other instances.
3. In the RPC layer, discover remote application instances and their state stores and query locally available state stores to make the full state of your application queryable. The remote application instances can forward queries to other app instances if a particular instance lacks the local data to respond to a query. The locally available state stores can directly respond to queries.

Discover any running instances of the same application as well as the respective RPC endpoints they expose for interactive queries

<a id="streams-developer-guide-interactive-queries--adding-an-rpc-layer-to-your-application"></a>

## Adding an RPC layer to your application

There are many ways to add an RPC layer. The only requirements are that the RPC layer is embedded within the Kafka Streams application and that it exposes an endpoint that other application instances and applications can connect to.

<a id="streams-developer-guide-interactive-queries--exposing-the-rpc-endpoints-of-your-application"></a>

## Exposing the RPC endpoints of your application

> [!TIP]
>

Consider leveraging the exposed RPC endpoints of your application for further functionality, such as piggybacking additional inter-application communication that goes beyond interactive queries.

This example shows how to configure and run a Kafka Streams application that supports the discovery of its state stores.

```
Properties props = new Properties();
// Set the unique RPC endpoint of this application instance through which it
// can be interactively queried.  In a real application, the value would most
// probably not be hardcoded but derived dynamically.
String rpcEndpoint = "host1:4460";
props.put(StreamsConfig.APPLICATION_SERVER_CONFIG, rpcEndpoint);
// ... further settings may follow here ...

StreamsBuilder builder = new StreamsBuilder();

KStream<String, String> textLines = builder.stream(stringSerde, stringSerde, "word-count-input");

final KGroupedStream<String, String> groupedByWord = textLines
    .flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\W+")))
    .groupBy((key, word) -> word, Grouped.with(stringSerde, stringSerde));

// This call to `count()` creates a state store named "word-count".
// The state store is discoverable and can be queried interactively.
groupedByWord.count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>as("word-count"));

// Start an instance of the topology
KafkaStreams streams = new KafkaStreams(builder, props);
streams.start();

// Then, create and start the actual RPC service for remote access to this
// application instance's local state stores.
//
// This service should be started on the same host and port as defined above by
// the property `StreamsConfig.APPLICATION_SERVER_CONFIG`.  The example below is
// fictitious, but we provide end-to-end demo applications (such as KafkaMusicExample)
// that showcase how to implement such a service to get you started.
MyRPCService rpcService = ...;
rpcService.listenAt(rpcEndpoint);
```

<a id="streams-developer-guide-interactive-queries--discovering-and-accessing-application-instances-and-their-local-state-stores"></a>

## Discovering and accessing application instances and their local state stores

- `KafkaStreams#allMetadata()`: find all instances of this application
- `KafkaStreams#allMetadataForStore(String storeName)`: find those applications instances that manage local instances of the state store “storeName”
- `KafkaStreams#metadataForKey(String storeName, K key, Serializer<K> keySerializer)`: using the default stream partitioning strategy, find the one application instance that holds the data for the given key in the given state store
- `KafkaStreams#metadataForKey(String storeName, K key, StreamPartitioner<K, ?> partitioner)`: using `partitioner`, find the one application instance that holds the data for the given key in the given state store

Attention

For example, we can now find the `StreamsMetadata` for the state store named “word-count” that we defined in the code example shown in the previous section:

```
KafkaStreams streams = ...;
// Find all the locations of local instances of the state store named "word-count"
Collection<StreamsMetadata> wordCountHosts = streams.allMetadataForStore("word-count");

// For illustrative purposes, we assume using an HTTP client to talk to remote app instances.
HttpClient http = ...;

// Get the word count for word (aka key) 'alice': Approach 1
//
// We first find the one app instance that manages the count for 'alice' in its local state stores.
StreamsMetadata metadata = streams.metadataForKey("word-count", "alice", Serdes.String().serializer());
// Then, we query only that single app instance for the latest count of 'alice'.
// Note: The RPC URL shown below is fictitious and only serves to illustrate the idea.  Ultimately,
// the URL (or, in general, the method of communication) will depend on the RPC layer you opted to
// implement.  Again, we provide end-to-end demo applications (such as KafkaMusicExample) that showcase
// how to implement such an RPC layer.
Long result = http.getLong("http://" + metadata.host() + ":" + metadata.port() + "/word-count/alice");

// Get the word count for word (aka key) 'alice': Approach 2
//
// Alternatively, we could also choose (say) a brute-force approach where we query every app instance
// until we find the one that happens to know about 'alice'.
Optional<Long> result = streams.allMetadataForStore("word-count")
    .stream()
    .map(streamsMetadata -> {
        // Construct the (fictituous) full endpoint URL to query the current remote application instance
        String url = "http://" + streamsMetadata.host() + ":" + streamsMetadata.port() + "/word-count/alice";
        // Read and return the count for 'alice', if any.
        return http.getLong(url);
    })
    .filter(s -> s != null)
    .findFirst();
```

At this point the full state of the application is interactively queryable:

- You can discover the running instances of the application and the state stores they manage locally.
- Through the RPC layer that was added to the application, you can communicate with these application instances over the network and query them for locally available state.
- The application instances are able to serve such queries because they can directly query their own local state stores and respond via the RPC layer.
- Collectively, this allows us to query the full state of the entire application.

To see an end-to-end application with interactive queries, review the demo applications.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-memory-mgmt"></a>

<a id="streams-developer-guide-memory-mgmt--memory-management"></a>

# Memory Management

You can specify the total memory (RAM) size used for internal caching and compacting of records. This caching happens before the records are written to state stores or forwarded downstream to other nodes.

The record caches are implemented slightly different in the DSL and Processor API.

<a id="streams-developer-guide-memory-mgmt--record-caches-in-the-dsl"></a>

# Record caches in the DSL

You can specify the total memory (RAM) size of the record cache for an instance of the processing topology. It is leveraged by the following `KTable` instances:

- Source `KTable`: `KTable` instances that are created via `StreamsBuilder#table()` or `StreamsBuilder#globalTable()`.
- Aggregation `KTable`: instances of `KTable` that are created as a result of [aggregations](https://kafka.apache.org/43/streams/developer-guide/memory-mgmt/dsl-api.html#streams-developer-guide-dsl-aggregating).

For such `KTable` instances, the record cache is used for:

- Internal caching and compacting of output records before they are written by the underlying stateful [processor node](https://kafka.apache.org/43/streams/developer-guide/core-concepts#streams_processor_node) to its internal state stores.
- Internal caching and compacting of output records before they are forwarded from the underlying stateful [processor node](https://kafka.apache.org/43/streams/developer-guide/core-concepts#streams_processor_node) to any of its downstream processor nodes.

Use the following example to understand the behaviors with and without record caching. In this example, the input is a `KStream<String, Integer>` with the records `<K,V>: <A, 1>, <D, 5>, <A, 20>, <A, 300>`. The focus in this example is on the records with key == `A`.

- An [aggregation](https://kafka.apache.org/43/streams/developer-guide/memory-mgmt/dsl-api.html#streams-developer-guide-dsl-aggregating) computes the sum of record values, grouped by key, for the input and returns a `KTable<String, Integer>`.

>
```
* **Without caching** : a sequence of output records is emitted for key `A` that represent changes in the resulting aggregation table. The parentheses (`()`) denote changes, the left number is the new aggregate value and the right number is the old aggregate value: `<A, (1, null)>, <A, (21, 1)>, <A, (321, 21)>`.
* **With caching** : a single output record is emitted for key `A` that would likely be compacted in the cache, leading to a single output record of `<A, (321, null)>`. This record is written to the aggregation's internal state store and forwarded to any downstream operations.
```

The cache size is specified through the `cache.max.bytes.buffering` parameter, which is a global setting per processing topology:

```
// Enable record cache of size 10 MB.
Properties props = new Properties();
props.put(StreamsConfig.CACHE_MAX_BYTES_BUFFERING_CONFIG, 10 * 1024 * 1024L);
```

This parameter controls the number of bytes allocated for caching. Specifically, for a processor topology instance with `T` threads and `C` bytes allocated for caching, each thread will have an even `C/T` bytes to construct its own cache and use as it sees fit among its tasks. This means that there are as many caches as there are threads, but no sharing of caches across threads happens.

The basic API for the cache is made of `put()` and `get()` calls. Records are evicted using a simple LRU scheme after the cache size is reached. The first time a keyed record `R1 = <K1, V1>` finishes processing at a node, it is marked as dirty in the cache. Any other keyed record `R2 = <K1, V2>` with the same key `K1` that is processed on that node during that time will overwrite `<K1, V1>`, this is referred to as “being compacted”. This has the same effect as [Kafka’s log compaction](https://kafka.apache.org/documentation.html#compaction), but happens earlier, while the records are still in memory, and within your client-side application, rather than on the server-side (i.e. the Kafka broker). After flushing, `R2` is forwarded to the next processing node and then written to the local state store.

The semantics of caching is that data is flushed to the state store and forwarded to the next downstream processor node whenever the earliest of `commit.interval.ms` or `cache.max.bytes.buffering` (cache pressure) hits. Both `commit.interval.ms` and `cache.max.bytes.buffering` are global parameters. As such, it is not possible to specify different parameters for individual nodes.

Here are example settings for both parameters based on desired scenarios.

- To turn off caching the cache size can be set to zero:

```
// Disable record cache
Properties props = new Properties();
props.put(StreamsConfig.CACHE_MAX_BYTES_BUFFERING_CONFIG, 0);
```

- To enable caching but still have an upper bound on how long records will be cached, you can set the commit interval. In this example, it is set to 1000 milliseconds:

```
Properties props = new Properties();
// Enable record cache of size 10 MB.
props.put(StreamsConfig.CACHE_MAX_BYTES_BUFFERING_CONFIG, 10 * 1024 * 1024L);
// Set commit interval to 1 second.
props.put(StreamsConfig.COMMIT_INTERVAL_MS_CONFIG, 1000);
```

The effect of these two configurations is described in the figure below. The records are shown using 4 keys: blue, red, yellow, and green. Assume the cache has space for only 3 keys.

- When the cache is disabled (a), all of the input records will be output.
- When the cache is enabled (b):

>
```
* Most records are output at the end of commit intervals (e.g., at `t1` a single blue record is output, which is the final over-write of the blue key up to that time).
* Some records are output because of cache pressure (i.e. before the end of a commit interval). For example, see the red record before `t2`. With smaller cache sizes we expect cache pressure to be the primary factor that dictates when records are output. With large cache sizes, the commit interval will be the primary factor.
* The total number of records output has been reduced from 15 to 8.
```

<a id="streams-developer-guide-memory-mgmt--record-caches-in-the-processor-api"></a>

# Record caches in the Processor API

You can specify the total memory (RAM) size of the record cache for an instance of the processing topology. It is used for internal caching and compacting of output records before they are written from a stateful processor node to its state stores.

The record cache in the Processor API does not cache or compact any output records that are being forwarded downstream. This means that all downstream processor nodes can see all records, whereas the state stores see a reduced number of records. This does not impact correctness of the system, but is a performance optimization for the state stores. For example, with the Processor API you can store a record in a state store while forwarding a different value downstream.

Following from the example first shown in section [State Stores](https://kafka.apache.org/43/streams/developer-guide/memory-mgmt/processor-api.html#streams-developer-guide-state-store), to disable caching, you can add the `withCachingDisabled` call (note that caches are enabled by default, however there is an explicit `withCachingEnabled` call).

```
StoreBuilder countStoreBuilder =
  Stores.keyValueStoreBuilder(
    Stores.persistentKeyValueStore("Counts"),
    Serdes.String(),
    Serdes.Long())
  .withCachingEnabled();
```

Record caches are not supported for [versioned state stores](https://kafka.apache.org/43/streams/developer-guide/memory-mgmt/processor-api.html#streams-developer-guide-state-store-versioned).

To avoid reading stale data, you can `flush()` the store before creating the iterator. Note, that flushing too often can lead to performance degration if RocksDB is used, so we advice to avoid flushing manually in general.

<a id="streams-developer-guide-memory-mgmt--rocksdb"></a>

# RocksDB

Each instance of RocksDB allocates off-heap memory for a block cache, index and filter blocks, and memtable (write buffer). Critical configs (for RocksDB version 4.1.0) include `block_cache_size`, `write_buffer_size` and `max_write_buffer_number`. These can be specified through the `rocksdb.config.setter` configuration.

<a id="streams-developer-guide-memory-mgmt--rocksdb-offset-durability"></a>
<a id="streams-developer-guide-memory-mgmt--changelog-offset-durability-and-flush-frequency"></a>

### Changelog offset durability and flush frequency

Since 4.3 ([KIP-1035](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1035%3A+StateStore+managed+changelog+offsets)), Kafka Streams stores each persistent store’s changelog offset inside RocksDB rather than in a per-task `.checkpoint` file. Kafka Streams runs RocksDB with the write-ahead log (WAL) disabled — the changelog topic is the durable log of record — so data and the changelog offset become durable on disk only when a memtable is **flushed** to an SST file. A flush happens when the memtable fills `write_buffer_size` (16 MB by default) or when the store is **closed cleanly** (`KafkaStreams#close`). Unlike earlier releases, Kafka Streams no longer force-flushes RocksDB on every commit.

The practical implication is that the on-disk changelog offset is only as fresh as the last organic flush or clean close. For a high-throughput store the memtable fills frequently, so this is not a concern. For a **low-traffic store** whose memtable may take a long time to fill, the persisted offset can lag the store’s actual position for an extended period. If the application then exits uncleanly (for example `SIGKILL`, an OOM-kill, or a `KafkaStreams#close` that does not complete within the process/pod shutdown grace period), only the last-flushed offset survives. Should the changelog topic’s log-start offset have advanced past that stale offset (via retention or compaction) in the meantime, the restore consumer seeks out of range on the next restart, and the task is re-initialized from the changelog (logged as `OffsetOutOfRangeException` / `TaskCorruptedException`). This recovers automatically with no data loss, but causes a full re-restore of the task.

To reduce the likelihood of this for an affected low-traffic store, you can make it flush more often by lowering its `write_buffer_size` (and adjusting `max_write_buffer_number`) through a custom `RocksDBConfigSetter`:

```
public static class CustomRocksDBConfig implements RocksDBConfigSetter {
    @Override
    public void setConfig(final String storeName, final Options options, final Map<String, Object> configs) {
        // smaller write buffer => more frequent flushes => fresher on-disk changelog offset,
        // at the cost of more (smaller) SST files and more compaction work
        options.setWriteBufferSize(4 * 1024 * 1024L);
    }

    @Override
    public void close(final String storeName, final Options options) {}
}
```

This is a trade-off: a smaller write buffer bounds how stale the persisted offset can get, but increases the number of SST files and the compaction load. So tune only the specific low-traffic stores that need it, and size the buffer to the store’s write rate. Note that flushing is **volume-based, not time-based**. A store that receives only a trickle of writes may still not flush until it is closed, so the most reliable protection is a **clean shutdown**. Register a shutdown hook that calls `KafkaStreams#close`, and ensure it is allowed to complete — on Kubernetes, set the close timeout comfortably below the pod termination grace period (default 30s) so the process is not `SIGKILL`ed mid-close. Note that the record cache (`statestore.cache.max.bytes`) in front of the store coalesces repeated updates to the same key in place before they are written to RocksDB. So for an update-heavy, small-keyspace workload even fewer bytes reach the memtable per commit, making it fill more slowly.

Also, we recommend changing RocksDB’s default memory allocator, because the default allocator may lead to increased memory consumption. To change the memory allocator to `jemalloc`, you need to set the environment variable `LD_PRELOAD`before you start your Kafka Streams application:

```
# example: install jemalloc (on Debian)
$ apt install -y libjemalloc-dev
# set LD_PRELOAD before you start your Kafka Streams application
$ export LD_PRELOAD="/usr/lib/x86_64-linux-gnu/libjemalloc.so"
```

As of 2.3.0 the memory usage across all instances can be bounded, limiting the total off-heap memory of your Kafka Streams application. To do so you must configure RocksDB to cache the index and filter blocks in the block cache, limit the memtable memory through a shared [WriteBufferManager](https://github.com/facebook/rocksdb/wiki/Write-Buffer-Manager) and count its memory against the block cache, and then pass the same Cache object to each instance. See [RocksDB Memory Usage](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB) for details. An example RocksDBConfigSetter implementing this is shown below:

```
public static class BoundedMemoryRocksDBConfig implements RocksDBConfigSetter {

   private static org.rocksdb.Cache cache = new org.rocksdb.LRUCache(TOTAL_OFF_HEAP_MEMORY, -1, false, INDEX_FILTER_BLOCK_RATIO);1
   private static org.rocksdb.WriteBufferManager writeBufferManager = new org.rocksdb.WriteBufferManager(TOTAL_MEMTABLE_MEMORY, cache);

   @Override
   public void setConfig(final String storeName, final Options options, final Map<String, Object> configs) {

     BlockBasedTableConfig tableConfig = (BlockBasedTableConfig) options.tableFormatConfig();

      // These three options in combination will limit the memory used by RocksDB to the size passed to the block cache (TOTAL_OFF_HEAP_MEMORY)
     tableConfig.setBlockCache(cache);
     tableConfig.setCacheIndexAndFilterBlocks(true);
     options.setWriteBufferManager(writeBufferManager);

      // These options are recommended to be set when bounding the total memory
     tableConfig.setCacheIndexAndFilterBlocksWithHighPriority(true);2
     tableConfig.setPinTopLevelIndexAndFilter(true);
     tableConfig.setBlockSize(BLOCK_SIZE);3
     options.setMaxWriteBufferNumber(N_MEMTABLES);
     options.setWriteBufferSize(MEMTABLE_SIZE);

     options.setTableFormatConfig(tableConfig);
   }

   @Override
   public void close(final String storeName, final Options options) {
     // Cache and WriteBufferManager should not be closed here, as the same objects are shared by every store instance.
   }
}
```

1. INDEX\_FILTER\_BLOCK\_RATIO can be used to set a fraction of the block cache to set aside for “high priority” (aka index and filter) blocks, preventing them from being evicted by data blocks. The boolean parameter in the cache constructor lets you control whether the cache should enforce a strict memory limit by failing the read or iteration in the rare cases where it might go larger than its capacity. See the full signature of the LRUCache constructor [here](https://github.com/facebook/rocksdb/blob/master/java/src/main/java/org/rocksdb/LRUCache.java#L72). 2. This must be set in order for INDEX\_FILTER\_BLOCK\_RATIO to take effect (see footnote 1) as described in the [RocksDB docs](https://github.com/facebook/rocksdb/wiki/Block-Cache#caching-index-and-filter-blocks) 3. You may want to modify the default [block size](https://github.com/apache/kafka/blob/2.3/streams/src/main/java/org/apache/kafka/streams/state/internals/RocksDBStore.java#L79) per these instructions from the [RocksDB docs](https://github.com/facebook/rocksdb/wiki/Memory-usage-in-RocksDB#indexes-and-filter-blocks). A larger block size means index blocks will be smaller, but the cached data blocks may contain more cold data that would otherwise be evicted.

Note:
While we recommend setting at least the above configs, the specific options that yield the best performance are workload dependent and you should consider experimenting with these to determine the best choices for your specific use case. Keep in mind that the optimal configs for one app may not apply to one with a different topology or input topic. In addition to the recommended configs above, you may want to consider using partitioned index filters as described by the [RocksDB docs](https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters).

<a id="streams-developer-guide-memory-mgmt--other-memory-usage"></a>

# Other memory usage

There are other modules inside Apache Kafka that allocate memory during runtime. They include the following:

- Producer buffering, managed by the producer config `buffer.memory`.
- Consumer buffering, currently not strictly managed, but can be indirectly controlled by fetch size, i.e., `fetch.max.bytes` and `fetch.max.wait.ms`.
- Both producer and consumer also have separate TCP send / receive buffers that are not counted as the buffering memory. These are controlled by the `send.buffer.bytes` / `receive.buffer.bytes` configs.
- Deserialized objects buffering: after `consumer.poll()` returns records, they will be deserialized to extract timestamp and buffered in the streams space. Currently this is only indirectly controlled by `buffered.records.per.partition`.

> [!TIP]
>

**Iterators should be closed explicitly to release resources:** Store iterators (e.g., `KeyValueIterator` and `WindowStoreIterator`) must be closed explicitly upon completeness to release resources such as open file handlers and in-memory read buffers, or use try-with-resources statement (available since JDK7) for this Closeable class.

Otherwise, stream application’s memory usage keeps increasing when running until it hits an OOM.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-running-app"></a>

<a id="streams-developer-guide-running-app--running-streams-applications"></a>

# Running Streams Applications

You can run Java applications that use the Kafka Streams library without any additional configuration or requirements. Kafka Streams also provides the ability to receive notification of the various states of the application. The ability to monitor the runtime status is discussed in [the monitoring guide](https://kafka.apache.org/documentation/#kafka_streams_monitoring).

<a id="streams-developer-guide-running-app--starting-a-kafka-streams-application"></a>

# Starting a Kafka Streams application

You can package your Java application as a fat JAR file and then start the application like this:

```
# Start the application in class `com.example.MyStreamsApp`
# from the fat JAR named `path-to-app-fatjar.jar`.
$ java -cp path-to-app-fatjar.jar com.example.MyStreamsApp
```

When you start your application you are launching a Kafka Streams instance of your application. You can run multiple instances of your application. A common scenario is that there are multiple instances of your application running in parallel. For more information, see [Parallelism Model](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams_architecture_tasks).

When the application instance starts running, the defined processor topology will be initialized as one or more stream tasks. If the processor topology defines any state stores, these are also constructed during the initialization period. For more information, see the State restoration during workload rebalance section).

<a id="streams-developer-guide-running-app--elastic-scaling-of-your-application"></a>

# Elastic scaling of your application

Kafka Streams makes your stream processing applications elastic and scalable. You can add and remove processing capacity dynamically during application runtime without any downtime or data loss. This makes your applications resilient in the face of failures and for allows you to perform maintenance as needed (e.g. rolling upgrades).

For more information about this elasticity, see the [Parallelism Model](https://kafka.apache.org/43/streams/developer-guide/architecture.html#streams_architecture_tasks) section. Kafka Streams leverages the Kafka group management functionality, which is built right into the [Kafka wire protocol](https://cwiki.apache.org/confluence/x/uxvVAQ). It is the foundation that enables the elasticity of Kafka Streams applications: members of a group coordinate and collaborate jointly on the consumption and processing of data in Kafka. Additionally, Kafka Streams provides stateful processing and allows for fault-tolerant state in environments where application instances may come and go at any time.

<a id="streams-developer-guide-running-app--adding-capacity-to-your-application"></a>

## Adding capacity to your application

If you need more processing capacity for your stream processing application, you can simply start another instance of your stream processing application, e.g. on another machine, in order to scale out. The instances of your application will become aware of each other and automatically begin to share the processing work. More specifically, what will be handed over from the existing instances to the new instances is (some of) the stream tasks that have been run by the existing instances. Moving stream tasks from one instance to another results in moving the processing work plus any internal state of these stream tasks (the state of a stream task will be re-created in the target instance by restoring the state from its corresponding changelog topic).

The various instances of your application each run in their own JVM process, which means that each instance can leverage all the processing capacity that is available to their respective JVM process (minus the capacity that any non-Kafka-Streams part of your application may be using). This explains why running additional instances will grant your application additional processing capacity. The exact capacity you will be adding by running a new instance depends of course on the environment in which the new instance runs: available CPU cores, available main memory and Java heap space, local storage, network bandwidth, and so on. Similarly, if you stop any of the running instances of your application, then you are removing and freeing up the respective processing capacity.

Before adding capacity: only a single instance of your Kafka Streams application is running. At this point the corresponding Kafka consumer group of your application contains only a single member (this instance). All data is being read and processed by this single instance.

After adding capacity: now two additional instances of your Kafka Streams application are running, and they have automatically joined the application’s Kafka consumer group for a total of three current members. These three instances are automatically splitting the processing work between each other. The splitting is based on the Kafka topic partitions from which data is being read.

<a id="streams-developer-guide-running-app--removing-capacity-from-your-application"></a>

## Removing capacity from your application

To remove processing capacity, you can stop running stream processing application instances (e.g., shut down two of the four instances), it will automatically leave the application’s consumer group, and the remaining instances of your application will automatically take over the processing work. The remaining instances take over the stream tasks that were run by the stopped instances. Moving stream tasks from one instance to another results in moving the processing work plus any internal state of these stream tasks. The state of a stream task is recreated in the target instance from its changelog topic.

<a id="streams-developer-guide-running-app--state-restoration-during-workload-rebalance"></a>

## State restoration during workload rebalance

When a task is migrated, the task processing state is fully restored before the application instance resumes processing. This guarantees the correct processing results. In Kafka Streams, state restoration is usually done by replaying the corresponding changelog topic to reconstruct the state store. To minimize changelog-based restoration latency by using replicated local state stores, you can specify `num.standby.replicas`. When a stream task is initialized or re-initialized on the application instance, its state store is restored like this:

- If no local state store exists, the changelog is replayed from the earliest to the current offset. This reconstructs the local state store to the most recent snapshot.
- If a local state store exists, the changelog is replayed from the previously checkpointed offset. The changes are applied and the state is restored to the most recent snapshot. This method takes less time because it is applying a smaller portion of the changelog.

For more information, see [Standby Replicas](https://kafka.apache.org/43/streams/developer-guide/running-app/config-streams.html#num-standby-replicas).

As of version 2.6, Streams will now do most of a task’s restoration in the background through warmup replicas. These will be assigned to instances that need to restore a lot of state for a task. A stateful active task will only be assigned to an instance once its state is within the configured [`acceptable.recovery.lag`](https://kafka.apache.org/43/streams/developer-guide/running-app/config-streams.html#acceptable-recovery-lag), if one exists. This means that most of the time, a task migration will **not** result in downtime for that task. It will remain active on the instance that’s already caught up, while the instance that it’s being migrated to works on restoring the state. Streams will [regularly probe](https://kafka.apache.org/43/streams/developer-guide/running-app/config-streams.html#probing-rebalance-interval-ms) for warmup tasks that have finished restoring and transition them to active tasks when ready.

Note, the one exception to this task availability is if none of the instances have a caught up version of that task. In that case, we have no choice but to assign the active task to an instance that is not caught up and will have to block further processing on restoration of the task’s state from the changelog. If high availability is important for your application, you are highly recommended to enable standbys.

<a id="streams-developer-guide-running-app--determining-how-many-application-instances-to-run"></a>

## Determining how many application instances to run

The parallelism of a Kafka Streams application is primarily determined by how many partitions the input topics have. For example, if your application reads from a single topic that has ten partitions, then you can run up to ten instances of your applications. You can run further instances, but these will be idle.

The number of topic partitions is the upper limit for the parallelism of your Kafka Streams application and for the number of running instances of your application.

To achieve balanced workload processing across application instances and to prevent processing hotpots, you should distribute data and processing workloads:

- Data should be equally distributed across topic partitions. For example, if two topic partitions each have 1 million messages, this is better than a single partition with 2 million messages and none in the other.
- Processing workload should be equally distributed across topic partitions. For example, if the time to process messages varies widely, then it is better to spread the processing-intensive messages across partitions rather than storing these messages within the same partition.

<a id="streams-developer-guide-running-app--handling-crashes-and-failures"></a>

# Handling crashes and failures

There are a few things you can do to reduce the likelihood of crashes and failures of your Kafka Streams application.

- Kafka Streams has a few configurations that can help with resilience in the face of broker failures. They can be found in the [configuration guide.](https://kafka.apache.org/43/streams/developer-guide/running-app/config-streams.html#recommended-configuration-parameters-for-resiliency)
- Ensure that your application is able to handle errors and failures. This includes things like configuring the correct exception handlers to handle errors such as authorization and deserialization errors, and using strategies such as dead letter queues to handle “poison pill” records.

If your Kafka Streams application does crash or fail, it will first enter the `PENDING_ERROR` state to gracefully close all of its existing resources, and then transition into the `ERROR` state. It is important to note that the `PENDING_ERROR` state is not recoverable, and only a restart will get the application back to the RUNNING state, thus monitoring for this state in addition to the `ERROR` state is important to ensure that your application is able to recover.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-manage-topics"></a>

<a id="streams-developer-guide-manage-topics--managing-streams-application-topics"></a>

# Managing Streams Application Topics

A Kafka Streams application continuously reads from Kafka topics, processes the read data, and then writes the processing results back into Kafka topics. The application may also auto-create other Kafka topics in the Kafka brokers, for example state store changelogs topics. This section describes the differences these topic types and how to manage the topics and your applications.

Kafka Streams distinguishes between user topics and internal topics.

<a id="streams-developer-guide-manage-topics--user-topics"></a>

# User topics

User topics exist externally to an application and are read from or written to by the application, including:

Input topics
Topics that are specified via source processors in the application’s topology; e.g. via `StreamsBuilder#stream()`, `StreamsBuilder#table()` and `Topology#addSource()`.
Output topics
Topics that are specified via sink processors in the application’s topology; e.g. via `KStream#to()`, `KTable.to()` and `Topology#addSink()`.

User topics must be created and manually managed ahead of time (e.g., via the [topic tools](https://kafka.apache.org/43/streams/kafka/post-deployment.html#kafka-operations-admin)). If user topics are shared among multiple applications for reading and writing, the application users must coordinate topic management. If user topics are centrally managed, then application users then would not need to manage topics themselves but simply obtain access to them.

Note

You should not use the auto-create topic feature on the brokers to create user topics, because:

- Auto-creation of topics may be disabled in your Kafka cluster.
- Auto-creation automatically applies the default topic settings such as the replicaton factor. These default settings might not be what you want for certain output topics (e.g., `auto.create.topics.enable=true` in the [Kafka broker configuration](http://kafka.apache.org/0100/documentation.html#brokerconfigs)).

<a id="streams-developer-guide-manage-topics--internal-topics"></a>

# Internal topics

Internal topics are used internally by the Kafka Streams application while executing, for example the changelog topics for state stores. These topics are created by the application and are only used by that stream application.

If security is enabled on the Kafka brokers, you must grant the underlying clients admin permissions so that they can create internal topics set. For more information, see [Streams Security](https://kafka.apache.org/43/streams/developer-guide/manage-topics/security.html#streams-developer-guide-security).

Note

The internal topics follow the naming convention `<application.id>-<operatorName>-<suffix>`, but this convention is not guaranteed for future releases.

The following settings apply to the default configuration for internal topics:

- For all internal topics, `message.timestamp.type` is set to `CreateTime`.
- For internal repartition topics, the compaction policy is `delete` and the retention time is `-1` (infinite).
- For internal changelog topics for key-value stores, the compaction policy is `compact`.
- For internal changelog topics for windowed key-value stores, the compaction policy is `delete,compact`. The retention time is set to 24 hours plus your setting for the windowed store.
- For internal changelog topics for versioned state stores, the cleanup policy is `compact`, and `min.compaction.lag.ms` is set to 24 hours plus the store’s historyRetentionMs` value.
- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-security"></a>

<a id="streams-developer-guide-security--streams-security"></a>

# Streams Security

Kafka Streams natively integrates with the [Kafka’s security features](#documentation--security) and supports all of the client-side security features in Kafka. Streams leverages the [Java Producer and Consumer API](#documentation--api).

To secure your Stream processing applications, configure the security settings in the corresponding Kafka producer and consumer clients, and then specify the corresponding configuration settings in your Kafka Streams application.

Kafka supports cluster encryption and authentication, including a mix of authenticated and unauthenticated, and encrypted and non-encrypted clients. Using security is optional.

Here a few relevant client-side security features:

Encrypt data-in-transit between your applications and Kafka brokers
You can enable the encryption of the client-server communication between your applications and the Kafka brokers. For example, you can configure your applications to always use encryption when reading and writing data to and from Kafka. This is critical when reading and writing data across security domains such as internal network, public internet, and partner networks.
Client authentication
You can enable client authentication for connections from your application to Kafka brokers. For example, you can define that only specific applications are allowed to connect to your Kafka cluster.
Client authorization
You can enable client authorization of read and write operations by your applications. For example, you can define that only specific applications are allowed to read from a Kafka topic. You can also restrict write access to Kafka topics to prevent data pollution or fraudulent activities.

For more information about the security features in Apache Kafka, see [Kafka Security](#documentation--security).

<a id="streams-developer-guide-security--required-acl-setting-for-secure-kafka-clusters"></a>

# Required ACL setting for secure Kafka clusters

Kafka clusters can use ACLs to control access to resources (like the ability to create topics), and for such clusters each client, including Kafka Streams, is required to authenticate as a particular user in order to be authorized with appropriate access. In particular, when Streams applications are run against a secured Kafka cluster, the principal running the application must have the ACL set so that the application has the permissions to create, read and write [internal topics](https://kafka.apache.org/43/streams/developer-guide/security/manage-topics.html#streams-developer-guide-topics-internal).

If the [streams rebalance protocol](https://cwiki.apache.org/confluence/display/KAFKA/KIP-1071%3A+Streams+Rebalance+Protocol) is enabled by setting `group.protocol=streams`, the following ACLs are required on the topic and group resources:

| API PROTOCOL | OPERATION | Resource | Notes |
| --- | --- | --- | --- |
| STREAMS\_GROUP\_HEARTBEAT | Read | Group | Required for the application’s streams group |
| STREAMS\_GROUP\_HEARTBEAT | Create | Cluster *or* Topic | Required only if auto-creating internal topics. • `Create` on Cluster resource • or `Create` on all topics in StateChangelogTopics and RepartitionSourceTopics Not required if internal topics are pre-created |
| STREAMS\_GROUP\_HEARTBEAT | Describe | Topic | Required for all topics used in the application’s topology, when first joining. |
| STREAMS\_GROUP\_DESCRIBE | Describe | Group | Required for the application’s streams group |
| STREAMS\_GROUP\_DESCRIBE | Describe | Topic | Required for all topics used in the group’s topology |

As mentioned earlier, Kafka Streams applications need appropriate ACLs to create internal topics when running against a secured Kafka cluster. To avoid providing this permission to your application, you can create the required internal topics manually. If the internal topics exist, Kafka Streams will not try to recreate them. Note, that the internal repartition and changelog topics must be created with the correct number of partitions–otherwise, Kafka Streams will fail on startup. The topics must be created with the same number of partitions as your input topic, or if there are multiple topics, the maximum number of partitions across all input topics. Additionally, changelog topics must be created with log compaction enabled–otherwise, your application might lose data. For changelog topics for windowed KTables, apply “delete,compact” and set the retention time based on the corresponding store retention time. To avoid premature deletion, add a delta to the store retention time. By default, Kafka Streams adds 24 hours to the store retention time. You can find out more about the names of the required internal topics via `Topology#describe()`. All internal topics follow the naming pattern `<application.id>-<operatorName>-<suffix>` where the `suffix` is either `repartition` or `changelog`. Note, that there is no guarantee about this naming pattern in future releases–it’s not part of the public API.

Since all internal topics as well as the embedded consumer group name are prefixed with the [application id](https://kafka.apache.org/43/documentation/streams/developer-guide/config-streams.html#required-configuration-parameters), it is recommended to use ACLs on prefixed resource pattern to configure control lists to allow client to manage all topics and consumer groups started with this prefix as `--resource-pattern-type prefixed --topic your.application.id --operation All` (see [KIP-277](https://cwiki.apache.org/confluence/x/zlOHB) and [KIP-290](https://cwiki.apache.org/confluence/x/QpvLB) for details).

<a id="streams-developer-guide-security--security-example"></a>

# Security example

The purpose is to configure a Kafka Streams application to enable client authentication and encrypt data-in-transit when communicating with its Kafka cluster.

This example assumes that the Kafka brokers in the cluster already have their security setup and that the necessary SSL certificates are available to the application in the local filesystem locations. For example, if you are using Docker then you must also include these SSL certificates in the correct locations within the Docker image.

The snippet below shows the settings to enable client authentication and SSL encryption for data-in-transit between your Kafka Streams application and the Kafka cluster it is reading and writing from:

```
# Essential security settings to enable client authentication and SSL encryption
bootstrap.servers=kafka.example.com:9093
security.protocol=SSL
ssl.truststore.location=/etc/security/tls/kafka.client.truststore.jks
ssl.truststore.password=test1234
ssl.keystore.location=/etc/security/tls/kafka.client.keystore.jks
ssl.keystore.password=test1234
ssl.key.password=test1234
```

Configure these settings in the application for your `Properties` instance. These settings will encrypt any data-in-transit that is being read from or written to Kafka, and your application will authenticate itself against the Kafka brokers that it is communicating with. Note that this example does not cover client authorization.

```
// Code of your Java application that uses the Kafka Streams library
Properties settings = new Properties();
settings.put(StreamsConfig.APPLICATION_ID_CONFIG, "secure-kafka-streams-app");
// Where to find secure Kafka brokers.  Here, it's on port 9093.
settings.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka.example.com:9093");
//
// ...further non-security related settings may follow here...
//
// Security settings.
// 1. These settings must match the security settings of the secure Kafka cluster.
// 2. The SSL trust store and key store files must be locally accessible to the application.
settings.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
settings.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, "/etc/security/tls/kafka.client.truststore.jks");
settings.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, "test1234");
settings.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, "/etc/security/tls/kafka.client.keystore.jks");
settings.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, "test1234");
settings.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, "test1234");
```

If you incorrectly configure a security setting in your application, it will fail at runtime, typically right after you start it. For example, if you enter an incorrect password for the `ssl.keystore.password` setting, an error message similar to this would be logged and then the application would terminate:

```
# Misconfigured ssl.keystore.password Exception in thread "main" org.apache.kafka.common.KafkaException: Failed to construct kafka producer [...snip...] Caused by: org.apache.kafka.common.KafkaException: org.apache.kafka.common.KafkaException:java.io.IOException: Keystore was tampered with, or password was incorrect [...snip...] Caused by: java.security.UnrecoverableKeyException: Password verification failed
```

Monitor your Kafka Streams application log files for such error messages to spot any misconfigured applications quickly.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-app-reset-tool"></a>

<a id="streams-developer-guide-app-reset-tool--application-reset-tool"></a>

# Application Reset Tool

You can reset an application and force it to reprocess its data from scratch by using the application reset tool. This can be useful for development and testing, or when fixing bugs.

The application reset tool handles the Kafka Streams [user topics](https://kafka.apache.org/43/streams/developer-guide/app-reset-tool/manage-topics.html#streams-developer-guide-topics-user) (input, and output) and [internal topics](https://kafka.apache.org/43/streams/developer-guide/app-reset-tool/manage-topics.html#streams-developer-guide-topics-internal) differently when resetting the application.

Here’s what the application reset tool does for each topic type:

- Input topics: Reset offsets to specified position (by default to the beginning of the topic).
- Internal topics: Delete the internal topic (this automatically deletes any committed offsets).

The application reset tool does not:

- Reset output topics of an application. If any output topics are consumed by downstream applications, it is your responsibility to adjust those downstream applications as appropriate when you reset the upstream application.
- Reset the local environment of your application instances. It is your responsibility to delete the local state on any machine on which an application instance was run. See the instructions in section Step 2: Reset the local environments of your application instances on how to do this.

Prerequisites

- All instances of your application must be stopped. Otherwise, the application may enter an invalid state, crash, or produce incorrect results. You can verify whether the consumer group with ID `application.id` is still active by using `bin/kafka-consumer-groups`. When long session timeout has been configured, active members could take longer to get expired on the broker thus blocking the reset job to complete. Use the `--force` option could remove those left-over members immediately. Make sure to shut down all stream applications when this option is specified to avoid unexpected rebalances.
- Use this tool with care and double-check its parameters: If you provide wrong parameter values (e.g., typos in `application.id`) or specify parameters inconsistently (e.g., specify the wrong input topics for the application), this tool might invalidate the application’s state or even impact other applications, consumer groups, or your Kafka topics.

<a id="streams-developer-guide-app-reset-tool--step-1-run-the-application-reset-tool"></a>
<a id="streams-developer-guide-app-reset-tool--step-1:-run-the-application-reset-tool"></a>

# Step 1: Run the application reset tool

If you are using **streams rebalance protocol** (available since AK 4.2), use the [Streams groups CLI](#streams-developer-guide-kafka-streams-group-sh--reset-offsets).

If you are using **classic rebalance protocol** , run the classic application reset tool as described below.

Invoke the application reset tool from the command line

Warning! This tool makes irreversible changes to your application. It is strongly recommended that you run this once with `--dry-run` to preview your changes before making them.

```
$ bin/kafka-streams-application-reset.sh
```

The tool accepts the following parameters:

```
Option (* = required)                 Description
---------------------                 -----------
* --application-id <String: id>       REQUIRED: The Kafka Streams application ID
                                        (application.id).
--bootstrap-server <String: server to  The server(s) to connect to.
                           connect to>  The broker list string in the form HOST1:PORT1,HOST2:PORT2.
                                        (default: localhost:9092)
--by-duration <String: urls>          Reset offsets to offset by duration from
                                        current timestamp. Format: 'PnDTnHnMnS'
                                        passed to admin clients and embedded consumer.
                                        This option will be removed in a future version.
                                        Use --command-config instead.
--command-config <String: file name>  Config properties file to be passed to admin clients
                                        and embedded consumer.
--dry-run                             Display the actions that would be
                                        performed without executing the reset
                                        commands.
--from-file <String: urls>            Reset offsets to values defined in CSV
                                        file.
--input-topics <String: list>         Comma-separated list of user input
                                        topics. For these topics, the tool will
                                        reset the offset to the earliest
                                        available offset.
--internal-topics <String: list>      Comma-separated list of internal topics
                                        to delete. Must be a subset of the
                                        internal topics marked for deletion by
                                        the default behaviour (do a dry-run without
                                        this option to view these topics).
--shift-by <Long: number-of-offsets>  Reset offsets shifting current offset by
                                        'n', where 'n' can be positive or
                                        negative
--to-datetime <String>                Reset offsets to offset from datetime.
                                        Format: 'YYYY-MM-DDThh:mm:ss.sss'
--to-earliest                         Reset offsets to earliest offset.
--to-latest                           Reset offsets to latest offset.
--to-offset <Long>                    Reset offsets to a specific offset.
--force                               Force removing members of the consumer group
                                      (intended to remove left-over members if
                                      long session timeout was configured).
```

Consider the following as reset-offset scenarios for `input-topics`:

- by-duration
- from-file
- shift-by
- to-datetime
- to-earliest
- to-latest
- to-offset

Only one of these scenarios can be defined. If not, `to-earliest` will be executed by default

All the other parameters can be combined as needed. For example, if you want to restart an application from an empty internal state, but not reprocess previous data, simply omit the parameter `--input-topics`.

<a id="streams-developer-guide-app-reset-tool--step-2-reset-the-local-environments-of-your-application-instances"></a>
<a id="streams-developer-guide-app-reset-tool--step-2:-reset-the-local-environments-of-your-application-instances"></a>

# Step 2: Reset the local environments of your application instances

For a complete application reset, you must delete the application’s local state directory on any machines where the application instance was run. You must do this before restarting an application instance on the same machine. You can use either of these methods:

- The API method `KafkaStreams#cleanUp()` in your application code.
- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-streams-rebalance-protocol"></a>

<a id="streams-developer-guide-streams-rebalance-protocol--streams-rebalance-protocol"></a>

# Streams Rebalance Protocol

The Streams Rebalance Protocol is a broker-driven rebalancing system designed specifically for Kafka Streams applications. Following the pattern of KIP-848, which moved rebalance coordination of plain consumers from clients to brokers, KIP-1071 extends this model to Kafka Streams workloads.

<a id="streams-developer-guide-streams-rebalance-protocol--overview"></a>

# Overview

Instead of clients computing new assignments on the client during rebalance events involving all members of the group, assignments are computed continuously on the broker. Instead of using a consumer group, the streams application registers as a **streams group** with the broker, which manages and exposes all metadata required for coordination of the streams application instances.

This approach brings Kafka Streams coordination in line with the modern broker-driven rebalance model introduced for consumers in KIP-848, providing a dedicated group type with streams-specific semantics and metadata management.

<a id="streams-developer-guide-streams-rebalance-protocol--whats-supported-in-this-version"></a>
<a id="streams-developer-guide-streams-rebalance-protocol--what-s-supported-in-this-version"></a>

# What’s Supported in This Version

The following features are available in the current release:

- **Core Streams Group Rebalance Protocol**: The `group.protocol=streams` configuration enables the dedicated streams rebalance protocol. This separates streams groups from consumer groups and provides a streams-specific group membership lifecycle and metadata management on the broker.
- **Sticky Task Assignor**: A basic task assignment strategy that minimizes task movement during rebalances is included.
- **Interactive Query Support**: IQ operations are compatible with the new streams protocol.
- **CLI Integration**: You can list, describe, and delete streams groups via the [bin/kafka-streams-groups.sh](#streams-developer-guide-kafka-streams-group-sh) script.
- **Offline Migration**: After shutting down all members and waiting for their `session.timeout.ms` to expire (or forcing an explicit group leave), a classic group can be converted to a streams group and a streams group can be converted to a classic group. The only broker-side group data that will be preserved are the committed offsets. Internal topics (changelog and repartition topics) will continue to exist as regular Kafka topics.

<a id="streams-developer-guide-streams-rebalance-protocol--whats-not-supported-in-this-version"></a>
<a id="streams-developer-guide-streams-rebalance-protocol--what-s-not-supported-in-this-version"></a>

# What’s Not Supported in This Version

The following features are not yet available and should be avoided when using the new protocol:

- **Static Membership**: Setting a client `instance.id` will be rejected.
- **Topology Updates**: If a topology is changed significantly (e.g., by adding new source topics or changing the number of subtopologies), a new streams group must be created.
- **High Availability Assignor**: Only the sticky assignor is supported. This implies that “warmup tasks” and rack aware assignment are not supported yet.
- **Regular Expressions**: Pattern-based topic subscription is not supported.
- **Online Migration**: Group migration while the application is running is not available between the classic and new streams protocol.
- **Custom Client Supplier**: Using a custom `KafkaClientSupplier` will only allow so provide restore/global consumer, producer, and admin client. It’s not possible to provide the “main” consumer when “streams” groups are enabled.

<a id="streams-developer-guide-streams-rebalance-protocol--why-use-the-streams-rebalance-protocol"></a>

# Why Use the Streams Rebalance Protocol?

The Streams Rebalance Protocol offers several key advantages over the classic client-driven protocol:

- **Broker-Driven Coordination**: Centralizes task assignment logic on brokers instead of the client. This provides consistent, authoritative task assignment decisions from a single coordination point, and reduces the potential for split-brain scenarios.
- **Faster, More Stable Rebalances**: Reduces rebalance duration and impact by removing the global synchronization point. This minimizes application downtime during membership changes or failures.
- **Better Observability**: Provides dedicated metrics and admin interfaces that separate streams from consumer groups, leading to clearer troubleshooting with broker-side observability. See the [streams groups metrics](#operations-monitoring--group-coordinator-monitoring) documentation for details.

<a id="streams-developer-guide-streams-rebalance-protocol--enabling-the-protocol"></a>

# Enabling the Protocol

The Streams Rebalance Protocol is enabled by default on new clusters starting with Apache Kafka 4.2. Both brokers and clients must be running Apache Kafka 4.2 or later to use this protocol.

<a id="streams-developer-guide-streams-rebalance-protocol--broker-configuration"></a>

## Broker Configuration

The protocol is enabled by default on new Apache Kafka 4.2 clusters. To enable the feature on existing clusters (after upgrading to 4.2) or to explicitly control it:

Enable the feature:

```
bin/kafka-features.sh --bootstrap-server localhost:9092 upgrade --feature streams.version=1
```

Disable the feature:

```
bin/kafka-features.sh --bootstrap-server localhost:9092 downgrade --feature streams.version=0
```

<a id="streams-developer-guide-streams-rebalance-protocol--client-configuration"></a>

## Client Configuration

In your Kafka Streams application configuration, set:

```
group.protocol=streams
```

<a id="streams-developer-guide-streams-rebalance-protocol--configuration"></a>

# Configuration

<a id="streams-developer-guide-streams-rebalance-protocol--broker-configuration-1"></a>
<a id="streams-developer-guide-streams-rebalance-protocol--broker-configuration-2"></a>

## Broker Configuration

The following broker configurations control the behavior of streams groups. For complete details, see the [broker configuration](#configuration-broker-configs) documentation.

- [`group.coordinator.rebalance.protocols`](#configuration-broker-configs--brokerconfigs_group.coordinator.rebalance.protocols): The list of enabled rebalance protocols. `"streams"` is included in the list of protocols to enable streams groups.
- [`group.streams.session.timeout.ms`](#configuration-broker-configs--brokerconfigs_group.streams.session.timeout.ms): The default timeout for all streams group (if not specifically overwritten for a specific streams group) to detect client failures when using the streams group protocol.
- [`group.streams.min.session.timeout.ms`](#configuration-broker-configs--brokerconfigs_group.streams.min.session.timeout.ms): The minimum session timeout.
- [`group.streams.max.session.timeout.ms`](#configuration-broker-configs--brokerconfigs_group.streams.max.session.timeout.ms): The maximum session timeout.
- [`group.streams.heartbeat.interval.ms`](#configuration-broker-configs--brokerconfigs_group.streams.heartbeat.interval.ms): The default heartbeat interval given to the members.
- [`group.streams.min.heartbeat.interval.ms`](#configuration-broker-configs--brokerconfigs_group.streams.min.heartbeat.interval.ms): The minimum heartbeat interval.
- [`group.streams.max.heartbeat.interval.ms`](#configuration-broker-configs--brokerconfigs_group.streams.max.heartbeat.interval.ms): The maximum heartbeat interval.
- [`group.streams.max.size`](#configuration-broker-configs--brokerconfigs_group.streams.max.size): The maximum number of streams clients that a single streams group can accommodate.
- [`group.streams.num.standby.replicas`](#configuration-broker-configs--brokerconfigs_group.streams.num.standby.replicas): The default number of standby replicas for each task.
- [`group.streams.max.standby.replicas`](#configuration-broker-configs--brokerconfigs_group.streams.max.standby.replicas): Maximum for dynamic configurations of the standby replica configuration.
- [`group.streams.initial.rebalance.delay.ms`](#configuration-broker-configs--brokerconfigs_group.streams.initial.rebalance.delay.ms): The first rebalance of a new (ie, previously empty) group is delayed by this amount to allow more members to join the group.

<a id="streams-developer-guide-streams-rebalance-protocol--group-configuration"></a>

## Group Configuration

For complete details, see the [group configuration](#configuration-group-configs) documentation.

The following group-level configurations are available for streams groups:

- [`streams.session.timeout.ms`](#configuration-group-configs--groupconfigs_streams.session.timeout.ms): The timeout to detect client failures when using the streams group protocol.
- [`streams.heartbeat.interval.ms`](#configuration-group-configs--groupconfigs_streams.heartbeat.interval.ms): The heartbeat interval given to the members.
- [`streams.num.standby.replicas`](#configuration-group-configs--groupconfigs_streams.num.standby.replicas): The number of standby replicas for each task.
- [`streams.initial.rebalance.delay.ms`](#configuration-group-configs--groupconfigs_streams.initial.rebalance.delay.ms): The first rebalance of a group is delayed by this amount to allow more members to join the group.

<a id="streams-developer-guide-streams-rebalance-protocol--example-setting-group-level-configuration"></a>
<a id="streams-developer-guide-streams-rebalance-protocol--example:-setting-group-level-configuration"></a>

### Example: Setting Group-Level Configuration

```
bin/kafka-configs.sh --bootstrap-server localhost:9092 \
  --alter --entity-type groups --entity-name wordcount \
  --add-config streams.num.standby.replicas=1
```

**Note:** In the streams rebalance protocol, `session.timeout.ms`, `heartbeat.interval.ms` and `num.standby.replicas` are group-level configurations, which are ignored when they are set on the client side. Use the `bin/kafka-configs.sh` tool to set these configurations as shown above.

<a id="streams-developer-guide-streams-rebalance-protocol--streams-configuration"></a>

## Streams Configuration

For complete details on all Kafka Streams configurations, see the [streams configuration](#configuration-kafka-streams-configs) documentation.

The following client configuration enables the streams rebalance protocol:

- [`group.protocol`](#configuration-kafka-streams-configs--streamsconfigs_group.protocol): A flag which indicates if the streams rebalance protocol should be used. Set to `streams` to enable (default is `classic`).

<a id="streams-developer-guide-streams-rebalance-protocol--ignored-configurations"></a>

### Ignored Configurations

The following configurations are ignored when the streams rebalance protocol is enabled:

<a id="streams-developer-guide-streams-rebalance-protocol--administration"></a>

# Administration

<a id="streams-developer-guide-streams-rebalance-protocol--admin-api"></a>

## Admin API

The main differences from consumer group APIs are:

- The `describeStreamsGroups` uses the DescribeStreamsGroup RPC and contains different information than consumer groups.
- A streams group has an extra state - `NOT_READY` - and no legacy states from the classic protocol.
- `removeMembersFromConsumerGroup` will not have a corresponding API in this version, as it uses the LeaveGroup RPC for classic consumer groups, which is not available for KIP-848-style groups.

<a id="streams-developer-guide-streams-rebalance-protocol--kafka-streams-groupssh"></a>
<a id="streams-developer-guide-streams-rebalance-protocol--kafka-streams-groups.sh"></a>

## kafka-streams-groups.sh

A new tool called `bin/kafka-streams-groups.sh` is added for working with streams groups. It replaces `bin/kafka-streams-application-reset.sh` for streams groups and can be used to list, describe, and delete streams groups. See the [kafka-streams-groups.sh documentation](#streams-developer-guide-kafka-streams-group-sh) for detailed usage information.

<a id="streams-developer-guide-streams-rebalance-protocol--architecture-and-how-it-works"></a>

# Architecture and How It Works

<a id="streams-developer-guide-streams-rebalance-protocol--streams-groups"></a>

## Streams Groups

The protocol introduces the concept of a **streams group** in parallel to a consumer group. Streams clients use a dedicated heartbeat RPC, `StreamsGroupHeartbeat`, to join a group, leave a group, and update the group coordinator about its currently owned tasks and its client-specific metadata.

The group coordinator manages a streams group similarly to a consumer group, continuously updating the group member metadata via heartbeat responses and running assignment logic when changes are detected. A new group type called `streams` is introduced to the group coordinator, with new record key and value types for group metadata, topology metadata, and group member metadata. These records are persisted in the `__consumer_offsets` topic.

A group can either be a streams group, a share group, or a consumer group, defined by the first heartbeat request using the corresponding GroupId.

<a id="streams-developer-guide-streams-rebalance-protocol--topology-configuration-and-validation"></a>

## Topology Configuration and Validation

To assign tasks among streams clients, the group coordinator uses topology metadata that is initialized when a member joins the group and persisted in the consumer offsets topic.

Whenever a member joins the streams group, the first heartbeat request contains metadata of the topology. The metadata describes the topology as a set of subtopologies, each identified by a unique string identifier and containing metadata relevant for creation of internal topics and assignment.

<a id="streams-developer-guide-streams-rebalance-protocol--topology-validation-and-not_ready-state"></a>

### Topology Validation and NOT\_READY State

During the handling of the streams group heartbeat, the group coordinator may detect that source/sink or internal topics required by the topology do not exist or differ in their configuration from what is required for the topology to execute successfully. This triggers a “topology configuration” process, in which the group coordinator performs the following steps:

- Check that all configured source topics exist.
- Check that “copartition groups” are satisfied - that is, all source topics that are supposed to be copartitioned are indeed copartitioned.
- Derive the required number of partitions for all internal topics from the source topic configuration.
- Check that all internal topics exist with the right configuration.

If any source topics or internal topics are missing, the group enters a state `NOT_READY`. In `NOT_READY`, all heartbeats will be handled as usual (so they typically should not fail), but in the heartbeat response, the status will indicate which kind of problem exists. All members will get an empty assignment when the group is in `NOT_READY` state.

<a id="streams-developer-guide-streams-rebalance-protocol--centralized-assignment-configuration"></a>

## Centralized Assignment Configuration

Core assignment options are configured centrally on the broker, without relying on each client’s configuration. This allows tuning a streams group without redeploying the streams application. The core assignment option introduced on the broker-side is `num.standby.replicas`. This can be configured both globally on the broker and dynamically for specific streams groups through the `IncrementalAlterConfigs` and `DescribeConfigs` RPCs.

The last used assignment configuration is stored in the group metadata on the broker. This way, if an assignment configuration is dynamically changed, reassignment can be triggered immediately.

<a id="streams-developer-guide-streams-rebalance-protocol--monitoring-and-metrics"></a>

# Monitoring and Metrics

The existing group metrics are extended to differentiate between streams groups and consumer groups and account for streams group states. For complete details, see the [streams groups metrics](#operations-monitoring--group-coordinator-monitoring) documentation.

<a id="streams-developer-guide-streams-rebalance-protocol--group-count-by-protocol"></a>

## Group Count by Protocol

Number of groups based on type of protocol, where the list of protocols is extended by the `protocol=streams` variation:

```
kafka.server:type=group-coordinator-metrics,name=group-count,protocol={consumer|classic|streams}
```

<a id="streams-developer-guide-streams-rebalance-protocol--streams-group-count-by-state"></a>

## Streams Group Count by State

Number of streams groups based on state:

```
kafka.server:type=group-coordinator-metrics,name=streams-group-count,state={empty|not_ready|assigning|reconciling|stable|dead}
```

<a id="streams-developer-guide-streams-rebalance-protocol--streams-group-rebalances"></a>

## Streams Group Rebalances

Streams group rebalances sensor:

```
kafka.server:type=group-coordinator-metrics,name=streams-group-rebalance-rate

kafka.server:type=group-coordinator-metrics,name=streams-group-rebalance-count
```

<a id="streams-developer-guide-streams-rebalance-protocol--migration-from-classic-protocol"></a>

# Migration from Classic Protocol

Currently, only offline migration is supported. To migrate a Kafka Streams application from the classic protocol to the streams rebalance protocol:

1. Shut down all application instances.
2. Wait for the `session.timeout.ms` to expire so the group becomes empty (or force an explicit group leave).
3. Update the application configuration to set `group.protocol=streams`.
4. Restart the application instances.

The only broker-side group data that will be preserved are the committed offsets. All other group metadata will be recreated when the application starts with the new protocol. Internal topics (changelog and repartition topics) will continue to exist as regular Kafka topics.

Similarly, you can convert a streams group back to a classic group by following the same process but setting `group.protocol=classic`.

**Warning:** Online migration (migrating while the application is running) is not available in this version. Plan for a maintenance window when migrating between protocols.

**Warning:** Due to a critical broker-side bug in the offline migration code ([KAFKA-20254](https://issues.apache.org/jira/browse/KAFKA-20254)), we recommend against doing migrations from classic to streams groups in 4.2.0. Newly created streams groups are not impacted. The fix is available in 4.2.1.

---

<a id="streams-developer-guide-kafka-streams-group-sh"></a>

<a id="streams-developer-guide-kafka-streams-group-sh--kafka-streams-groups-tool"></a>

# Kafka Streams Groups Tool

Use `kafka-streams-groups.sh` to manage **Streams groups** for the Streams Rebalance Protocol (KIP‑1071): list and describe groups, inspect members and offsets/lag, reset or delete offsets for input topics, and delete groups (optionally including internal topics).

<a id="streams-developer-guide-kafka-streams-group-sh--overview"></a>

# Overview

A **Streams group** is a broker‑coordinated group type for Kafka Streams that uses Streams‑specific RPCs and metadata, distinct from classic consumer groups. The CLI surfaces Streams‑specific states, assignments, and input‑topic offsets to simplify visibility and administration.

**Use with care:** Mutating operations (offset resets/deletes, group deletion) affect how applications will reprocess data when restarted. Always preview with --dry-run before executing and ensure application instances are stopped/inactive and the group is empty before executing the command.

<a id="streams-developer-guide-kafka-streams-group-sh--what-the-streams-groups-tool-does"></a>

# What the Streams Groups tool does

- **List Streams groups** across a cluster and display or filter by group state (Empty, Not Ready, Assigning, Reconciling, Stable, Dead).
- **Describe a Streams group** and show:
  - Group state, group epoch, target assignment epoch (with `--state`, `--verbose` for additional details).
  - Per‑member info such as epochs, current vs target assignments, and whether a member still uses the classic protocol (with `--members` and `--verbose`).
  - Input‑topic offsets and lag (with `--offsets`), to understand how far behind processing is.
- **Reset input‑topic offsets** for a Streams group to control reprocessing boundaries using precise specifiers (earliest, latest, to‑offset, to‑datetime, by‑duration, shift‑by, from‑file). Requires `--dry-run` or `--execute` and inactive instances.
- **Delete offsets** for input topics to force re‑consumption on next start.
- **Delete a Streams group** to clean up broker‑side Streams metadata (offsets, topology, assignments). Optionally delete all, or a subset of, **internal topics** at the same time using `--internal-topics`.

<a id="streams-developer-guide-kafka-streams-group-sh--usage"></a>

# Usage

The script is located in `bin/kafka-streams-groups.sh` and connects to your cluster via `--bootstrap-server`. For secured clusters, pass AdminClient properties using `--command-config`.

```
$ kafka-streams-groups.sh --bootstrap-server <host:port> [COMMAND] [OPTIONS]
```

**Note:** `kafka-streams-groups.sh` complements the Streams Admin API for Streams groups. The CLI exposes list/describe/delete operations and offset management similar in spirit to consumer-group tools, but tailored to Streams groups defined in KIP‑1071.

<a id="streams-developer-guide-kafka-streams-group-sh--commands"></a>

# Commands

<a id="streams-developer-guide-kafka-streams-group-sh--list-streams-groups"></a>

## List Streams groups

Discovering groups

```
# List all Streams groups kafka-streams-groups.sh --bootstrap-server localhost:9092 --list
```

<a id="streams-developer-guide-kafka-streams-group-sh--describe-streams-groups"></a>

## Describe Streams groups

Inspecting group’s state, members, and lag

```
# Describe a group: state + epochs kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --describe --group my-streams-app --state --verbose

# Describe a group: members (assignments vs target, classic/streams) kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --describe --group my-streams-app --members --verbose

# Describe a group: input-topic offsets and lag kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --describe --group my-streams-app --offsets
```

<a id="streams-developer-guide-kafka-streams-group-sh--reset-offsets"></a>
<a id="streams-developer-guide-kafka-streams-group-sh--reset-input-topic-offsets-preview-then-apply"></a>

## Reset input-topic offsets (preview, then apply)

Ensure all application instances are stopped/inactive. Always preview changes with `--dry-run` before using `--execute`.

```
# Preview resetting all input topics to a specific timestamp kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --group my-streams-app \ --reset-offsets --all-input-topics --to-datetime 2025-01-31T23:57:00.000 \ --dry-run

# Apply the reset kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --group my-streams-app \ --reset-offsets --all-input-topics --to-datetime 2025-01-31T23:57:00.000 \ --execute
```

<a id="streams-developer-guide-kafka-streams-group-sh--delete-offsets-to-force-re-consumption"></a>

## Delete offsets to force re-consumption

Delete offsets for all or specific input topics to have the group re-read data on restart.

```
# Delete offsets for all input topics (execute) kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --group my-streams-app \ --delete-offsets --all-input-topics --execute

# Delete offsets for specific topics kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --group my-streams-app \ --delete-offsets --topic input-a --topic input-b --execute
```

<a id="streams-developer-guide-kafka-streams-group-sh--delete-a-streams-group-cleanup"></a>

## Delete a Streams group (cleanup)

Delete broker-side Streams metadata for a group and optionally remove a subset of internal topics.

```
# Delete Streams group metadata kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --delete --group my-streams-app

# Delete a subset of internal topics alongside the group (use with care) kafka-streams-groups.sh --bootstrap-server localhost:9092 \ --delete --group my-streams-app \ --internal-topics my-app-repartition-0,my-app-changelog
```

<a id="streams-developer-guide-kafka-streams-group-sh--all-options-and-flags"></a>

# All options and flags

<a id="streams-developer-guide-kafka-streams-group-sh--core-actions"></a>

## Core actions

- `--list`: List Streams groups. Use `--state` to display/filter by state.
- `--describe`: Describe a group selected by `--group`. Combine with:
  - `--state` (group state and epochs), `--members` (members and assignments), `--offsets` (input and repartition topics offsets/lag).
  - `--verbose` for additional details (e.g., leader epochs where applicable).
- `--reset-offsets`: Reset input-topic offsets (one group at a time; instances should be inactive). Choose exactly one specifier:
  - `--to-earliest`, `--to-latest`, `--to-current`, `--to-offset <n>`
  - `--by-duration <PnDTnHnMnS>`, `--to-datetime <YYYY-MM-DDTHH:mm:SS.sss>`
  - `--shift-by <n>` (±), `--from-file` (CSV)
    Scope:
  - `--all-input-topics` or one/more `--topic <name>`; some builds also support `--all-topics` (all input topics per broker topology metadata).
    Safety:
  - Requires `--dry-run` or `--execute`.
- `--delete-offsets`: Delete offsets for `--all-input-topics`, specific `--topic` names, or `--from-file`.
- `--delete`: Delete Streams group metadata; optionally pass `--internal-topics <list>` to delete a subset of internal topics.

<a id="streams-developer-guide-kafka-streams-group-sh--common-flags"></a>

## Common flags

- `--group <id>`: Target Streams group (application.id).
- `--all-groups`: Operate on all groups (allowed with `--delete`).
- `--bootstrap-server <host:port>`: Broker(s) to connect to (required).
- `--command-config <file>`: Properties for AdminClient (security, timeouts, etc.).
- `--timeout <ms>`: Wait time for group stabilization in some operations (default: 5000ms).
- `--dry-run`, `--execute`: Preview vs apply for mutating operations.
- `--help`, `--version`, `--verbose`: Usage, version, verbosity.

<a id="streams-developer-guide-kafka-streams-group-sh--best-practices-and-safety"></a>

# Best practices and safety

- Preview changes with `--dry-run` to verify topic scope and impact before `--execute`.
- Use `--internal-topics` carefully: deleting internal topics removes state backing topics; only do this when you intend to rebuild state from input topics.

This page documents `kafka-streams-groups.sh` capabilities for Streams groups as defined by KIP‑1071 and implemented in Apache Kafka.

- [Documentation](https://kafka.apache.org/documentation)
- [Kafka Streams](https://kafka.apache.org/documentation/streams)
- [Developer Guide](https://kafka.apache.org/documentation/streams/developer-guide/)

---

<a id="streams-developer-guide-scala-migration"></a>

<a id="streams-developer-guide-scala-migration--migrating-from-streams-scala-to-java-api"></a>

# Migrating from Streams Scala to Java API

<a id="streams-developer-guide-scala-migration--migration-overview"></a>

## Migration Overview

The Java Streams API works well from Scala with minimal adjustments. The main differences are:

1. **Use Java types directly** instead of Scala wrapper classes
2. **Configure Serdes explicitly** via `StreamsConfig` or pass them to methods

<a id="streams-developer-guide-scala-migration--example-word-count-application"></a>
<a id="streams-developer-guide-scala-migration--example:-word-count-application"></a>

### Example: Word Count Application

```scala
import java.util.Properties

import org.apache.kafka.streams.scala.ImplicitConversions._
import org.apache.kafka.streams.scala._
import org.apache.kafka.streams.scala.kstream._
import org.apache.kafka.streams.{KafkaStreams, StreamsConfig}
import org.apache.kafka.streams.scala.serialization.Serdes._

object WordCountScala extends App {
  val props = new Properties()
  props.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount")
  props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092")

  val builder = new StreamsBuilder  // Scala wrapper
  val textLines: KStream[String, String] = builder.stream[String, String]("input-topic")

  val wordCounts: KTable[String, Long] = textLines
    .flatMapValues(line => line.toLowerCase.split("\\W+"))
    .groupBy((_, word) => word)
    .count()

  wordCounts.toStream.to("output-topic")

  val streams = new KafkaStreams(builder.build(), props)
  streams.start()
}
```

<a id="streams-developer-guide-scala-migration--java-api-approach"></a>

#### Java API Approach

```scala
import java.util.Properties

import org.apache.kafka.streams.{KafkaStreams, StreamsBuilder, StreamsConfig}
import org.apache.kafka.streams.kstream.{KStream, KTable, Produced}
import org.apache.kafka.common.serialization.Serdes
import scala.jdk.CollectionConverters._

object WordCountJava extends App {
  val props = new Properties()
  props.put(StreamsConfig.APPLICATION_ID_CONFIG, "wordcount")
  props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092")
  // Configure default serdes
  props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, classOf[Serdes.StringSerde])
  props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, classOf[Serdes.StringSerde])

  val builder = new StreamsBuilder  // Java StreamsBuilder
  val textLines = builder.stream[String, String]("input-topic")

  val wordCounts = textLines
    .flatMapValues(_.toLowerCase.split("\\W+"))
    .groupBy((_, word) => word)
    .count()

  wordCounts.toStream.to("output-topic", Produced.`with`(Serdes.String(), Serdes.Long()))

  val streams = new KafkaStreams(builder.build(), props)
  streams.start()
}
```
