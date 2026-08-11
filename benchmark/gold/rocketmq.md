---
entry_url: https://rocketmq.apache.org/docs/
page_count: 64
asset_count: 117
---
# Why choose RocketMQ
## Navigation
- [Introduction](#index)
  - [Why choose RocketMQ](#index)
  - [Concepts](#introduction-02concepts)
  - [Parameter Constraints and Suggestions](#introduction-03limits)
- [Quick Start](#quickstart-01quickstart)
  - [Run RocketMQ locally](#quickstart-01quickstart)
  - [Run RocketMQ in Docker](#quickstart-02quickstartwithdocker)
  - [Run RocketMQ with Docker Compose](#quickstart-03quickstartwithdockercompose)
  - [Run RocketMQ with Kubernetes](#quickstart-04quickstartwithhelminkubernetes)
- [Domain Model](#domainmodel-01main)
  - [Domain Model](#domainmodel-01main)
  - [Topic](#domainmodel-02topic)
  - [Message Queue](#domainmodel-03messagequeue)
  - [Message](#domainmodel-04message)
  - [Producer](#domainmodel-04producer)
  - [Consumer Group](#domainmodel-07consumergroup)
  - [Consumer](#domainmodel-08consumer)
  - [Subscription](#domainmodel-09subscription)
- [Feature Behavior](#featurebehavior-01normalmessage)
  - [Normal Message](#featurebehavior-01normalmessage)
  - [Delay Message](#featurebehavior-02delaymessage)
  - [Ordered Message](#featurebehavior-03fifomessage)
  - [Transaction Message](#featurebehavior-04transactionmessage)
  - [Sending Retry and Throttling Policy](#featurebehavior-05sendretrypolicy)
  - [Consumer Types](#featurebehavior-06consumertype)
  - [Message Filtering](#featurebehavior-07messagefilter)
  - [Consumer Load Balancing](#featurebehavior-08consumerloadbalance)
  - [Consumer Progress Management](#featurebehavior-09consumerprogress)
  - [Consumption Retry](#featurebehavior-10consumerretrypolicy)
  - [Message Storage and Cleanup](#featurebehavior-11messagestorepolicy)
- [Deployment & Operations](#deploymentoperations-01deploy)
  - [Deployment Method](#deploymentoperations-01deploy)
  - [Admin Tool](#deploymentoperations-02admintool)
  - [Master-Slave Automatic Failover Mode](#deploymentoperations-03autofailover)
  - [RocketMQ Dashboard](#deploymentoperations-04dashboard)
  - [RocketMQ Prometheus Exporter](#deploymentoperations-05exporter)
- [Observability](#observability-01metrics)
  - [Metrics](#observability-01metrics)
- [Client SDK](#sdk-01overview)
  - [Overview](#sdk-01overview)
  - [Java Client SDK](#sdk-02java)
  - [C++ Client SDK](#sdk-03cplusplus)
  - [C# Client SDK](#sdk-04csharp)
  - [Go Client SDK](#sdk-05go)
- [Best Practice](#bestpractice-01bestpractice)
  - [Basic Best Practices](#bestpractice-01bestpractice)
  - [DLedger](#bestpractice-02dledger)
  - [Access Control 2.0](#bestpractice-03access)
  - [JVM/OS Configuration](#bestpractice-04jvmos)
  - [Consistent Subscription Relationship](#bestpractice-05subscribe)
  - [FAQs](#bestpractice-06faq)
  - Access Control (ACL 1.0) (https://rocketmq.apache.org/docs/bestPractice/07access-1.0)
- [RocketMQ EventBridge](#eventbridge-01rocketmqeventbridgeconcepts)
  - [RocketMQ EventBridge Core Concept](#eventbridge-01rocketmqeventbridgeconcepts)
  - [RocketMQ EventBridge Overview](#eventbridge-02rocketmqeventbridgeoverview)
  - [RocketMQ EventBridge Quick Start](#eventbridge-03rocketmqeventbridgequickstart)
- [RocketMQ MQTT](#mqtt-01rocketmqmqttoverview)
  - [RocketMQ MQTT Overview](#mqtt-01rocketmqmqttoverview)
  - [RocketMQ MQTT QuickStart](#mqtt-02rocketmqmqttquickstart)
- [RocketMQ Connect](#connect-01rocketmq-connect-overview)
  - [RocketMQ Connect Overview](#connect-01rocketmq-connect-overview)
  - [RocketMQ Connect Concept](#connect-02rocketmq-connect-concept)
  - [RocketMQ Connect Quick Start](#connect-03rocketmq-connect-quick-start)
  - [RocketMQ Connect in Action 1](#connect-04rocketmq-connect-in-action1)
  - [RocketMQ Connect in Action 2](#connect-05rocketmq-connect-in-action2)
  - [RocketMQ Connect in Action 3](#connect-06rocketmq-connect-in-action3)
  - [RocketMQ Connect in Action 4](#connect-07rocketmq-connect-in-action4)
  - [RocketMQ Connect in Action 5](#connect-08rocketmq-connect-in-action5-es)
- [RocketMQ Streams](#streams-01rocketmq-streams-overview)
  - [RocketMQ Streams Overview](#streams-01rocketmq-streams-overview)
  - [RocketMQ Streams Core Concept](#streams-02rocketmq-streams-concept)
  - [RocketMQ Streams Quick Start](#streams-03rocketmq-streams-quick-start)
- [Contribution Guide](#contributionguide-01how-to-contribute)
  - [How to Contribute](#contributionguide-01how-to-contribute)
  - [Code Guidelines](#contributionguide-02code-guidelines)
  - [GitHub Submit PR](#contributionguide-03pull-request)
  - [Release Manual](#contributionguide-04release-manual)
- [Security](#security-01security)
  - [Security](#security-01security)

## Content

<a id="index"></a>

<!-- source_url: https://rocketmq.apache.org/docs/ -->

<!-- page_index: 1 -->

# Why choose RocketMQ

Version: 5.0

# Why choose RocketMQ

<a id="index--why-rocketmq"></a>

## Why RocketMQ

During the early stages of RocketMQ's development at Alibaba, we utilized it for a multitude of purposes, including asynchronous communications, search, social networking activity flows, data pipelines, and trade processes. As our trade business grew, we noticed that the messaging cluster was under increasing pressure.

After observing and analyzing the performance of the ActiveMQ IO module, we identified a bottleneck as the number of queues and virtual topics increased. We attempted to address this issue through various methods, such as throttling, circuit breakers, and service downgrades, but none proved satisfactory. We also considered using Kafka, a popular messaging solution, but it did not meet our requirements for low latency and high reliability, as explained below. As a result, we made the decision to develop a new messaging engine capable of handling a wider range of use cases, from traditional pub/sub to high-volume, real-time, zero-error transaction systems.

Since its inception, Apache RocketMQ has been widely adopted by enterprise developers and cloud vendors due to its simple architecture, rich business functionality, and extreme scalability. After more than a decade of extensive scenario polishing, RocketMQ has become the industry standard for financial-grade reliable business messages and is widely used in Internet, big data, mobile Internet, IoT, and other fields.

> [!TIP]
> The following table shows the comparison between RocketMQ, ActiveMQ and Kafka

<a id="index--rocketmq-vs-activemq-vs-kafka"></a>

## RocketMQ vs. ActiveMQ vs. Kafka

<table><thead><tr><th>Messaging Product</th><th>Client SDK</th><th>Protocol and Specification</th><th>Ordered Message</th><th>Scheduled Message</th><th>Batched Message</th><th>BroadCast Message</th><th>Message Filter</th><th>Server Triggered Redelivery</th><th>Message Storage</th><th>Message Retroactive</th><th>Message Priority</th><th>High Availability and Failover</th><th>Message Track</th><th>Configuration</th><th>Management and Operation Tools</th></tr></thead><tbody><tr><td>ActiveMQ</td><td>Java, .NET, C++ etc.</td><td>Push model, support OpenWire, STOMP, AMQP, MQTT, JMS</td><td>Exclusive Consumer or Exclusive Queues can ensure ordering</td><td>Supported</td><td>Not Supported</td><td>Supported</td><td>Supported</td><td>Not Supported</td><td>Supports very fast persistence using JDBC along with a high performance journal，such as levelDB, kahaDB</td><td>Supported</td><td>Supported</td><td>Supported, depending on storage,if using levelDB it requires a ZooKeeper server</td><td>Not Supported</td><td>The default configuration is low level, user need to optimize the configuration parameters</td><td>Supported</td></tr><tr><td>Kafka</td><td>Java, Scala etc.</td><td>Pull model, support TCP</td><td>Ensure ordering of messages within a partition</td><td>Not Supported</td><td>Supported, with async producer</td><td>Not Supported</td><td>Supported, you can use Kafka Streams to filter messages</td><td>Not Supported</td><td>High performance file storage</td><td>Supported offset indicate</td><td>Not Supported</td><td>Supported, requires a ZooKeeper server</td><td>Not Supported</td><td>Kafka uses key-value pairs format for configuration. These values can be supplied either from a file or programmatically.</td><td>Supported, use terminal command to expose core metrics</td></tr><tr><td>RocketMQ</td><td>Java, C++, Go</td><td>Pull model, support TCP, JMS, OpenMessaging</td><td>Ensure strict ordering of messages,and can scale out gracefully</td><td>Supported</td><td>Supported, with sync mode to avoid message loss</td><td>Supported</td><td>Supported, property filter expressions based on SQL92</td><td>Supported</td><td>High performance and low latency file storage</td><td>Supported timestamp and offset two indicates</td><td>Not Supported</td><td>Supported, Master-Slave model, without another kit</td><td>Supported</td><td>Work out of box,user only need to pay attention to a few configurations</td><td>Supported, rich web and terminal command to expose core metrics</td></tr></tbody></table>

- [Why RocketMQ](#index--why-rocketmq)
- [RocketMQ vs. ActiveMQ vs. Kafka](#index--rocketmq-vs-activemq-vs-kafka)

---

<a id="introduction-02concepts"></a>

<!-- source_url: https://rocketmq.apache.org/docs/introduction/02concepts/ -->

<!-- page_index: 2 -->

# Concepts

Version: 5.0

# Concepts

This section describes the core concepts of Apache RocketMQ.

<a id="introduction-02concepts--topic"></a>

## Topic

A topic is a top-level container that is used in Apache RocketMQ to transfer and store messages that belong to the same business logic.Learn more [Topic](#domainmodel-02topic).

<a id="introduction-02concepts--messagetype"></a>

## MessageType

Categories defined by message transfer characteristics for type management and security verification. Apache RocketMQ support NORMAL,FIFO,TRANSACTION and DELAY message type.

> [!INFO]
> Starting from version 5.0, Apache RocketMQ supports enforcing the validation of message types, that is, each topic only allows messages of a single type to be sent. This can better facilitate operation and management of production systems and avoid confusion. However, to ensure backward compatibility with version 4.x, the validation feature is enable by default.

<a id="introduction-02concepts--messagequeue"></a>

## MessageQueue

MessageQueue is a container that is used to store and transmit messages in Apache RocketMQ. MessageQueue is the smallest unit of storage for Apache RocketMQ messages. Learn more [MessageQueue](#domainmodel-03messagequeue).

<a id="introduction-02concepts--message"></a>

## Message

A message is the smallest unit of data transmission in Apache RocketMQ. A producer encapsulates the load and extended attributes of business data into messages and sends the messages to a Apache RocketMQ broker. Then, the broker delivers the messages to the consumer based on the relevant semantics. Learn more[Message](#domainmodel-04message).

<a id="introduction-02concepts--messageview"></a>

## MessageView

MessageView is read-only interface to message from a development perspective. The message view allows you to read multiple properties and payload information inside a message, but you cannot make any changes to the message itself.

<a id="introduction-02concepts--messagetag"></a>

## MessageTag

MessageTag is a fine-grained message classification property that allows message to be subdivided below the topic level. Consumers implement message filtering by subscribing to specific tags. Learn more [MessageFilter](#featurebehavior-07messagefilter).

<a id="introduction-02concepts--messageoffset"></a>

## MessageOffset

Messages are stored in the queue in order of precedence, each message has a unique coordinate of type Long in the queue, which is defined as the message site. Learn more [Consumer progress management](#featurebehavior-09consumerprogress)。

<a id="introduction-02concepts--consumeroffset"></a>

## ConsumerOffset

A message is not removed from the queue immediately after it has been consumed by a consumer, Apache RocketMQ will record the last consumed message based on each consumer group. Learn more [Consumer progress management](#featurebehavior-09consumerprogress).

<a id="introduction-02concepts--messagekey"></a>

## MessageKey

MessageKey is The message-oriented index property. By setting the message index, you can quickly find the corresponding message content.

<a id="introduction-02concepts--producer"></a>

## Producer

A producer in Apache RocketMQ is a functional messaging entity that creates messages and sends them to the server. A producer is typically integrated on the business system and serves to encapsulate data as messages in Apache RocketMQ and send the messages to the server. Learn more [Producer](#domainmodel-04producer)。

<a id="introduction-02concepts--transactionchecker"></a>

## TransactionChecker

Apache RocketMQ uses a transaction messaging mechanism that requires a producer to implement a transaction checker to ensure eventual consistency of transactions. Learn more[Transaction Message](#featurebehavior-04transactionmessage)。

<a id="introduction-02concepts--consumergroup"></a>

## ConsumerGroup

A consumer group is a load balancing group that contains consumers that use the same consumption behaviors in Apache RocketMQ. Learn more [ConsumerGroup](#domainmodel-07consumergroup)。

<a id="introduction-02concepts--consumer"></a>

## Consumer

A consumer is an entity that receives and processes messages in Apache RocketMQ. Consumers are usually integrated in business systems. They obtain messages from Apache RocketMQ brokers and convert the messages into information that can be perceived and processed by business logic. Learn more [Consumer](#domainmodel-08consumer)。

<a id="introduction-02concepts--subscription"></a>

## Subscription

A subscription is the rule and status settings for consumers to obtain and process messages in Apache RocketMQ. Subscriptions are dynamically registered by consumer groups with brokers. Messages are then matched and consumed based on the filter rules defined by subscriptions. Learn more [Subscription](#domainmodel-09subscription)。

- [Topic](#introduction-02concepts--topic)
- [MessageType](#introduction-02concepts--messagetype)
- [MessageQueue](#introduction-02concepts--messagequeue)
- [Message](#introduction-02concepts--message)
- [MessageView](#introduction-02concepts--messageview)
- [MessageTag](#introduction-02concepts--messagetag)
- [MessageOffset](#introduction-02concepts--messageoffset)
- [ConsumerOffset](#introduction-02concepts--consumeroffset)
- [MessageKey](#introduction-02concepts--messagekey)
- [Producer](#introduction-02concepts--producer)
- [TransactionChecker](#introduction-02concepts--transactionchecker)
- [ConsumerGroup](#introduction-02concepts--consumergroup)
- [Consumer](#introduction-02concepts--consumer)
- [Subscription](#introduction-02concepts--subscription)

---

<a id="introduction-03limits"></a>

<!-- source_url: https://rocketmq.apache.org/docs/introduction/03limits/ -->

<!-- page_index: 3 -->

# Parameter Constraints and Suggestions

Version: 5.0

# Parameter Constraints and Suggestions

There are many custom parameters and resource names in the Apache RocketMQ system. You are advised to set the system according to the following instructions to avoid application exceptions caused by improper setting of certain parameters.

<table><thead><tr><th>Parameters</th><th>Recommended range</th><th>Instructions</th></tr></thead><tbody><tr><td>Topic name</td><td>Characters suggest：a<!-- -->~<!-- -->z A<!-- -->~<!-- -->Z 0<!-- -->~<!-- -->9 （<em>）（-）（%）
 Suggested length：1<!-- -->~<!-- -->64 characters
 System reserved character：The following reserved characters or characters with special prefixes are not allowed for topic names.
 reserved characters: TBW102  <em> BenchmarkTest  </em> SELF_TEST_TOPIC  <em> OFFSET_MOVED_EVENT  </em> SCHEDULE_TOPIC_XXXX  <em> RMQ_SYS_TRANS_HALF_TOPIC  </em> RMQ_SYS_TRACE_TOPIC  <em> RMQ_SYS_TRANS_OP_HALF_TOPIC
  reserved prefix characters: </em> rmq_sys</em>   %RETRY%<em>   %DLQ%</em>   rocketmq-broker-</td><td>Topic name should use short, common characters and avoid special characters. Special characters may cause exceptions in system parsing. If the characters are too long, messages may be rejected.</td></tr><tr><td>ConsumerGroup name</td><td>Characters suggest：a<!-- -->~<!-- -->z A<!-- -->~<!-- -->Z 0<!-- -->~<!-- -->9 （<em>）（-）（%）
 Suggested length：1<!-- -->~<!-- -->64 characters
 System reserved character：The following reserved characters or characters with special prefixes are not allowed for consumerGroup names.
 reserved characters: <em> DEFAULT_CONSUMER  </em> DEFAULT_PRODUCER  <em> TOOLS_CONSUMER  </em> FILTERSRV_CONSUMER  <em> __MONITOR_CONSUMER  </em> CLIENT_INNER_PRODUCER  <em> SELF_TEST_P_GROUP  </em> SELF_TEST_C_GROUP  <em> CID_ONS-HTTP-PROXY  </em> CID_ONSAPI_PERMISSION  <em> CID_ONSAPI_OWNER  </em> CID_ONSAPI_PULL  <em> CID_RMQ_SYS_TRANS    </em> reserved characters * CID_RMQ_SYS</em>  * CID_HOUSEKEEPING</td><td>null</td></tr><tr><td>ACL credentials</td><td>Characters suggest：AK（AccessKey ID）、SK（AccessKey Secret）and Token only support a<!-- -->~<!-- -->z A<!-- -->~<!-- -->Z 0<!-- -->~<!-- -->9    Suggested length：less than 1024 characters.</td><td>null</td></tr><tr><td>Request timeout</td><td>Default value：3000ms.</td><td>The request timeout duration is the waiting time for local synchronous invocation of clients. Set a proper value based on the actual application to avoid long thread blocking time.</td></tr><tr><td>Max message size</td><td>Default value：4 MB.  Message compression is not involved, only the size of the message body is calculated.    Value range：Suggest less than 4 MB.</td><td>The message transmission should be compressed and the load should be controlled to avoid the transmission of large files.</td></tr><tr><td>Message custom properties</td><td>Character limit：All visible characters.    Suggested length：Sum of all keys and values less than 16KB.    System reserved properties：The following reserved properties are not allowed as keys for custom properties. System reserved Keys</td><td>null</td></tr><tr><td>MessageGroup</td><td>Character limit：All visible characters.   Suggested length：1<!-- -->~<!-- -->64.</td><td>Generally, messageGroup is set to a set of message identifiers that need to ensure order, such as order, user, etc.</td></tr><tr><td>Max number of message sending retries</td><td>Default values：3 times.   Value range：No limits.</td><td>Sending retry policy is invisible to applications. A small value is recommended to avoid blocking service threads.  If the message is not sent successfully after the maximum number of retries is reached, it is recommended that the service side perform backtracking to ensure message reliability.</td></tr><tr><td>Max number of message consume retries</td><td>Default value：16 times.</td><td>Consumption retry times set a proper value based on actual service requirements to avoid unlimited consumption retry times. If the number of retry times is too large, the system pressure increases.</td></tr><tr><td>Transaction exception check interval</td><td>Default value：60 seconds.</td><td>Transaction exception check interval refers to the interval at which semi-transaction messages are not committed due to system restart or abnormal conditions. The producer client will check back the transaction status according to this interval. Do not set the interval too short. Otherwise, the system performance may be affected by frequent callback calls.</td></tr><tr><td>Time of the first callback of a semi-transaction message</td><td>Default value：Refer to <!-- -->[<!-- -->Transaction exception check interval<!-- -->]<!-- -->  * Max check times</td><td>null</td></tr><tr><td>Maximum timeout duration of semi-transaction messages</td><td>Default value：4 Hour.</td><td>If the semi-transaction message is not committed due to system restart or abnormal conditions, the producer client will check back according to the transaction exception check interval. If no result is returned after the timeout period of the semi-transaction message, the semi-transaction message will be forcibly rolled back.</td></tr><tr><td>PushConsumer sdk cache</td><td>Default value：   <em> Maximum cache num：1024
</em> Maximum cache size：64 M.</td><td>The number and size of cached messages should be set to the limit allowed by system memory.</td></tr><tr><td>PushConsumer retry intervals</td><td>Default value：  <em> Concurrent deliver type：The interval time ladder changes.
</em> Fifo deliver type：3000 ms.</td><td>null</td></tr><tr><td>PushConsumer consume threads</td><td>Default value：20</td><td>null</td></tr><tr><td>Get message batch size</td><td>Default value：32</td><td>The consumer obtains the maximum number of messages from the server at a time. You are advised to set a proper parameter value based on actual services. If the number of messages obtained at one time is too large, a large number of messages may be duplicated when consumption fails.</td></tr><tr><td>SimpleConsumer max invisible time</td><td>Default value：This parameter is mandatory and has no default value.    Suggested range：10 seconds to 12 hours.</td><td>Consumption invisible time refers to the total time between message processing and retry after failure. You are advised to set the value to a little longer than the actual time.</td></tr></tbody></table>

---

<a id="quickstart-01quickstart"></a>

<!-- source_url: https://rocketmq.apache.org/docs/quickStart/01quickstart/ -->

<!-- page_index: 4 -->

# Run RocketMQ locally

Version: 5.0

# Run RocketMQ locally

This section will describe steps to quickly deploy a RocketMQ cluster with a single node; Commands to send and receive messages to/from it are also included as proof of work.

> [!TIP]
> **SYSTEM REQUIREMENT**
> 1. 64-bit OS，Linux/Unix/macOS is recommended
> 2. 64-bit JDK 1.8+

<a id="quickstart-01quickstart--1get-apache-rocketmq"></a>

## 1.Get Apache RocketMQ

> [!TIP]
> **Download RocketMQ**
> Apache RocketMQ is distributed both in binary and source packages. Click [here](assets/files/rocketmq-all-5-3-2-source-release_11ef6dc535f9b2f0.zip) to download Apache RocketMQ 5.3.2 source package. You may prefer [prebuilt binary package](assets/files/rocketmq-all-5-3-2-bin-release_a36140137f3f77f0.zip), which can be run directly since it has been compiled.

The following instruction takes the application of RocketMQ 5.3.2 source package in Linux environment as an example in order to introduce the installation process of RocketMQ.

Extract the source package of RocketMQ 5.3.2, then compile and build the binary executables:

```shell
$ unzip rocketmq-all-5.3.2-source-release.zip
$ cd rocketmq-all-5.3.2-source-release/
$ mvn -Prelease-all -DskipTests -Dspotbugs.skip=true clean install -U
$ cd distribution/target/rocketmq-5.3.2/rocketmq-5.3.2
```

<a id="quickstart-01quickstart--2-start-nameserver"></a>

## 2. Start NameServer

After the installation of RocketMQ, start the NameServer:

```shell
### start namesrv
$ nohup sh bin/mqnamesrv &

### verify namesrv
$ tail -f ~/logs/rocketmqlogs/namesrv.log The Name Server boot success...
```

> [!INFO]
> Once we see **'The Name Server boot success..'** from namesrv.log, it means the NameServer has been started successfully.

<a id="quickstart-01quickstart--3-start-broker-and-proxy"></a>

## 3. Start Broker and Proxy

After nameserver startup, we need start the broker and proxy. We recommend Local deployment mode, where Broker and Proxy are deployed in the same process. We also support cluster deployment mode. Learn more [Deployment introduction](#deploymentoperations-01deploy).

```shell
### start broker
$ nohup sh bin/mqbroker -n localhost:9876 --enable-proxy &

### verify broker
$ tail -f ~/logs/rocketmqlogs/proxy.log The broker[broker-a,192.169.1.2:10911] boot success...
```

> [!INFO]
> Once we see “The broker[brokerName,ip:port] boot success..” from proxy.log, it means the Broker has been started successfully.

> [!NOTE]
> Thus far, a single-Master RocketMQ cluster has been deployed, and we are able to send and receive simple messages by scripts.

<a id="quickstart-01quickstart--4-send-and-receive-messages-with-tools"></a>

## 4. Send and Receive Messages with tools

Before test with tools, we need set the nameserver address to system. like system environment variables `NAMESRV_ADDR`.

```shell
$ export NAMESRV_ADDR=localhost:9876
$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer SendResult [sendStatus=SEND_OK, msgId= ...

$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer ConsumeMessageThread_%d Receive New Messages: [MessageExt...
```

<a id="quickstart-01quickstart--5-send-and-receive-messages-with-sdk"></a>

## 5. Send and Receive Messages with SDK

We can also try to use the client sdk to send and receive messages, you can see more details from [rocketmq-clients](https://github.com/apache/rocketmq-clients).

1. Create a java project.
2. Add sdk dependency to *pom.xml*, remember to replace the `rocketmq-client-java-version` with the [latest release](https://search.maven.org/search?q=g:org.apache.rocketmq%20AND%20a:rocketmq-client-java).


```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client-java</artifactId>
    <version>${rocketmq-client-java-version}</version>
</dependency>
```

3. Create topic by mqadmin cli tools.


```shell
$ sh bin/mqadmin updatetopic -n localhost:9876 -t TestTopic -c DefaultCluster
```

4. In the Java project you have created, create a program that sends messages and run it with the following code:


```java
import java.io.IOException;
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientConfigurationBuilder;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.message.Message;
import org.apache.rocketmq.client.apis.producer.Producer;
import org.apache.rocketmq.client.apis.producer.SendReceipt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProducerExample {
    private static final Logger logger = LoggerFactory.getLogger(ProducerExample.class);

    public static void main(String[] args) throws ClientException, IOException {
        String endpoint = "localhost:8081";
        String topic = "TestTopic";
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        ClientConfigurationBuilder builder = ClientConfiguration.newBuilder().setEndpoints(endpoint);
        ClientConfiguration configuration = builder.build();
        Producer producer = provider.newProducerBuilder()
            .setTopics(topic)
            .setClientConfiguration(configuration)
            .build();
        Message message = provider.newMessageBuilder()
            .setTopic(topic)
            .setKeys("messageKey")
            .setTag("messageTag")
            .setBody("messageBody".getBytes())
            .build();
        try {
            SendReceipt sendReceipt = producer.send(message);
            logger.info("Send message successfully, messageId={}", sendReceipt.getMessageId());
        } catch (ClientException e) {
            logger.error("Failed to send message", e);
        }
        // producer.close();
    }
}
```

5. In the Java project you have created, create a consumer demo program and run it. Apache RocketMQ support [SimpleConsumer](#featurebehavior-06consumertype) and [PushConsumer](#featurebehavior-06consumertype).


```java
import java.io.IOException;
import java.util.Collections;
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.consumer.ConsumeResult;
import org.apache.rocketmq.client.apis.consumer.FilterExpression;
import org.apache.rocketmq.client.apis.consumer.FilterExpressionType;
import org.apache.rocketmq.client.apis.consumer.PushConsumer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PushConsumerExample {
    private static final Logger logger = LoggerFactory.getLogger(PushConsumerExample.class);

    private PushConsumerExample() {
    }

    public static void main(String[] args) throws ClientException, IOException, InterruptedException {
        final ClientServiceProvider provider = ClientServiceProvider.loadService();
        String endpoints = "localhost:8081";
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints(endpoints)
            .build();
        String tag = "*";
        FilterExpression filterExpression = new FilterExpression(tag, FilterExpressionType.TAG);
        String consumerGroup = "YourConsumerGroup";
        String topic = "TestTopic";
        PushConsumer pushConsumer = provider.newPushConsumerBuilder()
            .setClientConfiguration(clientConfiguration)
            .setConsumerGroup(consumerGroup)
            .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
            .setMessageListener(messageView -> {
                logger.info("Consume message successfully, messageId={}", messageView.getMessageId());
                return ConsumeResult.SUCCESS;
            })
            .build();
        Thread.sleep(Long.MAX_VALUE);
        // pushConsumer.close();
    }
}
```

<a id="quickstart-01quickstart--6-shutdown-servers"></a>

## 6. Shutdown Servers

After finishing the practice, we could shut down the service by the following commands.

```shell
$ sh bin/mqshutdown broker The mqbroker(36695) is running... Send shutdown request to mqbroker(36695) OK

$ sh bin/mqshutdown namesrv The mqnamesrv(36664) is running... Send shutdown request to mqnamesrv(36664) OK
```

- [1.Get Apache RocketMQ](#quickstart-01quickstart--1get-apache-rocketmq)
- [2. Start NameServer](#quickstart-01quickstart--2-start-nameserver)
- [3. Start Broker and Proxy](#quickstart-01quickstart--3-start-broker-and-proxy)
- [4. Send and Receive Messages with tools](#quickstart-01quickstart--4-send-and-receive-messages-with-tools)
- [5. Send and Receive Messages with SDK](#quickstart-01quickstart--5-send-and-receive-messages-with-sdk)
- [6. Shutdown Servers](#quickstart-01quickstart--6-shutdown-servers)

---

<a id="quickstart-02quickstartwithdocker"></a>

<!-- source_url: https://rocketmq.apache.org/docs/quickStart/02quickstartWithDocker/ -->

<!-- page_index: 5 -->

# Run RocketMQ in Docker

Version: 5.0

# Run RocketMQ in Docker

This section introduces how to quickly deploy a single-node, single-replica RocketMQ service using Docker and complete simple message sending and receiving.

> [!TIP]
> **System Requirements**
> 1. 64-bit operating system
> 2. 64-bit JDK 1.8+

<a id="quickstart-02quickstartwithdocker--1pull-rocketmq-image"></a>

## 1.Pull RocketMQ Image

Here, we take the RocketMQ 5.3.2 version image from [dockerhub](https://hub.docker.com/r/apache/rocketmq/tags) as an example to introduce the deployment process.

```shell
docker pull apache/rocketmq:5.3.2
```

<a id="quickstart-02quickstartwithdocker--2create-a-shared-network-for-containers"></a>

## 2.Create a Shared Network for Containers

RocketMQ involves multiple services and requires multiple containers. Creating a Docker network facilitates communication between containers.

```shell
docker network create rocketmq
```

<a id="quickstart-02quickstartwithdocker--3start-nameserver"></a>

## 3.Start NameServer

```shell
# Start NameServer docker run -d --name rmqnamesrv -p 9876:9876 --network rocketmq apache/rocketmq:5.3.2 sh mqnamesrv

# Verify if NameServer started successfully docker logs -f rmqnamesrv
```

> [!INFO]
> Once we see **'The Name Server boot success..'** from namesrv.log, it means the NameServer has been started successfully.

<a id="quickstart-02quickstartwithdocker--4start-broker-and-proxy"></a>

## 4.Start Broker and Proxy

After nameserver startup, we proceed to start the Broker and Proxy.

<div class="tabs-container tabList__CuJ"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_LNqP tabs__item--active" role="tab" tabindex="0">Linux</li><li aria-selected="false" class="tabs__item tabItem_LNqP" role="tab" tabindex="-1">Windows</li></ul><div class="margin-top--md"><div class="tabItem_Ymn6" role="tabpanel"><div class="language-code codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-code codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token plain"># Configure the broker's IP address</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">echo "brokerIP1=127.0.0.1" &gt; broker.conf</span> </span><span class="token-line" style="color:#393A34"><span class="token plain" style="display:inline-block"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"># Start the Broker and Proxy</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">docker run -d \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">--name rmqbroker \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">--network rocketmq \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-p 10912:10912 -p 10911:10911 -p 10909:10909 \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-p 8080:8080 -p 8081:8081 \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-e "NAMESRV_ADDR=rmqnamesrv:9876" \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain"># In PowerShell, replace %cd% with $pwd</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-v ./broker.conf:/home/rocketmq/rocketmq-5.3.2/conf/broker.conf \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">apache/rocketmq:5.3.2 sh mqbroker --enable-proxy \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-c /home/rocketmq/rocketmq-5.3.2/conf/broker.conf</span> </span><span class="token-line" style="color:#393A34"><span class="token plain" style="display:inline-block"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"># Verify if Broker started successfully</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">docker exec -it rmqbroker bash -c "tail -n 10 /home/rocketmq/logs/rocketmqlogs/proxy.log"</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div><div class="tabItem_Ymn6" hidden="" role="tabpanel"><div class="language-code codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-code codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token plain"># Configure the broker's IP address</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">echo "brokerIP1=127.0.0.1" &gt; broker.conf</span> </span><span class="token-line" style="color:#393A34"><span class="token plain" style="display:inline-block"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"># Start the Broker and Proxy</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">docker run -d ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">--name rmqbroker ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">--net rocketmq ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-p 10912:10912 -p 10911:10911 -p 10909:10909 ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-p 8080:8080 -p 8081:8081 \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-e "NAMESRV_ADDR=rmqnamesrv:9876" ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-v %cd%\broker.conf:/home/rocketmq/rocketmq-5.3.2/conf/broker.conf ^</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">apache/rocketmq:5.3.2 sh mqbroker --enable-proxy \</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">-c /home/rocketmq/rocketmq-5.3.2/conf/broker.conf</span> </span><span class="token-line" style="color:#393A34"><span class="token plain" style="display:inline-block"></span> </span><span class="token-line" style="color:#393A34"><span class="token plain"># Verify if Broker started successfully</span> </span><span class="token-line" style="color:#393A34"><span class="token plain">docker exec -it rmqbroker bash -c "tail -n 10 /home/rocketmq/logs/rocketmqlogs/proxy.log"</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div></div></div>

> [!INFO]
> Once we see **'The broker[brokerName,ip:port] boot success..'** from proxy.log, it means the Broker has been started successfully.

> [!NOTE]
> Thus far, a single-Master RocketMQ cluster has been deployed, and we are able to send and receive simple messages.

<a id="quickstart-02quickstartwithdocker--5send-and-receive-messages-with-sdk"></a>

## 5.Send and Receive Messages with SDK

We can also try to use the client sdk to send and receive messages, you can see more details from [rocketmq-clients](https://github.com/apache/rocketmq-clients).

1. Create a java project.
2. Add sdk dependency to *pom.xml*, remember to replace the `rocketmq-client-java-version` with the [latest release](https://search.maven.org/search?q=g:org.apache.rocketmq%20AND%20a:rocketmq-client-java).


```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client-java</artifactId>
    <version>${rocketmq-client-java-version}</version>
</dependency>
```

3. Enter the broker container and create a Topic using mqadmin.


```shell
$ docker exec -it rmqbroker bash
$ sh mqadmin updatetopic -t TestTopic -c DefaultCluster
```

4. In the created Java project, create and run a program to send a normal message. The sample code is as follows:


```java
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientConfigurationBuilder;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.message.Message;
import org.apache.rocketmq.client.apis.producer.Producer;
import org.apache.rocketmq.client.apis.producer.SendReceipt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProducerExample {
    private static final Logger logger = LoggerFactory.getLogger(ProducerExample.class);

    public static void main(String[] args) throws ClientException {
        // Endpoint address, set to the Proxy address and port list, usually xxx:8080;xxx:8081
        String endpoint = "localhost:8081";
        // The target topic name for message sending, which needs to be created in advance.
        String topic = "TestTopic";
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        ClientConfigurationBuilder builder = ClientConfiguration.newBuilder().setEndpoints(endpoint);
        ClientConfiguration configuration = builder.build();
        // When initializing Producer, communication configuration and pre-bound Topic need to be set.
        Producer producer = provider.newProducerBuilder()
            .setTopics(topic)
            .setClientConfiguration(configuration)
            .build();
        // Sending a normal message.
        Message message = provider.newMessageBuilder()
            .setTopic(topic)
            // Set the message index key, which can be used to accurately find a specific message.
            .setKeys("messageKey")
            // Set the message Tag, used by the consumer to filter messages by specified Tag.
            .setTag("messageTag")
            // Message body
            .setBody("messageBody".getBytes())
            .build();
        try {
            // Send the message, paying attention to the sending result and catching exceptions.
            SendReceipt sendReceipt = producer.send(message);
            logger.info("Send message successfully, messageId={}", sendReceipt.getMessageId());
        } catch (ClientException e) {
            logger.error("Failed to send message", e);
        }
        // producer.close();
    }
}
```

5. In the created Java project, create and run a program to subscribe to normal messages. Apache RocketMQ supports both [SimpleConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype) and [PushConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype) types of consumers. You can choose either method to subscribe to messages.

```java
import java.io.IOException;
import java.util.Collections;
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.consumer.ConsumeResult;
import org.apache.rocketmq.client.apis.consumer.FilterExpression;
import org.apache.rocketmq.client.apis.consumer.FilterExpressionType;
import org.apache.rocketmq.client.apis.consumer.PushConsumer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PushConsumerExample {
    private static final Logger logger = LoggerFactory.getLogger(PushConsumerExample.class);

    private PushConsumerExample() {
    }

    public static void main(String[] args) throws ClientException, IOException, InterruptedException {
        final ClientServiceProvider provider = ClientServiceProvider.loadService();
        // Endpoint address, set to the Proxy address and port list, usually xxx:8080;xxx:8081
        String endpoints = "localhost:8081";
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints(endpoints)
            .build();
        // Subscription message filtering rule, indicating subscription to all Tag messages.
        String tag = "*";
        FilterExpression filterExpression = new FilterExpression(tag, FilterExpressionType.TAG);
        // Specify the consumer group the consumer belongs to, Group needs to be created in advance.
        String consumerGroup = "YourConsumerGroup";
        // Specify which target Topic to subscribe to, Topic needs to be created in advance.
        String topic = "TestTopic";
        // Initialize PushConsumer
        PushConsumer pushConsumer = provider.newPushConsumerBuilder()
            .setClientConfiguration(clientConfiguration)
            // Set the consumer group
            .setConsumerGroup(consumerGroup)
            // Set pre-bound subscription relationship
            .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
            // Set the message listener
            .setMessageListener(messageView -> {
                // Handle messages and return the consumption result
                logger.info("Consume message successfully, messageId={}", messageView.getMessageId());
                return ConsumeResult.SUCCESS;
            })
            .build();
        Thread.sleep(Long.MAX_VALUE);
        // If PushConsumer is no longer needed, this instance can be closed.
        // pushConsumer.close();
    }
}
```

<a id="quickstart-02quickstartwithdocker--6-stop-the-containers"></a>

## 6. Stop the Containers

After completing the experiment, we can stop the containers as follows.

```shell
# Stop the NameServer container docker stop rmqnamesrv

# Stop the Broker container docker stop rmqbroker
```

- [1.Pull RocketMQ Image](#quickstart-02quickstartwithdocker--1pull-rocketmq-image)
- [2.Create a Shared Network for Containers](#quickstart-02quickstartwithdocker--2create-a-shared-network-for-containers)
- [3.Start NameServer](#quickstart-02quickstartwithdocker--3start-nameserver)
- [4.Start Broker and Proxy](#quickstart-02quickstartwithdocker--4start-broker-and-proxy)
- [5.Send and Receive Messages with SDK](#quickstart-02quickstartwithdocker--5send-and-receive-messages-with-sdk)
- [6. Stop the Containers](#quickstart-02quickstartwithdocker--6-stop-the-containers)

---

<a id="quickstart-03quickstartwithdockercompose"></a>

<!-- source_url: https://rocketmq.apache.org/docs/quickStart/03quickstartWithDockercompose/ -->

<!-- page_index: 6 -->

# Run RocketMQ with Docker Compose

Version: 5.0

# Run RocketMQ with Docker Compose

This section introduces how to quickly deploy a single-node, single-replica RocketMQ service using Docker-compose and complete simple message sending and receiving.

> [!TIP]
> **System Requirements**
> 1. 64-bit operating system
> 2. 64-bit JDK 1.8+

<a id="quickstart-03quickstartwithdockercompose--1-write-docker-compose"></a>

## 1. Write docker-compose

To quickly start and run the RocketMQ cluster, you can use the following template to create a docker-compose.yml file by modifying or adding configurations in the environment section.

```text
version: '3.8'
services:
  namesrv:
    image: apache/rocketmq:5.3.2
    container_name: rmqnamesrv
    ports:
      - 9876:9876
    networks:
      - rocketmq
    command: sh mqnamesrv
  broker:
    image: apache/rocketmq:5.3.2
    container_name: rmqbroker
    ports:
      - 10909:10909
      - 10911:10911
      - 10912:10912
    environment:
      - NAMESRV_ADDR=rmqnamesrv:9876
    depends_on:
      - namesrv
    networks:
      - rocketmq
    command: sh mqbroker
  proxy:
    image: apache/rocketmq:5.3.2
    container_name: rmqproxy
    networks:
      - rocketmq
    depends_on:
      - broker
      - namesrv
    ports:
      - 8080:8080
      - 8081:8081
    restart: on-failure
    environment:
      - NAMESRV_ADDR=rmqnamesrv:9876
    command: sh mqproxy
networks:
  rocketmq:
    driver: bridge
```

<a id="quickstart-03quickstartwithdockercompose--2start-rocketmq-cluster"></a>

## 2.Start RocketMQ cluster

tart all defined services according to the docker-compose.yml file.

<div class="tabs-container tabList__CuJ"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_LNqP tabs__item--active" role="tab" tabindex="0">Linux</li><li aria-selected="false" class="tabs__item tabItem_LNqP" role="tab" tabindex="-1">Windows</li></ul><div class="margin-top--md"><div class="tabItem_Ymn6" role="tabpanel"><div class="language-code codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-code codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token plain">docker-compose up -d</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div><div class="tabItem_Ymn6" hidden="" role="tabpanel"><div class="language-code codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_biex"><pre class="prism-code language-code codeBlock_bY9V thin-scrollbar" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token plain">docker-compose -p rockermq_project up -d</span> </span></code></pre><div class="buttonGroup__atx"></div></div></div></div></div></div>
<a id="quickstart-03quickstartwithdockercompose--3send-and-receive-messages-with-sdk"></a>

## 3.Send and Receive Messages with SDK

1. After testing with tools, we can try to send and receive messages using the SDK. Here is an example of using the Java SDK for message sending and receiving. More details can be found at [rocketmq-clients](https://github.com/apache/rocketmq-clients).
2. Add the following dependency to the pom.xml file to introduce the Java dependency library, replacing `rocketmq-client-java-version` with [the latest version](https://search.maven.org/search?q=g:org.apache.rocketmq%20AND%20a:rocketmq-client-java).


```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client-java</artifactId>
    <version>${rocketmq-client-java-version}</version>
</dependency>
```

3. Enter the broker container and create a Topic using mqadmin.


```shell
$ docker exec -it rmqbroker bash
$ sh mqadmin updatetopic -t TestTopic -c DefaultCluster
```

4. In the created Java project, create and run a program to send a normal message. The sample code is as follows:


```java
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientConfigurationBuilder;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.message.Message;
import org.apache.rocketmq.client.apis.producer.Producer;
import org.apache.rocketmq.client.apis.producer.SendReceipt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProducerExample {
    private static final Logger logger = LoggerFactory.getLogger(ProducerExample.class);

    public static void main(String[] args) throws ClientException {
        // Endpoint address, set to the Proxy address and port list, usually xxx:8080;xxx:8081
        String endpoint = "localhost:8081";
        // The target Topic name for message sending, which needs to be created in advance.
        String topic = "TestTopic";
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        ClientConfigurationBuilder builder = ClientConfiguration.newBuilder().setEndpoints(endpoint);
        ClientConfiguration configuration = builder.build();
        // When initializing Producer, communication configuration and pre-bound Topic need to be set.
        Producer producer = provider.newProducerBuilder()
            .setTopics(topic)
            .setClientConfiguration(configuration)
            .build();
        // Sending a normal message.
        Message message = provider.newMessageBuilder()
            .setTopic(topic)
            // Set the message index key, which can be used to accurately find a specific message.
            .setKeys("messageKey")
            // Set the message Tag, used by the consumer to filter messages by specified Tag.
            .setTag("messageTag")
            // Message body.
            .setBody("messageBody".getBytes())
            .build();
        try {
            // Send the message, paying attention to the sending result and catching exceptions.
            SendReceipt sendReceipt = producer.send(message);
            logger.info("Send message successfully, messageId={}", sendReceipt.getMessageId());
        } catch (ClientException e) {
            logger.error("Failed to send message", e);
        }
        // producer.close();
    }
}
```

5. In the created Java project, create and run a program to subscribe to normal messages. Apache RocketMQ supports both [SimpleConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype) and [PushConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype) types of consumers. You can choose either method to subscribe to messages.

```java
import java.io.IOException;
import java.util.Collections;
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.consumer.ConsumeResult;
import org.apache.rocketmq.client.apis.consumer.FilterExpression;
import org.apache.rocketmq.client.apis.consumer.FilterExpressionType;
import org.apache.rocketmq.client.apis.consumer.PushConsumer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PushConsumerExample {
    private static final Logger logger = LoggerFactory.getLogger(PushConsumerExample.class);

    private PushConsumerExample() {
    }

    public static void main(String[] args) throws ClientException, IOException, InterruptedException {
        final ClientServiceProvider provider = ClientServiceProvider.loadService();
        // Endpoint address, set to the Proxy address and port list, usually xxx:8080;xxx:8081
        String endpoints = "localhost:8081";
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints(endpoints)
            .build();
        // Subscription message filtering rule, indicating subscription to all Tag messages.
        String tag = "*";
        FilterExpression filterExpression = new FilterExpression(tag, FilterExpressionType.TAG);
        // Specify the consumer group the consumer belongs to, Group needs to be created in advance.
        String consumerGroup = "YourConsumerGroup";
        // Specify which target Topic to subscribe to, Topic needs to be created in advance.
        String topic = "TestTopic";
        // Initialize PushConsumer
        PushConsumer pushConsumer = provider.newPushConsumerBuilder()
            .setClientConfiguration(clientConfiguration)
            // Set the consumer group.
            .setConsumerGroup(consumerGroup)
            // Set pre-bound subscription relationship.
            .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
            // Set the message listener.
            .setMessageListener(messageView -> {
                // Handle messages and return the consumption result.
                logger.info("Consume message successfully, messageId={}", messageView.getMessageId());
                return ConsumeResult.SUCCESS;
            })
            .build();
        Thread.sleep(Long.MAX_VALUE);
        // If PushConsumer is no longer needed, this instance can be closed.
        // pushConsumer.close();
    }
}
```

<a id="quickstart-03quickstartwithdockercompose--4stop-all-services"></a>

## 4.Stop all services

```shell
docker-compose down
```

- [1. Write docker-compose](#quickstart-03quickstartwithdockercompose--1-write-docker-compose)
- [2.Start RocketMQ cluster](#quickstart-03quickstartwithdockercompose--2start-rocketmq-cluster)
- [3.Send and Receive Messages with SDK](#quickstart-03quickstartwithdockercompose--3send-and-receive-messages-with-sdk)
- [4.Stop all services](#quickstart-03quickstartwithdockercompose--4stop-all-services)

---

<a id="quickstart-04quickstartwithhelminkubernetes"></a>

<!-- source_url: https://rocketmq.apache.org/docs/quickStart/04quickstartWithHelmInKubernetes/ -->

<!-- page_index: 7 -->

# Run RocketMQ with Kubernetes

Version: 5.0

# Run RocketMQ with Kubernetes

This section describes how to quickly deploy a single-node RocketMQ 5.x service in a Kubernetes and perform simple message sending and receiving.

> [!TIP]
> **SYSTEM REQUIREMENTS**
> - A running Kubernetes cluster
> - Installed Helm 3.7.0+
> - 64-bit JDK 1.8+

<a id="quickstart-04quickstartwithhelminkubernetes--1install-helm"></a>

## 1.Install Helm

Make sure Helm is installed on your system:

```bash
$ helm version
```

If Helm (version 3.7.0 or above) is not installed, you can install it using the following command:

```bash
$ curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

<a id="quickstart-04quickstartwithhelminkubernetes--2download-rocketmq-helm-chart"></a>

## 2.Download RocketMQ Helm Chart

```bash
$ helm pull oci://registry-1.docker.io/apache/rocketmq --version 0.0.1
$ tar -zxvf rocketmq-0.0.1.tgz
```

<a id="quickstart-04quickstartwithhelminkubernetes--3deploy-rocketmq"></a>

## 3.Deploy RocketMQ

Use the Helm chart to deploy RocketMQ.

```yaml
# Modify the configuration in values.yaml
$ vim values.yaml
## values.yaml, adjust memory requests and limits in broker resources according to available memory size ##
  resources:
    limits:
      cpu: 2
      memory: 10Gi
    requests:
      cpu: 2
      memory: 10Gi
##values.yaml##
```

```bash
$ helm install rocketmq-demo ./rocketmq
# Check pod status
# If the parameters are normal, it indicates successful deployment
$ kubectl get pods -o wide -n default NAME READY STATUS RESTARTS AGE IP NODE NOMINATED NODE READINESS GATES rocketmq-demo-broker-0 1/1 Running 0 6h3m 192.168.58.225 k8s-node02 <none> <none> rocketmq-demo-nameserver-757877747b-k669k 1/1 Running 0 6h3m 192.168.58.226 k8s-node02 <none> <none> rocketmq-demo-proxy-6c569bd457-wcg6g 1/1 Running 0 6h3m 192.168.85.227 k8s-node01 <none> <none>
```

<a id="quickstart-04quickstartwithhelminkubernetes--4validate-message-sending-and-receiving"></a>

## 4.Validate Message Sending and Receiving

Use the JAVA SDK to test message sending and receiving (since the local network and the k8s network are not on the same internal network, you need to package the project locally and run it remotely. After packaging, copy the jar file from the target directory to the target server and execute java -jar jar file name). The specifics are as follows:

1）Create a Java project in IDE.

2）Add the following dependency to the pom.xml file to import the Java library:

```xml
 ......
    <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-client-java</artifactId>
            <version>5.0.7</version>
      </dependency>
    .....
```

3）Log into the pod (management tools are needed), or it can also be executed on the host

```bash
# Log into the pod
$ kubectl exec -ti rocketmq-demo-broker-0  -- /bin/bash

# Create Topic using mqadmin tools
$ sh mqadmin updatetopic  -t TestTopic -c DefaultCluster

# Create subscription group using mqadmin tools
$ sh mqadmin updateSubGroup -c DefaultCluster -g TestGroup
```

4）In the created Java project, create a program to send normal messages (ProducerDemo.java); the sample code is as follows:

```java
package com.rocketmq.producer;

import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientConfigurationBuilder;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.message.Message;
import org.apache.rocketmq.client.apis.producer.Producer;
import org.apache.rocketmq.client.apis.producer.SendReceipt;

public class ProducerDemo {
    public static void main(String[] args) throws ClientException {
        // The endpoint address, which needs to be set to the address and port list of the Proxy; the following is the proxy address in the k8s environment.
        String endpoint = "192.168.85.227:8081";
        // The target Topic name for sending messages, which needs to be created in advance.
        String topic = "TestTopic";
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        ClientConfigurationBuilder builder = ClientConfiguration.newBuilder().setEndpoints(endpoint);
        ClientConfiguration configuration = builder.build();
        // When initializing the Producer, communication configuration and pre-bound Topic need to be set.
        Producer producer = provider.newProducerBuilder()
            .setTopics(topic)
            .setClientConfiguration(configuration)
            .build();
        // Sending normal messages.
        Message message = provider.newMessageBuilder()
            .setTopic(topic)
            // Set message index key for precise search of a specific message.
            .setKeys("messageKey")
            // Set message Tag for filtering messages based on specific tags on the consumer side.
            .setTag("messageTag")
            // Message body.
            .setBody("messageBody".getBytes())
            .build();
        try {
            // Send the message, you need to pay attention to the sending result and handle failures and other exceptions.
            SendReceipt sendReceipt = producer.send(message);
            System.out.println("Send message successfully, messageId=" + sendReceipt.getMessageId());
        } catch (ClientException e) {
        }
        // producer.close();
    }
}
```

5）In the created Java project, create a program to subscribe to normal messages (Consumer.java). Apache RocketMQ supports [SimpleConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype) and [PushConsumer](https://rocketmq.apache.org/zh/docs/featureBehavior/06consumertype), here we use the PushConsumer.

```java
package com.rocketmq.consumer;

import java.io.IOException;
import java.util.Collections;
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientException;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.consumer.ConsumeResult;
import org.apache.rocketmq.client.apis.consumer.FilterExpression;
import org.apache.rocketmq.client.apis.consumer.FilterExpressionType;
import org.apache.rocketmq.client.apis.consumer.PushConsumer;
import java.util.List;

public class Consumer {
    public static void main(String[] args) throws ClientException, IOException, InterruptedException {
        final ClientServiceProvider provider = ClientServiceProvider.loadService();
        // The endpoint address, which needs to be set to the address and port list of the Proxy; the following is the proxy address in the k8s environment.
        String endpoints = "192.168.85.227:8081";
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints(endpoints)
            .build();
        // The filter rule for subscribing to messages, indicating subscription to messages of all Tags.
        String tag = "*";
        FilterExpression filterExpression = new FilterExpression(tag, FilterExpressionType.TAG);
        // Specify the consumer group to which the consumer belongs; the Group needs to be created in advance.
        String consumerGroup = "TestGroup";
        // Specify which target Topic needs to be subscribed to; the Topic needs to be created in advance.
        String topic = "TestTopic";
        // Initialize PushConsumer, binding to the consumer group ConsumerGroup, communication parameters, and subscription relationship.
        PushConsumer pushConsumer = provider.newPushConsumerBuilder()
            .setClientConfiguration(clientConfiguration)
            // Set consumer group.
            .setConsumerGroup(consumerGroup)
            // Set pre-bound subscription relationship.
            .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
            // Set consumption listener.
            .setMessageListener(messageView -> {
                // Process the message and return the consumption result.
                System.out.println("Consume message successfully, messageId=" + messageView.getMessageId());
                return ConsumeResult.SUCCESS;
            })
            .build();
        Thread.sleep(Long.MAX_VALUE);
        // If you don't need to use PushConsumer anymore, you can close this instance.
        // pushConsumer.close();
    }
}
```

<a id="quickstart-04quickstartwithhelminkubernetes--5release-rocketmq-resources"></a>

## 5.Release RocketMQ Resources

```bash
#Release all RocketMQ resources
$ helm uninstall rocketmq-demo
```

- [1.Install Helm](#quickstart-04quickstartwithhelminkubernetes--1install-helm)
- [2.Download RocketMQ Helm Chart](#quickstart-04quickstartwithhelminkubernetes--2download-rocketmq-helm-chart)
- [3.Deploy RocketMQ](#quickstart-04quickstartwithhelminkubernetes--3deploy-rocketmq)
- [4.Validate Message Sending and Receiving](#quickstart-04quickstartwithhelminkubernetes--4validate-message-sending-and-receiving)
- [5.Release RocketMQ Resources](#quickstart-04quickstartwithhelminkubernetes--5release-rocketmq-resources)

---

<a id="domainmodel-01main"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/01main/ -->

<!-- page_index: 8 -->

# Domain Model

Version: 5.0

# Domain Model

This section describes the domain model of Apache RocketMQ.

Apache RocketMQ is a distributed middleware service that adopts an asynchronous communication model and a publish/subscribe message transmission model.

For more information about the communication model and transmission model, see **Communication model** and **Message transmission model**.

The asynchronous communication model of Apache RocketMQ features simple system topology and weak upstream-downstream coupling. Apache RocketMQ is used in asynchronous decoupling and load shifting scenarios.

<a id="domainmodel-01main--domain-model-of-apache-rocketmq"></a>

## Domain model of Apache RocketMQ

![领域模型](assets/images/mainarchi-9b036e7ff5133d050950f25838367a17_07cbfe5e9f5cbcdd.png)

As shown in the preceding figure, the lifecycle of a Apache RocketMQ message consists of three stages: production, storage, and consumption.

A producer generates a message and sends it to a Apache RocketMQ broker. The message is stored in a topic on the broker. A consumer subscribes to the topic to consume the message.

**Message production**

[Producer](#domainmodel-04producer)：

The running entity that is used to generate messages in Apache RocketMQ. Producers are the upstream parts of business call links. Producers are lightweight, anonymous, and do not have identities.

**Message storage**

- [Topic](#domainmodel-02topic)：

  The grouping container that is used for message transmission and storage in Apache RocketMQ. A topic consists of multiple message queues, which are used to store messages and scale out the topic.
- [MessageQueue](#domainmodel-03messagequeue)：

  The unit container that is used for message transmission and storage in Apache RocketMQ. Message queues are similar to partitions in Kafka. Apache RocketMQ stores messages in a streaming manner based on an infinite queue structure. Messages are stored in order in a queue.
- [Message](#domainmodel-04message)：

  The minimum unit of data transmission in Apache RocketMQ. Messages are immutable after they are initialized and stored.

**Message consumption**

- [ConsumerGroup](#domainmodel-07consumergroup)：

  An independent group of consumption identities defined in the publish/subscribe model of Apache RocketMQ. A consumer group is used to centrally manage consumers that run at the bottom layer. Consumers in the same group must maintain the same consumption logic and configurations with each other, and consume the messages subscribed by the group together to scale out the consumption capacity of the group.
- [Consumer](#domainmodel-08consumer)：

  The running entity that is used to consume messages in Apache RocketMQ. Consumers are the downstream parts of business call links, A consumer must belong to a specific consumer group.
- [Subscription](#domainmodel-09subscription)：

  The collection of configurations in the publish/subscribe model of Apache RocketMQ. The configurations include message filtering, retry, and consumer progress Subscriptions are managed at the consumer group level. You use consumer groups to specify subscriptions to manage how consumers in the group filter messages, retry consumption, and restore a consumer offset.

  The configurations in a Apache RocketMQ subscription are all persistent, except for filter expressions. Subscriptions are unchanged regardless of whether the broker restarts or the connection is closed.

<a id="domainmodel-01main--communication-model"></a>

## Communication model

According to the concept of distributed system architecture, a complex system can be split into multiple independent modules, such as microservice modules. Remote communication between the modules must be ensured in the system. There are two typical communication models for this purpose: RPC-based synchronous communication model and middleware-based asynchronous communication model.

RPC-based synchronous model

![Synchronous invocation](assets/images/syncarchi-ebbd41e1afd6adf432792ee2d7a91748_6e45f47e76c84d70.png)

In this model, remote systems communicate with each other directly. Each request is sent directly from the caller to the callee, and the callee returns the call result immediately to the caller.
**Notice** The word "synchronous" does not refer to the mode of the programming interface. RPC also supports the programming mode of asynchronous non-blocking calls, in which case the caller still expects a direct response from the callee within a specified period.

Asynchronous communication model
![Asynchronous invocation](assets/images/asyncarchi-e7ee18dd77aca472fb80bb2238d9528b_fbdf9f3fdb8d5273.png)

In this model, subsystems are not connected in a tightly coupled manner. The caller needs only to convert a request into an asynchronous event, or message, and send it to the agent. As long as the message is sent, the call is considered complete. The agent delivers the message to the called downstream subsystem and ensures that the task is accomplished. The role of agent is typically assumed by a message middleware.

Asynchronous communication provides the following benefits:

- Simple system topology. Because the caller and callee both communicate only with the agent, the system works in a star structure that is easy to maintain and manage.

- Weak upstream and downstream coupling. Weak coupling enables the system structure to be more flexible. The agent performs buffering and asynchronous recovery. Systems deployed at the upstream and downstream can be upgraded and changed independently without affecting each other.

- Load shifting. Message-oriented agents typically provide a large traffic buffer and powerful traffic shaping capability. This prevents traffic peaks from drowning downstream systems.

<a id="domainmodel-01main--message-transmission-model"></a>

## Message transmission model

Message middleware services have two common transmission models: the point-to-point model and the publish/subscribe model.

Point-to-point model
![Point-to-point model](assets/images/p2pmode-fefdc2fbe4792e757e26befc0b3acbff_edbb82ed368b6c1f.png)

The point-to-point model, also known as the queue model, has the following characteristics:

- Consumer anonymity: The queue is the only identity used during upstream-downstream communication. Downstream consumers cannot declare an identity when they obtain messages from the queue.
- One-to-one communication: Consumers do not have identities. All consumers in a consumer group consume the subscribed messages together. Each message can be consumed only by one specific consumer. For this reason, this model supports only one-to-one communication.

Publish/subscribe model
![Publish/subscribe model](assets/images/pubsub-042a4e5e5d76806943bd7dcfb730c5d5_fdfc5d02d6a9384b.png)

This model has the following characteristics:

- Independent consumption: In this model, consumers use the identity of a consumer group, or a subscription, to receive and consume messages. Consumer groups are independent of each other.
- One-to-many communication: Based on the design of independent identity, this model allows a topic to be subscribed to by multiple consumer groups, each having full access to all the messages. Therefore, the publish/subscribe model supports one-to-many communication.

Comparison between transmission models

The point-to-point model is simpler in structure, while the publish/subscribe model offers better scalability. Apache RocketMQ uses and has the same high scalability as the publish/subscribe model.

- [Domain model of Apache RocketMQ](#domainmodel-01main--domain-model-of-apache-rocketmq)
- [Communication model](#domainmodel-01main--communication-model)
- [Message transmission model](#domainmodel-01main--message-transmission-model)

---

<a id="domainmodel-02topic"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/02topic/ -->

<!-- page_index: 9 -->

# Topic

Version: 5.0

# Topic

This section describes the definition, model relationship, internal attributes, and behavior constraints of topics in Apache RocketMQ. This topic also provides version compatibility information and usage notes for topics.

<a id="domainmodel-02topic--definition"></a>

## Definition

A topic is logically a collection of queues; we may publish messages to or receive from it.

Topics provide the following benefits:

- **Message categorization and message isolation**: When you create a messaging service based on Apache RocketMQ, we recommend that you use different topics to manage messages of different business types for isolated storage and subscription.

- **Identity and permission management**: Messages in Apache RocketMQ are anonymous. You can use a topic to perform identity and permission management for messages of a specific category.

<a id="domainmodel-02topic--model-relationship"></a>

## Model relationship

The following figure shows the position of a topic in the domain model of Apache RocketMQ.
![Topic](assets/images/archifortopic-ef512066703a22865613ea9216c4c300_ae8b47ff036119e0.png)

In Apache RocketMQ, a topic is a top-level storage container in which all message resources are defined. A topic is a logical concept and not the actual unit that stores messages.

A topic contains one or more queues. Message storage and scalability are implemented based on queues. All constraints and attribute settings for a topic are implemented based on the queues in the topic.

<a id="domainmodel-02topic--internal-attributes"></a>

## Internal attributes

**Topic name**

- Definition: the name of a topic. A topic name identifies the topic and is globally unique in a cluster.
- Value: A topic name is specified by the user when a topic is created.
- Constraint: See [Parameter limits](#introduction-03limits).

**Queues**

- Definition: the actual storage unit that stores messages. A topic contains one or more queues. For more information, see [Message queues](#domainmodel-03messagequeue).
- Value: You can specify the number of queues when you create a topic. Apache RocketMQ allocates the specified number of queues to the topic.
- Constraint: A topic must contain at least one queue.

**Message type**

- Definition: the message type that is specified for a topic.
- Value: When you create a topic in Apache RocketMQ, select one of the following message types for the topic:

  - Normal: [Normal messages](#featurebehavior-01normalmessage). A normal message does not require special semantics and is not correlated with other normal messages.
  - FIFO: [Fifo messages](#featurebehavior-03fifomessage). Apache RocketMQ uses a message group to determine the order of a specified set of messages. The messages are delivered in the order in which they are sent.
  - Delay: [Delayed messages](#featurebehavior-02delaymessage). You can specify a delay to make messages available to consumers only after the delay has elapsed, instead of delivering messages immediately when they are produced.
  - Transaction: [Transaction messages](#featurebehavior-04transactionmessage). Apache RocketMQ supports distributed transaction messages and ensures transaction consistency of database updates and message calls.
- Constraint: Starting from version 5.0, Apache RocketMQ supports enforcing the validation of message types, that is, each topic only allows messages of a single type to be sent. This can better facilitate operation and management of production systems and avoid confusion. However, to ensure backward compatibility with version 4.x, the validation feature is enable by default.

<a id="domainmodel-02topic--behavior-constraints"></a>

## Behavior constraints

**Forced message type verification**

Apache RocketMQ version 5.x allows you to specify a message type for a topic. This way, you can manage and process messages of the specified type in a separate topic. Apache RocketMQ forcibly verifies the type of messages that are sent and the message type of the topic to which the messages are sent. If message type verification fails, message delivery requests are rejected, and a type mismatch error is returned. The following verification rules apply:

- Consistent message types. The messages that you want to send must use the same message type as the message type that is specified for the topic to which you want to send the messages.
- Only one type of messages sent to a topic. The messages that you want to send to a topic must use the same message type. Only one message type can be specified for a topic.

> [!INFO]
> To ensure backward compatibility with version 4.x, the above validation feature is disabled by default. It is recommended to enable the validation by using the server parameter "enableTopicMessageTypeCheck".

**Examples of common usage errors**

- Send messages that do not match the message type of a topicFor example, a request that is initiated to send Transaction messages to a topic that uses the FIFO message type is rejected, and a type mismatch error is returned.
- Send messages of different types to a topicFor example, a request that is initiated to send normal messages and fifo messages to a topic that uses the Normal message type is rejected, and a type mismatch error is returned.

<a id="domainmodel-02topic--version-compatibility"></a>

## Version compatibility

Forced message type verification is available only in Apache RocketMQ version 5.x. The SDKs of Apache RocketMQ versions 4.x and 3.x do not support forced message type verification. If you use version 4.x or 3.x, make sure that message types are consistent.

We recommend that you use Apache RocketMQ version 5.x.

<a id="domainmodel-02topic--usage-example"></a>

## Usage Example

For creating topics in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that message type needs to be added as a property parameter. The following is an example:

```shell
sh mqadmin updateTopic -n <nameserver_address> -t <topic_name> -c <cluster_name> -a +message.type=<message_type>
```

Among these, the message\_type parameter can be set as Normal/FIFO/Delay/Transaction based on the message type. If it is not specified, it defaults to the Normal type.

<a id="domainmodel-02topic--usage-notes"></a>

## Usage notes

**Plan topics based on your business requirements**

We recommend that you use a topic to process messages that are produced for the same business module of a business aspect when you plan topics in Apache RocketMQ. Take note of the following factors when you plan topics:

- Message types: Use different topics to store messages of different types. For example, you can create two topics to separately store fifo messages and normal messages.
- Message correlation: Use separate topics to store messages that are not directly correlated. For example, create two topics for Taobao transaction messages and Freshippo logistics messages, which are not correlated. If the messages are directly correlated, you can use the same topic. For example, you can create one topic for order messages that are produced for the men's clothing category and women's clothing category on Taobao. If the business volume or submodules require more fine-grained topics, you can also use different topics for messages that can be classified into one topic.
- Message volume and timeliness: Use different topics to process messages that have differences in volume or timeliness. For example, do not use the same topic for one business that generates a small number of time-sensitive messages and another business that generates trillions of messages. This prevents time-sensitive messages from waiting too long for consumption.

**Example of correct topic planning:** In e-commerce scenarios, you can use a topic for order-related messages, such as order creation, payment, and canceling, a topic for logistics messages, and another topic for reward point-related messages.

**Examples of incorrect topic planning:**

- Excessively coarse granularity: causes poor isolation. This does not facilitate independent O\&M and fault handling. An example of this incorrect topic planning practice is to use the same topic for all transaction messages and logistics messages.
- Excessively fine granularity: consumes a large number of topic resources and increases the system load. An example of this incorrect topic planning practice is to use a separate topic for messages that are produced for each user.

**Use a topic to send and receive messages of the same type**

Topic-based business isolation is a design principle of Apache RocketMQ. We recommend that you use different topics for messages that use different business logic. A specific topic must send or receive the same type of messages.

**Avoid automated management of topics**

Topics in Apache RocketMQ are top-level resources and containers that provide separate permission management, observability metrics collection, and monitoring capabilities. System resources are required to create and manage topics. We recommend that you add, delete, modify, or query topics in a production environment only when the operation is required.

Although Apache RocketMQ provides automatic topic creation, we recommend that you use the feature only in a test environment. If you use the feature in a production environment, a large number of unnecessary topics may be generated. This hinders topic management and consumes additional system resources.

- [Definition](#domainmodel-02topic--definition)
- [Model relationship](#domainmodel-02topic--model-relationship)
- [Internal attributes](#domainmodel-02topic--internal-attributes)
- [Behavior constraints](#domainmodel-02topic--behavior-constraints)
- [Version compatibility](#domainmodel-02topic--version-compatibility)
- [Usage Example](#domainmodel-02topic--usage-example)
- [Usage notes](#domainmodel-02topic--usage-notes)

---

<a id="domainmodel-03messagequeue"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/03messagequeue/ -->

<!-- page_index: 10 -->

# Message Queue

Version: 5.0

# Message Queue

This section describes the definition, model relationship, and internal attributes of message queues in Apache RocketMQ. This topic also provides version compatibility information and usage notes for message queues.

<a id="domainmodel-03messagequeue--definition"></a>

## Definition

A queue is a container that is used to store and transmit messages in Apache RocketMQ. A queue is the smallest unit of storage for Apache RocketMQ messages.

A topic in Apache RocketMQ consists of multiple queues. This way, queues support horizontal partitioning and streaming storage.

Queues provide the following benefits:

- Ordered Storage Queues are ordered in nature: Messages are stored in the same order in which they are queued. The earliest message is at the start of the queue and the latest message is at the end of the queue. Offsets are used to label the locations and the order of messages in a queue.
- Streaming Operation Semantics: The queue-based storage in Apache RocketMQ allows consumers to read one or more messages from an offset. This helps implement features such as aggregate read and backtrack read. These features are not available in RabbitMQ or ActiveMQ.

<a id="domainmodel-03messagequeue--model-relationship"></a>

## Model relationship

The following figure shows the position of queues in the domain model of Apache RocketMQ.![队列](assets/images/archiforqueue-dd6788b33bf2fc96b4a1dab83a1b0d71_be0579fbfb153f91.png)

By default, Apache RocketMQ provides reliable message storage. All messages that are successfully delivered are persistently stored in queues. Messages are sent by the producer and received by the consumer client. Each message can be successfully delivered at least once.

The queue model of Apache RocketMQ is similar to the partition model of Kafka. In Apache RocketMQ, a queue is part of a topic. Messages are operated in queues even though they are managed by topic. For example, when a producer sends a message to a specific topic, the message is sent to a queue in the topic.

You can change the number of queues in Apache RocketMQ to scale out or scale in.

<a id="domainmodel-03messagequeue--internal-attributes"></a>

## Internal attributes

Read and write permissions

- Definition: whether data can be read from or written to the current queue.
- Values: defined by the broker. The following describes the enumerations:

  - 6: read and write. Messages can be written to and read from the current queue.
  - 4: read-only. Messages can be read from but not written to the current queue.
  - 2: write-only. Messages can be written to but not read from the current queue.
  - 0: The read or write status is unavailable. The current queue does not allow read or write operations.

- Constraint: The read and write permissions are related to O\&M operations. We recommend that you do not frequently modify the permissions.

<a id="domainmodel-03messagequeue--behavior-constraints"></a>

## Behavior constraints

Each topic consists of one or more queues that are used to store messages. The number of queues in each topic is related to the message type and the region where the instance resides. The number of queues cannot be changed.

<a id="domainmodel-03messagequeue--version-compatibility"></a>

## Version compatibility

Queue names vary based on the versions of Apache RocketMQ brokers. The following describes the differences:

- Broker versions 3.x and 4.x: A queue name consists of the topic name, broker ID, and queue ID, and is bound to physical nodes.
- Broker versions 5.x: A queue name is a globally unique string that is assigned by the cluster, and is decoupled from physical nodes.

We recommend that you do not construct queue names or bind them to other operations. Otherwise, the queue names may fail to be resolved when the broker is updated.

<a id="domainmodel-03messagequeue--usage-notes"></a>

## Usage notes

**Queue number setting**

You can specify the number of queues in Apache RocketMQ when you create or change a topic. We recommend that you configure a small number of queues and avoid adding queues that you do not require.

The following describes the issues that occur due to a large number of queues in a topic:

- **Increase in the volume of metadata in a cluster** Apache RocketMQ collects metrics and monitors data based on queues. A large number of queues may cause the volume of metadata to increase.

- **Overloaded client** Message reads and writes in Apache RocketMQ are performed based on queues. A large number of queues may generate empty polling requests that increase system load.

**Scenarios for adding queues**

- Load balancing of physical nodes

  Queues of each topic in Apache RocketMQ can be distributed to different service nodes. To ensure the load balancing of cluster traffic after the cluster is scaled out, we recommend that you add queues or migrate previous queues to the new service nodes.

- Performance bottleneck issue related to fifo messages

  In Apache RocketMQ broker versions 4.x, fifo messages take effect in only queues. As a result, the concurrency of fifo messages is based on the number of queues. We recommend that you increase the number of queues when a performance bottleneck issue occurs in the system.

- [Definition](#domainmodel-03messagequeue--definition)
- [Model relationship](#domainmodel-03messagequeue--model-relationship)
- [Internal attributes](#domainmodel-03messagequeue--internal-attributes)
- [Behavior constraints](#domainmodel-03messagequeue--behavior-constraints)
- [Version compatibility](#domainmodel-03messagequeue--version-compatibility)
- [Usage notes](#domainmodel-03messagequeue--usage-notes)

---

<a id="domainmodel-04message"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/04message/ -->

<!-- page_index: 11 -->

# Message

Version: 5.0

# Message

This section describes the definition, model relationship, internal attributes, and behavior constraints of messages in Apache RocketMQ. This topic also provides usage notes for messages.

<a id="domainmodel-04message--definition"></a>

## Definition

A message is the smallest unit of data transmission in Apache RocketMQ. A producer encapsulates the load and extended attributes of business data into messages and sends the messages to a Apache RocketMQ broker. Then, the broker delivers the messages to the consumer based on the relevant semantics.

The characteristics of the message model in Apache RocketMQ are:

- **Immutability**: A message is an event that is generated. After the message is generated, the content of the message does not change. Even if the message passes through a transmission channel, the content of the message remains the same. The messages that consumers obtain are read-only messages.

- **Persistence**: By default, Apache RocketMQ persists messages. The received messages are stored in the storage file of the Apache RocketMQ broker to ensure that the messages can be traced and restored if system failures occur.

<a id="domainmodel-04message--model-relationship"></a>

## Model relationship

The following figure shows the position of messages in the domain model of Apache RocketMQ.![消息](assets/images/archiforqueue-dd6788b33bf2fc96b4a1dab83a1b0d71_be0579fbfb153f91.png)

1. Messages are initialized by producers and are sent to the Apache RocketMQ broker.
2. Messages are stored in queues in the order in which the messages are received on the Apache RocketMQ broker.
3. Consumers obtain and consume messages from the Apache RocketMQ broker based on the specified subscriptions.

<a id="domainmodel-04message--internal-attributes"></a>

## Internal attributes

**System retention attributes**

**Topic name**

- Definition: the name of the topic to which a message belongs. The topic name is globally unique in a cluster. For more information, see [Topic](#domainmodel-02topic).
- Values: obtained from the SDK of the client.

**Message type**

- Definition: the type of a message.
- Values: obtained from the SDK of the client. Apache RocketMQ supports the following message types:

  - Normal: [Normal messages](#featurebehavior-01normalmessage). A normal message does not require special semantics and is not correlated with other normal messages.
  - FIFO: [Fifo messages](#featurebehavior-03fifomessage). Apache RocketMQ uses a message group to determine the order of a specified set of messages. The messages are delivered in the order in which they are sent.
  - Delay: [Delayed messages](#featurebehavior-02delaymessage). You can specify a delay to make messages available to consumers only after the delay has elapsed, instead of delivering messages immediately when they are produced.
  - Transaction: [Transaction messages](#featurebehavior-04transactionmessage). Apache RocketMQ supports distributed transaction messages and ensures transaction consistency of database updates and message calls.

**Message queue**

- Definition: the queue to which a message belongs. For more information, see [Message queues](#domainmodel-03messagequeue).
- Values: specified and populated by the broker.

**Message offset**

- Definition: the location where the current message is stored in the queue. For more information, see [Working mechanism](#featurebehavior-09consumerprogress).
- Values: specified and populated by the broker. Valid values: 0 to Long.Max.

**Message ID**

- Definition: the unique identifier of a message. The ID of each message is globally unique in the cluster.
- Values: automatically generated by the producer client. A message ID is a string of 32 characters that consists of digits and uppercase letters.

**(Optional) Message keys**

- Definition: the list of index keys for messages. You can configure different keys to distinguish between messages and quickly find messages.
- Values: defined by the producer client.

**(Optional) Message tag**

- Definition: the tag that is used to filter messages. Consumers can filter messages by tags and receive only messages that contain specified tags.
- Values: defined by the producer client.
- Constraint: Only one tag can be specified for each message.

**(Optional) Scheduled time**

- Definition: the millisecond-level timestamp that is used when a message triggers delayed delivery in a scheduled time scenario. For more information, see [Delayed messages](#featurebehavior-02delaymessage).
- Values: defined by the message producer.
- Constraint: The maximum duration is 40 days.

**Message sending time**

- Definition: the local millisecond-level timestamp of the producer client when the message is sent.
- Values: populated by the producer client.
- Note: The client time may be different from the broker time. In this case, the message sending time is based on the client time.

**Message store timestamp**

- Definition: the local millisecond-level timestamp of the Apache RocketMQ broker when the message is stored.

  For delay messages and transaction messages, the message retention time is the broker time that is displayed for the consumer when the message takes effect.
- Values: populated by the broker.
- Note: The client time may be different from the broker time. In this case, the message retention time is based on the broker time.

**Retry times**

- Definition: the number of times that the Apache RocketMQ broker redelivers a message after the message fails to be consumed. After each retry, the maximum number of retries is increased by one. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).
- Values: labeled by the broker. The first time that a message is consumed, the number of retries is zero. The first time that a message fails to be consumed, the number of retries is one.

**Custom attributes for messages**

**Custom attributes**

- Definition: the extended information that can be specified by the producer.
- Values: specified by the producer based on key-value pairs from a string.

**Message load**

- Definition: the actual message data of the service message.
- Values: serialized by the producer and transmitted in binary bytes.
- Constraints: see [Parameter limits](#introduction-03limits).

<a id="domainmodel-04message--behavior-constraints"></a>

## Behavior constraints

The size of a message cannot exceed the upper limit. If the size of a message exceeds the corresponding upper limit, the message fails to be sent.

The following describes the default limits for messages:

- max size of message: 4 MB

<a id="domainmodel-04message--usage-notes"></a>

## Usage notes

**Overloaded transmission is not recommended for a single message.**

Apache RocketMQ is a messaging middleware that transmits data for business events. If the size of a message is large, the network transmission layer may be overloaded. This affects retries upon errors and throttling. We recommend that you limit the data size of a single message event.

If an overloaded transmission is required in the production environment, we recommend that you split the message based on a fixed size or use the file storage method.

**Immutability of messages**

Messages cannot be modified in Apache RocketMQ broker versions 5.x and the messages that consumers obtain are read-only messages. No strong constraints related to immutability are imposed on versions 3.x and 4.x. We recommend that you re-initialize messages if you want to transmit messages.

- Correct example:


```java
Message m = Consumer.receive();
Message m2= MessageBuilder.buildFrom(m);
Producer.send(m2);
```

- Incorrect example：


```java
Message m = Consumer.receive();
m.update()；
Producer.send(m);
```

- [Definition](#domainmodel-04message--definition)
- [Model relationship](#domainmodel-04message--model-relationship)
- [Internal attributes](#domainmodel-04message--internal-attributes)
- [Behavior constraints](#domainmodel-04message--behavior-constraints)
- [Usage notes](#domainmodel-04message--usage-notes)

---

<a id="domainmodel-04producer"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/04producer/ -->

<!-- page_index: 12 -->

# Producer

Version: 5.0

# Producer

This section describes the concept of producers in Apache RocketMQ. It also describes the role of producers in the messaging model, producer attributes and compatibility, and some usage notes of working with producers.

<a id="domainmodel-04producer--definition"></a>

## Definition

A producer in Apache RocketMQ is a functional messaging entity that creates messages and sends them to the server.

A producer is typically integrated on the business system and serves to encapsulate data as messages in Apache RocketMQ and send the messages to the server. For more information about messages, see [Messages](#domainmodel-04message).

The following message delivery elements are defined on the producer side:

- Transmission mode: A producer can specify the message transmission mode in an API operation. Apache RocketMQ supports synchronous transmission and asynchronous transmission.
- Batch transmission: A producer can specify batch transmission in an API operation. For example, the number or size of messages sent at a time can be specified.
- Transactional behavior: Apache RocketMQ supports transaction messages. Producers are involved in transaction checks to ensure eventual consistency of transactions. For more information, see [Transactional messages](#featurebehavior-04transactionmessage).

Producers and topics have an n-to-n relationship. A producer can send messages to multiple topics, and a topic can receive messages from multiple producers. This many-to-many relationship facilitates performance scaling and disaster recovery.
![Producers and topics](assets/images/producer-topic-f9a6348396228a2976e34a5ad0774314_638b71480e9aab83.png)

<a id="domainmodel-04producer--model-relationship"></a>

## Model relationship

The following figure shows the role of producers in the messaging model of Apache RocketMQ.![Producer](assets/images/archiforproducer-ebb8ff832f6e857cbebc2c17c2044a3b_a60bb9728fb449b6.png)

1. The message is initialized by the producer and sent to the Apache RocketMQ server.
2. Messages are stored in the specified queue of the topic in the order in which they arrive at the Apache RocketMQ server.
3. The consumer obtains and consumes messages from the Apache RocketMQ server based on the specified subscription relationship.

<a id="domainmodel-04producer--internal-attributes"></a>

## Internal attributes

**Client ID**

- Definition: the identity of a producer client. This attribute is used to distinguish between different producers. A client ID is globally unique within a cluster.
- Value: The client ID is automatically generated by Apache RocketMQ SDKs. It is mainly used for O\&M purposes such as log viewing and problem locating. The client ID cannot be modified.

**Communication parameters**

- **(Required)** : the endpoint used to connect to the server. This endpoint is used to identify the cluster.

  The access point must be configured in the format. We recommend that you use domain names to avoid using IP addresses to prevent node changes from failing to perform hotspot migration.

- **(Optional)** : the credential used by the client for authentication.

  Transmission is required only when identity recognition and authentication are enabled on the server.

- Request Timeout **(Optional)** : the timeout period of the network request. For more information about the value range and default value, see [Parameter limits](#introduction-03limits).

**Prebound topic list**

- Definition: the list of topics to which a producer of Apache RocketMQ sends messages. Prebound topics provide the following benefits:

  - Transaction messages **(Required)**: The prebound topic list attribute must be specified for transaction messages. In transaction messaging scenarios, when a producer recovers from a fault or is restarted, the producer checks whether a transaction message topic contains uncommitted transaction messages. This prevents latency caused by uncommitted transaction messages in the topic after the producer sends new messages to the topic.
  - Non-transaction messages **(Optional)**: The server checks the access permissions and validity of the destination topics based on the list of prebound topics during producer initialization, instead of performing the check after the application is started. We recommend that you specify the prebound topic list attribute for non-transaction messages.

    If the prebound topic list attribute is not specified for non-transaction messages or destination topics are changed, Apache RocketMQ dynamically checks and identifies destination topics.
- Limit: For transaction messages, prebound topics must be specified and used together with a transaction checker.

**Transaction checker**

- Apache RocketMQ uses a transaction messaging mechanism that requires a producer to implement a transaction checker to ensure eventual consistency of transactions. For more information, see [Transaction messages](#featurebehavior-04transactionmessage).
- When a producer sends transaction messages, a transaction checker must be configured and used together with prebound topics.

**Send retry policy**

Send retry policy specifies how a producer retries the delivery of messages upon a failed message delivery attempt. For more information, see [Message sending retry](#featurebehavior-05sendretrypolicy).

<a id="domainmodel-04producer--version-compatibility"></a>

## Version compatibility

Starting from Apache RocketMQ version 5.x, producers are anonymous, and producer groups are discontinued. For Apache RocketMQ version 3.x and version 4.x, existing producer groups can be discontinued, without affecting your business.

<a id="domainmodel-04producer--usage-notes"></a>

## Usage notes

**We recommend that you limit the number of producers on individual processes.**

In Apache RocketMQ, producers and topics provide a many-to-many form of communication. A single producer can send messages to multiple topics. We recommend that you create and initialize the minimum number of producers that your business scenarios require, and reuse as many producers as you can. For example, in a scenario that requires message delivery to multiple topics, you do not need to create a producer for each topic.

**We recommend that you do not create and destroy producers on a regular basis.**

The producers of Apache RocketMQ are underlying resources that can be reused, like the connection pool of a database. You do not need to create producers each time you send messages or destroy the producers after you send messages. If you regularly create and destroy producers, a large number of short connection requests are generated on the broker. This imposes a high level of load on your system.

- Example of correct usage


```java
  Producer p = ProducerBuilder.build();
  for (int i =0;i<n;i++)
  {
    Message m= MessageBuilder.build();
    p.send(m);
  }
  p.shutdown();
```

- Example of incorrect usage


```java
  for (int i =0;i<n;i++)
  {
    Producer p = ProducerBuilder.build();
    Message m= MessageBuilder.build();
    p.send(m);
    p.shutdown();
  }
```

- [Definition](#domainmodel-04producer--definition)
- [Model relationship](#domainmodel-04producer--model-relationship)
- [Internal attributes](#domainmodel-04producer--internal-attributes)
- [Version compatibility](#domainmodel-04producer--version-compatibility)
- [Usage notes](#domainmodel-04producer--usage-notes)

---

<a id="domainmodel-07consumergroup"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/07consumergroup/ -->

<!-- page_index: 13 -->

# Consumer Group

Version: 5.0

# Consumer Group

This section describes the definition, model relationship, internal attributes, and behavior constraints of consumer groups in Apache RocketMQ. This topic also provides version compatibility information and usage notes for consumer groups.

<a id="domainmodel-07consumergroup--definition"></a>

## Definition

A consumer group is a load balancing group that contains consumers that use the same consumption behaviors in Apache RocketMQ.

Unlike consumers that are running entities, consumer groups are logical resources. Apache RocketMQ initializes multiple consumers in a consumer group to achieve the scaling of consumption performance and high availability disaster recovery.

In a consumer group, consumers consume messages based on the consumption behaviors and load balancing policy that are defined in the group. The following section describes the consumption behaviors that are defined:

- Subscription: Apache RocketMQ manages and traces subscriptions based on consumer groups. For more information, see [Subscriptions](#domainmodel-09subscription).
  aa
- Delivery order: The Apache RocketMQ broker delivers messages to consumers by using ordered delivery or concurrent delivery. You can configure the delivery method in the consumer group. For more information, see [fifo messages](#featurebehavior-03fifomessage).
- Consumption retry policy: the retry policy that is used when a consumer fails to consume a message. The policy includes the number of retries and the setting of dead-letter queues. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).

<a id="domainmodel-07consumergroup--model-relationship"></a>

## Model relationship

The following figure shows the position of consumer groups in the domain model of Apache RocketMQ.![Consumer groups](assets/images/archiforconsumergroup-9d98f4f7fc0302aa2363454a552477d9_d8cbc78cf88e2d71.png)

1. The message is initialized by the producer and sent to the Apache RocketMQ server.
2. Messages are stored in the specified queue of the topic in the order in which they arrive at the Apache RocketMQ server.
3. The consumer obtains and consumes messages from the Apache RocketMQ server based on the specified subscription relationship.

<a id="domainmodel-07consumergroup--internal-attributes"></a>

## Internal attributes

**Consumer group name**

- Definition: the name of a consumer group. Consumer group names are used to distinguish between consumer groups. Consumer group names are globally unique in a cluster.
- Values: created and configured by users. For more information, see [Parameter limits](#introduction-03limits).

**Delivery order**

- Definition: the order in which Apache RocketMQ delivers messages to a consumer client.

  Apache RocketMQ supports ordered delivery and concurrent delivery based on different consumption scenarios. For more information, see [Fifo messages](#featurebehavior-03fifomessage).

- Values: The default delivery method is concurrent delivery.

**Consumption retry policy**

- Definition: the retry policy that is used when a consumer fails to consume a message. If a consumer fails to consume a message, the system re-delivers the failed message to the consumer for re-consumption based on the policy. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).
- Values:A consumption retry policy contains the following items:

  - Maximum retries: the maximum number of times that a message can be re-delivered. If a message fails to be consumed and the maximum number of retries is exceeded, the message is delivered to the dead-letter queue or is discarded.
  - Retry interval: the interval between which the Apache RocketMQ broker re-delivers a failed message.

For more information about the valid values and default values of maximum retries and retry intervals, see [Parameter limits](#introduction-03limits).

- Constraint: Retry interval is available only for push consumers.

**Subscription**

- Definition: the set of subscription relationships that are associated with the current consumer group. A subscription includes the topics to which the consumers subscribe and the message filter rules that are used by consumers. For more information, see [Subscriptions](#domainmodel-09subscription).

Consumers dynamically register subscriptions for consumer groups. The Apache RocketMQ broker persists subscriptions and matches the subscriptions to the consumption progress of messages.

<a id="domainmodel-07consumergroup--behavior-constraints"></a>

## Behavior constraints

In the Apache RocketMQ domain model, consumer management is implemented through consumer grouping, and consumers in the same group share messages for consumption. Therefore, to ensure the normal load and consumption of messages in a group, Apache RocketMQ require all consumers in the same group to keep the following consumption behaviors consistent:

- **Delivery Order**
- **Consumption retry policy**

<a id="domainmodel-07consumergroup--version-compatibility"></a>

## Version compatibility

As described in Behavior Constraints, the delivery order and consumption retry policy of all consumers in the same group need to be consistent.

- Apache RocketMQ server version 5.x: The consumption behavior of the preceding consumers is obtained from the associated consumer groups. Therefore, the consumption behavior of all consumers in the same group must be consistent, and the client does not need to pay attention to it.
- Apache RocketMQ server version 3.x/ 4.x history: The preceding consumption logic is defined by the consumer client interface. Therefore, you must ensure that the consumption behavior of consumers in the same group is consistent when you set the consumer client.

If you use the Apache RocketMQ server version 5.x and the client uses the previous version SDK, the consumer's consumption logic is subject to the settings of the consumer client interface.

<a id="domainmodel-07consumergroup--usage-notes"></a>

## Usage notes

**Create consumer groups based on your business requirements**

In Apache RocketMQ, consumers and topics are in a many-to-many mapping relationship. We recommend that you take note of the following rules before you create consumer groups:

- Consistent message delivery order: The message delivery order must be consistent for all consumers in a consumer group. The delivery method is either ordered delivery or concurrent delivery. We recommend that you do not use the same consumer group for different business scenarios.
- Consistent business type: A consumer group corresponds to a topic. Different business domains have different requirements for message consumption, such as message filter rules and consumption retry policies. We recommend that you use different consumer groups in different business domains. We also recommend that you add up to 10 topics in a consumer group.

**Avoid using automated mechanisms to manage consumer groups**

In the Apache RocketMQ architecture, consumer groups are logical resources that are used to manage the status of consumers. Each consumer group is associated with various data, such as consumption status, accumulated messages, observable metrics, and monitoring data. We recommend that you strictly manage your consumer groups. Proceed with caution when you add, delete, modify, or query consumption groups.

Apache RocketMQ provides the automatic consumer group creation feature. However, if you enable this feature in production environments, a large number of consumer groups may be created. A large number of consumer groups can be difficult to manage and reclaim and results in the waste of system resources. Therefore, we recommend that you use this feature in only test environments.

- [Definition](#domainmodel-07consumergroup--definition)
- [Model relationship](#domainmodel-07consumergroup--model-relationship)
- [Internal attributes](#domainmodel-07consumergroup--internal-attributes)
- [Behavior constraints](#domainmodel-07consumergroup--behavior-constraints)
- [Version compatibility](#domainmodel-07consumergroup--version-compatibility)
- [Usage notes](#domainmodel-07consumergroup--usage-notes)

---

<a id="domainmodel-08consumer"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/08consumer/ -->

<!-- page_index: 14 -->

# Consumer

Version: 5.0

# Consumer

This section describes the definition, model relationship, internal attributes, and behavior constraints for consumers in Apache RocketMQ. This topic also provides version compatibility information and usage notes for consumers.

<a id="domainmodel-08consumer--definition"></a>

## Definition

A consumer is an entity that receives and processes messages in Apache RocketMQ.

Consumers are usually integrated in business systems. They obtain messages from Apache RocketMQ brokers and convert the messages into information that can be perceived and processed by business logic.

The following items determine consumer behavior:

- Consumer identity: A consumer must be associated with a consumer group to obtain behavior settings and consumption status.
- Consumer type: Apache RocketMQ provides a variety of consumer types for different development scenarios, including push consumers, simple consumers and pull consumers. For more information, see [Consumer types](#featurebehavior-06consumertype).
- Local settings for consumers: These settings specify how consumer clients run based on the consumer type. For example, you can configure the number of threads and concurrency settings on consumers to achieve different transmission effects.

<a id="domainmodel-08consumer--model-relationship"></a>

## Model relationship

The following figure shows how consumers are positioned in the domain model of Apache RocketMQ.![Consumers](assets/images/archiforconsumer-24914573add839fdf2ba2cbc0fcab7c4_d11f33c0f3075330.png)

1. The message is initialized by the producer and sent to the Apache RocketMQ server.
2. Messages are stored in the specified queue of the topic in the order in which they arrive at the Apache RocketMQ server.
3. The consumer obtains and consumes messages from the Apache RocketMQ server based on the specified subscription relationship.

<a id="domainmodel-08consumer--internal-attributes"></a>

## Internal attributes

**Consumer group name**

- Definition: the name of the consumer group associated with the current consumer. Consumers inherit their behavior from the consumer groups. For more information, see [Consumer groups](#domainmodel-07consumergroup).
- Values: Consumer groups are the logical resources of Apache RocketMQ{#product-name}

  . You must create consumer groups by using the console or calling API operations in advance. For more information about the limits on this operation, see[Parameter limits](#introduction-03limits).

**Client ID**

- Definition: the identity of a consumer client. This attribute is used to distinguish between different consumers. The value must be unique within a cluster.
- Values: The client ID is automatically generated by the Apache RocketMQ SDK. It is mainly used for O\&M purposes such as log viewing and problem locating. The client ID cannot be modified.

**Communication parameters**

- Endpoints **(Required)** : the endpoint used to connect to the server. This endpoint is used to identify the cluster.

  The access point must be configured in the format. We recommend that you use domain names to avoid using IP addresses to prevent node changes from failing to perform hotspot migration.

- Credential **(Optional)** : the credential used by the client for authentication.

  Transmission is required only when identity recognition and authentication are enabled on the server.

- Request Timeout **(Optional)** : the timeout period of the network request. For more information about the value range and default value, see [Parameter limits](#introduction-03limits).

**Pre-bound subscription list**

- Definition: the subscription list of the specified consumer. The Apache RocketMQ broker can use the pre-bound subscription list to verify the permissions and validity of the subscribed topic during consumer initialization instead of after the application is started.
- Values: We recommend that you specify the subscription or the list of subscribed topics during consumer initialization. If the subscription is not specified or the subscribed topics are changed, Apache RocketMQ dynamically verifies the topics.

**Message listener**

- Definition: the listener that a consumer uses to invoke the message consumption logic after Apache RocketMQ broker pushes a message to the consumer.
- Values: The value of a message listener is configured on the consumer client.
- Constraints: When you consume messages as a push consumer, you must configure the message listener on the consumer client. For more information about consumer types, see [Consumer types](#featurebehavior-06consumertype).

<a id="domainmodel-08consumer--behavior-constraints"></a>

## Behavior constraints

In the Apache RocketMQ domain model, consumer management is implemented through consumer grouping, and consumers in the same group share messages for consumption. Therefore, to ensure the normal load and consumption of messages in a group, Apache RocketMQ require all consumers in the same group to keep the following consumption behaviors consistent:

- **Delivery Order**
- **Consumption retry policy**

<a id="domainmodel-08consumer--version-compatibility"></a>

## Version compatibility

As described in Behavior Constraints, the delivery order and consumption retry policy of all consumers in the same group need to be consistent.

- Apache RocketMQ server version 5.x: The consumption behavior of the preceding consumers is obtained from the associated consumer groups. Therefore, the consumption behavior of all consumers in the same group must be consistent, and the client does not need to pay attention to it.
- Apache RocketMQ server version 3.x/ 4.x history: The preceding consumption logic is defined by the consumer client interface. Therefore, you must ensure that the consumption behavior of consumers in the same group is consistent when you set the consumer client.

If you use the Apache RocketMQ server version 5.x and the client uses the previous version SDK, the consumer's consumption logic is subject to the settings of the consumer client interface.

<a id="domainmodel-08consumer--usage-notes"></a>

## Usage notes

**We recommend that you limit the number of consumers on individual processes.**

The consumers of Apache RocketMQ support the non-blocking transmission mode at the communication protocol level. The non-blocking transmission mode has higher communication efficiency and supports concurrent access by multiple threads. Therefore, in most scenarios, only one consumer needs to be initialized for a consumer group in a single process. Avoid initializing multiple consumers with the same configurations during the development phase.

**We recommend that you do not create and destroy consumers on a regular basis.**

The consumers of Apache RocketMQ are underlying resources that can be reused, like the connection pool of a database. You do not need to create consumers each time you receive messages or destroy the consumers after you consume messages. If you regularly create and destroy consumers, a large number of short connection requests are generated on the broker. This imposes a high level of load on your system.

- Correct example


```java
Consumer c = ConsumerBuilder.build();
for (int i =0;i<n;i++)
{
  Message m= c.receive();
  //process message
}
c.shutdown();
```

- Incorrect example


```java
for (int i =0;i<n;i++)
{
  Consumer c = ConsumerBuilder.build();
  Message m= c.receive();
  //process message
  c.shutdown();
}
```

- [Definition](#domainmodel-08consumer--definition)
- [Model relationship](#domainmodel-08consumer--model-relationship)
- [Internal attributes](#domainmodel-08consumer--internal-attributes)
- [Behavior constraints](#domainmodel-08consumer--behavior-constraints)
- [Version compatibility](#domainmodel-08consumer--version-compatibility)
- [Usage notes](#domainmodel-08consumer--usage-notes)

---

<a id="domainmodel-09subscription"></a>

<!-- source_url: https://rocketmq.apache.org/docs/domainModel/09subscription/ -->

<!-- page_index: 15 -->

# Subscription

Version: 5.0

# Subscription

This section describes the definition, model relationship, internal attributes, and usage notes for subscriptions in Apache RocketMQ.

<a id="domainmodel-09subscription--definition"></a>

## Definition

A subscription is the rule and status settings for consumers to obtain and process messages in Apache RocketMQ.

Subscriptions are dynamically registered by consumer groups with brokers. Messages are then matched and consumed based on the filter rules defined by subscriptions.

By configuring subscriptions, you can control the following messaging behaviors:

- Message filter rules: These rules are used to define which messages in a topic are consumed by a consumer. By configuring message filter rules, consumers can effectively obtain messages that they want and specify message receiving ranges based on different business scenarios. For more information, see [Message filtering](#featurebehavior-07messagefilter).
- Consumption status: By default, the Apache RocketMQ broker provides persistent subscriptions. In other words, after a consumer group subscribes to a broker, consumers in the group can continue consuming messages from where the consumers left off after they reconnect.

<a id="domainmodel-09subscription--rules-for-determining-a-subscription"></a>

## Rules for determining a subscription

The subscriptions of Apache RocketMQ are designed based on consumer groups and topics. Therefore, a subscription refers to the subscription of a specified consumer group to a topic. The following describes the rules for determining a subscription:

- One topic to many subscribersThe following figure shows two consumer groups (Group A and Group B) subscribed to Topic A. These two subscriptions are independent of each other and can be defined separately.
  ![Subscription relationships are grouped differently](assets/images/subscription-diff-group-0b215b9bb822b4bf43c388e9155ecca1_f5987622e1f57bc7.png)
- One subscriber to multiple topicsThe following figure shows a consumer group (Group A) subscribed to two topics: Topic A and Topic B. Consumers in Group A have two separate subscriptions to Topic A and Topic B. The two subscriptions are independent of each other and can be defined separately.
  ![Subscription relationships are grouped differently](assets/images/subscription-one-group-77bd92b987e8264ad3c5f27b29463942_f9b6906b06fcd038.png)

<a id="domainmodel-09subscription--model-relationship"></a>

## Model relationship

The following figure shows the position of subscriptions in the domain model of Apache RocketMQ.![Subscriptions](assets/images/archiforsubsciption-a495c04e71ed64b9403b689f9413ed08_8c2d35feae21aaca.png)

1. The message is initialized by the producer and sent to the Apache RocketMQ server.
2. Messages are stored in the specified queue of the topic in the order in which they arrive at the Apache RocketMQ server.
3. The consumer obtains and consumes messages from the Apache RocketMQ server based on the specified subscription relationship.

<a id="domainmodel-09subscription--internal-attributes"></a>

## Internal attributes

**Filter types**

- Definition: the type of a message filter rule. After a message filter rule is set for a subscription, the system matches the messages in a topic based on the filter rule. Only the messages that meet the conditions are delivered to consumers. This feature helps you classify messages sent to consumers based on your requirements.
- Values:

  - Tag filter: filters and matches the full text based on tag strings.
  - SQL92 filter: filters and matches message attributes based on SQL syntax.

**Filter expressions**

- Definition: the expression of a custom filter rule.
- Values: For more information, see [Syntax for filter expressions](#featurebehavior-07messagefilter).

<a id="domainmodel-09subscription--behavior-constraints"></a>

## Behavior constraints

**Subscription consistency**

Apache RocketMQ manages subscriptions based on consumer groups. Therefore, consumers in the same consumer group must maintain the same consumption logic. Otherwise, consumption conflicts occur, which in turn causes some messages to be incorrectly consumed.

- Correct example


```java
//Consumer c1
Consumer c1 = ConsumerBuilder.build(groupA);
c1.subscribe(topicA,"TagA");
//Consumer c2
Consumer c2 = ConsumerBuilder.build(groupA);
c2.subscribe(topicA,"TagA");
```

- Incorrect example


```java
//Consumer c1
Consumer c1 = ConsumerBuilder.build(groupA);
c1.subscribe(topicA,"TagA");
//Consumer c2Consumer
c2 = ConsumerBuilder.build(groupA);
c2.subscribe(topicA,"TagB");
```

<a id="domainmodel-09subscription--usage-notes"></a>

## Usage notes

**Do not frequently modify subscriptions.**

In Apache RocketMQ, subscriptions are associated with metadata and configurations such as filter rules and consumption progress. The system must also ensure that the consumption behavior, consumption logic, and load policy of all consumers in the consumer group are consistent. These factors result in a complex web of relationships that need to be managed. Therefore, we recommend that you do not regularly modify subscriptions to change the business logic in the production environment. Otherwise, the client constantly needs to adjust its load distribution, which causes message reception problems.

- [Definition](#domainmodel-09subscription--definition)
- [Rules for determining a subscription](#domainmodel-09subscription--rules-for-determining-a-subscription)
- [Model relationship](#domainmodel-09subscription--model-relationship)
- [Internal attributes](#domainmodel-09subscription--internal-attributes)
- [Behavior constraints](#domainmodel-09subscription--behavior-constraints)
- [Usage notes](#domainmodel-09subscription--usage-notes)

---

<a id="featurebehavior-01normalmessage"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/01normalmessage/ -->

<!-- page_index: 16 -->

# Normal Message

Version: 5.0

# Normal Message

Normal messages are messages that have no special features in Apache RocketMQ. They are different from featured messages such as fifo messages, delay messages, and transaction messages. This topic describes the scenarios, working mechanism, usage, and usage notes of normal messages.

<a id="featurebehavior-01normalmessage--scenarios"></a>

## Scenarios

Normal messages are generally used in microservice decoupling, data integration, and event-driven scenarios. Most of these scenarios have low or no requirements on timing or the sequence for processing messages other than reliable transmission channels.

**Scenario 1: Asynchronous decoupling of microservices**
![在线消息处理](assets/images/onlineprocess-cfd38e3de3a5fc1ee76f17331cc5b828_894aac82c6b6acc7.png)

The preceding figure shows an online e-commerce transaction scenario. In this scenario, the upstream order system encapsulates order placement and payment as an independent normal message and sends the message to the Apache RocketMQ broker. Downstream systems then subscribe to the message from the broker on demand and process tasks based on the local consumption logic. Messages are independent of each other and do not need to be associated.

**Scenario 2: Data integration transmission**
![数据传输](assets/images/offlineprocess-027f6f1642db3d78ff29890abbe38bf8_660a751024eaee03.png)

The preceding figure uses offline log collection as an example. An instrumentation component is used to collect operations logs from frontend applications and forward the logs to Apache RocketMQ. Each message is a piece of log data that requires no processing from Apache RocketMQ. Apache RocketMQ needs only to send the log data to the downstream storage and analysis systems. The backend applications are responsible for subsequent processing tasks.

<a id="featurebehavior-01normalmessage--working-mechanism"></a>

## Working mechanism

**Definition of normal messages**

Normal messages are messages with basic functions in Apache RocketMQ. Normal messages support asynchronous decoupling and communication between producers and consumers.
![生命周期](assets/images/lifecyclefornormal-e8a2a7e42a0722f681eb129b51e1bd66_11a6f5942e0e78e1.png)

**Lifecycle of a normal message**

- Initialized: The message is built and initialized by the producer and is ready to be sent to a broker.
- Ready: The message is sent to the broker, and is visible to the consumer and available for consumption.
- Inflight: The message is obtained by the consumer and processed based on the local business logic of the consumer.

  In this process, the broker waits for the consumer to complete the consumption and submit the consumption result. If no response is received from the consumer in a certain period of time, Apache RocketMQ retries the message. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).
- Acked: The consumer completes consumption and submits the consumption result to the broker. The broker marks whether the current message is successfully consumed.

  By default, Apache RocketMQ retains all messages. When the consumption result is submitted, the message data is logically marked as consumed instead of being deleted immediately. Therefore, the consumer can backtrack the message for re-consumption before it is deleted due to the expiration of the retention period or insufficient storage space.
- Deleted: When the retention period of the message expires or the storage space is insufficient, Apache RocketMQ deletes the earliest saved message from the physical file in a rolling manner. For more information, see [Message storage and cleanup](#featurebehavior-11messagestorepolicy).

<a id="featurebehavior-01normalmessage--usage-limits"></a>

## Usage limits

Normal messages support only topics whose MessageType is Normal.

<a id="featurebehavior-01normalmessage--example"></a>

## Example

**Create topic**

For creating topics in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that message type needs to be added as a property parameter. Here is an example:

```shell
sh mqadmin updateTopic -n <nameserver_address> -t <topic_name> -c <cluster_name> -a +message.type=NORMAL
```

**Send messages**

You can set index keys and filter tags to filter or search for normal messages. The following sample code shows how to send and receive normal messages in Java:

```java
// Send a normal message.
  MessageBuilder messageBuilder = new MessageBuilder();
  Message message = messageBuilder.setTopic("topic")
  // Specify the message index key so that you can accurately search for the message by using a keyword.
  .setKeys("messageKey")
  // Specify the message tag so that the consumer can filter the message based on the specified tag.
  .setTag("messageTag")
  // Message body.
  .setBody("messageBody".getBytes())
  .build();
  try {
    // Send the message. You need to pay attention to the sending result and capture exceptions such as failures.
    SendReceipt sendReceipt = producer.send(message);
    System.out.println(sendReceipt.getMessageId());
  } catch (ClientException e) {
      e.printStackTrace();
  }
  // Consumption example 1: When you consume a normal message as a push consumer, you need only to process the message in the message listener.
  MessageListener messageListener = new MessageListener() {
      @Override
      public ConsumeResult consume(MessageView messageView) {
          System.out.println(messageView);
          // Return the status based on the consumption result.
          return ConsumeResult.SUCCESS;
      }
  };
  // Consumption example 2: When you consume a normal message as a simple consumer, you must obtain and consume the message, and submit the consumption result.
  List<MessageView> messageViewList = null;
  try {
      messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
      messageViewList.forEach(messageView -> {
          System.out.println(messageView);
          // After consumption is complete, you must invoke ACK to submit the consumption result.
          try {
              simpleConsumer.ack(messageView);
          } catch (ClientException e) {
              e.printStackTrace();
          }
      });
      } catch (ClientException e) {
      // If the pull fails due to system traffic throttling or other reasons, you must re-initiate the request to obtain the message.
      e.printStackTrace();
  }
```

<a id="featurebehavior-01normalmessage--usage-notes"></a>

## Usage notes

**Set a globally unique index key to facilitate troubleshooting**

You can set custom index keys, which are message keys, in Apache RocketMQ. When you query and trace messages, the index key can help you find these messages efficiently and accurately.

Therefore, when you send messages, we recommend that you use the unique information of the service, such as order ID and user ID, as an index. This helps you find messages quickly in the future.

- [Scenarios](#featurebehavior-01normalmessage--scenarios)
- [Working mechanism](#featurebehavior-01normalmessage--working-mechanism)
- [Usage limits](#featurebehavior-01normalmessage--usage-limits)
- [Example](#featurebehavior-01normalmessage--example)
- [Usage notes](#featurebehavior-01normalmessage--usage-notes)

---

<a id="featurebehavior-02delaymessage"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/02delaymessage/ -->

<!-- page_index: 17 -->

# Delay Message

Version: 5.0

# Delay Message

Delay messages are messages with advanced features in Apache RocketMQ. This topic describes the scenarios, working mechanism, limits, usage examples, and usage notes of delay messages and delayed messages.

> [!NOTE]
> Scheduled message and delay message are essentially the same. Both of them deliver messages to consumers at a fixed time according to the timing time set by the message. Therefore, delay messages are used in the following sections.

<a id="featurebehavior-02delaymessage--scenarios"></a>

## Scenarios

Accurate and reliable time-based event triggers are required in scenarios such as distributed timed scheduling and task timeout processing. Apache RocketMQ provides delay messages to help you simplify the development of timed scheduling tasks and implement high-performance, scalable, and reliable timed triggering.

**Scenario 1: Distributed timed scheduling**
![定时消息](assets/images/delaywork-e9647b539ae35898102a336a27d3ad94_34ef1f6adf1f125e.png)

A distributed timed scheduling scenario involves tasks that require various time granularity levels, for example, a task to execute file cleanup at 5 o'clock every day or a task to trigger push messages every 2 minutes. Traditional dataset-based timed scheduling solutions are complex and inefficient in distributed scenarios. In comparison, delay messages in Apache RocketMQ allow you to encapsulate multiple types of time triggers.

**Scenario 2: Task timeout processing**
![超时任务处理](assets/images/scheduletask-1944aea7bf2a4a4c56be4d90ead4f1f3_26bbdf716b20f6f5.png)

A typical scenario that involves task timeout processing is e-commerce payment, where an unpaid order is canceled after it remains unpaid for a specific time period instead of being canceled immediately. In this case, you can use delay messages in Apache RocketMQ to check and trigger timeout tasks.

Task timeout processing based on delay messages provides the following benefits:

- Various time granularity levels and simplified development: Scheduled messaging in Apache RocketMQ does not have the limit of fixed time increments. You can trigger tasks at any time granularity level and without deduplication.
- High performance and scalability: delay messages in Apache RocketMQ offer high concurrency and scalability. This outperforms traditional database scanning methods, which are complex to implement and can cause performance bottlenecks due to frequent API calls for scanning.

<a id="featurebehavior-02delaymessage--working-mechanism"></a>

## Working mechanism

**Definition of delay messages**

delay messages are messages with advanced features in Apache RocketMQ. delay messages allow consumers to consume messages that are sent to the server only after a specified period of time or at a specified time. You can use delay messages to implement delayed scheduling and triggering in distributed scenarios.

**Time setting rules**

- The scheduled or delayed time for delay messages in Apache RocketMQ is represented as a timestamp, not a time period.
- The scheduled time is in the format of a millisecond-level Unix timestamp. You must convert the scheduled time of message delivery to a millisecond-level Unix timestamp. You can use the [Unix timestamp converter](https://www.unixtimestamp.com/) to convert a time to a millisecond-level Unix timestamp.
- The scheduled time must be within the allowed time range. If the scheduled time exceeds the range, the scheduled time does not take effect and the messages are immediately delivered from the server side.
- By default, the maximum time range for delay messages is 24 hours. You cannot change the default value. For more information, see[Parameter limits](#introduction-03limits).
- The scheduled time must be later than the current time. If the scheduled time is set to a time earlier than the current time, the scheduled time does not take effect and the messages are immediately delivered from the server side.

**The following section provides two time setting examples:**

- delay messages: If the current time is 2022-06-09 17:30:00 and you want to deliver messages at 2022-06-09 19:20:00, the millisecond-level Unix timestamp of the scheduled time is 1654773600000.
- Delayed messages: If the current time is 2022-06-09 17:30:00 and you want to deliver messages after 1 hour, the message delivery time is 2022-06-09 18:30:00 and the millisecond-level Unix timestamp is 1654770600000.

**Lifecycle of a scheduled message**

![定时消息生命周期](assets/images/lifecyclefordelay-2ce8278df69cd026dd11ffd27ab09a17_8308d8c8a27d4e2c.png)

- Initialized: The message is built and initialized by the producer and is ready to be sent to the server.
- Timing: The message is sent to the server side, where the message is stored in a time-based storage system until the specified delivery time. An index is not immediately created for the message.
- Ready: At the specified time, the message is written into a regular storage engine, where the message is visible for consumers and waits for consumption by consumers.

- Inflight: The message is obtained by the consumer and processed based on the local business logic of the consumer.

  In this process, the broker waits for the consumer to complete the consumption and submit the consumption result. If no response is received from the consumer in a certain period of time, Apache RocketMQ retries the message. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).

- Acked: The consumer completes consumption and submits the consumption result to the broker. The broker marks whether the current message is successfully consumed.

  By default, Apache RocketMQ retains all messages. When the consumption result is submitted, the message data is logically marked as consumed instead of being deleted immediately. Therefore, the consumer can backtrack the message for re-consumption before it is deleted due to the expiration of the retention period or insufficient storage space.

- Deleted: When the retention period of the message expires or the storage space is insufficient, Apache RocketMQ deletes the earliest saved message from the physical file in a rolling manner. For more information, see [Message storage and cleanup](#featurebehavior-11messagestorepolicy).

<a id="featurebehavior-02delaymessage--usage-limits"></a>

## Usage limits

**Message type consistency**

delay messages can be sent only to topics whose MessageType is Delay.

**Time granularity**

The time granularity for delay messages in Apache RocketMQ is down to milliseconds. The default granularity value is 1000 ms.

The status of delay messages in Apache RocketMQ can be persistently stored. If the messaging system experiences a failure and is restarted, messages are still delivered based on the specified delivery time. However, if the storage system experiences an exception or is restarted, latency may occur in delivering delay messages.

<a id="featurebehavior-02delaymessage--example"></a>

## Example

**Create topic**

For creating topics in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that message type needs to be added as a property parameter. Here is an example:

```shell
sh mqadmin updateTopic -n <nameserver_address> -t <topic_name> -c <cluster_name> -a +message.type=Delay
```

**Send messages**

Unlike normal messages, delay messages must have a delivery timestamp specified for them.

**Create DELAY Topic**

```bash
/bin/mqadmin updateTopic -c DefaultCluster -t DelayTopic -n 127.0.0.1:9876 -a +message.type=DELAY
```

- -c the cluster name
- -t the topic name
- -n the address of the nameserver
- **-a extra attributes，we add an `message.type` attribute with value `DELAY` to support delivery DELAY message.**

The following code provides Java examples of delivery and consumption of delay messages:

```java
        // Send delay messages.
        MessageBuilder messageBuilder = null;
        // Specify a millisecond-level Unix timestamp. In this example, the specified timestamp indicates that the message will be delivered in 10 minutes from the current time.
        Long deliverTimeStamp = System.currentTimeMillis() + 10L * 60 * 1000;
        Message message = messageBuilder.setTopic("topic")
                // Specify the message index key. The system uses the key to locate the message.
                .setKeys("messageKey")
                // Specify the message tag. The consumer can use the tag to filter messages.
                .setTag("messageTag")
                .setDeliveryTimestamp(deliverTimeStamp)
                // Configure the message body.
                .setBody("messageBody".getBytes())
                .build();
        try {
            // Send the messages. Focus on the result of message sending and exceptions such as failures.
            SendReceipt sendReceipt = producer.send(message);
            System.out.println(sendReceipt.getMessageId());
        } catch (ClientException e) {
            e.printStackTrace();
        }
        // Consumption example 1: If a scheduled message is consumed by a push consumer, the consumer needs to process the message only in the message listener.
        MessageListener messageListener = new MessageListener() {
            @Override
            public ConsumeResult consume(MessageView messageView) {
                System.out.println(messageView.getDeliveryTimestamp());
                // Return the status based on the consumption result.
                return ConsumeResult.SUCCESS;
            }
        };
        // Consumption example 2: If a scheduled message is consumed by a simple consumer, the consumer must obtain the message for consumption and submit the consumption result.
        List<MessageView> messageViewList = null;
        try {
            messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
            messageViewList.forEach(messageView -> {
                System.out.println(messageView);
                // After consumption is complete, the consumer must invoke ACK to submit the consumption result.
                try {
                    simpleConsumer.ack(messageView);
                } catch (ClientException e) {
                    e.printStackTrace();
                }
            });
        } catch (ClientException e) {
            // If the pull fails due to system traffic throttling or other reasons, you must re-initiate the request to obtain the message.
            e.printStackTrace();
        }
    }
```

<a id="featurebehavior-02delaymessage--usage-notes"></a>

## Usage notes

**We recommend that you do not schedule the same delivery time for a large number of messages.**

delay messages are stored in a time-based storage system before they are delivered to consumers at the specified delivery time. If you specify the same delivery time for a large number of delay messages, the system has to simultaneously process the messages at the delivery time. This puts the system under heavy load and results in delays in message delivery.

- [Scenarios](#featurebehavior-02delaymessage--scenarios)
- [Working mechanism](#featurebehavior-02delaymessage--working-mechanism)
- [Usage limits](#featurebehavior-02delaymessage--usage-limits)
- [Example](#featurebehavior-02delaymessage--example)
- [Usage notes](#featurebehavior-02delaymessage--usage-notes)

---

<a id="featurebehavior-03fifomessage"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/03fifomessage/ -->

<!-- page_index: 18 -->

# Ordered Message

Version: 5.0

# Ordered Message

Ordered messages are a type of message with advanced features in Apache RocketMQ. This topic describes the scenarios, working mechanism, limits, usage examples, and usage notes of ordered messages.

<a id="featurebehavior-03fifomessage--scenarios"></a>

## Scenarios

Heterogeneous systems use state synchronization to maintain strong consistency in scenarios such as ordered event processing, transaction matchmaking, and real-time incremental data synchronization. The preceding scenarios require ordered delivery of messages from upstream applications to downstream applications when an event change occurs. Apache RocketMQ provides ordered messages to help you implement ordered message transmission.

**Scenario 1: Transaction matchmaking**
![交易撮合](assets/images/fifo-trade-a8bac55b8fb3fceb995891c64c2f0a5a_63a07574c5d950c9.png)

For example, in securities and stock trading scenarios, if multiple bidders offer the same bid price for a bid order, the bidder who first offers the bid price wins the bid. Therefore, the downstream order processing system must be designed to process orders in the order in which prices were offered.

**Scenario 2: Real-time incremental data synchronization**

Normal message![普通消息](assets/images/tradewithnormal-5273283ffa54ec08017f356227411f83_96eeb8d605ed4e07.png)
Fifo message![顺序消息](assets/images/tradewithfifo-30884dfeb909c54d7379641fcec437fa_4ebf8d729e12194f.png)

For example, you want to perform incremental synchronization of data that is related to database modifications. You can use ordered messages provided in Apache RocketMQ to transmit messages from the upstream source database to the downstream query system. The messages can be binary logs of addition, deletion, and modification operations. The downstream system retrieves the messages in the order in which the messages are sent to make the database status updated in the same order. Ordered messages help you ensure consistency between the operations in the upstream system and the status data in the downstream system. If you use normal messages in this scenario, state inconsistency may occur.

<a id="featurebehavior-03fifomessage--working-mechanism"></a>

## Working mechanism

**Definition of ordered messages**

Ordered messages are an advanced type of message in Apache RocketMQ. Ordered messages are delivered to consumers in the order in which the messages are sent. This message type allows you to implement ordered processing in business scenarios.

The defining characteristics of ordered messages are the order of message sending, storage, and delivery.

Apache RocketMQ uses message groups to determine the order of ordered messages. You must configure message groups for ordered messages. The messages in a message group are processed in the first-in, first-out (FIFO) order. Message ordering does not apply to different message groups or messages that are not in a message group.

Message group-based message ordering allows you to specify fine-grained message ordering based on your business logic. This helps you implement partial message ordering in your business system and improve the degree of concurrency and throughput of the business system.

**Message ordering**

Two types of message order apply in Apache RocketMQ: the production order and the consumption order.

- **Production order** ： Apache RocketMQ uses the protocol that is established between the producer and the server to ensure that messages are serially sent from the producer to the server and that the messages are stored and persisted in the order in which the messages are sent.

  To ensure the production order of messages, make sure that the following conditions are met:

  - Single producer: The production order of messages applies to individual producers. Apache RocketMQ cannot determine the order of messages from different producers in different systems, even if you configure the same message group for the messages.
  - Serial transmission: A producer in Apache RocketMQ supports secure access by using multiple threads. If a producer uses multiple threads to concurrently send messages, Apache RocketMQ cannot determine the order of messages from different threads.

If producers that meet the preceding conditions send messages to Apache RocketMQ, the messages that belong to the same message group are stored in the same queue in the order in which the messages are sent. The following figure describes the sequential storage logic of Apache RocketMQ.

![顺序存储逻辑](assets/images/fifomessagegroup-aad0a1b7e64089075db956c0eca0cbf4_05809fe634c1341b.png)

In the preceding figure, messages from MessageGroup 1 and MessageGroup 4 are stored in the same queue (MessageQueue 1). Apache RocketMQ ensures that messages G1-M1, G1-M2, and G1-M3 from MessageGroup 1 are stored in the queue in the order in which the messages are sent. Messages G4-M1 and G4-M2 from MessageGroup 4 are also stored in the order in which the messages are sent. However, messages from MessageGroup 1 and MessageGroup 4 are stored in no particular order.

- **Consumption order** ：

  Apache RocketMQ uses the protocol that is established between the consumers and the server to ensure that messages are consumed in the order in which the messages are stored.

  To ensure the consumption order of messages, make sure that the following conditions are met:

  - Delivery order: Apache RocketMQ ensures that message are delivered in the message storage order on the server by using the client SDK and the communications protocol on the server side. When consumer applications consume messages, the applications must follow the receive-process-reply path to prevent out-of-order messages caused by asynchronous processing.


> [!NOTE]
> - When a PushConsumer consumer consumes messages, Apache RocketMQ ensures that messages are delivered to the consumer one by one in the order in which the messages are stored.
> - When a SimpleConsumer consumer consumes messages, the consumer may pull multiple messages at a time, and the business application must have a solution to implement the message consumption order. For more information about consumer types, see [Consumer types](#featurebehavior-06consumertype).

  - Limited retries:Apache RocketMQ limits the number of delivery retries for ordered messages. If a message reaches the maximum number of delivery retries, Apache RocketMQ stops retrying the delivery of the message for consumption. This prevents other messages in the queue from constantly waiting for delivery.

  In scenarios in which the consumption order is critical, we recommend that you specify an appropriate number of retries to prevent out-of-order message processing.

**Combination of production order and consumption order**

If you want messages to be processed based on the FIFO principle, the production order and the consumption order are required. In most business scenarios, a producer may map to multiple consumers, and not all consumers require ordered consumption of messages. You can combine the settings of production order and consumption order to meet your requirements in different business scenarios. For example, you can send ordered messages and use non-sequential concurrent consumption to improve throughput. The following table describes different combinations of production order and consumption order settings.

<table><thead><tr><th>Production order</th><th>Consumption order</th><th>Effect</th></tr></thead><tbody><tr><td>Configure message groups to implement ordered delivery of messages.</td><td>Ordered consumption of messages</td><td>The order of messages is ensured at the message group level. Messages in the same message group are sent and consumed in the same order.</td></tr><tr><td>Configure message groups to implement ordered delivery of messages.</td><td>Concurrent consumption</td><td>Messages are concurrently and chronologically consumed.</td></tr><tr><td>Configure no message groups to implement unordered delivery of messages.</td><td>Ordered consumption of messages</td><td>The order of messages is ensured at the queue level. The message consumption is based on the attributes of the queue. Apache RocketMQ ensures that the consumption order is the same as the storage order in the queue, but not necessarily the same as the message sending order.</td></tr><tr><td>Configure no message groups to implement unordered delivery of messages.</td><td>Concurrent consumption</td><td>Messages are concurrently and chronologically consumed.</td></tr></tbody></table>

**Lifecycle of an ordered message**
![生命周期](assets/images/lifecyclefornormal-e8a2a7e42a0722f681eb129b51e1bd66_11a6f5942e0e78e1.png)

- Initialized: The message is built and initialized by the producer and is ready to be sent to a broker.
- Ready: The message is sent to the broker, and is visible to the consumer and available for consumption.
- Inflight: The message is obtained by the consumer and processed based on the local business logic of the consumer.

  In this process, the broker waits for the consumer to complete the consumption and submit the consumption result. If no response is received from the consumer in a certain period of time, Apache RocketMQ retries the message. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).
- Acked: The consumer completes consumption and submits the consumption result to the broker. The broker marks whether the current message is successfully consumed.

  By default, Apache RocketMQ retains all messages. When the consumption result is submitted, the message data is logically marked as consumed instead of being deleted immediately. Therefore, the consumer can backtrack the message for re-consumption before it is deleted due to the expiration of the retention period or insufficient storage space.
- Deleted: When the retention period of the message expires or the storage space is insufficient, Apache RocketMQ deletes the earliest saved message from the physical file in a rolling manner. For more information, see [Message storage and cleanup](#featurebehavior-11messagestorepolicy).

> [!NOTE]
> - Message consumption failures or timeouts trigger the retry logic of the server. If a consumption retry is triggered for a message, the message reaches the end of its lifecycle. The original message is considered a new message with a new message ID.
> - If a consumption retry is triggered for an ordered message, the messages that follow the ordered message can be processed only after the ordered message is consumed.

<a id="featurebehavior-03fifomessage--usage-limits"></a>

## Usage limits

Ordered messages support only topics whose MessageType is FIFO.

<a id="featurebehavior-03fifomessage--example"></a>

## Example

**Create topic**

For creating topics in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that message type needs to be added as a property parameter. Here is an example:

```shell
sh mqadmin updateTopic -n <nameserver_address> -t <topic_name> -c <cluster_name> -a +message.type=FIFO
```

**Create subscriptionGroup**

For creating subscriptionGroup in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that `-o` option needs to be set to true. Here is an example:

```shell
sh mqadmin updateSubGroup -c <cluster_name> -g <consumer_group_name> -n <nameserver_address> -o true
```

**Send messages**

Compared with normal messages, ordered messages must have message groups configured for them. We recommend that you configure message groups at a fine-grained level based on your business requirements to allow for workload decoupling and concurrency scaling.

**Create FIFO topic**

```bash
./bin/mqadmin updateTopic -c DefaultCluster -t FIFOTopic -o true -n 127.0.0.1:9876 -a +message.type=FIFO
```

- -c the cluster name
- -t the topic name
- -n the address of the nameserver
- **-o the flag to create a ordered topic**

**Create FIFO subscriptionGroup**

```bash
./bin/mqadmin updateSubGroup -c DefaultCluster -g FIFOGroup -n 127.0.0.1:9876 -o true
```

- -c the cluster name
- -g the subscription group name
- -n the address of the nameserver
- **-o the flag to create a ordered subscription group**

The following sample code provides an example on how to send and receive ordered messages in Java:

```java
        // Send ordered messages.
        MessageBuilder messageBuilder = null;
        Message message = messageBuilder.setTopic("topic")
                // Specify the message index key. The system uses the key to locate the message.
                .setKeys("messageKey")
                // Specify the message tag. The consumer can use the tag to filter the message.
                .setTag("messageTag")
                // Configure a message group for the ordered messages. We recommend that you do not include a large number of messages in the group.
                .setMessageGroup("fifoGroup001")
                // Configure the message body.
                .setBody("messageBody".getBytes())
                .build();
        try {
            // Send the messages. Focus on the result of message sending and exceptions such as failures.
            SendReceipt sendReceipt = producer.send(message);
            System.out.println(sendReceipt.getMessageId());
        } catch (ClientException e) {
            e.printStackTrace();
        }
        // Make sure that ordered delivery is applied to the consumer group. Otherwise, the messages are delivered concurrently and in no particular order.
        // Consumption example 1: If the consumer type is PushConsumer, the consumer needs to only process the message in the message listener.
        MessageListener messageListener = new MessageListener() {
            @Override
            public ConsumeResult consume(MessageView messageView) {
                System.out.println(messageView);
                // Return the status based on the consumption result.
                return ConsumeResult.SUCCESS;
            }
        };
        // Consumption example 2: If the consumer type is SimpleConsumer, the consumer must actively obtain the message for consumption and submit the consumption result.
        // If the consumption of a message in the message group has not finished, the next message in the message group cannot be retrieved if you call the Receive function.
        List<MessageView> messageViewList = null;
        try {
            messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
            messageViewList.forEach(messageView -> {
                System.out.println(messageView);
                // After consumption is complete, the consumer must invoke ACK to submit the consumption result.
                try {
                    simpleConsumer.ack(messageView);
                } catch (ClientException e) {
                    e.printStackTrace();
                }
            });
        } catch (ClientException e) {
            // If the pull fails due to system traffic throttling or other reasons, the consumer must re-initiate the request to obtain the message.
            e.printStackTrace();
        }
```

<a id="featurebehavior-03fifomessage--usage-notes"></a>

## Usage notes

**Use serial consumption to prevent out-of-order message processing.**

We recommend that you use serial message consumption instead of batch consumption. Consumption of multiple messages at the same time may cause out-of-order message processing.

For example, messages 1, 2, 3, and 4 are sent in the 1-2-3-4 order and the order of batch consumption is 1-[2, 3](processed in batches but failed)-[2, 3](retry)-4. The system may repeatedly process Message 2 if Message 3 fails to be processed. As a result, out-of-order message consumption occurs.

**Avoid including a large number of messages in a message group.**

Apache RocketMQ ensures that the messages in the same message group are stored in the same queue. A message group that contains a large number of messages causes the corresponding queue to be overloaded. This affects messaging performance and hinders scalability. When you configure message groups, you can use order IDs and user IDs as the message sequencing conditions. This ensures the order of messages of the same user.

We recommend that you split messages in your business applications by message group. For example, you can use order IDs and user IDs as message group keywords to implement ordered processing of messages of the same user. You do not need to ensure the order of messages of different users.

- [Scenarios](#featurebehavior-03fifomessage--scenarios)
- [Working mechanism](#featurebehavior-03fifomessage--working-mechanism)
- [Usage limits](#featurebehavior-03fifomessage--usage-limits)
- [Example](#featurebehavior-03fifomessage--example)
- [Usage notes](#featurebehavior-03fifomessage--usage-notes)

---

<a id="featurebehavior-04transactionmessage"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/04transactionmessage/ -->

<!-- page_index: 19 -->

# Transaction Message

Version: 5.0

# Transaction Message

Transactional messages are an advanced message type in Apache RocketMQ. This topic describes the application scenarios, working mechanism, limits, usage, and usage notes of transactional messages.

<a id="featurebehavior-04transactionmessage--scenarios"></a>

## Scenarios

**Distributed transactions**

When a core business logic is executed in a distributed system, multiple downstream businesses are invoked to process the logic simultaneously. Therefore, ensuring the consistency of the execution results between the core business and the downstream businesses is the biggest challenge that needs to be solved for distributed transactions.
![事务消息诉求](assets/images/tradetrans01-636d42fb6584de6c51692d0889af5c2d_e2c8285314827615.png)

In an e-commerce scenario, when a user places an order, downstream systems are triggered to make changes accordingly. For example, the logistics system must initiate shipment, the credit system must update the user's credit points, and the shopping cart system must clear the user's shopping cart. The processing branches include:

- The order system changes the order status from unpaid to paid.
- The logistics system adds a to-be-shipped record and creates an order logistics record.
- The credit system updates the credit points of the user.
- The shopping cart system clears the shopping cart and updates the user's shopping cart records.

**Traditional XA-based solution: poor performance**

The typical method used to ensure result consistency among the branches is by using a distributed transaction system based on the eXtended Architecture (XA) protocol. The system encapsulates the four call branches into a large transaction that contains four independent transaction branches. While this solution can ensure result consistency, a large number of resources need to be locked to achieve this. This number increases with the number of branches, which results in low system concurrency. As more downstream branches are added, the system performance deteriorates.

**Normal message-based solution: poor result consistency**

A simpler solution based on the XA solution treats the change of the order system as a local transaction and the changes of downstream systems as downstream tasks. Transaction branches are treated as normal messages with added order table transactions. This solution processes messages asynchronously to shorten the processing lifecycle and improves system concurrency. ![普通消息方案](assets/images/transwithnormal-f7d951385520fc18aea8d85f0cd86c27_1788fe79da1e7caa.png)

However, this solution is prone to deliver inconsistent results between the core transaction and transaction branches, for example:

- The message is sent, but the order is not executed. As a result, the whole transaction needs to be rolled back.
- The order is executed, but the message is not sent. In this case, the message has to be resent for consumption.
- Timeout errors cannot be reliably detected, which makes it difficult to determine whether the order needs to be rolled back or an order change needs to be committed.

**Distributed transaction message-based solution of Apache RocketMQ: thorough consistency**

The reason why consistency cannot be guaranteed in the preceding solution is that normal messages do not have the commit, rollback, and unified coordination capabilities of standalone database transactions.

The transactional message feature of Apache RocketMQ supports two-phase commit on the basis of the normal message-based solution. The feature combines two-phase commit and local transaction to achieve global consistency of commit results.
![事务消息](assets/images/tradewithtrans-25be17fcdedb8343a0d2633e693d126d_9b95ff2642872f97.png)

The transactional message solution of Apache RocketMQ is powerful, scalable, and easy to develop. For more information about the working mechanism and process of transactional message, see Working mechanism。

<a id="featurebehavior-04transactionmessage--working-mechanism"></a>

## Working mechanism

**Definition**

Transactional messages are an advanced message type provided by Apache RocketMQ to ensure the ultimate consistency between message production and local transaction.
**Processing workflow**

The following figure shows the interaction process of transactional messages.![事务消息](assets/images/transflow-0b07236d124ddb814aeaf5f6b5f3f72c_22eec6399a6b117e.png)

1. The producer sends a message to a Apache RocketMQ broker.
2. The Apache RocketMQ broker saves the message and marks it as not ready for delivery. A message in this state is called a half message. After that, the broker sends an acknowledgment message (ACK) back to the producer.
3. The producer executes the local transaction.
4. The producer sends a second ACK to the broker to submit the execution result of the local transaction. The execution result may be Commit or Rollback.

   - If the status of the message received by the broker is Commit, the broker marks the half message as deliverable and delivers the message to the consumer.
   - If the status of the message received by the broker is Rollback, the broker rolls back the transaction and does not deliver the half message to the consumer.
5. If the network is disconnected or the producer application is restarted and the broker does not receive a second ACK or the status of the half message is Unknown, the broker waits a period of time and sends a request to a producer in the producer cluster to query the status of the half message.
   **Note** For more information about the length of the period and the maximum number of queries, see[Parameter limits](#introduction-03limits).

6. After the producer receives the request, the producer checks the execution result of the local transaction that corresponds to the half message.
7. The producer sends another ACK to the Apache RocketMQ broker based on the execution result of the local transaction. Then, the broker processes the half message by following Step 4.

**Lifecycle of a transactional message**
![事务消息](assets/images/lifecyclefortrans-fe4a49f1c9fdae5d590a64546722036f_cf19950601e5da1f.png)

- Initialized: The message is built and initialized by the producer and is ready to be sent to a broker.
- Transaction pending: The half message is sent to the broker. However, it is not immediately written to a disk for permanent storage. Instead, it is stored in a transaction storage system. The message is not committed until the system verifies that the second phase of the local transaction is successful. During this period, the message is invisible to downstream consumers.
- Rollback: In the second phase, if the execution result of the transaction is rollback, the broker rolls back the half message and terminates the workflow.
- Ready: The message is sent to the broker, and is visible to the consumer and available for consumption.
- Inflight: The message is obtained by the consumer and processed based on the local business logic of the consumer.

  In this process, the broker waits for the consumer to complete the consumption and submit the consumption result. If no response is received from the consumer in a certain period of time, Apache RocketMQ retries the message. For more information, see [Consumption retry](#featurebehavior-10consumerretrypolicy).
- Acked: The consumer completes consumption and submits the consumption result to the broker. The broker marks whether the current message is successfully consumed.

  By default, Apache RocketMQ retains all messages. When the consumption result is submitted, the message data is logically marked as consumed instead of being deleted immediately. Therefore, the consumer can backtrack the message for re-consumption before it is deleted due to the expiration of the retention period or insufficient storage space.
- Deleted: When the retention period of the message expires or the storage space is insufficient, Apache RocketMQ deletes the earliest saved message from the physical file in a rolling manner. For more information, see [Message storage and cleanup](#featurebehavior-11messagestorepolicy).

<a id="featurebehavior-04transactionmessage--usage-limits"></a>

## Usage limits

**Message type consistency**

Transactional messages can only be used in topics whose MessageType is Transaction.

**Transaction-centered consumption**

The transactional message feature of Apache RocketMQ guarantees that the same transaction can be processed between the local core transaction and downstream branches. However, it does not guarantee the consistency between the message consumption result and the upstream execution result. Therefore, downstream businesses must ensure that messages are processed correctly. We recommend that consumers [Consumption retry](#featurebehavior-10consumerretrypolicy) properly to ensure that the message is processed correctly in the event of failure.

**Intermediate state visibility**

The transactional message feature of Apache RocketMQ ensures only final consistency, which means that status consistency is not guaranteed between an upstream transaction and a downstream branch before a message is delivered to a consumer. Therefore, transactional messages are only suitable for transaction scenarios that accept asynchronous execution.

**Transaction timeout mechanism**

Apache RocketMQ implements a timeout mechanism for transactional messages. Upon receiving a half message, if the broker cannot determine whether to commit or roll back the transaction after a certain period of time, the broker rolls back the message by default. For more information about the timeout period, see[Parameter limits](#introduction-03limits).

<a id="featurebehavior-04transactionmessage--example"></a>

## Example

**Create topic**

For creating topics in Apache RocketMQ 5.0, it is recommended to use the mqadmin tool. However, it is worth noting that message type needs to be added as a property parameter. Here is an example:

```shell
sh mqadmin updateTopic -n <nameserver_address> -t <topic_name> -c <cluster_name> -a +message.type=Transaction
```

**Send messages**

Sending transactional messages is different from sending normal messages in the following aspects:

- Before sending transactional messages, you must enable the transaction checker and associate it with local transaction execution.
- When creating a producer, you must set the transaction checker and bind the list of topics of messages to be sent. These actions enable the built-in transaction checker of the client to restore topics in the event of exceptions.

**Create TRANSACTION Topic**

*NORMAL Topic doesn't support delivery TRANSACTION message, you'll get an error if you send a TRANSACTION message to a NORMAL topic.*

```bash
./bin/mqadmin updatetopic -n localhost:9876 -t TestTopic -c DefaultCluster -a +message.type=TRANSACTION
```

- -c the cluster name
- -t the topic name
- -n the address of the nameserver
- **-a extra attributes，we add an `message.type` attribute with value `TRANSACTION` to support delivery TRANSACTION message.**

The following example uses Java as an example to show you how to send transactional messages:

```java
    // The demo is used to simulate the order table query service to check whether the order transaction is submitted.
    private static boolean checkOrderById(String orderId) {
        return true;
    }
    // The demo is used to simulate the execution result of a local transaction.
    private static boolean doLocalTransaction() {
        return true;
    }
    public static void main(String[] args) throws ClientException {
        ClientServiceProvider provider = new ClientServiceProvider();
        MessageBuilder messageBuilder = new MessageBuilder();
        // Build a transaction producer: The transactional message requires the producer to build a transaction checker to check the intermediate status of an exceptional half message.
        Producer producer = provider.newProducerBuilder()
                .setTransactionChecker(messageView -> {
                    /**
                     * The transaction checker checks whether the local transaction is correctly committed or rolled back based on the business ID, for example, an order ID.
                     * If this order is found in the order table, the order insertion action is committed correctly by the local transaction. If no order is found in the order table, the local transaction has been rolled back.
                     */
                    final String orderId = messageView.getProperties().get("OrderId");
                    if (Strings.isNullOrEmpty(orderId)) {
                        // Message error. Rollback is returned.
                        return TransactionResolution.ROLLBACK;
                    }
                    return checkOrderById(orderId) ? TransactionResolution.COMMIT : TransactionResolution.ROLLBACK;
                })
                .build();
        // Create a transaction branch.
        final Transaction transaction;
        try {
            transaction = producer.beginTransaction();
        } catch (ClientException e) {
            e.printStackTrace();
            // If the transaction branch fails to be created, the transaction is terminated.
            return;
        }
        Message message = messageBuilder.setTopic("topic")
                // Specify the message index key so that the system can use a keyword to accurately locate the message.
                .setKeys("messageKey")
                // Specify the message tag so that consumers can use the tag to filter the message.
                .setTag("messageTag")
                // For transactional messages, a unique ID associated with the local transaction is created to verify the query of the local transaction status.
                .addProperty("OrderId", "xxx")
                // Message body.
                .setBody("messageBody".getBytes())
                .build();
        // Send a half message.
        final SendReceipt sendReceipt;
        try {
            sendReceipt = producer.send(message, transaction);
        } catch (ClientException e) {
            // If the half message fails to be sent, the transaction can be terminated and the message is rolled back.
            return;
        }
        /**
         * Execute the local transaction and check the execution result.
         * 1. If the result is Commit, deliver the message.
         * 2. If the result is Rollback, roll back the message.
         * 3. If an unknown exception occurs, no action is performed until a response is obtained from a half message status query.
         *
         */
        boolean localTransactionOk = doLocalTransaction();
        if (localTransactionOk) {
            try {
                transaction.commit();
            } catch (ClientException e) {
                // You can determine whether to retry the message based on your business requirements. If you do not want to retry the message, you can use the half message status query to submit the transaction status.
                e.printStackTrace();
            }
        } else {
            try {
                transaction.rollback();
            } catch (ClientException e) {
                // We recommend that you record the exception information. This enables you to submit the transaction status based on the half message status query in the event of a rollback exception. Otherwise, you have to retry the message.
                e.printStackTrace();
            }
        }
    }
```

<a id="featurebehavior-04transactionmessage--usage-notes"></a>

## Usage notes

**Avoid timeout of a large number of half messages.**

Apache RocketMQ allows you to check the transaction in the event of an exception during a transaction commit to ensure transaction consistency. However, producers should try to avoid local transactions returning unknown results. A large number of transaction checks can cause system performance to deteriorate and delay transaction processing.

**Properly handle transactions in progress.**

During a half message status query, do not return Rollback or Commit for a transaction in progress. Instead, keep the Unknown status for the transaction.

Generally, the reason why the transaction is in progress is that the transaction execution is slow and the query is frequent. Two solutions are recommended:

- Set the interval for the first query to a larger value. However, this may cause a large delay for messages that depend on the query result.
- Make the program correctly identify ongoing transactions.

- [Scenarios](#featurebehavior-04transactionmessage--scenarios)
- [Working mechanism](#featurebehavior-04transactionmessage--working-mechanism)
- [Usage limits](#featurebehavior-04transactionmessage--usage-limits)
- [Example](#featurebehavior-04transactionmessage--example)
- [Usage notes](#featurebehavior-04transactionmessage--usage-notes)

---

<a id="featurebehavior-05sendretrypolicy"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/05sendretrypolicy/ -->

<!-- page_index: 20 -->

# Sending Retry and Throttling Policy

Version: 5.0

# Sending Retry and Throttling Policy

This topic describes the message sending retry mechanism and throttling mechanism of Apache RocketMQ.

<a id="featurebehavior-05sendretrypolicy--background"></a>

## Background

**Message sending retry**

The sending retry mechanism of Apache RocketMQ answers the following questions:

- Can messages be sent if some nodes are faulty?
- Does a retry request block the call thread?
- What are the shortcomings of sending retry?

**Throttling**

The throttling mechanism of Apache RocketMQ answers the following questions:

- Under what circumstances is throttling triggered?
- What is the client behavior when throttling is triggered?
- How do I avoid triggering throttling and how do I handle unexpected throttling?

<a id="featurebehavior-05sendretrypolicy--message-sending-retry"></a>

## Message sending retry

<a id="featurebehavior-05sendretrypolicy--introduction-to-sending-retry"></a>

### Introduction to sending retry

When a producer client of Apache RocketMQ calls a broker to send a message, the call may fail due to reasons such as network failure or service exception. To ensure message reliability, Apache RocketMQ provides built-in logic in the client SDK to retry failed requests until the requests succeed.

Message sending retries are supported in both the synchronous and asynchronous sending modes.

**Trigger conditions**

Sending retry can be triggered by one of the following conditions:

- The call from the client fails or the request times out.

  - A network exception causes a connection failure or request timeout.
  - The connection is closed because the broker node is shut down or being restarted.
  - The request times out because the broker is running slowly.
- The broker returns an error code.

  - Logic error: an error caused by incorrect running logic.
  - Throttling: throttling triggered by excessive traffic.

> [!NOTE]
> For transaction messages, only [transparent retries](https://github.com/grpc/proposal/blob/master/A6-client-retries.md#transparent-retries) are performed. No retries are performed in network exception or timeout scenarios.

<a id="featurebehavior-05sendretrypolicy--retry-process"></a>

### Retry process

You can specify the maximum number of retries on the producer when the producer initializes messages. When one of the preceding trigger conditions occurs, a producer client tries to send the message again until the message is sent or the maximum number of retries is reached. If the failure persists on the last retry, a call error is returned.

- Synchronous sending: The call thread is blocked until a retry succeeds or the last retry fails. If the last retry fails, the system returns an error code and an exception.
- Asynchronous sending: The call thread is not blocked. The call result is returned as an exception event or success event.

<a id="featurebehavior-05sendretrypolicy--retry-interval"></a>

### Retry interval

- Messages are immediately retried upon failures, except when a retry is triggered by throttling.
- If a retry is triggered by throttling, the message is retried at intervals specified in the exponential backoff protocol. The exponential backoff algorithm uses the following parameters to control retry behavior:

  - INITIAL\_BACKOFF: specifies the interval between the first failure and the first retry. Default value: 1 second.
  - MULTIPLIER : specifies the factor by which to multiply the interval after each failed retry. Default value: 1.6.
  - JITTER : specifies the factor by which to randomize intervals. Default value: 0.2.
  - MAX\_BACKOFF: specifies the upper limit of an interval. Default value: 120 seconds.
  - MIN\_CONNECT\_TIMEOUT: specifies the minimum interval. Default value: 20 seconds.

The following algorithm is recommended:

```java
ConnectWithBackoff()
  current_backoff = INITIAL_BACKOFF
  current_deadline = now() + INITIAL_BACKOFF
  while (TryConnect(Max(current_deadline, now() + MIN_CONNECT_TIMEOUT))!= SUCCESS)
    SleepUntil(current_deadline)
    current_backoff = Min(current_backoff * MULTIPLIER, MAX_BACKOFF)
    current_deadline = now() + current_backoff + UniformRandom(-JITTER * current_backoff, JITTER * current_backoff)
```

For more information, see [connection-backoff.md](https://github.com/grpc/grpc/blob/master/doc/connection-backoff.md).

<a id="featurebehavior-05sendretrypolicy--limits"></a>

### Limits

- Link blocking evaluation: From the retry mechanism, we can see that a producer can configure only the maximum number of retries in the retry process. If a system exception triggers the built-in retry logic of the SDK, the broker must wait for the final retry result, and the sending request link is blocked. Therefore, you must evaluate the timeout duration and maximum number of retries for each call to prevent retries from blocking links.
- Handling of final exceptions: The built-in sending retry mechanism of a Apache RocketMQ client does not ensure that the failed message is successfully sent. If the final retry still fails, the caller must capture the exception and provide redundancy protection to prevent inconsistency in message sending results.
- Duplicate messages: When a Apache RocketMQ producer client resends a message, the client does not know the processing result of the presumably failed message on the broker. As a result, duplicate messages may exist on the broker. Make sure that your business logic can properly handle such situations.

<a id="featurebehavior-05sendretrypolicy--throttling"></a>

## Throttling

<a id="featurebehavior-05sendretrypolicy--introduction-to-throttling"></a>

### Introduction to throttling

When the system capacity usage exceeds the threshold, a Apache RocketMQ broker rejects requests and returns an error to avoid over-burdening the underlying resources.

<a id="featurebehavior-05sendretrypolicy--trigger-conditions"></a>

### Trigger conditions

The throttling mechanism of Apache RocketMQ is triggered by one of the following conditions:

- High storage pressure: As described in the Working mechanism section of [Consumer progress management](#featurebehavior-09consumerprogress), a consumer group starts consuming messages from the maximum offset of the queue. If the consumer group is required to consume from an earlier moment, the storage pressure on the queue surges and throttling is triggered. This happens in backtracking scenarios, such as new business rollout.
- Excessive unconsumed messages on the broker: If consumers are unable to consume at the same rate messages are sent to them, requests pile up in the queue. If the number of messages piling up exceeds the threshold, throttling is triggered to alleviate burden on the downstream system.

<a id="featurebehavior-05sendretrypolicy--behavior"></a>

### Behavior

When throttling is triggered, a producer client receives the following error message and an exception:

- reply-code:530
- reply-text:TOO\_MANY\_REQUESTS

Upon receiving these, the client retries the message according to the exponential backoff protocol. For more information, see [Message sending retry](#featurebehavior-05sendretrypolicy--section-bcp-jf7-hud).

<a id="featurebehavior-05sendretrypolicy--suggestions"></a>

### Suggestions

Suggestions

- How to avoid triggering throttling: Use observable metrics to monitor the system capacity and scale the underlying resources accordingly.
- How to handle throttling: If throttling is triggered and the built-in retry process fails in the client, you can temporarily switch calls to another system.

- [Background](#featurebehavior-05sendretrypolicy--background)
- [Message sending retry](#featurebehavior-05sendretrypolicy--message-sending-retry)
  - [Introduction to sending retry](#featurebehavior-05sendretrypolicy--introduction-to-sending-retry)
  - [Retry process](#featurebehavior-05sendretrypolicy--retry-process)
  - [Retry interval](#featurebehavior-05sendretrypolicy--retry-interval)
  - [Limits](#featurebehavior-05sendretrypolicy--limits)
- [Throttling](#featurebehavior-05sendretrypolicy--throttling)
  - [Introduction to throttling](#featurebehavior-05sendretrypolicy--introduction-to-throttling)
  - [Trigger conditions](#featurebehavior-05sendretrypolicy--trigger-conditions)
  - [Behavior](#featurebehavior-05sendretrypolicy--behavior)
  - [Suggestions](#featurebehavior-05sendretrypolicy--suggestions)

---

<a id="featurebehavior-06consumertype"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/06consumertype/ -->

<!-- page_index: 21 -->

# Consumer Types

Version: 5.0

# Consumer Types

Apache RocketMQ supports the following types of consumers: PushConsumer, SimpleConsumer and PullConsumer. This topic describes the usage, working and retry mechanisms, and scenarios of the three consumer types.

<a id="featurebehavior-06consumertype--background-information"></a>

## Background information

Apache RocketMQ provides the PushConsumer, SimpleConsumer and PullConsumer consumer types. The three consumer types have different integration and control methods that you can use to meet messaging requirements in different business scenarios. The following factors can help you choose a suitable consumer type for your business scenarios:

- Concurrent consumption: How can consumers use the multithreading technique to implement concurrent message consumption for higher message processing efficiency?
- Synchronous or asynchronous message processing: For different integration scenarios, consumers may need to asynchronously distribute messages that they received to the business logic system for processing. How do I implement asynchronous message processing?
- Reliable message processing: How do consumers return response results when they process messages? How do I implement message retries when message errors occur to ensure reliable message processing?

For answers to the preceding problems, see [PushConsumer](#featurebehavior-06consumertype--section-r97-urp-who) and [SimpleConsumer](#featurebehavior-06consumertype--section-b6m-nr8-8ii).

<a id="featurebehavior-06consumertype--feature-overview"></a>

## Feature overview

![消息消费流程](assets/images/consumerflow-eaa625a6a01a048a155a3809a603529a_91c53ea31d494346.png)

The preceding figure shows that message consumption by consumers in Apache RocketMQ involves the following stages: receiving messages, processing messages, and committing the consumption status.

The three types of consumers are suitable for various message consumption scenarios by providing different implementation methods and API operations. The following table describes the differences between the three types of consumers.

> [!INFO]
> PullConsumer is only recommended for integration in a stream processing framework. PushConsumer and simpleConsumer could satisfy most scenarios.
>
> You can switch between the PushConsumer and SimpleConsumer based on your business scenarios. When you switch to a different consumer type, the usage of existing resources and existing business processing tasks in Apache RocketMQ are not affected.

> [!DANGER]
> Mixing consumer type between pullConsumer and other consumer type in same consumerGroup is strictly prohibited.

<table><thead><tr><th>Item</th><th>PushConsumer</th><th>SimpleConsumer</th><th>PullConsumer</th></tr></thead><tbody><tr><td>API operation call</td><td>The callback operation is called to return the consumption result by using a message listener. Consumers can process the consumption logic only within the scope of the message listener.</td><td>Business applications implement message processing and call the corresponding operation to return the consumption result.</td><td>Business applications implement message pulling and processing and call the corresponding operation to return the consumption result.</td></tr><tr><td>Consumption concurrency management</td><td>Apache RocketMQ SDKs are used to manage the number of concurrent threads for message consumption.</td><td>The number of concurrent threads that are used for message consumption is based on the consumption logic of individual business applications.</td><td>The number of concurrent threads that are used for message consumption is based on the consumption logic of individual business applications.</td></tr><tr><td>LoadBalance mechanism</td><td>Message-based load balancing in 5.0 version, Queue-based load balancing in earlier version.</td><td>Message-based load balancing.</td><td>Queue-based load balancing.</td></tr><tr><td>API flexibility</td><td>The API operations are encapsulated and provide poor flexibility.</td><td>The atomic operations provide great flexibility.</td><td>The atomic operations provide great flexibility.</td></tr><tr><td>Scenarios</td><td>This consumer type is suitable for development scenarios that do not require a custom process.</td><td>This consumer type is suitable for development scenarios that require custom processes.</td><td>It is recommended to be integrated only in the stream processing framework scenario</td></tr></tbody></table>
<a id="featurebehavior-06consumertype--pushconsumer"></a>

## PushConsumer

PushConsumer is a consumer type that provides a high degree of encapsulation. Message consumption and consumption result submission are processed by using only the message listener. The message acquisition, consumption status submission, and consumption retries are completed by using Apache RocketMQ client SDKs.

**Usage**

PushConsumer is used in a fixed manner. A message listener is registered with a PushConsumer consumer when the consumer is initialized, and message processing logic is implemented in the message listener. Message acquisition, listener call triggering, and message retries are processed by using Apache RocketMQ SDKs.

Sample code:

```java
// Message consumption example: Use a PushConsumer consumer to consume messages.
ClientServiceProvider provider = ClientServiceProvider.loadService();
String topic = "YourTopic";
FilterExpression filterExpression = new FilterExpression("YourFilterTag", FilterExpressionType.TAG);
PushConsumer pushConsumer = provider.newPushConsumerBuilder()
    // Configure consumer group.
    .setConsumerGroup("YourConsumerGroup")
    // Specify the access point.
    .setClientConfiguration(ClientConfiguration.newBuilder().setEndpoints("YourEndpoint").build())
    // Specify the pre-bound subscriptions.
    .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
    // Set the message listener.
    .setMessageListener(new MessageListener() {
        @Override
        public ConsumeResult consume(MessageView messageView) {
            // Consume the messages and return the consumption result.
            return ConsumeResult.SUCCESS;
        }
    })
    .build();
```

The message listener for a PushConsumer consumer returns one of the following results:

- Consumption success: For example, when you use Apache RocketMQ SDK for Java and a message is consumed, `ConsumeResult.SUCCESS` is returned. The server updates the consumption progress based on the consumption result.
- Consumption failure: For example, when you use Apache RocketMQ SDK for Java and a message fails to be consumed, `ConsumeResult.FAILURE` is returned. Whether Apache RocketMQ retries to consume the message depends on the consumption retry logic.
- Unexpected failure: For example, if an unexpected exception is thrown, the message fails to be consumed. Whether Apache RocketMQ retries to consume the message depends on the consumption retry logic.

If an unexpected error in the message processing logic constantly prevents a message from being consumed by a PushConsumer consumer, the SDK considers that the consumption has timed out and forcibly commits a consumption failure result. Then, the message is processed based on the consumption retry logic. For more information about consumption timeouts, see [Retry policy for push consumers](#featurebehavior-10consumerretrypolicy).

> [!INFO]
> When a consumption timeout occurs, the SDK commits the consumption failure result. However, the current consumption thread may fail to respond to the result and continues to process the message.:::
>
> **Working mechanism**
>
> For PushConsumer, real-time message processing is based on the typical Reactor thread model of the SDK. The SDK has a built-in long polling thread, which pulls messages and stores the messages to a queue. Then, the messages are delivered from the queue to individual message consumption threads. The message listener behaves based on the message consumption logic. The following figure shows the message consumption process of PushConsumer consumers.
> ![PushConsumer原理](assets/images/pushconsumer-26b909b090d4f911a40d5050d3ceba1d_f8edda8f259fb202.png)
>
> **Retry for reliability**
>
> For PushConsumer, the communication between the client SDK and the consumption logic unit is implemented by using only a message listener. The client SDK checks whether the message is consumed based on the result that is returned by the message listener, and performs retries based on the consumption retry logic to ensure message reliability. All messages must be consumed in a synchronous manner. Consumption results are returned when the listener operation call ends. Asynchronous distribution is not allowed. For more information about message retries, see [Retry policy for push consumers](#featurebehavior-10consumerretrypolicy).
>
> To ensure messaging reliability, Apache RocketMQ prohibits the following behaviors in message consumption by PushConsumer consumers.
>
> - Return the consumption result before the consumption of a message is complete. For example, a consumption success result is returned in advance for a message that fails to be consumed later. In this case, Apache RocketMQ cannot check the actual consumption result and does not retry the consumption of the message.
> - Distribute a message to other custom threads from the message listener and return the consumption result in advance. If the message fails to be consumed but a consumption success result is returned in advance, Apache RocketMQ cannot check the actual consumption result and does not retry the consumption of the message.
>
> **Ensured message order**
>
> For [Fifo messages](#featurebehavior-03fifomessage) in Apache RocketMQ, if ordered message consumption is configured for consumer groups, PushConsumer consumers consume messages in the consumption order. When PushConsumer consumers consume messages, the consumption order is ensured without requiring individual business applications to define the consumption order in the business logic.

In Apache RocketMQ, synchronous committing is the prerequisite to ordered message processing. If asynchronous distribution is defined in the business logic, Apache RocketMQ cannot ensure the order of messages.
:::

Scenarios

PushConsumer limits message processing to synchronous processing and restricts the timeout for processing each message. PushConsumer is suitable for the following scenarios:

- Predictable message processing duration: If the message processing duration is not limited, message retries are continuously triggered for messages that require a long processing duration to ensure message reliability. This causes a large number of repeated messages.
- No asynchronization and no custom process: PushConsumer limits the thread model of the consumption logic to the Reactor thread model. The client SDK processes messages based on the maximum throughput. This model is easy to develop, but does not allow asynchronous or custom processes.

<a id="featurebehavior-06consumertype--simpleconsumer"></a>

## SimpleConsumer

SimpleConsumer is a consumer type that supports atomic operations for message processing. Such type of consumers call operations to acquire messages, commit the consumption status, and perform message retries based on the business logic.

**Usage**

SimpleConsumer involves multiple API operations. The corresponding operations are called as needed to obtain and distribute messages to business threads for processing. Then, the commit operation is called to commit message processing results. Sample code:

```java
// Consumption example: When a SimpleConsumer consumer consumes normal messages, the consumer obtain messages and commit message consumption results.
ClientServiceProvider provider = ClientServiceProvider.loadService();
String topic = "YourTopic";
FilterExpression filterExpression = new FilterExpression("YourFilterTag", FilterExpressionType.TAG);
SimpleConsumer simpleConsumer = provider.newSimpleConsumerBuilder()
        // Configure consumer group.
        .setConsumerGroup("YourConsumerGroup")
        // Specify the access point.
        .setClientConfiguration(ClientConfiguration.newBuilder().setEndpoints("YourEndpoint").build())
        // Specify the pre-bound subscriptions.
        .setSubscriptionExpressions(Collections.singletonMap(topic, filterExpression))
        // Specify the max await time when receive messages from the server.
        .setAwaitDuration(Duration.ofSeconds(1))
        .build();
try {
    // A SimpleConsumer consumer must obtain and process messages.
    List<MessageView> messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
    messageViewList.forEach(messageView -> {
        System.out.println(messageView);
        // After consumption is complete, the consumer must invoke ACK to submit the consumption result.
        try {
            simpleConsumer.ack(messageView);
        } catch (ClientException e) {
            logger.error("Failed to ack message, messageId={}", messageView.getMessageId(), e);
        }
    });
} catch (ClientException e) {
    // If the pull fails due to system traffic throttling or other reasons, the consumer must re-initiate the request to obtain the message.
    logger.error("Failed to receive message", e);
}
```

The following table describes the API operations that are provided for SimpleConsumer.

<table><thead><tr><th>Operation</th><th>Description</th><th>Modifiable parameter</th></tr></thead><tbody><tr><td><code>ReceiveMessage</code></td><td>Consumers can call this operation to obtain messages from the server. <strong>Note</strong> Because the server uses distributed storage, the server may return an empty result, although the requested message actually exists on the server.  You can call the ReceiveMessage operation again or increase the concurrency value in the ReceiveMessage operation.</td><td><em> Batch pull size: the number of messages that are obtained at a time. A SimpleConsumer consumer can obtain multiple messages for batch consumption.   </em> Message invisibility duration: the maximum processing duration of a message. This parameter controls the message retry interval if consumption fails. For more information, see <strong>Retry policy for SimpleConsumer</strong>. This parameter is required when you call the <code>ReceiveMessage</code> operation.</td></tr><tr><td><code>AckMessage</code></td><td>After a message is consumed by a consumer, the consumer calls this operation to return the consumption success result to the server.</td><td>None</td></tr><tr><td><code>ChangeInvisibleDuration</code></td><td>In consumption retry scenarios, consumers can call this operation to change the message processing duration to control the message retry interval.</td><td>Message invisibility duration: the maximum processing time of a message. You can call this operation to change the message invisibility duration that is specified in the <code>ReceiveMessage</code> operation. In most cases, this operation is used in scenarios in which you want to increase the message processing duration.</td></tr></tbody></table>

**Retry for reliability**

When SimpleConsumer consumers consume messages, the communication between the client SDK and the Apache RocketMQ server is implemented by using the `ReceiveMessage` and `AckMessage` operations. When the client SDK successfully processes a message, the `AckMessage` operation is called. When the message fails to be processed, no ack message is returned to trigger the message retry mechanism after the specified message invisibility duration elapses. For more information, see [Retry policy for simple consumers](#featurebehavior-10consumerretrypolicy).

**Ensured message order**

In Apache RocketMQ, a SimpleConsumer consumer obtains [Fifo messages](#featurebehavior-03fifomessage) in the order in which they are stored. If a message in a set of ordered messages is not completely processed, the next message in the set of order messages cannot be obtained.

Scenarios

SimpleConsumer provides atomic API operations to obtain messages and commit consumption results. Compared with PushConsumer, SimpleConsumer provides better flexibility. SimpleConsumer is suitable for the following scenarios:

- Uncontrollable message processing duration: If the message processing duration is inestimable, we recommend that you use SimpleConsumer to prevent messages from being processed for an excessively long period of time. You can specify an estimated message processing duration during message consumption. If an existing processing duration is not suitable for your business scenarios, you can call the corresponding API operation to change the message processing duration.
- Asynchronous processing and batch consumption: SimpleConsumer does not involve complex thread encapsulation in the SDK. Business applications can use custom settings. This way, SimpleConsumer consumers can implement asynchronous distribution, batch consumption, and other custom scenarios.
- Custom message consumption rate: When SimpleConsumer is used, business applications call the ReceiveMessage operation to obtain messages. You can adjust the frequency of obtaining message to control the message consumption rate.

<a id="featurebehavior-06consumertype--pullconsumer"></a>

## PullConsumer

To be continued.

<a id="featurebehavior-06consumertype--usage-notes"></a>

## Usage notes

**Specify a proper consumption duration limit for PushConsumer**

We recommend that you limit the message consumption duration for PushConsumer consumers to prevent a message from being processed for a long time. Long-time processing of a message can cause duplicate messages due to message processing timeouts and keep the next message continuously waiting from consumption. If messages are frequently processed for an excessively long period of time, we recommend that you use SimpleConsumer and specify a suitable message invisibility duration based on your business requirements.

- [Background information](#featurebehavior-06consumertype--background-information)
- [Feature overview](#featurebehavior-06consumertype--feature-overview)
- [PushConsumer](#featurebehavior-06consumertype--pushconsumer)
- [SimpleConsumer](#featurebehavior-06consumertype--simpleconsumer)
- [PullConsumer](#featurebehavior-06consumertype--pullconsumer)
- [Usage notes](#featurebehavior-06consumertype--usage-notes)

---

<a id="featurebehavior-07messagefilter"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/07messagefilter/ -->

<!-- page_index: 22 -->

# Message Filtering

Version: 5.0

# Message Filtering

After a consumer is subscribed to a topic, Apache RocketMQ delivers all messages in the topic to the consumer. However, if you want the consumer to receive only messages that are relevant to your business, you can set filters on the Apache RocketMQ broker. This topic describes the message filtering feature and how it works. This topic also describes how messages are classified and provides examples on how different filtering methods can be used.

<a id="featurebehavior-07messagefilter--scenarios"></a>

## Scenarios

Apache RocketMQ follows the publish-subscribe pattern. Apache RocketMQ is a message-oriented-middleware, and is widely used to facilitate communication between distributed upstream and downstream applications. In a real-world scenario, applications may use different methods to consume messages. These applications can all subscribe to the same Apache RocketMQ topic, and filters can be set to allow these applications to receive only the messages relevant to them.

By using the message filtering feature of Apache RocketMQ, you can effectively manage the messages sent to different consumers. This prevents your system from being overburdened by a huge number of messages that are not mission-critical.

The message filtering feature of Apache RocketMQ takes effect at the topic level, allowing you to manage messages of one business that are distributed across multiple services. If you want to manage messages for different businesses, you can subscribe to different topics.

<a id="featurebehavior-07messagefilter--feature-overview"></a>

## Feature overview

**Definition**

The message filtering feature filters messages based on consumer-configured conditions and sends messages that meet the conditions to the consumers.

First, message attributes and tags are defined on Apache RocketMQ producers and consumers. Then filter conditions are set on the consumers, and Apache RocketMQ brokers filter messages based on the conditions and send the filtered messages to the consumers.

**Working mechanism**
![消息过滤](assets/images/messagefilter0-ad2c8360f54b9a622238f8cffea12068_caf3b9ac09fd932a.png)

Message filtering involves the following steps:

- Producer: The producer attaches attributes and tags to messages before initializing the messages. These attributes and tags are used to match the filter conditions set by the consumers.
- Consumer: The consumer calls the subscription registration operation to inform the broker of the subscribed topic and messages, or filter conditions, during message initialization and consumption.
- Broker: Upon receiving a consumer's request for messages, a Apache RocketMQ broker dynamically filters messages based on the expression of filter conditions that is submitted by the consumer, and sends messages that match the filter conditions to the consumer.

**Classification**

Apache RocketMQ supports tag-based filtering and attribute-based SQL filtering. The following table compares the two methods.

<table><thead><tr><th>Item</th><th>Tag-based filtering</th><th>Attribute-based SQL filtering</th></tr></thead><tbody><tr><td>Filter target</td><td>Message tags.</td><td>Message attributes, which include custom attributes and system attributes. Message tags are a system attribute (TAGS).</td></tr><tr><td>Filtering capacity</td><td>Precise match.</td><td>SQL syntax-based match.</td></tr><tr><td>Scenarios</td><td>Simple filtering based on tags.</td><td>Complex filtering involving relationships between tags and attributes.</td></tr></tbody></table>

For more information about how to use the filtering methods, see [Tag-based filtering](#featurebehavior-07messagefilter--section-4vy-ole-5nw) and [Attribute-based SQL filtering](#featurebehavior-07messagefilter--section-ge0-q7e-lsb).

<a id="featurebehavior-07messagefilter--subscription-consistency"></a>

## Subscription consistency

Filter expressions are part of a subscription. According to the publish-subscribe pattern of Apache RocketMQ, the subscription of one consumer must be consistent with that of another within a consumer group, including their filter expressions, to avoid situations where some messages cannot be consumed. For more information, see [Subscriptions](#domainmodel-09subscription).

<a id="featurebehavior-07messagefilter--tag-based-filtering"></a>

## Tag-based filtering

Tag-based filtering is the basic message filtering capability provided by Apache RocketMQ. This feature filters messages based on the tags set on producers. Consumers use the tags to specify which messages to consume.

**Scenarios**

The following figure shows an example in the e-commerce transaction scenario. A series of messages are generated in the process, from placing an order to receiving the product, such as:

- Order messages
- Payment messages
- Logistics messages

These messages are sent to the topic named Trade\_Topic, which have multiple systems as its subscribers, including:

- Payment system: subscribes only to payment messages.
- Logistics system: subscribes only to logistics messages.
- Transaction success rate analysis system: subscribes to order and payment messages.
- Real-time computing system: subscribes to all messages.

![Tag过滤](assets/images/messagefilter-09e82bf396d7c4100ed742e8d0d2c185_91a88116d1c856e0.png)

**Tag setting**

- The producer attaches only one tag to each message before sending the messages.
- The tag is a string of characters. The recommended maximum length of the string is 128 characters.

**Filtering rules**

Tag-based filtering implements precise filtering based on character strings. You can set the following filtering rules:

- Single-tag match: You can set the filter expression to a single tag to receive only messages that carry that tag.
- Multi-tag match: You can set multiple tags in your filter expression to receive messages that carry any one of the tags. Separate the tags with two vertical bars (||). For example, Tag1||Tag2||Tag3 indicates that messages that are attached with Tag1, Tag2, or Tag3 are all sent to the consumer.
- All match: You can use an asterisk (\*) to match all tags, which means that all messages in the topic will be sent to the consumer.

**Example**

- Set a tag and send a message


```java
Message message = messageBuilder.setTopic("topic")
// Specify the message index key so that the system can use a keyword to accurately locate the message.
.setKeys("messageKey")
// Specify the message tag so that consumers can use the tag to filter the message.
// This example indicates that the tag of the message is set to "TagA".
.setTag("TagA")
// Message body.
.setBody("messageBody".getBytes())
.build();
```

- Specify a tag and subscribe to messages


```java
String topic = "Your Topic";
// Subscribe to messages that carry tag "TagA".
FilterExpression filterExpression = new FilterExpression("TagA", FilterExpressionType.TAG);
pushConsumer.subscribe(topic, filterExpression);
```

- Specify multiple tags and subscribe to messages


```java
String topic = "Your Topic";
// Subscribe to messages that carry tag TagA, TagB, or TagC.
FilterExpression filterExpression = new FilterExpression("TagA||TagB||TagC", FilterExpressionType.TAG);
pushConsumer.subscribe(topic, filterExpression);
```

- Subscribe to all the messages in a topic


```java
String topic = "Your Topic";
// Subscribe to all messages.
FilterExpression filterExpression = new FilterExpression("*", FilterExpressionType.TAG);
pushConsumer.subscribe(topic, filterExpression);
```

<a id="featurebehavior-07messagefilter--attribute-based-sql-filtering"></a>

## Attribute-based SQL filtering

Attribute-based SQL filtering is an advanced message filtering method provided byApache RocketMQ. It filters messages based on the attributes and attribute values, which are also called keys and values, that producers configure for messages. Producers can set multiple attributes for a message. Consumers can then specify attributes in SQL expressions to receive certain messages.

> [!INFO]
> Because tags are a system attribute, tag-based filtering is a type of attribute-based SQL filtering. In SQL syntaxes, the tag attribute is represented by TAGS.

**Scenarios**

The following figure shows an example in the e-commerce transaction scenario. A series of messages are generated in the process, from placing an order to receiving the product. The messages are classified into order messages and logistics messages. A region attribute is configured for the logistics messages, and the values of the region attribute are Hangzhou and Shanghai.

- Order messages
- Logistics messages

  - Logistics messages whose value of the region attribute is Hangzhou
  - Logistics messages whose value of the region attribute is Shanghai

These messages are sent to the topic named Trade\_Topic, which has the following systems as its subscribers:

- Logistics system 1: subscribes to only logistics messages whose value of the region attribute is Hangzhou.
- Logistics system 2: subscribes to all logistics messages.
- Order tracking system: subscribes to only order messages.
- Real-time computing system: subscribes to all messages.

![sql过滤](assets/images/messagefilter2-dbf55cf4a63ac6d3b9c5f02603ce92ce_77e4dfcab4e3e36f.png)

**Message attribute setting**

Producers can set custom attributes for messages before sending the messages. Each attribute is a custom key-value pair.

More than one attribute can be set for a message.

**Filtering rules**

You must follow the SQL92 syntax when you write filter expressions. Specifically:

<table><thead><tr><th>Syntax</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td>IS NULL</td><td>Specifies that an attribute does not exist.</td><td><code>a IS NULL</code>: Attribute a does not exist.</td></tr><tr><td>IS NOT NULL</td><td>Specifies that an attribute exists.</td><td><code>a IS NOT NULL</code>: Attribute a exists.</td></tr><tr><td><em> <!-- -->&gt;<!-- --> </em> <!-- -->&gt;<!-- -->=  <em>  &lt;  </em>  &lt;=</td><td>Compares numeric values. The syntax cannot be used to compare strings. If it is used to compare strings, an error is reported when the consumer is started. <strong>Note</strong> Strings that can be converted into numeric values are also considered as numeric values.</td><td><em> <code>a IS NOT NULL AND a &gt; 100</code>: Attribute a exists and the value of Attribute a is greater than 100.   </em> <code>a IS NOT NULL AND a &gt; 'abc'</code>: An error example. abc is a string. Therefore, you cannot compare a with abc.</td></tr><tr><td>BETWEEN xxx AND xxx</td><td>Compares numeric values. The syntax cannot be used to compare strings. If it is used to compare strings, an error is reported when the consumer is started. The syntax is equivalent to <!-- -->&gt;<!-- -->= xxx AND \&lt;= xxx. It means that the value of the attribute is between two numeric values or equal to either of the two numeric values.</td><td><code>a IS NOT NULL AND (a BETWEEN 10 AND 100)</code>: Attribute a exists and the value of Attribute a is greater than or equal to 10 and less than or equal to 100.</td></tr><tr><td>NOT BETWEEN xxx AND xxx</td><td>Compares numeric values. The syntax cannot be used to compare strings. If it is used to compare strings, an error is reported when the consumer is started. The syntax is equivalent to \&lt; xxx OR <!-- -->&gt;<!-- --> xxx. It means that the value of the attribute is less than the left-side numeric value or greater than the right-side numeric value.</td><td><code>a IS NOT NULL AND (a NOT BETWEEN 10 AND 100)</code>: Attribute a exists and the value of Attribute a is less than 10 or greater than 100.</td></tr><tr><td>IN (xxx, xxx)</td><td>Indicates that the value of the attribute is included in a set. The elements in the set can only be strings.</td><td><code>a IS NOT NULL AND (a IN ('abc', 'def'))</code>: Attribute a exists and the value of Attribute a is abc or def.</td></tr><tr><td><em> =  </em>  &lt;<!-- -->&gt;</td><td>The equal to operator and the not equal to operator. They can be used to compare numeric values and strings.</td><td><code>a IS NOT NULL AND (a = 'abc' OR a&lt;&gt;'def')</code>: Attribute a exists and the value of Attribute a is abc or the value of Attribute a is not def.</td></tr><tr><td><em> AND  </em> OR</td><td>The logical AND operator and the logical OR operator. They can be used to combine simple logical functions, and each logical function must be put in parentheses.</td><td><code>a IS NOT NULL AND (a &gt; 100) OR (b IS NULL)</code>: Attribute a exists and the value of Attribute a is greater than 100 or Attribute b does not exist.</td></tr></tbody></table>

SQL attribute-based filtering is implemented by configuring custom message attributes and defining an SQL filter expression. The filter expression may not generate valid results. The Apache RocketMQ broker processes messages based on the following logic:

- Exception handling: If an exception is reported when a filter expression is being evaluated, the broker filters out received messages by default and does not deliver the messages to the consumer. For example, an exception occurs when numeric values and non-numeric values are compared.
- Handling of null values: If the calculated result of the filter expression is NULL or the value is not a Boolean value, the broker filters out received messages by default and does not deliver the messages to the consumer. A Boolean value represents a truth value, which can be true or false. Assume that you did not configure a custom attribute for a message that the producer sends, but this custom attribute is used as a filter condition in the SQL expression. In this case, the evaluation result of the filter expression is NULL.
- Handling of inconsistent numeric values: If the values of the custom message attribute are floating-point numbers but the attribute values used in the filter expression are integers, the broker filters out received messages by default and does not deliver the messages to the consumer.

**Example**

- Set a tag and an attribute for messages and send a message


```java
Message message = messageBuilder.setTopic("topic")
// Specify the message index key so that the system can use a keyword to accurately locate the message.
.setKeys("messageKey")
// Specify the message tag so that consumers can use the tag to filter the message.
// This example indicates that the message tag is set to "messageTag".
.setTag("messageTag")
// You can also set custom attributes for the messages, such as environment, region, and logical branch.
// In this example, the custom attribute is region and the attribute value is Hangzhou.
.addProperty("Region", "Hangzhou")
// Message body.
.setBody("messageBody".getBytes())
.build();
```

- Subscribe to and filter messages based on a custom attribute


```java
String topic = "topic";
// Subscribe only to messages whose value of the region attribute is Hangzhou.
FilterExpression filterExpression = new FilterExpression("Region IS NOT NULL AND Region='Hangzhou'", FilterExpressionType.SQL92);
simpleConsumer.subscribe(topic, filterExpression);
```

- Subscribe to and filter messages based on multiple custom attributes


```java
String topic = "topic";
// Subscribe to messages whose value of the region attribute is Hangzhou and value of the price attribute is greater than 30.
FilterExpression filterExpression = new FilterExpression("Region IS NOT NULL AND price IS NOT NULL AND Region = 'Hangzhou' AND price > 30", FilterExpressionType.SQL92);
simpleConsumer.subscribe(topic, filterExpression);
```

- Subscribe to all the messages in the topic


```java
String topic = "topic";
// Subscribe to all the messages.
FilterExpression filterExpression = new FilterExpression("True", FilterExpressionType.SQL92);
simpleConsumer.subscribe(topic, filterExpression);
```

<a id="featurebehavior-07messagefilter--usage-notes"></a>

## Usage notes

**Set topics and tags for messages properly.**

You can use topics, tags, and attributes to split messages. Pay attention to the following items when you split messages:

- Message type: Messages of different types, such as ordered messages and normal messages, must be split by using different topics. Do not use tags to split message types.
- Business domain: Different business domains and departments must use different topics. For example, the topics must be different for logistics messages and payment messages. Logistics messages can be further divided into ordinary messages and urgent messages by using tags.
- Quantity and importance of messages: Messages that differ in quantity or link importance must be split into different topics.

- [Scenarios](#featurebehavior-07messagefilter--scenarios)
- [Feature overview](#featurebehavior-07messagefilter--feature-overview)
- [Subscription consistency](#featurebehavior-07messagefilter--subscription-consistency)
- [Tag-based filtering](#featurebehavior-07messagefilter--tag-based-filtering)
- [Attribute-based SQL filtering](#featurebehavior-07messagefilter--attribute-based-sql-filtering)
- [Usage notes](#featurebehavior-07messagefilter--usage-notes)

---

<a id="featurebehavior-08consumerloadbalance"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/08consumerloadbalance/ -->

<!-- page_index: 23 -->

# Consumer Load Balancing

Version: 5.0

# Consumer Load Balancing

When consumers in a consumer group pull messages from a Apache RocketMQ topic, a load balancing policy is used to determine how the messages are allocated to the consumers. Load balancing policies improve service concurrency and application scalability. This topic describes the load balancing policies that Apache RocketMQ provides for consumers.

<a id="featurebehavior-08consumerloadbalance--background-information"></a>

## Background information

Familiarizing yourself with the load balancing policies provided by Apache RocketMQ can help you determine the appropriate measures to take when confronted with the following scenarios:

- Disaster recovery: You can determine how messages are retried and switched over when local nodes fail.
- Message ordering: You can better understand how Apache RocketMQ ensures strict first-in-first-out message ordering.
- Horizontal partitioning: You can plan for traffic migration and horizontal scaling operations based on how messages are allocated.

<a id="featurebehavior-08consumerloadbalance--broadcast-consumption-and-cluster-consumption"></a>

## Broadcast consumption and cluster consumption

Apache RocketMQ allows multiple consumer groups to subscribe to the same message and each consumer group to initialize multiple consumers. Consumer groups and consumers can be configured to consume messages in the following scenarios:![Consumption modes](assets/images/consumemode-74d53c59b3266f1f633b1392f5a0f279_3da3979482673965.png)

- **Broadcast consumption across consumer groups** : This scenario is illustrated on the left side of the preceding figure. Each consumer group initializes its own consumer who consumes all messages. Messages are delivered to multiple subscribers from topics in a one-to-many relationship.

  This mode is typically used in scenarios such as gateway push and configuration push.

- **Cluster consumption within a consumer group** : This scenario is illustrated on the right side of the preceding figure. Each consumer group initializes multiple consumers, and the messages are sent to all consumers in the group. This is useful when you want to implement horizontal traffic partitioning and load balancing within the group.

  This mode is suitable for microservice decoupling.

<a id="featurebehavior-08consumerloadbalance--introduction-to-the-load-balancing-policy-for-consumers"></a>

## Introduction to the load balancing policy for consumers

In scenarios that use broadcast consumption, load balancing is not required because each consumer group contains only one consumer.

However, in scenarios that use cluster consumption, each consumer group contains multiple consumers. Load balancing policies can help determine how messages are allocated.

Based on consumer types, load balancing policies can be divided into the following two types:

- [Message-based load balancing](#featurebehavior-08consumerloadbalance--section-x2b-2cu-gpf): the default policy for push consumers and simple consumers.
- [Queue-based load balancing](#featurebehavior-08consumerloadbalance--section-n9m-6xy-y77): the default policy for pull consumers.

<a id="featurebehavior-08consumerloadbalance--message-based-load-balancing"></a>

## Message-based load balancing

**Usage scope**

Message-based load balancing is the only and default policy for push consumers and simple consumers.

**Working mechanism**

Message-based load balancing evenly allocates messages in a topic to multiple consumers in a consumer group.
![Message-based load balancing](assets/images/clustermode-dfd781d08bc0c69111841bda537aa302_0994586d693a3ad2.png)

As shown in the preceding figure, Consumer Group A consists of three consumers: A1, A2, and A3. These three consumers consume the messages of Queue1 in the topic.

> [!NOTE]
> Message-based load balancing ensures that messages in a queue can be concurrently processed by multiple consumers. However, messages are randomly sent to consumers, which means that you cannot specify how messages are allocated to consumers.

Message-based load balancing is based on the acknowledgment semantics of a single message in a topic. After a consumer receives a message, the broker locks the message to ensure that it is invisible to other consumers until it is consumed or times out. This prevents messages of the same queue to be consumed multiple times by different consumers.

**Load policy for ordered messages**

In ordered messages, the order of messages refers to the sequence of multiple messages in a message group. These messages must be processed in the exactly same order as they are stored on the broker. Therefore, message-based load balancing needs to ensure that messages in a message group are consumed in the same order as they are stored on the server. When different consumers process messages in the same group, the system locks the messages in strict accordance with the message order to ensure messages are consumed sequentially.
![Load policy for ordered messages](assets/images/fifoinclustermode-60b2f917ab49333f93029cee178b13f0_63734b473dee737f.png)

In the preceding figure, there are four ordered messages in message group G1 of Queue1. Their saving orders are represented by M1 to M4. During consumption, when the messages M1 and M2 are processed by consumer A1, consumer A2 cannot consume messages M3 and M4 in parallel if the consumption status for M1 and M2 is not submitted. Consumers can only consume messages when the consumption status for preceding messages is submitted.

**Features**

Compared with queue-based load balancing, message-based load balancing has the following features:

- More balanced consumption allocation. In conventional queue-based load balancing, the number of queues and the number of consumers may not be properly balanced. This results in a system where some consumers may be idle while some consumers are overburdened. In comparison, message-based load balancing ensures even load balancing among consumers without requiring you to manage the number of queues and consumers.

- More forgiving to differences in networking capacities. In an online production environment, the processing capabilities of consumers may be different due to actual network conditions or inconsistent networking hardware specifications. If messages are allocated based on queues, there might be cases where some consumers have accumulated messages while some other consumers are idle. In contrast, message-based load balancing allocates messages on demand to achieve a more balanced load distribution among consumers.

- Easier O\&M for queue allocation. In scenarios where conventional queue-based load balancing is used, you must make sure that the number of queues is greater or equal to the number of consumers to ensure that no consumers are idle. This issue is not present with message-based load balancing.

**Scenarios**

Since messages in a queue are discretely allocated to consumers, message-based load balancing is suitable for most online event handling scenarios. In these scenarios, consumers require only basic processing capabilities instead of batch aggregation of messages. As for scenarios such as stream processing and aggregation computing where aggregation and batch processing of messages is required, queue-based load balancing is a better choice.
**Example**

Consumers do not need to perform extra configurations for message-based load balancing. By default, this policy is enabled for push consumers and simple consumers.

```java
        SimpleConsumer simpleConsumer = null;
        // Consumption example 1: When push consumers consume normal messages, they need only to process messages on a message listener and do not need to consider load balancing.
        MessageListener messageListener = new MessageListener() {
            @Override
            public ConsumeResult consume(MessageView messageView) {
                System.out.println(messageView);
                // Return the status based on the consumption result.
                return ConsumeResult.SUCCESS;
            }
        };
        // Consumption example 2: When simple consumers consume normal messages, they obtain and submit messages. The consumers obtain messages based on the subscribed topic and do not need to consider load balancing.
        List<MessageView> messageViewList = null;
        try {
            messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
            messageViewList.forEach(messageView -> {
                System.out.println(messageView);
                // After consumption is complete, consumers must invoke ACK to submit the consumption result.
                try {
                    simpleConsumer.ack(messageView);
                } catch (ClientException e) {
                    e.printStackTrace();
                }
            });
        } catch (ClientException e) {
            // If the pull fails due to system traffic throttling or other reasons, consumers must re-initiate the request to obtain the message.
            e.printStackTrace();
        }
```

<a id="featurebehavior-08consumerloadbalance--queue-based-load-balancing"></a>

## Queue-based load balancing

**Usage scope**

For consumers of broker versions 4.x and 3.x, including PullConsumer, DefaultPushConsumer, DefaultPullConsumer and DefaultLitePullConsumer, only queue-based load balancing can be used.

Working mechanism

In the queue-based load balancing policy, consumers in the same consumer group consume messages in the queue allocated to them. Each queue is consumed by one consumer.
![队列级负载均衡原理](assets/images/clusterqueuemode-ce4f88dc594c1237ba95db2fa9146b8c_640f977b76bf829c.png)

As shown in the preceding figure, the three queues (Queue1, Queue2, and Queue3) in the topic are assigned to two consumers in a consumer group. Since each queue can be assigned to only one consumer, consumer A2 is assigned two queues. If the number of queues is less than the number of consumers, some consumers will not have queues assigned to them.

Queue-based load balancing allocates messages based on operating data such as the number of queues and the number of consumers. Each queue is bound to a specific consumer. Then, each consumer processes messages according to the consumption semantics of obtaining messages > submitting offsets > persisting offsets. The consumption status is not returned to the queue when consumers obtain messages. Therefore, to avoid repeated consumption of messages by multiple consumers, each queue can be consumed by only one consumer.

> [!NOTE]
> Queue-based load balancing guarantees that a queue is processed by only one consumer. However, the implementation of this policy depends on the information negotiation mechanism between the consumer and the broker.
>
> Apache RocketMQ does not guarantee that messages in a queue are processed by only one consumer. Therefore, when the number of consumers and the number of queues change, temporary inconsistency in queue allocation may occur, which causes a small number of messages to be processed more than once.

**Features**

Compared with message-based load balancing, the granularity of queue-based load balancing is larger and less flexible. However, queue-based load balancing is ideal for stream processing scenarios. It ensures that messages in a queue are processed by one consumer. Therefore, queue-based load balancing is more suitable for scenarios where you want to process aggregated messages or messages in batches.

**Scenarios**

Queue-based load balancing is applicable to scenarios where you want to process aggregated messages or messages in batches. These are common scenarios in stream computing and data aggregation applications.

**Example**

Consumers do not need to perform extra configurations for queue-based load balancing. By default, this policy is enabled for pull consumers of broker versions 4.x and 3.x.

For more information about the sample code, visit the [code library of Apache RocketMQ](https://github.com/apache/rocketmq/blob/develop/example/src/main/java/org/apache/rocketmq/example/simple/LitePullConsumerAssign.java).

<a id="featurebehavior-08consumerloadbalance--version-compatibility"></a>

## Version compatibility

The message-based load balancing policy is available from broker version 5.0 of Apache RocketMQ. For broker versions 4.x and 3.x, only the queue-based load balancing policy is available.

Both the message-based and queue-based load balancing policies are available for broker version 5.x of Apache RocketMQ. Which policy is effective depends on the client version and consumer type.

<a id="featurebehavior-08consumerloadbalance--usage-notes"></a>

## Usage notes

**Implement message idempotence for consumption logic.**

Both the message-based and queue-based load balancing policies trigger temporary re-balancing in scenarios such as adding consumers, removing consumers, and broker scaling. This may cause temporary load inconsistency and result in a small number of messages being consumed more than once. Therefore, it is necessary to perform deduplication to ensure idempotence for message consumption.

- [Background information](#featurebehavior-08consumerloadbalance--background-information)
- [Broadcast consumption and cluster consumption](#featurebehavior-08consumerloadbalance--broadcast-consumption-and-cluster-consumption)
- [Introduction to the load balancing policy for consumers](#featurebehavior-08consumerloadbalance--introduction-to-the-load-balancing-policy-for-consumers)
- [Message-based load balancing](#featurebehavior-08consumerloadbalance--message-based-load-balancing)
- [Queue-based load balancing](#featurebehavior-08consumerloadbalance--queue-based-load-balancing)
- [Version compatibility](#featurebehavior-08consumerloadbalance--version-compatibility)
- [Usage notes](#featurebehavior-08consumerloadbalance--usage-notes)

---

<a id="featurebehavior-09consumerprogress"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/09consumerprogress/ -->

<!-- page_index: 24 -->

# Consumer Progress Management

Version: 5.0

# Consumer Progress Management

Apache RocketMQ uses consumer offsets to manage the progress of consumers. This topic describes the consumer progress management mechanism of Apache RocketMQ.

<a id="featurebehavior-09consumerprogress--background"></a>

## Background

In Apache RocketMQ, messages can be generated before or after they are subscribed to by consumers. So how does a consumer know where to start consuming messages, and how are consumed messages marked? In order to overcome this challenge, Apache RocketMQ has developed the consumer progress management mechanism.

The consumer progress management mechanism of Apache RocketMQ solves the following problems:

- Where does a client start to consume messages after it is launched?
- How is a consumed message marked to ensure that it is not processed multiple times?
- Can a message be consumed again by the same client if a service exception occurs?

<a id="featurebehavior-09consumerprogress--working-mechanism"></a>

## Working mechanism

**Message Offset**

In Apache RocketMQ, messages are queued in topics in the order that they arrive, and are assigned a unique Long-type coordinate. This is also known as the offset of the message. For more information about the individual definitions of these concepts, see [Topic](#domainmodel-02topic) and [Message queue](#domainmodel-03messagequeue).

Theoretically speaking, a message queue can store an indefinite number of messages. Therefore, the value range of offset is from 0 to Long.MAX\_VALUE. You can locate any message based on its topic, queue, and offset. The following figure shows the relationship between these three concepts.![Offset](assets/images/consumerprogress-da5f38e59a7fcb4ff40325b0f7fbf8a3_bfcb91485f7b7a53.png)

In Apache RocketMQ, the offset of the earliest message in a queue is called the minimum offset (MinOffset), and the offset of the latest message is called the maximum offset (MaxOffset). Although a message queue can theoretically hold an indefinite number of messages, the physical machines on which they are stored have limited space. Therefore, Apache RocketMQ dynamically deletes the earliest message from a queue, and the MinOffset and MaxOffset values of the queue increase constantly. ![Consumer offset update](assets/images/updateprogress-02d1a9de72aa4f72c3b1e1c6e03d2407_b2f12fafcc8310f5.png)

**Consumer Offset**

Apache RocketMQ follows the publish-subscribe pattern. Multiple consumer groups can subscribe to the same queue. In scenarios such as this, when a consumer deletes a message after consuming it, the other consumers are unable to consume it.

To prevent this from happening, Apache RocketMQ uses consumer offsets to manage the message consumption progress of different consumers. Apache RocketMQ does not delete a message immediately after it is consumed. Instead, Apache RocketMQ maintains a record of the latest message consumed by a consumer group, which is also called a consumer offset.

In the event that a client is restarted, the consumer is able to continue processing messages based on the consumer offset saved in a server. If the consumer offset expires and gets deleted, the MinOffset value of the queue saved in the server is used as the consumer offset.

> [!INFO]
> Consumer offsets are saved to and restored from Apache RocketMQ servers, and are not related to any specific consumer. Therefore, Apache RocketMQ can restore consumer progress across different consumers.

The following figure shows the relationships between the minimum offset, maximum offset, and a consumer offset in a message queue.![Consumer progress](assets/images/consumerprogress1-07d9f77dd7e62f2250330ed36f36fe3c_0d2a6b2569a9d1c2.png)

- The consumer offset is always smaller than or equal to the maximum offset.

  - If messages are produced and consumed at the same rate and there are no unconsumed messages in the queue, the consumer offset is the same as the maximum offset.
  - If messages are consumed slower than they are produced, unconsumed messages exist in the queue. Consequently, the consumer offset is smaller than the maximum offset, and the difference is the number of unconsumed messages.
- Typically, the consumer offset is larger than or equal to the minimum offset. If the consumer offset is smaller than the minimum offset, the consumer is unable to consume messages. In this case, the server restores the correct consumer offset to the consumer.

**Initial consumer offset**

An initial consumer offset is the consumer offset saved in a server when a consumer group starts to consume a message queue for the first time.

Apache RocketMQ uses the maximum offset of a message queue when a consumer obtains messages from the queue for the first time as the initial consumer offset. In other words, the consumer starts consuming from the latest message in the queue.

<a id="featurebehavior-09consumerprogress--reset-consumer-offset"></a>

## Reset consumer offset

If the initial or current consumer offset is not aligned with the state of your business, you can reset the consumer offset to adjust your consumer progress.

**Scenarios**

- Improper initial consumer offset: The initial consumer offset is the maximum offset of the queue, that is, the client starts consuming from the latest message. If you need to consume earlier messages, you can reset the consumer offset to that of an earlier message.
- Consumer lag: A large number of messages can accumulate if the consumer is unable to keep up with the speed at which messages are generated. If the accumulated messages are not mission-critical, you can adjust the consumer offset to a larger value to skip these messages and alleviate downstream burden.
- Business backtracking and corrective processing: If you want to re-consume messages that have been incorrectly consumed due to business errors, you can set the consumer offset to a smaller value.

**The consumer offset reset feature**

The consumer offset reset feature of Apache RocketMQ allows you to:

- Reset a consumer offset to any offset in the message queue.
- Reset a consumer offset to a specific point in time. The server adjusts the consumer offset to an offset closest to the time point.

**Limits**

- After you reset a consumer offset, the consumer starts to consume messages from the new offset. In backtracking scenarios, the consumer starts with historical messages that are mostly cold data. Referred to as cold reads, this may cause undue burden to your system. Evaluate the risks and benefits before you proceed with this operation. We recommend that you implement strict control policies for this permission to prevent abuse and frequent resets.
- Apache RocketMQ allows you to reset the consumer offset only for visible messages. You cannot reset the offset for messages that are in the scheduling or retry pending states. For more information, see [Delay messages](#featurebehavior-02delaymessage) and [Consumption retry](#featurebehavior-10consumerretrypolicy).

<a id="featurebehavior-09consumerprogress--version-compatibility"></a>

## Version compatibility

Servers have different definitions for the initial consumer offset in different versions of Apache RocketMQ.

- In 4.x and 3.x versions, the initial consumer offset is defined to the message status of a queue.
- In 5.x versions, the initial consumer offset is the maximum offset of the queue at the time when the consumer starts receiving messages.

Therefore, if you upgrade from an earlier version, you must pay attention to the initial consumer offset when you launch your client.

<a id="featurebehavior-09consumerprogress--usage-notes"></a>

## Usage notes

**Strictly control the reset permissions**

Resetting the consumer offset incurs additional burden on the system and may affect message reads and writes. Therefore, we recommend that you evaluate the risks and benefits before you perform this operation.

- [Background](#featurebehavior-09consumerprogress--background)
- [Working mechanism](#featurebehavior-09consumerprogress--working-mechanism)
- [Reset consumer offset](#featurebehavior-09consumerprogress--reset-consumer-offset)
- [Version compatibility](#featurebehavior-09consumerprogress--version-compatibility)
- [Usage notes](#featurebehavior-09consumerprogress--usage-notes)

---

<a id="featurebehavior-10consumerretrypolicy"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/10consumerretrypolicy/ -->

<!-- page_index: 25 -->

# Consumption Retry

Version: 5.0

# Consumption Retry

If a message fails to be consumed, Apache RocketMQ redelivers the message based on a consumption retry policy. This helps remove some faults. This topic describes the working mechanism, version compatibility, and usage notes of the consumption retry feature.

<a id="featurebehavior-10consumerretrypolicy--scenarios"></a>

## Scenarios

The consumption retry feature of Apache RocketMQ ensures consumption integrity that may be affected by the failure of a business processing logic. This feature is a protective measure against business logic failures. It cannot be used to control the business process.

The feature is suitable for use in the following scenarios:

- The business fails because of the message content. For example, the transaction status is not returned and the business is expected to be restored within a specific period of time.
- The cause of consumption failure does not affect business continuity. The failure has a small possibility of occurring and subsequent messages are very likely to be delivered and consumed as expected. In these cases, you can use the retry mechanism to redeliver the message to avoid blocking the process.

Do not use the feature in the following scenarios:

- Consumption failure is used as a condition to divert message flows in the processing logic. The processing logic assumes that many messages will fail to be consumed.
- Consumption failure is used to limit the rate of message processing. Rate limiting should be used to temporarily stack excessive messages in the queue for later processing instead of making the messages enter the retry link.

<a id="featurebehavior-10consumerretrypolicy--purpose"></a>

## Purpose

A common issue of message middleware in asynchronous decoupling is how to ensure the integrity of the entire call link if the downstream service fails to process messages. As a financial-grade reliable message middleware service, Apache RocketMQ uses a well-designed message acknowledgement and retry mechanism to ensure that every message is processed according to business expectations.

Understanding the message acknowledgement and retry mechanism of Apache RocketMQ helps solve the following issues:

- How to ensure that every message is processed: You can ensure that every message is processed based on their consumer logic and business statuses are consistent.
- How to ensure that the status of messages that are being processed are correct when an exception occurs: You can ensure the correct message status when an exception, such as power failure, occurs.

<a id="featurebehavior-10consumerretrypolicy--policy-overview"></a>

## Policy overview

When the consumption retry feature is enabled, the Apache RocketMQ broker resends a message when the message fails to be consumed. If the message fails to be consumed even after a specified number of retries, the broker sends the message to the dead-letter queue.

**Trigger conditions**

- A message fails to be consumed. In this case, the consumer returns a failure status or the system throws an exception.
- A timeout error occurs or a message stays in a push consumer queue for an excessive period of time.

**Behaviors**

- Retry process state machine: controls the state and the change logic of messages in the retry process.
- Retry interval: the time that elapses from when a consumption failure or timeout occurs to when the message is retried.
- Maximum retries: the maximum number of times that a message can be retried for consumption.

**Policy differences**

Message retry policies use different retry mechanisms and configuration methods based on the consumer type. The following table describes the differences between the policies.

<table><thead><tr><th>Consumer type</th><th>Retry process state machine</th><th>Retry interval</th><th>Maximum number of retries</th></tr></thead><tbody><tr><td>PushConsumer</td><td><em> Ready  </em> Inflight  <em> WaitingRetry  </em> Commit  * DLQ</td><td>Specified in the metadata when a consumer group is created. <em> Unordered messages: incremental  </em> Ordered messages: fixed</td><td>Specified in the metadata when a consumer group is created.</td></tr><tr><td>SimpleConsumer</td><td><em> Ready  </em> Inflight  <em> Commit  </em> DLQ</td><td>Specified in the InvisibleDuration parameter in the API.</td><td>Specified in the metadata when a consumer group is created.</td></tr></tbody></table>

For more information about retry policies, see [Retry policy for push consumers](#featurebehavior-10consumerretrypolicy--section-qqo-bil-rc6) and [Retry policy for simple consumers](#featurebehavior-10consumerretrypolicy--section-my2-2au-7gl).

<a id="featurebehavior-10consumerretrypolicy--retry-policy-for-pushconsumer"></a>

## Retry policy for PushConsumer

**Retry process state machine**

When a push consumer consumes a message, the message can be in one of the following states:![State machine for push consumers](assets/images/retrymachinestatus-37ddbd0a20b8736e34bb88f565945d16_62d4736fcdf6993f.png)

- Ready The message is waiting to be consumed on the Apache RocketMQ broker.

- Inflight The message has been obtained and is being consumed by the consumer. However, the consumption result has not been returned.

- WaitingRetry This state is exclusive to push consumers. The message fails to be consumed or a timeout error occurs when the broker waits for the consumer to return the consumption status. In these cases, the consumption retry logic is triggered. If the maximum number of retries is not reached, the message goes back to the Ready state after the retry interval elapses. Messages that are in the Ready state can be consumed again. You can increase the interval between retries to prevent frequent retries.

- Commit The message is consumed. After the consumer returns a success response, the state machine can be terminated.

- DLQ A preventive measure for the consumption logic. If the message fails to be consumed even after the maximum number of retries is reached, the message is no longer retried and is sent to the dead-letter queue. You can consume messages in a dead-letter queue to restore your business.

When a message is retried, its state changes from Ready to Inflight and then to WaitingRetry. The interval between two consumptions is the sum of the actual time spent on consumption and the retry interval. The maximum consumption interval is specified by a system parameter on the broker and cannot be exceeded. ![Retry interval](assets/images/retrytimeline-27247ef53fbcf08c745b9f7d356de6f9_d57496faac071ce1.png)

**Maximum number of retries**

The maximum number of retries for a push consumer is specified in the metadata when the consumer group is created. For more information, see [Consumer groups](#domainmodel-07consumergroup).

For example, if the maximum number of retries is three, the message can be delivered four times: one original attempt and three retries.

**Retry interval**

- Unordered messages (messages that are not ordered messages): incremental. The following table describes the details.

  <table><thead><tr><th>Retry number</th><th>Interval</th><th>Retry number</th><th>Interval</th></tr></thead><tbody><tr><td>1</td><td>10 seconds</td><td>9</td><td>7 minutes</td></tr><tr><td>2</td><td>30 seconds</td><td>10</td><td>8 minutes</td></tr><tr><td>3</td><td>1 minute</td><td>11</td><td>9 minutes</td></tr><tr><td>4</td><td>2 minutes</td><td>12</td><td>10 minutes</td></tr><tr><td>5</td><td>3 minutes</td><td>13</td><td>20 minutes</td></tr><tr><td>6</td><td>4 minutes</td><td>14</td><td>30 minutes</td></tr><tr><td>7</td><td>5 minutes</td><td>15</td><td>1 hour</td></tr><tr><td>8</td><td>6 minutes</td><td>16</td><td>2 hours</td></tr></tbody></table>

> [!INFO]
> If the number of retries exceeds 16, the interval of each subsequent retry is 2 hours.

- Ordered messages: fixed. For more information, see[Parameter limits](#introduction-03limits).

**Example**

For push consumers, a message retry is triggered only by the status code of consumption failure. Unexpected exceptions are also captured by the SDK.

```java
        SimpleConsumer simpleConsumer = null;
        // Consumption example: Consume normal messages as a push consumer and trigger a message retry by using a consumption failure.
        MessageListener messageListener = new MessageListener() {
            @Override
            public ConsumeResult consume(MessageView messageView) {
                System.out.println(messageView);
                // Retry the message until the maximum number of retries is reached.
                return ConsumeResult.FAILURE;
            }
        };
```

<a id="featurebehavior-10consumerretrypolicy--retry-policy-for-simpleconsumer"></a>

## Retry policy for SimpleConsumer

**Retry process state machine**

When a simple consumer consumes a message, the message can be in one of the following states:![Push consumer state machine](assets/images/simplemachinestatus-1844bd0115b315e32661cf20b1732db0_54fe3963243a7c20.png)

- Ready The message is waiting to be consumed on the Apache RocketMQ broker.
- Inflight The message has been obtained and is being consumed by the consumer. However, the consumption result has not been returned.
- Commit The message is consumed. After the consumer returns a success response, the state machine can be terminated.
- DLQ A preventive measure for the consumption logic. If the message fails to be consumed even after the maximum number of retries is reached, the message is no longer retried and is sent to the dead-letter queue. You can consume messages in a dead-letter queue to restore your business.

The retry interval is fixed and pre-allocated. It is configured in the InvisibleDuration parameter by the consumer when the consumer calls the API. The parameter specifies the maximum processing duration of the message. When a message is retried, the value of the parameter is reused. You do not need to configure the interval for the subsequent retries.
![Retry by a simple consumer](assets/images/simpletimeline-130218b5dca33422638d2ee6409a8330_94be4f4098d838fb.png)

Because the InvisibleDuration value is pre-allocated, it may not meet your business requirements. You can change it in the code that is used to call the API.

For example, if you set the InvisibleDuration value to 20 ms and a message cannot be processed within the duration, you can change the value to a larger value to avoid triggering the retry mechanism.

Before you can change the InvisibleDuration value, the following conditions must be met:

- A timeout error has not occurred on the current message.
- A consumption status of the current message is not returned.

As shown in the following figure, the change takes effect immediately, that is, the InvisibleDuration value is recalculated from the point in time when the API is called.
![Modify the InvisibleDuration value](assets/images/changeinvisibletime-769fd45237e26f2ff333ee1149e66d47_3ed443c82457b57c.png)

**Maximum number of retries**

The maximum number of retries for a simple consumer is specified in the metadata when the consumer group is created. For more information, see [Consumer groups](#domainmodel-07consumergroup).

**Message retry interval**

Message retry interval = InvisibleDuration value − Actual duration of message processing

The consumption retry interval is therefore controlled by the InvisibleDuration value. For example, if the InvisibleDuration value is 30 ms and a consumption failure is returned 10 ms after the processing starts, the time to the next retry is 20 ms, which means that the retry interval is 20 ms. If no consumption result is returned within 30 ms, a timeout error occurs and a retry is triggered. Then, the retry interval is 0 ms.

**Examples**

Simple consumers need only to wait for a message to be retried.

```java
 // Consumption example: Consume normal messages as a simple consumer. If you want a message to be retried, do not process the message. Wait for it to time out, and the broker retries it automatically.
        List<MessageView> messageViewList = null;
        try {
            messageViewList = simpleConsumer.receive(10, Duration.ofSeconds(30));
            messageViewList.forEach(messageView -> {
                System.out.println(messageView);
                // If you want a message to be retried after it fails to be consumed, ignore the failure and wait for the message to be visible. Then try to obtain it again from the broker.
            });
        } catch (ClientException e) {
            // If the message fails to be pulled due to throttling or other reasons, you must re-initiate the request to obtain the message.
            e.printStackTrace();
        }
```

<a id="featurebehavior-10consumerretrypolicy--usage-notes"></a>

## Usage notes

**Do not use consumption retry to deal with consumption throttling**

As mentioned in [Scenarios](#featurebehavior-10consumerretrypolicy--section-d2i-0sk-rtf), message retry is suitable for scenarios where failure of business processing and message consumption is a small-possibility event. Message retry is not suitable for scenarios where the failure continues, such as consumption throttling.

- Incorrect example:Return consumption failures to trigger retries when the current consumption rate is higher than the upper limit.
- Correct example:Obtain and consume messages at a later time if the current consumption rate is higher than limited.

**Set a proper number of retries to avoid infinite retries**

Although Apache RocketMQ supports custom numbers of consumption retries, we recommend that you set a small number of retries and a long retry interval to reduce the burden on the system. Avoid a large number of retries or infinite retries.

- [Scenarios](#featurebehavior-10consumerretrypolicy--scenarios)
- [Purpose](#featurebehavior-10consumerretrypolicy--purpose)
- [Policy overview](#featurebehavior-10consumerretrypolicy--policy-overview)
- [Retry policy for PushConsumer](#featurebehavior-10consumerretrypolicy--retry-policy-for-pushconsumer)
- [Retry policy for SimpleConsumer](#featurebehavior-10consumerretrypolicy--retry-policy-for-simpleconsumer)
- [Usage notes](#featurebehavior-10consumerretrypolicy--usage-notes)

---

<a id="featurebehavior-11messagestorepolicy"></a>

<!-- source_url: https://rocketmq.apache.org/docs/featureBehavior/11messagestorepolicy/ -->

<!-- page_index: 26 -->

# Message Storage and Cleanup

Version: 5.0

# Message Storage and Cleanup

This topic describes how Apache RocketMQ stores messages, including storage granularity, determination criteria, and processing policies.

<a id="featurebehavior-11messagestorepolicy--background-information"></a>

## Background information

Based on the definition of [MessageQueue](#domainmodel-03messagequeue) in Apache RocketMQ, messages are stored in queues in the order in which the messages are received by the broker. In theory, the number of messages that a queue can store is unlimited.

In actual deployment scenarios, messages cannot be permanently stored because the physical storage space of a broker is limited. Therefore, when you deploy messages, you need to answer three questions: What criteria are used to determine how to store messages on a broker? What granularity is used to manage the stored messages? What measures must be taken when message storage usage exceeds the limit? The message storage and cleanup mechanisms of Apache RocketMQ provide answers to the preceding questions.

You can better perform O\&M by using message storage and cleanup mechanisms based on the following aspects:

- SLA for storage: Storage duration refers to the time period in which users can obtain messages. This feature is suitable for scenarios in which a long consumption period is required, messages are accumulated, and fault recovery is required.
- Evaluation and control of storage costs: Apache RocketMQ stores messages on disks. You can evaluate storage space and reserve storage resources in advance.

<a id="featurebehavior-11messagestorepolicy--message-storage-mechanism"></a>

## Message storage mechanism

**Working mechanism**

Each node of Apache RocketMQ stores messages for a specific period of time. This period of time, known as storage duration, is used to determine how long a message is stored. Messages that are within the storage duration are retained, while messages that exceed the duration limit are cleaned up, regardless of whether they are consumed.

The following section describes the items related to the message storage mechanism:

- Management granularity: Apache RocketMQ manages message storage duration based on nodes.
- Determination criterion: Message storage duration is used as the determination criterion. Compared with message quantity or size, storage duration can help you evaluate the values of messages in a more efficient manner.
- The message storage and consumption status are unrelated: The message storage duration in Apache RocketMQ starts from the point in time when the message is produced and is not related to consumption status. You can simplify the message storage mechanism by using a unified calculation strategy.

The following figure shows how messages are stored in a queue.![消息存储](assets/images/cleanpolicy-aa812156263be0605a22b9348ebdc22c_e4bfa6a7df68fd40.png)

> [!NOTE]
> **Management granularity**
>
> Apache RocketMQ manages storage duration based on broker nodes due to the following reasons:
>
> - Advantages of message storage: Apache RocketMQ manages physical data by using a unified two-level organization method that consists of physical log queues and lightweight logical queues. This method provides the benefits of ordered read and write operations, high throughput, and high performance. However, you cannot manage message storage based on topics or queues by using this method.
> - Capacity assurance and data security: Even though Apache RocketMQ generates independent storage files based on topics or queues, the files share the same underlying storage medium. You can manage storage duration based on topics or queues in a flexible manner. The SLA for storage may not be fulfilled if the storage capacity of the cluster becomes insufficient. If you want to manage messages in a secure manner, the best way is to store messages by using different storage durations in different clusters.

**Relationship between message storage and consumption status**

Apache RocketMQ manages message storage duration in a centralized manner, regardless of whether the messages are consumed.

Messages may be accumulated in a queue due to inactive consumers or abnormal consumption. There is no effective solution to this problem for the time being. If all messages that are not consumed are retained, the storage space is quickly used up. This affects the speed of read and write operations for new messages.

Consumers can manage messages based on storage duration to determine the lifecycle of each message. Consumers can consume a message any time during the storage duration, or consume the message multiple times by using the [Reset a consumer offset](#featurebehavior-09consumerprogress) feature.

**Message Storage File Structure**
Apache RocketMQ messages are stored by default in local disk files, and the root directory of the storage files is determined by the configuration parameter storePathRootDir. The storage structure is shown in the following figure, where the commitlog folder stores the physical message files, the consumeCQueue folder stores the logical queue indexes.
![MessageStore](assets/images/store-2eb2d519dd4030480ca3ea63f2dc1b70_a1d1179b6dac2745.jpg)

<a id="featurebehavior-11messagestorepolicy--message-cleanup-mechanism"></a>

## Message cleanup mechanism

In Apache RocketMQ, the storage duration of a message is different from the actual storage duration. This is because messages are stored in local disks. When the local disk space becomes insufficient, the system forcibly deletes messages to ensure service stability. As a result, the actual storage duration is shorter than the specified storage duration.

The Apache RocketMQ storage system is developed based on the cloud-native technologies of Alibaba Cloud. This allows all instances to use storage space without imposing limits on storage capacity. All messages are stored based on their specified storage duration. You do not need to worry about the deletion of messages due to insufficient storage space.

<a id="featurebehavior-11messagestorepolicy--usage-notes"></a>

## Usage notes

**Increase the storage duration based on your business requirements**

Apache RocketMQ controls whether to retain messages based on storage duration. We recommend that you specify a longer storage duration based on your business requirements. A longer storage duration allows you more room to perform operations for emergency fault recovery, emergency troubleshooting, and message backtracking.

- [Background information](#featurebehavior-11messagestorepolicy--background-information)
- [Message storage mechanism](#featurebehavior-11messagestorepolicy--message-storage-mechanism)
- [Message cleanup mechanism](#featurebehavior-11messagestorepolicy--message-cleanup-mechanism)
- [Usage notes](#featurebehavior-11messagestorepolicy--usage-notes)

---

<a id="deploymentoperations-01deploy"></a>

<!-- source_url: https://rocketmq.apache.org/docs/deploymentOperations/01deploy/ -->

<!-- page_index: 27 -->

# Deployment Method

Version: 5.0

# Deployment Method

In the Apache RocketMQ 5.0 version, basic message sending and receiving is completed, including the NameServer, Broker, and Proxy components. In the 5.0 version, the Proxy and Broker can be divided into Local mode and Cluster mode according to actual requirements. Generally, if there are no special requirements or if you follow the approach of smoothly upgrading from earlier versions, you can use Local mode.

- In Local mode, the Broker and Proxy are deployed in the same process, and you can run it by simply adding a Proxy configuration based on the original Broker configuration.
- In Cluster mode, the Broker and Proxy are deployed separately, that is, in addition to the existing cluster, you can deploy the Proxy separately.

<a id="deploymentoperations-01deploy--deployment-in-local-mode"></a>

## Deployment in Local Mode

Since the Proxy and Broker are deployed in the same process in Local mode, the Proxy is stateless, so the main cluster configuration can still be based on the Broker.

<a id="deploymentoperations-01deploy--start-nameserver"></a>

### Start NameServer

```bash
### Start Name Server first
$ nohup sh mqnamesrv &

### Verify that the Name Server has started successfully.
$ tail -f ~/logs/rocketmqlogs/namesrv.log The Name Server boot success...
```

<a id="deploymentoperations-01deploy--start-brokerproxy"></a>

### Start Broker+Proxy

<a id="deploymentoperations-01deploy--single-node-single-replica-mode"></a>

#### Single Node Single Replica Mode

> [!WARNING]
> **caution**
> This method carries a high risk, as there is only one node for the Broker, and if the Broker restarts or goes down, the entire service will be unavailable. It is not recommended in online environments, but can be used for local testing.

```bash
$ nohup sh bin/mqbroker -n localhost:9876 --enable-proxy &

### Verify that the Broker has started successfully, for example, the broker IP is 192.168.1.2, and the name is broker-A
$ tail -f ~/logs/rocketmqlogs/broker_default.log The broker[xxx, 192.169.1.2:10911] boot success...
```

<a id="deploymentoperations-01deploy--multiple-node-cluster-single-replica-mode"></a>

#### Multiple Node (Cluster) Single Replica Mode

All nodes in a cluster are deployed with the Master role, and no Slave replicas are deployed, such as 2 Masters or 3 Masters. The advantages and disadvantages of this mode are as follows:

- Advantages: Simple configuration, a single Master's downtime or restart has no effect on the application, and when the disk is configured as RAID10, even if the machine goes down irrecoverably, the message will not be lost due to the reliability of the RAID10 disk (asynchronous disk flush loses a small amount of messages, synchronous disk flush does not lose a single message), and has the highest performance;
- Disadvantages: During a single machine's downtime, messages that have not been consumed on this machine cannot be subscribed before the machine recovers, and message timeliness will be affected.

Start Broker+Proxy cluster

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-noslave/broker-a.properties --enable-proxy &

### On machine A, start the second Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-noslave/broker-b.properties --enable-proxy &

...
```

> [!NOTE]
> The above start command is used in the case of a single NameServer. For a cluster with multiple NameServers, the address list after `-n` in the Broker start command is separated by semicolons, such as `192.168.1.1:9876;192.161.2:9876`.

<a id="deploymentoperations-01deploy--multiple-node-cluster-multiple-replica-mode-asynchronous-replication"></a>

#### Multiple Node (Cluster) Multiple Replica Mode - Asynchronous Replication

Each Master is configured with a Slave, and there are multiple Master-Slave pairs. HA uses asynchronous replication, and there is a brief message delay (millisecond level) between the primary and secondary. The advantages and disadvantages of this mode are as follows:

- Advantages: Even if the disk is damaged, very few messages are lost, and message timeliness is not affected. At the same time, after the Master goes down, consumers can still consume from the Slave, and this process is transparent to the application and does not require manual intervention, and the performance is almost the same as the multiple Master mode;
- Disadvantages: A small number of messages will be lost in the event of a Master outage or disk damage.

Start Broker+Proxy cluster

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-a.properties --enable-proxy &

### On machine B, start the second Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-b.properties --enable-proxy &

### On machine C, start the first slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-a-s.properties --enable-proxy &

### On machine D, start the second slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-b-s.properties --enable-proxy &
```

<a id="deploymentoperations-01deploy--multiple-node-cluster-multiple-replica-mode-synchronous-dual-write"></a>

#### Multiple Node (Cluster) Multiple Replica Mode - Synchronous Dual Write

Each Master is configured with a Slave, and there are multiple Master-Slave pairs. HA uses synchronous dual write, which means that only if both primary and secondary write succeed, it returns success to the application. The advantages and disadvantages of this mode are as follows:

- Advantages: Both data and service have no single point of failure, and there is no delay in messages in the event of a Master outage, and both service availability and data availability are very high;
- Disadvantages: Performance is slightly lower than asynchronous replication mode (about 10% lower), the RT for sending a single message is slightly higher, and in the current version, after the primary node goes down, the standby cannot automatically switch to the primary.

<a id="deploymentoperations-01deploy--start-brokerproxy-cluster"></a>

#### Start Broker+Proxy cluster

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-a.properties --enable-proxy &

### On machine B, start the second Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-b.properties --enable-proxy &

### On machine C, start the first slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-a-s.properties --enable-proxy &

### On machine D, start the second slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-b-s.properties --enable-proxy &
```

> [!TIP]
> The pairing of the above Broker and Slave is done by specifying the same BrokerName parameter. The BrokerId of the Master must be 0, and the BrokerId of the Slave must be a number greater than 0. In addition, multiple Slaves can be mounted on another Master, and multiple Slaves under the same Master are distinguished by specifying different BrokerIds. $ROCKETMQ\_HOME refers to the RocketMQ installation directory, and this environment variable needs to be set by the user.

<a id="deploymentoperations-01deploy--50-ha"></a>

#### 5.0 HA

RocketMQ 5.0 Provides a more flexible HA mechanism, allowing users to better balance cost, service availability, and data reliability, while supporting messaging and streaming storage scenarios. [See details](#deploymentoperations-03autofailover)

<a id="deploymentoperations-01deploy--deployment-in-cluster-mode"></a>

## Deployment in Cluster Mode

In Cluster mode, the Broker and Proxy are deployed separately, and I can deploy the Proxy after the NameServer and Broker have been started.

In Cluster mode, a Proxy cluster and a Broker cluster have a one-to-one correspondence, and the `rocketMQClusterName` can be configured in the Proxy's configuration file `rmq-proxy.json`.

<a id="deploymentoperations-01deploy--start-nameserver-1"></a>

### Start NameServer

```bash
### Start NameServer first
$ nohup sh mqnamesrv &

### Verify tha Name Server has started successfully
$ tail -f ~/logs/rocketmqlogs/namesrv.log The Name Server boot success...
```

<a id="deploymentoperations-01deploy--start-broker"></a>

### Start Broker

<a id="deploymentoperations-01deploy--single-node-single-replica-mode-1"></a>

#### Single node single replica mode

> [!WARNING]
> **caution**
> This method has a higher risk because the Broker has only one node. If the Broker restarts or goes down, the entire service will be unavailable. It is not recommended for use in a production environment, but can be used for local testing.

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 &
```

<a id="deploymentoperations-01deploy--multiple-node-cluster-single-replica-mode-1"></a>

#### Multiple node (cluster) single replica mode

In this mode, all nodes in a cluster are deployed as Master roles, without deploying any Slave replicas, such as 2 Masters or 3 Masters. The advantages and disadvantages of this mode are as follows:

- Advantages: Simple configuration, single Master downtime or restart has no impact on the application, and when the disk is configured as RAID10, even if the machine goes down and cannot be recovered, due to the reliability of RAID10 disks, messages will not be lost (asynchronous flush disk loses a small amount of messages, synchronous flush disk does not lose any messages), and the performance is the highest;
- Disadvantages: During the downtime of a single machine, the messages on this machine that have not been consumed cannot be subscribed before the machine recovers, and the real-time nature of the messages will be affected.

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-noslave/broker-a.properties &

### On machine B, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-noslave/broker-b.properties &

...
```

> [!NOTE]
> The above startup command is used in the case of a single NameServer. For a cluster of multiple NameServers, the address list following the `-n` in the Broker startup command can be separated by semicolons, for example `192.168.1.1:9876;192.161.2:9876`.

<a id="deploymentoperations-01deploy--multiple-node-cluster-multiple-replica-mode-asynchronous-replication-1"></a>

#### Multiple Node (Cluster) Multiple Replica Mode - Asynchronous Replication

Each Master is configured with one Slave, and there are multiple Master-Slave pairs. HA uses asynchronous replication, with a brief delay (millisecond level) between the primary and the standby. The advantages and disadvantages of this mode are as follows:

- Advantages: Even if the disk is damaged, the loss of messages is very small, and the timeliness of messages is not affected. In addition, after the Master goes down, consumers can still consume from the Slave, and this process is transparent to the application and does not require manual intervention. The performance is almost the same as in the multiple Master mode.
- Disadvantages: In the event of a Master crash or disk damage, a small number of messages will be lost.

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-a.properties &

### On machine B, start the second Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-b.properties &

### On machine C, start the first Slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-a-s.properties &

### On machine B, start the second Slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-async/broker-b-s.properties &
```

<a id="deploymentoperations-01deploy--multiple-node-cluster-multiple-replica-mode-synchronous-dual-write-1"></a>

#### Multiple Node (Cluster) Multiple Replica Mode - Synchronous Dual Write

Each Master is configured with one Slave, and there are multiple Master-Slave pairs. HA uses synchronous dual write, which only returns success to the application if both the primary and the standby have written successfully. The advantages and disadvantages of this mode are as follows:

- Advantages: Both data and service are free from single point failures. In the event of a Master crash, there is no delay in messages, and both the availability of the service and the availability of the data are very high.
- Disadvantages: Performance is slightly lower than in the asynchronous replication mode (about 10% lower), RT for sending a single message is slightly higher, and in the current version, the standby cannot automatically switch to the primary after the primary node goes down.

```bash
### On machine A, start the first Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-a.properties &

### On machine B, start the second Master, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-b.properties &

### On machine C, start the first Slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-a-s.properties &

### On machine B, start the second Slave, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqbroker -n 192.168.1.1:9876 -c $ROCKETMQ_HOME/conf/2m-2s-sync/broker-b-s.properties &
```

> [!TIP]
> The pairing of Broker and Slave is done by specifying the same BrokerName parameter. The BrokerId of the Master must be 0, and the BrokerId of the Slave must be a number greater than 0. In addition, multiple Slaves can be mounted under one Master, and multiple Slaves under the same Master are distinguished by specifying different BrokerIds. $ROCKETMQ\_HOME refers to the RocketMQ installation directory, which needs to be set by the user as an environment variable.

<a id="deploymentoperations-01deploy--50-ha-1"></a>

#### 5.0 HA

RocketMQ 5.0 Provides a more flexible HA mechanism, allowing users to better balance cost, service availability, and data reliability, while supporting messaging and streaming storage scenarios. [See details](#deploymentoperations-03autofailover)

<a id="deploymentoperations-01deploy--start-proxy"></a>

### Start Proxy

Multiple Proxies can be started on multiple machines.

```shell
### On machine A start the first Proxy, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqproxy -n 192.168.1.1:9876 &

### On machine B start the second Proxy, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqproxy -n 192.168.1.1:9876 &

### On machine C start the third Proxy, for example, the IP of the NameServer is: 192.168.1.1
$ nohup sh bin/mqproxy -n 192.168.1.1:9876 &
```

If you need to specify a configuration file, you can use `-pc` or `--proxyConfigPath` to specify it.

```shell
### custom config file
$ nohup sh bin/mqproxy -n 192.168.1.1:9876 -pc /path/to/proxyConfig.json &
```

- [Deployment in Local Mode](#deploymentoperations-01deploy--deployment-in-local-mode)
  - [Start NameServer](#deploymentoperations-01deploy--start-nameserver)
  - [Start Broker+Proxy](#deploymentoperations-01deploy--start-brokerproxy)
- [Deployment in Cluster Mode](#deploymentoperations-01deploy--deployment-in-cluster-mode)
  - [Start NameServer](#deploymentoperations-01deploy--start-nameserver-1)
  - [Start Broker](#deploymentoperations-01deploy--start-broker)
  - [Start Proxy](#deploymentoperations-01deploy--start-proxy)

---

<a id="deploymentoperations-02admintool"></a>

<!-- source_url: https://rocketmq.apache.org/docs/deploymentOperations/02admintool/ -->

<!-- page_index: 28 -->

# Admin Tool

Version: 5.0

# Admin Tool

> [!TIP]
> **Notice**
> 1. To execute a command: `./mqadmin {command} {args}`
> 2. Most commands require the configuration of the NameServer address with the `-n` flag, in the format `ip:port`
> 3. Most commands can get help with the `-h` flag
> 4. If both the Broker address (`-b`) and the clusterName (`-c`) are configured, the command will be executed using the Broker address. If the Broker address is not configured, the command will be executed on all hosts in the cluster. Only one Broker address is supported, in the format `ip:port`, where the port is 10911 by default.
> 5. In the `tools` directory, you can see many commands, but not all of them can be used. Only those initialized in `MQAdminStartup` can be used. You can also modify this class to add or define your own commands.
> 6. Some commands may not have been updated due to version updates, and may cause errors. In this case, please read the relevant command source code.

<a id="deploymentoperations-02admintool--topic-related"></a>

## Topic-related

> [!INFO]
> **Topic\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="185"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="132" style="height:99.0pt"><td class="xl68" height="593" rowspan="8" style="border-bottom:1.0pt;height:444.0pt;border-top:none;width:122pt" width="163">updateTopic</td><td class="xl70" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Create/update topic configuration</td><td class="xl65" style="width:112pt" width="149">-b</td><td class="xl66" style="width:119pt" width="159">Broker address, representing the Broker where the topic is located. Only a single Broker is supported, with the address in the format ip:port.</td></tr><tr height="132" style="height:99.0pt"><td class="xl65" height="132" style="height:99.0pt;width:112pt" width="149">-c</td><td class="xl66" style="width:119pt" width="159">Cluster name, representing the cluster where the topic is located (the cluster can be queried with the clusterList command).</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="76" style="height:57.0pt"><td class="xl65" height="76" style="height:57.0pt;width:112pt" width="149">-p</td><td class="xl66" style="width:119pt" width="159">Specify the read-write permissions for the new topic( W=2|R=4|WR=6 )</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:112pt" width="149">-r</td><td class="xl66" style="width:119pt" width="159">Number of readable queues（default is 8）</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:112pt" width="149">-w</td><td class="xl66" style="width:119pt" width="159">Number of writable queues（default is 8）</td></tr><tr height="95" style="height:71.0pt"><td class="xl65" height="95" style="height:71.0pt;width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">Topic name (the name can only use the characters ^[a-zA-Z0-9_-]+$ ）</td></tr><tr height="132" style="height:99.0pt"><td class="xl68" height="307" rowspan="4" style="border-bottom:1.0pt;height:230.0pt;border-top:none;width:122pt" width="163">deleteTopic</td><td class="xl70" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Delete Topic</td><td class="xl65" style="width:112pt" width="149">-c</td><td class="xl66" style="width:119pt" width="159">Cluster name, representing the deletion of a specific topic under a certain cluster (the cluster can be queried with the clusterList command).</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="95" style="height:71.0pt"><td class="xl65" height="95" style="height:71.0pt;width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name (the name can only use the characters ^[a-zA-Z0-9_-]+$ ）</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="287" rowspan="3" style="border-bottom:1.0pt;height:215.0pt;border-top:none;width:122pt" width="163">topicList</td><td class="xl70" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Query topic list information</td><td class="xl65" style="width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="207" style="height:155.0pt"><td class="xl65" height="207" style="height:155.0pt;width:112pt" width="149">-c</td><td class="xl66" style="width:119pt" width="159">Without the -c flag, only the topic list is returned. Adding -c returns the clusterName, topic, and consumerGroup information, i.e. the cluster that the topic belongs to and the subscription relationship. There are no parameters.</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="103" rowspan="3" style="border-bottom:1.0pt;height:77.0pt;border-top:none;width:122pt" width="163">topicRoute</td><td class="xl70" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Query topic routing information</td><td class="xl65" style="width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="103" rowspan="3" style="border-bottom:1.0pt;height:77.0pt;border-top:none;width:122pt" width="163">topicStatus</td><td class="xl70" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Query topic message queue offsets</td><td class="xl65" style="width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="103" rowspan="3" style="border-bottom:1.0pt;height:77.0pt;border-top:none;width:122pt" width="163">topicClusterList</td><td class="xl70" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Query list of clusters where the topic is located</td><td class="xl65" style="width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="518" rowspan="6" style="border-bottom:1.0pt;height:380pt;border-top:none;width:122pt" width="163">updateTopicPerm</td><td class="xl70" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Update topic read-write permissions</td><td class="xl65" style="width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="132" style="height:99.0pt"><td class="xl65" height="132" style="height:99.0pt;width:112pt" width="149">-b</td><td class="xl66" style="width:119pt" width="159">Broker address, representing the Broker where the topic is located. Only a single Broker is supported, with the address in the format ip:port.</td></tr><tr height="76" style="height:57.0pt"><td class="xl65" height="76" style="height:57.0pt;width:112pt" width="149">-p</td><td class="xl66" style="width:119pt" width="159">Specify the read-write permissions for the new topic( W=2|R=4|WR=6 )</td></tr><tr height="207" style="height:155.0pt"><td class="xl65" height="207" style="height:155.0pt;width:112pt" width="149">-c</td><td class="xl66" style="width:119pt" width="159">Cluster name, representing the cluster where the topic is located (the cluster can be queried with the clusterList command). The -b flag takes precedence. If there is no -b flag, the command will be executed on all Brokers in the cluster.</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="199" rowspan="5" style="border-bottom:1.0pt;height:149.0pt;border-top:none;width:122pt" width="163">updateOrderConf</td><td class="xl70" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Create, delete, and get specific kv configurations from the NameServer. This feature is currently not available.</td><td class="xl65" style="width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic,key</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:112pt" width="149">-v</td><td class="xl66" style="width:119pt" width="159">orderConf,value</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-m</td><td class="xl66" style="width:119pt" width="159">method，optional get、put、delete</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="198" rowspan="4" style="border-bottom:1.0pt;height:140pt;border-top:none;width:122pt" width="163">allocateMQ</td><td class="xl70" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Calculate the load results of the message queue for the consumer list using an average load algorithm.</td><td class="xl65" style="width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="95" style="height:71.0pt"><td class="xl65" height="95" style="height:71.0pt;width:112pt" width="149">-i</td><td class="xl66" style="width:119pt" width="159">ipList,separated by commas, calculates the message queue load for these IPs for the topic.</td></tr><tr height="23" style="height:17.0pt"><td class="xl68" height="142" rowspan="4" style="border-bottom:1.0pt solid black;height:106.0pt;border-top:1.0pt;width:122pt" width="163">statsAll</td><td class="xl70" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:101pt" width="135">Print information about the topic's subscriptions, TPS, accumulation, 24-hour total read-write volume, etc.</td><td class="xl65" style="width:112pt" width="149">-h</td><td class="xl66" style="width:119pt" width="159">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:112pt" width="149">-n</td><td class="xl66" style="width:119pt" width="159">NameServer address，format ip:port</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:112pt" width="149">-a</td><td class="xl66" style="width:119pt" width="159">Print only active topics</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:112pt" width="149">-t</td><td class="xl66" style="width:119pt" width="159">Specify topic</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--cluster-related"></a>

## Cluster-related

> [!INFO]
> **Cluster\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="185"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="207" style="height:155.0pt"><td class="xl67" height="326" rowspan="4" style="border-bottom:1.0pt;height:244.0pt;border-top:none;width:133pt" width="177"><span style="mso-spacerun:yes"> </span>clusterList</td><td class="xl70" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:131pt" width="175">Query cluster information, including the cluster, BrokerName, BrokerId, TPS, and other information.</td><td class="xl65" style="width:133pt" width="177">-m</td><td class="xl66" style="width:139pt" width="185">Print more information (additional information printed includes: #InTotalYest, #OutTotalYest,#InTotalToday ,#OutTotalToday)</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:133pt" width="177">-h</td><td class="xl66" style="width:139pt" width="185">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:133pt" width="177">-n</td><td class="xl66" style="width:139pt" width="185">NameServer address，format ip:port</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:133pt" width="177">-i</td><td class="xl66" style="width:139pt" width="185">Print interval, in seconds.</td></tr><tr height="95" style="height:71.0pt"><td class="xl67" height="391" rowspan="8" style="border-bottom:1.0pt;height:292.0pt;border-top:none;width:133pt" width="177">clusterRT</td><td class="xl70" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:131pt" width="175">Send a message to test the RT of each Broker in the cluster. The message is sent to the$<!-- -->{<!-- -->BrokerName<!-- -->}<!-- --> Topic。</td><td class="xl65" style="width:133pt" width="177">-a</td><td class="xl66" style="width:139pt" width="185">amount,the total number of probes each time. RT = total time / amount</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:133pt" width="177">-s</td><td class="xl66" style="width:139pt" width="185">Message size，Unit: B</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:133pt" width="177">-c</td><td class="xl66" style="width:139pt" width="185">Which cluster to probe</td></tr><tr height="76" style="height:57.0pt"><td class="xl65" height="76" style="height:57.0pt;width:133pt" width="177">-p</td><td class="xl66" style="width:139pt" width="185">Whether to print formatted logs, separated by |, default is not printed.</td></tr><tr height="23" style="height:17.0pt"><td class="xl65" height="23" style="height:17.0pt;width:133pt" width="177">-h</td><td class="xl66" style="width:139pt" width="185">Print help</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:133pt" width="177">-m</td><td class="xl66" style="width:139pt" width="185">Belonging datacenter, for printing purposes.</td></tr><tr height="39" style="height:29.0pt"><td class="xl65" height="39" style="height:29.0pt;width:133pt" width="177">-i</td><td class="xl66" style="width:139pt" width="185">Send interval,in seconds.</td></tr><tr height="57" style="height:43.0pt"><td class="xl65" height="57" style="height:43.0pt;width:133pt" width="177">-n</td><td class="xl66" style="width:139pt" width="185">NameServer address，format ip:port</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--broker-related"></a>

## Broker-related

> [!INFO]
> **Broker\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="185"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="128" style="height:96.0pt"><td class="xl69" height="208" rowspan="3" style="border-bottom:1.0pt;height:156.0pt;border-top:none;width:65pt" width="87">queryMsgById</td><td class="xl72" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query the msg based on offsetMsgId. If using the open source console, offsetMsgId should be used. This command has additional parameters, for more information on their function, please read QueryMsgByIdSubCommand.</td><td class="xl67" style="width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">msgId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="126" rowspan="4" style="border-bottom:1.0pt;height:94.0pt;border-top:none;width:65pt" width="87">queryMsgByKey</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query message based on message key.</td><td class="xl67" style="width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">msgKey</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">Topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address，format ip:port</td></tr><tr height="225" style="height:169.0pt"><td class="xl69" height="390" rowspan="6" style="border-bottom:1.0pt;height:292.0pt;border-top:none;width:65pt" width="87">queryMsgByOffset</td><td class="xl72" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query message based on offset.</td><td class="xl67" style="width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Broker name (note that the name of the Broker, not its address, should be entered here. The Broker name can be found using the clusterList command).</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-i</td><td class="xl68" style="width:65pt" width="87">query queue id</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-o</td><td class="xl68" style="width:65pt" width="87">offset value</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="47"><td class="xl69" height="209" rowspan="6" style="border-bottom:1.0pt;height:156.0pt;border-top:none;width:65pt" width="87">queryMsgByUniqueKey</td><td class="xl72" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query based on msgId. msgId is different from offsetMsgId, for more information see common operations issues. -g and -d are used together, after finding the message, try to let a specific consumer consume the message and return the consumption result.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">unique msg id</td></tr><tr height="36" style="height:27.0pt"><td class="xl67" height="36" style="height:27.0pt;width:65pt" width="87">-g</td><td class="xl67" style="width:65pt" width="87">consumerGroup</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-d</td><td class="xl67" style="width:65pt" width="87">clientId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="149" rowspan="5" style="border-bottom:1.0pt;height:111.0pt;border-top:none;width:65pt" width="87">checkMsgSendRT</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Check the RT of sending messages to a topic. The function is similar to clusterRT.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td> <td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-a</td><td class="xl68" style="width:65pt" width="87">Number of probes</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">message size</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="218" rowspan="8" style="border-bottom:1.0pt;height:162.0pt;border-top:none;width:65pt" width="87">sendMessage</td><td class="xl72" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Send a message, which can be sent to a specific message queue based on configuration, or a normal send.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-p</td><td class="xl68" style="width:65pt" width="87">message body</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">keys</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-c</td><td class="xl67" style="width:65pt" width="87">tags</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="312" rowspan="10" style="border-bottom:1.0pt;height:232.0pt;border-top:none;width:65pt" width="87">consumeMessage</td><td class="xl72" rowspan="10" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consume messages. Messages can be consumed based on offset, start &amp; end timestamps, and message queues. Different configurations execute different consumption logic, see ConsumeMessageCommand for more information.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-o</td><td class="xl68" style="width:65pt" width="87">Consume from offset</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Consume a certain number of messages</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="282" rowspan="8" style="border-bottom:1.0pt;height:210.0pt;border-top:none;width:65pt" width="87">printMsg</td><td class="xl72" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consume messages from Broker and print them, optional time period.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Character set, e.g. UTF-8</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">subExpress,filter expression</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-e</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Whether to print the message body.</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="390" rowspan="12" style="border-bottom:1.0pt;height:290.0pt;border-top:none;width:65pt" width="87">printMsgByQueue</td><td class="xl72" rowspan="12" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Similar to printMsg, but for a specific message queue.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-a</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Character set, e.g. UTF-8</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">subExpress, filter expression</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-e</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-p</td><td class="xl68" style="width:65pt" width="87">Whether to print the message body.</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Whether to print the message body.</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-f</td><td class="xl68" style="width:65pt" width="87">Whether to count and print the number of tags</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="410" rowspan="7" style="border-bottom:1.0pt;height:307.0pt;border-top:none;width:65pt" width="87">resetOffsetByTime</td><td class="xl72" rowspan="7" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Reset offset based on timestamp, both Broker and consumer will be reset.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address, format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Reset to the offset corresponding to this timestamp.</td></tr><tr height="188" style="height:141.0pt"><td class="xl67" height="188" style="height:141.0pt;width:65pt" width="87">-f</td><td class="xl68" style="width:65pt" width="87">Whether to force reset. If false, only backward offset is supported. If true, regardless of the relationship between the timestamp-corresponding offset and consumeOffset.</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Whether to reset the offset for the C++ client.</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--message-related"></a>

## Message-related

> [!INFO]
> **Message\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="185"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="128" style="height:96.0pt"><td class="xl69" height="208" rowspan="3" style="border-bottom:1.0pt;height:156.0pt;border-top:none;width:65pt" width="87">queryMsgById</td><td class="xl72" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">To query a message by its offset message ID (offsetMsgId), you can use the offsetMsgId command if using an open source console. This command has additional parameters, the specific function of which can be found by reading the QueryMsgByIdSubCommand.</td><td class="xl67" style="width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">msgId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="126" rowspan="4" style="border-bottom:1.0pt;height:94.0pt;border-top:none;width:65pt" width="87">queryMsgByKey</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query a message by key.</td><td class="xl67" style="width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">msgKey</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">Topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="225" style="height:169.0pt"><td class="xl69" height="390" rowspan="6" style="border-bottom:1.0pt;height:292.0pt;border-top:none;width:65pt" width="87">queryMsgByOffset</td><td class="xl72" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query a message by offset</td><td class="xl67" style="width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Broker name (Note that this should be the name of the Broker, not the address. The name of the Broker can be found in clusterList.)</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-i</td><td class="xl68" style="width:65pt" width="87">query queue id</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-o</td><td class="xl68" style="width:65pt" width="87">offset value</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="47"><td class="xl69" height="209" rowspan="6" style="border-bottom:1.0pt;height:156.0pt;border-top:none;width:65pt" width="87">queryMsgByUniqueKey</td><td class="xl72" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query based on msgId. Note that msgId is different from offsetMsgId. For more information, see Common Operations and Maintenance Issues. Use -g and -d together to try to have a specific consumer consume the message and return the consumption result once the message has been found.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">unique msg id</td></tr><tr height="36" style="height:27.0pt"><td class="xl67" height="36" style="height:27.0pt;width:65pt" width="87">-g</td><td class="xl67" style="width:65pt" width="87">consumerGroup</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-d</td><td class="xl67" style="width:65pt" width="87">clientId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="149" rowspan="5" style="border-bottom:1.0pt;height:111.0pt;border-top:none;width:65pt" width="87">checkMsgSendRT</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Check the RT (round-trip time) for sending messages to a topic. This function is similar to clusterRT.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td> <td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-a</td><td class="xl68" style="width:65pt" width="87">Number of probes.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Message size</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="218" rowspan="8" style="border-bottom:1.0pt;height:162.0pt;border-top:none;width:65pt" width="87">sendMessage</td><td class="xl72" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Send a message, which can be sent to a specific Message Queue according to configuration or sent normally.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-p</td><td class="xl68" style="width:65pt" width="87">body，message body</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">keys</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-c</td><td class="xl67" style="width:65pt" width="87">tags</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="312" rowspan="10" style="border-bottom:1.0pt;height:232.0pt;border-top:none;width:65pt" width="87">consumeMessage</td><td class="xl72" rowspan="10" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consume messages. Messages can be consumed based on offset, start &amp; end timestamps, and message queue. Different configurations will execute different consumption logic. See ConsumeMessageCommand for more information.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-o</td><td class="xl68" style="width:65pt" width="87">Consume from a specified offset.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Consume a specified number of messages.</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="282" rowspan="8" style="border-bottom:1.0pt;height:210.0pt;border-top:none;width:65pt" width="87">printMsg</td><td class="xl72" rowspan="8" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consume and print messages from the Broker within a specified time period.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Character set, e.g. UTF-8</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">subExpress，filter expression</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-e</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Whether to print message body</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="390" rowspan="12" style="border-bottom:1.0pt;height:290.0pt;border-top:none;width:65pt" width="87">printMsgByQueue</td><td class="xl72" rowspan="12" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Similar to printMsg, but specifies a Message Queue.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">queueId</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-a</td><td class="xl67" style="width:65pt" width="87">BrokerName</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Character set, e.g. UTF-8</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">subExpress,filter expression</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Start timestamp, see -h for format.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-e</td><td class="xl68" style="width:65pt" width="87">End timestamp</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-p</td><td class="xl68" style="width:65pt" width="87">Whether to print the message</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Whether to print the message body</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-f</td><td class="xl68" style="width:65pt" width="87">Whether to count and print the number of tags</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="410" rowspan="7" style="border-bottom:1.0pt;height:307.0pt;border-top:none;width:65pt" width="87">resetOffsetByTime</td><td class="xl72" rowspan="7" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Resetting the offset by timestamp will reset both the broker and the consumer.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address, format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Reset to the offset corresponding to this timestamp.</td></tr><tr height="188" style="height:141.0pt"><td class="xl67" height="188" style="height:141.0pt;width:65pt" width="87">-f</td><td class="xl68" style="width:65pt" width="87">Whether to force reset. If false, only backward offset is supported. If true, the relationship between the timestamp corresponding offset and consumeOffset is ignored.</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Whether to reset the offset for the C++ client.</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--consume-related"></a>

## Consume-related

> [!INFO]
> **Consume\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="200"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definitation</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="39" style="height:29.0pt"><td class="xl69" height="158" rowspan="4" style="border-bottom:1.0pt;height:110pt;border-top:none;width:65pt" width="87">consumerProgress</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consumer group consumption status, including specific client IP's message accumulation.</td><td class="xl67" style="width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">consumer group name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Whether to print the client IP.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Pirnt help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="105" style="mso-height-source:userset;height:79.0pt"><td class="xl69" height="260" rowspan="5" style="border-bottom:1.0pt;height:195.0pt;border-top:none;width:65pt" width="87">consumerStatus</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Consumer status refers to the status of a consumer, including whether all consumers in the same group have the same subscriptions, whether the Process Queue is stacking up, and the jstack result of the consumer. The information returned by this command is extensive, and users should refer to the ConsumerStatusSubCommand for more details.</td><td class="xl67" style="width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="36" style="height:27.0pt"><td class="xl67" height="36" style="height:27.0pt;width:65pt" width="87">-g</td><td class="xl67" style="width:65pt" width="87">consumer group</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-i</td><td class="xl67" style="width:65pt" width="87">clientId</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Whether to execute jstack</td></tr><tr height="39" style="height:29.0pt"><td class="xl69" height="181" rowspan="5" style="border-bottom:1.0pt;height:135.0pt;border-top:none;width:65pt" width="87">getConsumerStatus</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Get Consumer consumption progress</td><td class="xl67" style="width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group name</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">Query topic</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-i</td><td class="xl68" style="width:65pt" width="87">Consumer client ip</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="761" rowspan="13" style="border-bottom:1.0pt;height:569.0pt;border-top:none;width:65pt" width="87">updateSubGroup</td><td class="xl72" rowspan="13" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Update or create a subscription relationship.</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Broker address</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Cluster name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">whether the group is allowed to consume</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-m</td><td class="xl68" style="width:65pt" width="87">Whether to start consuming from the smallest offset.</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Whether it is broadcast mode.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-q</td><td class="xl68" style="width:65pt" width="87">Number of retry queues.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-r</td><td class="xl68" style="width:65pt" width="87">Maximum number of retries</td></tr><tr height="207" style="height:155.0pt"><td class="xl67" height="207" style="height:155.0pt;width:65pt" width="87">-i</td><td class="xl68" style="width:65pt" width="87">When slaveReadEnable is turned on and it has not yet reached the point where it is recommended to consume from the slave, it is possible to configure the standby machine id to actively consume from the standby machine.</td></tr><tr height="132" style="height:99.0pt"><td class="xl67" height="132" style="height:99.0pt;width:65pt" width="87">-w</td><td class="xl68" style="width:65pt" width="87">If the Broker suggests consuming from the slave, the configuration determines which slave to consume from. The BrokerId can be configured, for example 1.</td></tr><tr height="76" style="height:57.0pt"><td class="xl67" height="76" style="height:57.0pt;width:65pt" width="87">-a</td><td class="xl68" style="width:65pt" width="87">Whether other consumers are notified of load balancing when the number of consumers changes.</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="165" rowspan="5" style="border-bottom:1.0pt;height:123.0pt;border-top:none;width:65pt" width="87">deleteSubGroup</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">To remove a subscription from a Broker</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-b</td><td class="xl68" style="width:65pt" width="87">Broker address</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-c</td><td class="xl68" style="width:65pt" width="87">Cluster name</td></tr><tr height="39" style="height:29.0pt"><td class="xl67" height="39" style="height:29.0pt;width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Consumer group name</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="172" rowspan="6" style="border-bottom:1.0pt;height:120pt;border-top:none;width:65pt" width="87">cloneGroupOffset</td><td class="xl72" rowspan="6" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Using the offsets from the source consumer group in the target consumer group.</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Source consumer group</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-d</td><td class="xl68" style="width:65pt" width="87">Target consumer group</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topicname</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-o</td><td class="xl68" style="width:65pt" width="87">Not currently in use.</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--connection-related"></a>

## Connection-related

> [!INFO]
> **Connection\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><colgroup><col width="177"/><col width="175"/><col width="177"/><col width="185"/></colgroup><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="39" style="height:29.0pt"><td class="xl69" height="119" rowspan="3" style="border-bottom:1.0pt;height:89.0pt;border-top:none;width:65pt" width="87">consumerConnection</td><td class="xl72" rowspan="3" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query consumer network connections.</td><td class="xl67" style="width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Name of consumer group.</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address，format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="39" style="height:29.0pt"><td class="xl69" height="142" rowspan="4" style="border-bottom:1.0pt;height:106.0pt;border-top:none;width:65pt" width="87">producerConnection</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Query producer network connections.</td><td class="xl67" style="width:65pt" width="87">-g</td><td class="xl68" style="width:65pt" width="87">Name of producer group.</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-t</td><td class="xl68" style="width:65pt" width="87">topic name</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--nameserver-related"></a>

## NameServer-related

> [!INFO]
> **Connection\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="21" style="height:16.0pt"><td class="xl69" height="143" rowspan="5" style="border-bottom:1.0pt;height:100pt;border-top:none;width:65pt" width="87">updateKvConfig</td><td class="xl72" rowspan="5" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Update NameServer KV configuration, currently not in use.</td><td class="xl75" style="width:65pt" width="87">-s</td><td class="xl76" style="width:65pt" width="87">Name space</td></tr><tr height="21" style="height:16.0pt"><td class="xl75" height="21" style="height:16.0pt;width:65pt" width="87">-k</td><td class="xl75" style="width:65pt" width="87">key</td></tr><tr height="21" style="height:16.0pt"><td class="xl75" height="21" style="height:16.0pt;width:65pt" width="87">-v</td><td class="xl75" style="width:65pt" width="87">value</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="23" style="height:17.0pt"><td class="xl69" height="126" rowspan="4" style="border-bottom:1.0pt;height:94.0pt;border-top:none;width:65pt" width="87">deleteKvConfig</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Delete NameServer KV configuration.</td><td class="xl67" style="width:65pt" width="87">-s</td><td class="xl68" style="width:65pt" width="87">Name space</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">key</td></tr><tr height="57" style="height:43.0pt"><td class="xl67" height="57" style="height:43.0pt;width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="80" rowspan="2" style="border-bottom:1.0pt;height:60.0pt;border-top:none;width:65pt" width="87">getNamesrvConfig</td><td class="xl72" rowspan="2" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Get NameServer configuration.</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="126" rowspan="4" style="border-bottom:1.0pt;height:94.0pt;border-top:none;width:65pt" width="87">updateNamesrvConfig</td><td class="xl72" rowspan="4" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Modify NameServer configuration.</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-k</td><td class="xl67" style="width:65pt" width="87">key</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-v</td><td class="xl67" style="width:65pt" width="87">value</td></tr></tbody></table>

<a id="deploymentoperations-02admintool--others"></a>

## Others

> [!INFO]
> **Connection\-related parameters**
> <table border="0" cellpadding="0" cellspacing="0" width="714"><tbody><tr height="23" style="height:17.0pt"><td class="xl63" height="23" style="height:17.0pt;width:133pt" width="177">Name</td><td class="xl64" style="width:131pt" width="175">Definition</td><td class="xl64" style="width:133pt" width="177">Command options</td><td class="xl64" style="width:139pt" width="185">Explain</td></tr><tr height="57" style="height:43.0pt"><td class="xl69" height="80" rowspan="2" style="border-bottom:1.0pt;height:60.0pt;border-top:none;width:65pt" width="87">startMonitoring</td><td class="xl71" rowspan="2" style="border-bottom:1.0pt;border-top:none;width:65pt" width="87">Start the monitoring process to monitor events such as message deletion errors and the number of messages in the retry queue.</td><td class="xl67" style="width:65pt" width="87">-n</td><td class="xl68" style="width:65pt" width="87">NameServer address,format ip:port</td></tr><tr height="23" style="height:17.0pt"><td class="xl67" height="23" style="height:17.0pt;width:65pt" width="87">-h</td><td class="xl68" style="width:65pt" width="87">Print help</td></tr></tbody></table>

- [Topic-related](#deploymentoperations-02admintool--topic-related)
- [Cluster-related](#deploymentoperations-02admintool--cluster-related)
- [Broker-related](#deploymentoperations-02admintool--broker-related)
- [Message-related](#deploymentoperations-02admintool--message-related)
- [Consume-related](#deploymentoperations-02admintool--consume-related)
- [Connection-related](#deploymentoperations-02admintool--connection-related)
- [NameServer-related](#deploymentoperations-02admintool--nameserver-related)
- [Others](#deploymentoperations-02admintool--others)

---

<a id="deploymentoperations-03autofailover"></a>

<!-- source_url: https://rocketmq.apache.org/docs/deploymentOperations/03autofailover/ -->

<!-- page_index: 29 -->

# Master-Slave Automatic Failover Mode

Version: 5.0

# Master-Slave Automatic Failover Mode

![架构图](assets/images/controller-e6-9e-b6-e6-9e-84-d431b0cc0815713f46cf9adbe3e26957_ea159edc2fbc778a.png)

This document mainly introduces how to deploy a RocketMQ cluster that supports automatic master-slave switchover. Its architecture is shown in the above figure. It mainly adds the controller component that supports automatic master-slave switchover, which can be deployed independently or embedded in the NameServer.

> [!TIP]
> **Refer to**
> For more details, refer to [Design Ideas](https://github.com/apache/rocketmq/blob/develop/docs/en/controller/design.md) and [Quick Start](https://github.com/apache/rocketmq/blob/develop/docs/en/controller/quick_start.md)

<a id="deploymentoperations-03autofailover--controller-deployment"></a>

## Controller Deployment

The controller component provides selection of the master. If the controller needs to be fault-tolerant, it needs to be deployed in three or more replicas (following the Raft majority protocol).

> [!TIP]
> If the controller is only deployed as a single copy, it can still complete broker failover, but if the single-point controller fails, it will affect the switchover ability but not affect the normal send and receive of the existing cluster.

There are two ways to deploy the controller. One is to embed it in the NameServer for deployment. This can be opened by setting enableControllerInNamesrv (it can be selectively opened and is not required to be opened on every NameServer). In this mode, the NameServer itself is still stateless, which means that if the NameServer fails in the embedded mode, it will only affect the switchover ability, not the original routing acquisition and other functions. The other is to deploy the controller component independently.

<a id="deploymentoperations-03autofailover--embedding-the-controller-in-the-nameserver-for-deployment"></a>

### Embedding the Controller in the NameServer for deployment

![内嵌部署图](assets/images/controller-as-plugin-afd8d004541eb46736d8ea20594a4bb8_6a2912950cbf4fde.png)

When the Controller is embedded in the NameServer for deployment, you only need to set **`enableControllerInNamesrv=true`** in the NameServer configuration file and fill in the controller configuration.

```properties
enableControllerInNamesrv = true
controllerDLegerGroup = group1
controllerDLegerPeers = n0-127.0.0.1:9877;n1-127.0.0.1:9878;n2-127.0.0.1:9879
controllerDLegerSelfId = n0
controllerStorePath = /home/admin/DledgerController
enableElectUncleanMaster = false
notifyBrokerRoleChanged = true
```

Parameter explain：

- enableControllerInNamesrv: Whether to enable the controller in the Nameserver, the default is false.
- controllerDLegerGroup: The name of the DLedger Raft Group, it must be consistent within the same DLedger Raft Group.
- controllerDLegerPeers: Port information of the nodes within the DLedger Group, the configuration of the nodes within the same Group must be consistent.
- controllerDLegerSelfId: Node id, must be one of the controllerDLegerPeers; each node within the same Group must be unique.
- controllerStorePath: Location of the controller log storage. The controller is stateful, and the controller needs to rely on the log to recover data when restarting or crashing. This directory is very important and cannot be easily deleted.
- enableElectUncleanMaster: Whether it is possible to elect a Master from outside SyncStateSet. If true, it may choose a replica with outdated data as the master and lose messages. The default is false.
- notifyBrokerRoleChanged: Whether to actively notify when the role of the Broker replica group changes, the default is true.

After setting the parameters, you can start the Nameserver by specifying the configuration file.

```shell
$ nohup sh bin/mqnamesrv -c namesrv.conf &
```

<a id="deploymentoperations-03autofailover--controller-independent-deployment"></a>

### Controller independent deployment

![架构图](assets/images/controller-deploy-indepdent-76249b759fd9d4e728e09a10d278467e_3f1712e8e7d26db8.png)

To deploy independently, run the following script:

```shell
$ nohup sh bin/mqcontroller -c controller.conf &
```

The mqcontroller script is located at **`distribution/bin/mqcontroller`** in the source code package, and the configuration parameters are the same as in the embedded mode.

> [!WARNING]
> **Caution**
> After independently deploying the Controller, you still need to deploy the NameServer separately to provide routing discovery capability.

<a id="deploymentoperations-03autofailover--broker-deployment"></a>

## Broker deployment

The Broker start method is the same as before, with the following additional parameters:

- enableControllerMode: The overall switch for the Broker controller mode. Only when this value is true will the automatic primary-secondary switch mode be enabled. The default is false.
- controllerAddr: The address of the controller, separated by semicolons between multiple controllers. For example, `controllerAddr = 127.0.0.1:9877;127.0.0.1:9878;127.0.0.1:9879`
- syncBrokerMetadataPeriod: The time interval for syncing Broker replica information to the controller. The default is 5000 (5s).
- checkSyncStateSetPeriod: The time interval for checking SyncStateSet, checking SyncStateSet may shrink SyncState. The default is 5000 (5s).
- syncControllerMetadataPeriod: The time interval for syncing controller metadata, mainly to obtain the address of the active controller. The default is 10000 (10s).
- haMaxTimeSlaveNotCatchup: The maximum time interval for Slave not catching up to Master, if a slave in SyncStateSet exceeds this time interval, it will be removed from SyncStateSet. The default is 15000 (15s).
- storePathEpochFile: The location of the epoch file. The epoch file is very important and cannot be deleted casually. The default is in the store directory.
- allAckInSyncStateSet: If this value is true, a message will only be returned to the client as successful when it has been replicated to every replica in SyncStateSet, ensuring that the message is not lost. The default is false.
- syncFromLastFile: If the slave is a blank disk startup, whether to replicate from the last file. The default is false.
- asyncLearner: If this value is true, the replica will not enter SyncStateSet, that is, it will not be elected as Master, but will always act as a learner replica and perform asynchronous replication. The default is false.
- inSyncReplicas: The number of replica groups that need to be kept in sync, the default is 1, and this parameter is invalid when allAckInSyncStateSet=true.
- minInSyncReplicas: The minimum number of replica groups that need to be kept in sync. If the number of replicas in SyncStateSet is less than minInSyncReplicas, putMessage will return PutMessageStatus.IN\_SYNC\_REPLICAS, the default is 1

In controller mode, the Broker configuration must set enableControllerMode=true and fill in controllerAddr, and start with the following command:

```shell
$ nohup sh bin/mqbroker -c broker.conf &
```

> [!WARNING]
> **Caution**
> In automatic primary and secondary switching mode, Broker does not need to specify brokerId and brokerRole, which are assigned by the controller component.

<a id="deploymentoperations-03autofailover--compatibility"></a>

## Compatibility

This mode does not make any changes or modifications to any client-level APIs, and there are no compatibility issues with clients.

The Nameserver itself has not been modified and there are no compatibility issues with the Nameserver. If enableControllerInNamesrv is enabled and the controller parameters are configured correctly, the controller function is enabled.

If Broker is set to **`enableControllerMode=false`**, it will still operate as before. If **`enableControllerMode=true`**, the Controller must be deployed and the parameters must be configured correctly in order to operate properly.

The specific behavior is shown in the following table:

<table><thead><tr><th></th><th>Old nameserver</th><th>Old nameserver + Deploy controllers independently</th><th>New nameserver enables controller</th><th>New nameserver disable controller</th></tr></thead><tbody><tr><td>Old broker</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td></tr><tr><td>New broker enable controller mode</td><td>Unable to go online normally</td><td>Normal running, can failover</td><td>Normal running, can failover</td><td>Unable to go online normally</td></tr><tr><td>New broker disable controller mode</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td><td>Normal running, cannot failover</td></tr></tbody></table>
<a id="deploymentoperations-03autofailover--upgrade-considerations"></a>

## Upgrade considerations

From the compatibility statements above, it can be seen that NameServer can be upgraded normally without compatibility issues. In the case where the Nameserver is not to be upgraded, the controller component can be deployed independently to obtain switching capabilities. For broker upgrades, there are two cases:

1. Master-Slave deployment is upgraded to controller switching architecture

   In-place upgrade with data is possible. For each group of Brokers, stop the primary and secondary Brokers and ensure that the CommitLogs of the primary and secondary are aligned (you can either disable writing to this group of Brokers for a certain period of time before the upgrade or ensure consistency by copying). After upgrading the package, restart it.


> [!WARNING]
> **Caution**
> If the primary and secondary CommitLogs are not aligned, it is necessary to ensure that the primary is online before the secondary is online, otherwise messages may be lost due to data truncation.

2. Upgrade from DLedger mode to Controller switching architecture

   Due to the differences in the format of message data in DLedger mode and Master-Slave mode, there is no in-place upgrade with data. In the case of deploying multiple groups of Brokers, it is possible to disable writing to a group of Brokers for a certain period of time (as long as it is confirmed that all existing messages have been consumed), and then upgrade and deploy the Controller and new Brokers. In this way, the new Brokers will consume messages from the existing Brokers and the existing Brokers will consume messages from the new Brokers until the consumption is balanced, and then the existing Brokers can be decommissioned.

- [Controller Deployment](#deploymentoperations-03autofailover--controller-deployment)
  - [Embedding the Controller in the NameServer for deployment](#deploymentoperations-03autofailover--embedding-the-controller-in-the-nameserver-for-deployment)
  - [Controller independent deployment](#deploymentoperations-03autofailover--controller-independent-deployment)
- [Broker deployment](#deploymentoperations-03autofailover--broker-deployment)
- [Compatibility](#deploymentoperations-03autofailover--compatibility)
- [Upgrade considerations](#deploymentoperations-03autofailover--upgrade-considerations)

---

<a id="deploymentoperations-04dashboard"></a>

<!-- source_url: https://rocketmq.apache.org/docs/deploymentOperations/04Dashboard/ -->

<!-- page_index: 30 -->

# RocketMQ Dashboard

Version: 5.0

# RocketMQ Dashboard

**`RocketMQ Dashboard`** is a tool for managing RocketMQ, providing various statistical information on events and performance of clients and applications, and supporting visualized tools to replace command line operations such as topic configuration and broker management.

<a id="deploymentoperations-04dashboard--introduction"></a>

## Introduction

<a id="deploymentoperations-04dashboard--feature-overview"></a>

### Feature Overview

<table><thead><tr><th>Dashboard</th><th>Function</th></tr></thead><tbody><tr><td>OPS</td><td>Modify nameserver address; use <code>VIPChannel</code></td></tr><tr><td>Dashboard</td><td>Check broker, topic message volume</td></tr><tr><td>Cluster</td><td>Cluster distribution, broker configuration, runtime information</td></tr><tr><td>Topic</td><td>Search, filter, delete, update/add topics, message routing, send messages, reset consumption points</td></tr><tr><td>Consumer</td><td>Search, delete, add/update consumer groups, terminals, consumption details, configuration</td></tr><tr><td>Message</td><td>Message records, private messages, message trace, etc. message details</td></tr></tbody></table>

Operation panel：

![1657630174311](assets/images/1-dashboard-b20f8e9d3aeddbbf6820034c6eac7c31_3e0f2dfdec9ad4cf.png)

<a id="deploymentoperations-04dashboard--quick-start"></a>

## Quick Start

System requirements：

1. Linux/Unix/Mac
2. 64bit JDK 1.8+
3. Maven 3.2.x
4. Start [RocketMQ](https://rocketmq.apache.org/docs/quick-start/)

Network configuration：

1. The cloud server can be accessed remotely or the local virtual machine can PING the external network
2. `rocketmq` configuration file `broker.conf / broker-x.properties` set nameserver's address and port.
3. Start the broker with the configuration file

<a id="deploymentoperations-04dashboard--1-docker-image-installation"></a>

### 1. Docker image installation

① Install docker and pull the rocketmq-dashboard image

```shell
docker pull apacherocketmq/rocketmq-dashboard:latest
```

② Run in a docker container `rocketmq-dashboard`

```shell
docker run -d --name rocketmq-dashboard -e "JAVA_OPTS=-Drocketmq.namesrv.addr=127.0.0.1:9876" -p 8080:8080 -t apacherocketmq/rocketmq-dashboard:latest
```

> [!TIP]
> Replace namesrv.addr:port with the nameserver address and port configured in rocketmq
>
> 1. Open port numbers: 8080, 9876, 10911, 11011
>
> - Cloud server: Set security group access rules
> - Local virtual machine: Turn off firewall, or -add-port

<a id="deploymentoperations-04dashboard--2-source-installation"></a>

### 2. Source installation

Source address：[apache/rocketmq-dashboard](https://github.com/apache/rocketmq-dashboard)

Download it, unzip it, and navigate to the source directory `rocketmq-dashboard-master/`

① Compile `rocketmq-dashboard`

```shell
mvn clean package -Dmaven.test.skip=true
```

② Run `rocketmq-dashboard`

```shell
java -jar target/rocketmq-dashboard-1.0.1-SNAPSHOT.jar
```

> [!TIP]
> **Started App in x.xxx seconds (JVM running for x.xxx)** ，Indicates successful startup.

Browser page access：namesrv.addr:8080

Close `rocketmq-dashboard` : ctrl + c

Restart：execution ②

**tips**：The downloaded source code needs to be uploaded to the Linux system for compilation, and local compilation may return errors

<a id="deploymentoperations-04dashboard--tutorial"></a>

## Tutorial

<a id="deploymentoperations-04dashboard--1create-topic-topic"></a>

### 1.Create topic-Topic

Topic `>` ADD/UPDATE

![1657547091545](assets/images/2-createtopic-69ff3f87c23f95124e875ec73bf85b08_de05ce01282bb894.png)

<a id="deploymentoperations-04dashboard--2-create-consumer-group-consumer"></a>

### 2. Create consumer group-Consumer

Consumer `>` ADD/UPDATE

![1657547745254](assets/images/3-createconsumer-cd5dfb10e6e993bf7deaea31f9a30548_91f8c82a750bb530.png)

<a id="deploymentoperations-04dashboard--3-reset-consumption-offset"></a>

### 3. Reset consumption offset

Topic `>` REST CONSUMER OFFSET

![1657547891994](assets/images/4-resetoffset-d8f1ba3eab460f7bcce5058e4363c4ab_c8202cb0163e87d2.png)

> [!TIP]
> - Cluster consumption supports resetting consumption offsets, but broadcast mode does not.
> - If a consumer is not online, it is not possible to reset the consumption offset.

<a id="deploymentoperations-04dashboard--4-expand-topic-queues"></a>

### 4. Expand topic queues

Topic `>` TOPIC CONFIG

![1657548375401](assets/images/5-enlargetopic-60b15fc11e9d39631d7b9fe0b678b6cc_2f12bfcbc069cf94.png)

<a id="deploymentoperations-04dashboard--5-expand-broker"></a>

### 5. Expand Broker

- To install and deploy a new broker with the same nameserver address as the current cluster

  ![1657549432610](assets/images/6-cluster-4f5dd8b7657815fb15e5b9dad561c9a2_b65eef5780b10d5a.png)
- To update the `BROKER_NAME` of topic

  Topic `>` ADD/UPDATE `>` BROKER\_NAME

![1657549599728](assets/images/7-enlargebroker-32c0818aad2302d84c9d423ef9201d64_46a5d0c3a55e93b6.png)

<a id="deploymentoperations-04dashboard--6-send-message"></a>

### 6. Send message

- To send a message to a specific topic

  Topic `>` SEND MESSAGE

  ![1657550506673](assets/images/8-sendmessage-888a2cb2da8869ba6bdfc4333f0ca443_b6b8d021c9a030ad.png)
- Send result

  ![1657550592049](assets/images/9-sendresult-fb7347023b19e760f663664daba3f5c6_d648d85aca19f23c.png)

- [Introduction](#deploymentoperations-04dashboard--introduction)
  - [Feature Overview](#deploymentoperations-04dashboard--feature-overview)
- [Quick Start](#deploymentoperations-04dashboard--quick-start)
  - [1. Docker image installation](#deploymentoperations-04dashboard--1-docker-image-installation)
  - [2. Source installation](#deploymentoperations-04dashboard--2-source-installation)
- [Tutorial](#deploymentoperations-04dashboard--tutorial)
  - [1.Create topic-Topic](#deploymentoperations-04dashboard--1create-topic-topic)
  - [2. Create consumer group-Consumer](#deploymentoperations-04dashboard--2-create-consumer-group-consumer)
  - [3. Reset consumption offset](#deploymentoperations-04dashboard--3-reset-consumption-offset)
  - [4. Expand topic queues](#deploymentoperations-04dashboard--4-expand-topic-queues)
  - [5. Expand Broker](#deploymentoperations-04dashboard--5-expand-broker)
  - [6. Send message](#deploymentoperations-04dashboard--6-send-message)

---

<a id="deploymentoperations-05exporter"></a>

<!-- source_url: https://rocketmq.apache.org/docs/deploymentOperations/05Exporter/ -->

<!-- page_index: 31 -->

# RocketMQ Prometheus Exporter

Version: 5.0

# RocketMQ Prometheus Exporter

<a id="deploymentoperations-05exporter--introduction"></a>

## Introduction

`Rocketmq-exporter` is a system for monitoring all relevant metrics of the RocketMQ broker and client sides, which packages the metric values obtained from the broker side through mqAdmin into 87 caches.

> [!WARNING]
> **caution**
> In previous versions, there were 87 concurrentHashMaps, but since the Map does not delete expired metrics, once there is a label change, a new metric is generated and the old, unused metric cannot be automatically deleted, which eventually causes a memory overflow. However, using the Cache structure can enable expired deletion, and the expiration time can be configured.

The process for `Rocketmq-exporter` to obtain monitoring metrics is shown in the following figure. The exporter requests data from the MQ cluster through MQAdminExt, and the requested data is standardized into the format required by Prometheus through the MetricService, and then exposed to Prometheus through the `/metrics` interface.
![4586095434](assets/images/rocketmq-20prometheus-20exporter-1-569c982f31d232cb9ddcafaf2aaf5ee7_f7241cd07ace21bf.jpeg)

<a id="deploymentoperations-05exporter--metric-structure"></a>

### Metric structure

The Metric class is located in the **`org.apache.rocketmq.expoter.model.metrics`** package, and is essentially a set of entity classes, with each entity class representing a type of metric, for a total of 14 Metric classes. These classes serve as the keys for the 87 caches and are distinguished by different label values.

> [!NOTE]
> **The entity classes contain three dimensions of labels：broker、consumer、producer**
> - **Metric classes related to the broker** : BrokerRuntimeMetric、BrokerMetric、DLQTopicOffsetMetric、TopicPutNumMetric
> - **Consumer-related classes** : ConsumerRuntimeConsumeFailedMsgsMetric 、ConsumerRuntimeConsumeFailedTPSMetric 、ConsumerRuntimeConsumeOKTPSMetric、ConsumerRuntimeConsumeRTMetric、ConsumerRuntimePullRTMetric、ConsumerRuntimePullTPSMetric、ConsumerCountMetric、ConsumerMetric、ConsumerTopicDiffMetric
> - **Producer-related metric classes**: ProducerMetric

<a id="deploymentoperations-05exporter--prometheus-pulls-metrics"></a>

### Prometheus pulls metrics

The `RocketMQ-exporter` project and `Prometheus` are equivalent to the server-client relationship, where the RocketMQ-exporter project introduces the Prometheus client package, which specifies the type of information to be obtained in the project's MetricFamilySamples class. Prometheus requests metrics from exporter, and exporter returns the information to Prometheus after packaging it into the corresponding type.

After the rocketmq-exporter project is started, it will collect various metrics from rocketmq into the mfs object. When the browser or Prometheus accesses the corresponding interface, the samples in the mfs object will be generated into the formatted data supported by Prometheus through the service. It mainly includes the following steps:

The browser accesses ip:5557/metrics to call the metrics method in the RMQMetricsController class, where ip is the IP of the host where the rocketmq-exporter project is running.

```java
private void metrics(HttpServletResponse response) throws IOException {
    StringWriter writer = new StringWriter();
    metricsService.metrics(writer);
    response.setHeader("Content-Type", "text/plain; version=0.0.4; charset=utf-8");
    response.getOutputStream().print(writer.toString());
}
```

By creating a new StringWriter object to collect metric indicators, the metrics in the exporter are collected into the writer object through the metrics method in the MetricsService class, and then the collected indicators are output to the webpage.

The format of the collected metrics is:

```javascript
<metric name>{<label name>=<label value>, ...} <metric value>
```

Example：

```javascript
rocketmq_group_diff{group="rmq_group_test_20220114",topic="fusion_console_tst",countOfOnlineConsumers="0",msgModel="1",} 23.0
```

<a id="deploymentoperations-05exporter--the-5-scheduled-tasks-in-the-metriccollecttask-class"></a>

### The 5 scheduled tasks in the MetricCollectTask class

The MetricCollectTask class has five scheduled tasks: collectTopicOffset, collectConsumerOffset, collectBrokerStatsTopic, collectBrokerStats, and collectBrokerRuntimeStats. They are used to collect consumer offset information and Broker state information, etc. Its cron expression is: cron: 15 0/1 \* \* \* ?, which means it will collect once per minute. Its core function is to obtain information from the broker in the cluster through the mqAdminExt object and then add it to the corresponding 87 monitoring indicators, taking collectTopicOffset as an example:

1. First, initialize the TopicList object and obtain all topic information in the cluster through the mqAdminExt.fetchAllTopicList() method.


```java
TopicList topicList = null;
try {
    topicList = mqAdminExt.fetchAllTopicList();
} catch (Exception ex) {
        log.error(String.format("collectTopicOffset-exception comes getting topic list from namesrv, address is %s",
            JSON.toJSONString(mqAdminExt.getNameServerAddressList())));
        return;
}
```

2. Add the topic to the topicSet, and iterate through each topic, checking the topic status through the mqAdminExt.examineTopicStats(topic) function.


```java
Set < String > topicSet = topicList != null ? topicList.getTopicList() : null;
for (String topic: topicSet) {
     TopicStatsTable topicStats = null;
     try {
         topicStats = mqAdminExt.examineTopicStats(topic);
     } catch (Exception ex) {
         log.error(String.format("collectTopicOffset-getting topic(%s) stats error. the namesrv address is %s",
             topic,
             JSON.toJSONString(mqAdminExt.getNameServerAddressList())));
         continue;}
```

3. Initialize the topic status set, the hash table brokerOffsetMap for topic information offset divided by broker, and a hash table brokerUpdateTimestampMap with broker name as the key to store the update timestamp.


```java
Set<Map.Entry<MessageQueue, TopicOffset>> topicStatusEntries = topicStats.getOffsetTable().entrySet();
HashMap<String, Long> brokerOffsetMap = new HashMap<>();
HashMap<String, Long> brokerUpdateTimestampMap = new HashMap<>();
for (Map.Entry<MessageQueue, TopicOffset> topicStatusEntry : topicStatusEntries) {
    MessageQueue q = topicStatusEntry.getKey();
    TopicOffset offset = topicStatusEntry.getValue();
    if (brokerOffsetMap.containsKey(q.getBrokerName())) {
        brokerOffsetMap.put(q.getBrokerName(), brokerOffsetMap.get(q.getBrokerName()) + offset.getMaxOffset());
    } else {
        brokerOffsetMap.put(q.getBrokerName(), offset.getMaxOffset());
    }
    if (brokerUpdateTimestampMap.containsKey(q.getBrokerName())) {
        if (offset.getLastUpdateTimestamp() > brokerUpdateTimestampMap.get(q.getBrokerName())) {
            brokerUpdateTimestampMap.put(q.getBrokerName(), offset.getLastUpdateTimestamp());
        }
    } else {
        brokerUpdateTimestampMap.put(q.getBrokerName(),
        offset.getLastUpdateTimestamp());
    }
}
```

4. Finally, by iterating through each item in the brokerOffsetMap, the metricCollector object is obtained through the metricsService and the addTopicOffsetMetric method in the RMQMetricsCollector class is called to add the corresponding value to one of the caches of the 87 metrics in the RMQMetricsCollector class.


```java
 Set<Map.Entry<String, Long>> brokerOffsetEntries = brokerOffsetMap.entrySet();
        for (Map.Entry<String, Long> brokerOffsetEntry : brokerOffsetEntries) {
            metricsService.getCollector().addTopicOffsetMetric(clusterName, brokerOffsetEntry.getKey(), topic,
                brokerUpdateTimestampMap.get(brokerOffsetEntry.getKey()), brokerOffsetEntry.getValue());
        }
    }
    log.info("topic offset collection task finished...." + (System.currentTimeMillis() - start));
}
```

<a id="deploymentoperations-05exporter--rocketmq-exporter-collects-metrics-flowchart"></a>

### Rocketmq-exporter collects metrics flowchart

![95680412354](assets/images/rocketmq-20prometheus-20exporter-20-202-fdd37b4d6c89244c23bac2bf87ff7e26_d4d416788e47b918.jpeg)

<a id="deploymentoperations-05exporter--quick-star"></a>

## Quick star

<a id="deploymentoperations-05exporter--configure-applicationyml"></a>

### Configure `application.yml`

Important configurations in `application.yml` include:

- server.port sets the port that Prometheus listens to for the rocketmq-exporter, with a default value of 5557.
- rocketmq.config.webTelemetryPath configures the path for Prometheus to obtain metrics, with a default value of /metrics. The default value can be used.
- rocketmq.config.enableACL If the RocketMQ cluster has enabled ACL verification, it needs to be set to true and the corresponding ak and sk need to be configured in accessKey and secretKey.
- rocketmq.config.outOfTimeSeconds is used to configure the expiration time of storing metrics and their values. If it exceeds this time and the key in the cache has not undergone a write change, it will be deleted. Generally, it can be configured as 60s (the time interval for Prometheus to obtain metrics should be reasonably configured according to the expiration time, as long as the expiration time is greater than or equal to the time interval for Prometheus to collect metrics).
- task.*.cron configures the time interval for the exporter to pull metrics from the broker through a scheduled task, with a default value of "15 0/1*  \* \* ?" which means it will pull metrics every 15s of every minute.

<a id="deploymentoperations-05exporter--start-exporter-application"></a>

### Start exporter application

<a id="deploymentoperations-05exporter--start-prometheus-according-to-the-configuration-on-its-official-website"></a>

### Start Prometheus according to the configuration on its official website

Configure Prometheus's static\_config: -targets to the exporter's starting IP and port, such as: localhost:5557.

<a id="deploymentoperations-05exporter--access-the-prometheus-page"></a>

### Access the Prometheus page

If the localhost starts at the default localhost:9090, you can view the collected metric values, as shown in the following figure:

![90671925984](assets/images/rocketmq-20prometheus-20exporter-3-f5d7bc508a5e4f791de91d2835b261b7_a6ff7442f8bede53.jpeg)

> [!TIP]
> For better visualization effects and to observe the trend of metric value changes, Prometheus is better used with Grafana!

<a id="deploymentoperations-05exporter--observability-metrics"></a>

## Observability metrics

Observability metrics mainly include two categories: server-side metrics and client-side metrics. Server-side metrics are directly generated by the server, and client-side metrics are generated on the client and obtained by the server through an RPC request to the client. Client-side metrics can be further divided into producer metrics and consumer metrics. All 87 observability metrics and their main meanings are as follows:

> [!INFO]
> **Server metrics**
> DOC2MDPLACEHOLDERTOKEN11END
>
> ### Server metrics
>
> <table><thead><tr><th>Metrics name</th><th>Definition</th><th>Corresponds to Broker metric name</th></tr></thead><tbody><tr><td>rocketmq_broker_tps</td><td>Broker-level production TPS</td><td></td></tr><tr><td>rocketmq_broker_qps</td><td>Broker-level consumption QPS</td><td></td></tr><tr><td>rocketmq_broker_commitlog_diff</td><td>Broker group synchronization behind message size from slave node</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_0ms</td><td>Server-side processing time for write request to completion of write（0ms）</td><td>putMessageDistributeTime</td></tr><tr><td>rocketmq_brokeruntime_pmdt_0to10ms</td><td>Server-side processing time for write request to completion of write（0~10ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_10to50ms</td><td>Server-side processing time for write request to completion of write（10~50ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_50to100ms</td><td>Server-side processing time for write request to completion of write（50~100ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_100to200ms</td><td>Server-side processing time for write request to completion of write（100~200ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_200to500ms</td><td>Server-side processing time for write request to completion of write（200~500ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_500to1s</td><td>Server-side processing time for write request to completion of write（500~1000ms）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_1to2s</td><td>Server-side processing time for write request to completion of write（1~2s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_2to3s</td><td>Server-side processing time for write request to completion of write（2~3s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_3to4s</td><td>Server-side processing time for write request to completion of write（3~4s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_4to5s</td><td>Server-side processing time for write request to completion of write（4~5s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_5to10s</td><td>Server-side processing time for write request to completion of write（5~10s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_pmdt_10stomore</td><td>Server-side processing time for write request to completion of write（&gt; 10s）</td><td></td></tr><tr><td>rocketmq_brokeruntime_dispatch_behind_bytes</td><td>The number of bytes of messages that have not been distributed yet (operations such as building indexes)</td><td>dispatchBehindBytes</td></tr><tr><td>rocketmq_brokeruntime_put_message_size_total</td><td>The total sum of the sizes of messages written to the broker</td><td>putMessageSizeTotal</td></tr><tr><td>rocketmq_brokeruntime_put_message_average_size</td><td>The average size of messages written to the broker</td><td>putMessageAverageSize</td></tr><tr><td>rocketmq_brokeruntime_remain_transientstore_buffer_numbs</td><td>The capacity of the queue in the TransientStorePool</td><td>remainTransientStoreBufferNumbs</td></tr><tr><td>rocketmq_brokeruntime_earliest_message_timestamp</td><td>The earliest timestamp of the messages stored by the broker</td><td>earliestMessageTimeStamp</td></tr><tr><td>rocketmq_brokeruntime_putmessage_entire_time_max</td><td>The maximum time it took to write messages to the broker since it started running</td><td>putMessageEntireTimeMax</td></tr><tr><td>rocketmq_brokeruntime_start_accept_sendrequest_time</td><td>The time at which the broker started accepting send requests</td><td>startAcceptSendRequestTimeStamp</td></tr><tr><td>rocketmq_brokeruntime_putmessage_times_total</td><td>The total number of times messages were written to the broker</td><td>putMessageTimesTotal</td></tr><tr><td>rocketmq_brokeruntime_getmessage_entire_time_max</td><td>The maximum time it took to process message pulls since the broker started running</td><td>getMessageEntireTimeMax</td></tr><tr><td>rocketmq_brokeruntime_pagecache_lock_time_mills</td><td></td><td>pageCacheLockTimeMills</td></tr><tr><td>rocketmq_brokeruntime_commitlog_disk_ratio</td><td>The usage ratio of the disk where the commitLog is located</td><td>commitLogDiskRatio</td></tr><tr><td>rocketmq_brokeruntime_dispatch_maxbuffer</td><td>A value that the broker has not calculated and remains at 0</td><td>dispatchMaxBuffer</td></tr><tr><td>rocketmq_brokeruntime_pull_threadpoolqueue_capacity</td><td>The capacity of the thread pool queue for processing pull requests.</td><td>pullThreadPoolQueueCapacity</td></tr><tr><td>rocketmq_brokeruntime_send_threadpoolqueue_capacity</td><td>Capacity of the queue in the thread pool handling pull requests</td><td>sendThreadPoolQueueCapacity</td></tr><tr><td>rocketmq_brokeruntime_query_threadpool_queue_capacity</td><td>Capacity of the queue in the thread pool handling query requests</td><td>queryThreadPoolQueueCapacity</td></tr><tr><td>rocketmq_brokeruntime_pull_threadpoolqueue_size</td><td>Actual size of the queue in the thread pool handling pull requests</td><td>pullThreadPoolQueueSize</td></tr><tr><td>rocketmq_brokeruntime_query_threadpoolqueue_size</td><td>Actual size of the queue in the thread pool handling query requests</td><td>queryThreadPoolQueueSize</td></tr><tr><td>rocketmq_brokeruntime_send_threadpool_queue_size</td><td>Actual size of the queue in the thread pool handling send requests</td><td>sendThreadPoolQueueSize</td></tr><tr><td>rocketmq_brokeruntime_pull_threadpoolqueue_headwait_timemills</td><td>Waiting time for the head task in the queue in the thread pool handling pull requests</td><td>pullThreadPoolQueueHeadWaitTimeMills</td></tr><tr><td>rocketmq_brokeruntime_query_threadpoolqueue_headwait_timemills</td><td>Waiting time for the head task in the queue in the thread pool handling query requests</td><td>queryThreadPoolQueueHeadWaitTimeMills</td></tr><tr><td>rocketmq_brokeruntime_send_threadpoolqueue_headwait_timemills</td><td>Waiting time for the head task in the queue in the thread pool handling send requests</td><td>sendThreadPoolQueueHeadWaitTimeMills</td></tr><tr><td>rocketmq_brokeruntime_msg_gettotal_yesterdaymorning</td><td>Total number of times messages were read up until midnight last night</td><td>msgGetTotalYesterdayMorning</td></tr><tr><td>rocketmq_brokeruntime_msg_puttotal_yesterdaymorning</td><td>Total number of times messages were written up until midnight last night</td><td>msgPutTotalYesterdayMorning</td></tr><tr><td>rocketmq_brokeruntime_msg_gettotal_todaymorning</td><td>Total number of times messages were read up until midnight tonight</td><td>msgGetTotalTodayMorning</td></tr><tr><td>rocketmq_brokeruntime_msg_puttotal_todaymorning</td><td>Total number of times messages were written up until midnight tonight</td><td>putMessageTimesTotal</td></tr><tr><td>rocketmq_brokeruntime_msg_put_total_today_now</td><td>The number of messages written to each broker so far.</td><td>msgPutTotalTodayNow</td></tr><tr><td>rocketmq_brokeruntime_msg_gettotal_today_now</td><td>The number of messages read from each broker so far.</td><td>msgGetTotalTodayNow</td></tr><tr><td>rocketmq_brokeruntime_commitlogdir_capacity_free</td><td>The available space in the directory where the commitLog are stored.</td><td>commitLogDirCapacity</td></tr><tr><td>rocketmq_brokeruntime_commitlogdir_capacity_total</td><td>The total space in the directory where the commit logs are stored.</td><td></td></tr><tr><td>rocketmq_brokeruntime_commitlog_maxoffset</td><td>The maximum offset of the commitLog.</td><td>commitLogMaxOffset</td></tr><tr><td>rocketmq_brokeruntime_commitlog_minoffset</td><td>The minimum offset of the commitLog.</td><td>commitLogMinOffset</td></tr><tr><td>rocketmq_brokeruntime_remain_howmanydata_toflush</td><td></td><td>remainHowManyDataToFlush</td></tr><tr><td>rocketmq_brokeruntime_getfound_tps600</td><td>The average TPS of messages received during getMessage in the past 600 seconds.</td><td>getFoundTps</td></tr><tr><td>rocketmq_brokeruntime_getfound_tps60</td><td>The average TPS of messages received during getMessage in the past 60 seconds.</td><td></td></tr><tr><td>rocketmq_brokeruntime_getfound_tps10</td><td>The average TPS of messages received during getMessage in the past 10 seconds.</td><td></td></tr><tr><td>rocketmq_brokeruntime_gettotal_tps600</td><td>The average TPS of getMessage calls in the past 600 seconds.</td><td>getTotalTps</td></tr><tr><td>rocketmq_brokeruntime_gettotal_tps60</td><td>The average TPS of getMessage calls in the past 60 seconds.</td><td></td></tr><tr><td>rocketmq_brokeruntime_gettotal_tps10</td><td>The average TPS of getMessage calls in the past 10 seconds.</td><td></td></tr><tr><td>rocketmq_brokeruntime_gettransfered_tps600</td><td></td><td>getTransferedTps</td></tr><tr><td>rocketmq_brokeruntime_gettransfered_tps60</td><td></td><td></td></tr><tr><td>rocketmq_brokeruntime_gettransfered_tps10</td><td></td><td></td></tr><tr><td>rocketmq_brokeruntime_getmiss_tps600</td><td>Average TPS for getMessage with no messages obtained in the past 600 seconds</td><td>getMissTps</td></tr><tr><td>rocketmq_brokeruntime_getmiss_tps60</td><td>Average TPS for getMessage with no messages obtained in the past 60 seconds</td><td></td></tr><tr><td>rocketmq_brokeruntime_getmiss_tps10</td><td>Average TPS for getMessage with no messages obtained in the past 10 seconds</td><td></td></tr><tr><td>rocketmq_brokeruntime_put_tps600</td><td>Average TPS for message write operations in the past 600 seconds</td><td>putTps</td></tr><tr><td>rocketmq_brokeruntime_put_tps60</td><td>Average TPS for message write operations in the past 60 seconds</td><td></td></tr><tr><td>rocketmq_brokeruntime_put_tps10</td><td>Average TPS for message write operations in the past 10 seconds</td><td></td></tr></tbody></table>

> [!INFO]
> **Producer metrics**
> DOC2MDPLACEHOLDERTOKEN12END
>
> ### Producer metrics
>
> <table><thead><tr><th>Metrics name</th><th>Definition</th></tr></thead><tbody><tr><td>rocketmq_producer_offset</td><td>The maximum offset of the topic at the current time</td></tr><tr><td>rocketmq_topic_retry_offset</td><td>The maximum offset of the retry topic at the current time</td></tr><tr><td>rocketmq_topic_dlq_offset</td><td>The maximum offset of the dead letter topic at the current time</td></tr><tr><td>rocketmq_producer_tps</td><td>The production TPS of the topic on a Broker group</td></tr><tr><td>rocketmq_producer_message_size</td><td>The TPS of the production message size of the topic on a Broker group</td></tr><tr><td>rocketmq_queue_producer_tps</td><td>Queue-level production TPS</td></tr><tr><td>rocketmq_queue_producer_message_size</td><td>Queue-level production TPS of message size</td></tr></tbody></table>

> [!INFO]
> **Consumer metrics**
> DOC2MDPLACEHOLDERTOKEN13END
>
> ### Consumer metrics
>
> <table><thead><tr><th>Metrics name</th><th>Definition</th></tr></thead><tbody><tr><td>rocketmq_group_diff</td><td>Consumer group message accumulation message count</td></tr><tr><td>rocketmq_group_retrydiff</td><td>Consumer group retry queue accumulation message count</td></tr><tr><td>rocketmq_group_dlqdiff</td><td>Consumer group dead letter queue accumulation message count</td></tr><tr><td>rocketmq_group_count</td><td>Number of consumers in the consumer group</td></tr><tr><td>rocketmq_client_consume_fail_msg_count</td><td>Number of times consumers in the consumer group have failed to consume in the past 1 hour</td></tr><tr><td>rocketmq_client_consume_fail_msg_tps</td><td>Consumer group consumer failure TPS</td></tr><tr><td>rocketmq_client_consume_ok_msg_tps</td><td>Consumer group consumer success TPS</td></tr><tr><td>rocketmq_client_consume_rt</td><td>Time taken for a message to be consumed after it has been pulled</td></tr><tr><td>rocketmq_client_consumer_pull_rt</td><td>Time taken for a client to pull a message</td></tr><tr><td>rocketmq_client_consumer_pull_tps</td><td>Client pull message TPS</td></tr><tr><td>rocketmq_consumer_tps</td><td>Consumption TPS of subscription group on each Broker group</td></tr><tr><td>rocketmq_group_consume_tps</td><td>Current consumption TPS of subscription group (aggregated by broker for rocketmq_consumer_tps)</td></tr><tr><td>rocketmq_consumer_offset</td><td>The current consumption Offset of the subscription group in a broker group</td></tr><tr><td>rocketmq_group_consume_total_offset</td><td>The current consumption Offset of the subscription group (aggregated by broker for rocketmq_consumer_offset)</td></tr><tr><td>rocketmq_consumer_message_size</td><td>The TPS of the subscription group consuming message size in a broker group</td></tr><tr><td>rocketmq_send_back_nums</td><td>The number of times the subscription group in a broker group has failed to consume and written to the retry message</td></tr><tr><td>rocketmq_group_get_latency_by_storetime</td><td>The consumption delay of the consumer group, the difference between the current time and when the exporter gets the message.</td></tr></tbody></table>

- [Introduction](#deploymentoperations-05exporter--introduction)
  - [Metric structure](#deploymentoperations-05exporter--metric-structure)
  - [Prometheus pulls metrics](#deploymentoperations-05exporter--prometheus-pulls-metrics)
  - [The 5 scheduled tasks in the MetricCollectTask class](#deploymentoperations-05exporter--the-5-scheduled-tasks-in-the-metriccollecttask-class)
  - [Rocketmq-exporter collects metrics flowchart](#deploymentoperations-05exporter--rocketmq-exporter-collects-metrics-flowchart)
- [Quick star](#deploymentoperations-05exporter--quick-star)
  - [Configure `application.yml`](#deploymentoperations-05exporter--configure-applicationyml)
  - [Start exporter application](#deploymentoperations-05exporter--start-exporter-application)
  - [Start Prometheus according to the configuration on its official website](#deploymentoperations-05exporter--start-prometheus-according-to-the-configuration-on-its-official-website)
  - [Access the Prometheus page](#deploymentoperations-05exporter--access-the-prometheus-page)
- [Observability metrics](#deploymentoperations-05exporter--observability-metrics)
  - [Server metrics](#deploymentoperations-05exporter--server-metrics)
  - [Producer metrics](#deploymentoperations-05exporter--producer-metrics)
  - [Consumer metrics](#deploymentoperations-05exporter--consumer-metrics)

---

<a id="observability-01metrics"></a>

<!-- source_url: https://rocketmq.apache.org/docs/observability/01metrics/ -->

<!-- page_index: 32 -->

# Metrics

Version: 5.0

# Metrics

RocketMQ exposes the following metrics in Prometheus format. You can monitor your clusters with those metrics.

- Broker metrics
- Producer metrics
- Consumer metrics

> Version support: The following metrics for RocketMQ were introduced since 5.1.0 and only support the broker.

<a id="observability-01metrics--details-of-metrics"></a>

## Details of metrics

<a id="observability-01metrics--metric-types"></a>

### Metric types

The standard for defining metrics in RocketMQ complies with that for defining the metrics in open source Prometheus. The metric types that RocketMQ offers include counters, gauges, and histograms. For more information, see [METRIC TYPES](https://prometheus.io/docs/concepts/metric_types/).

<a id="observability-01metrics--broker-metrics"></a>

### Broker metrics

The following table describes the labels of the metrics that are related to the Message Queue for Apache RocketMQ broker.

- cluster: RocketMQ cluster name.
- node\_type: the type of service node, whitch includes the following:proxy,broker,nameserver.
- node\_id: the ID of the service node.
- topic: the topic of RocketMQ.
- message\_type: the type of a message, which includes the following: normal:normal messages; fifo:ordered messages; transaction:Transactional messages; delay:scheduled or delayed messages.
- consumer\_group: the ID of the consumer group.
- invocation\_status: the result of the API call for create topic or consumer group, which includes success and failure.

<table><thead><tr><th>Type</th><th>Name</th><th>Unit</th><th>Description</th><th>Label</th></tr></thead><tbody><tr><td>counter</td><td>rocketmq_messages_in_total</td><td>count</td><td>The number of messages that are produced.</td><td>cluster,node_type,node_id,topic,message_type</td></tr><tr><td>counter</td><td>rocketmq_messages_out_total</td><td>count</td><td>The number of messages that are consumed.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>counter</td><td>rocketmq_throughput_in_total</td><td>byte</td><td>The write throughput that are produced.</td><td>cluster,node_type,node_id,topic,message_type</td></tr><tr><td>counter</td><td>rocketmq_throughput_out_total</td><td>byte</td><td>The read throughput that are produced.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>histogram</td><td>rocketmq_message_size</td><td>byte</td><td>The distribution of message sizes. This metric is counted only when messages are sent. The following shows the distribution ranges: le_1_kb: ≤ 1 KB  le_4_kb: ≤ 4 KB le_512_kb: ≤ 512 KB le_1_mb: ≤ 1 MB le_2_mb: ≤ 2 MB le_4_mb: ≤ 4 MB le_overflow: &gt; 4 MB</td><td>cluster,node_type,node_id,topic,message_type</td></tr><tr><td>gauge</td><td>rocketmq_consumer_ready_messages</td><td>count</td><td>The number of ready messages.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>gauge</td><td>rocketmq_consumer_inflight_messages</td><td>count</td><td>The number of inflight messages.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>gauge</td><td>rocketmq_consumer_queueing_latency</td><td>millisecond</td><td>Ready messages queueing delay time.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>gauge</td><td>rocketmq_consumer_lag_latency</td><td>millisecond</td><td>The delayed time before messages are consumed.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>counter</td><td>rocketmq_send_to_dlq_messages_total</td><td>count</td><td>The number of messages that are sent to the dead-letter queue.</td><td>cluster,node_type,node_id,topic, consumer_group</td></tr><tr><td>histogram</td><td>rocketmq_rpc_latency</td><td>millisecond</td><td>The rpc call latency</td><td>cluster,node_typ,node_id,protocol_type,request_code,response_code</td></tr><tr><td>gauge</td><td>rocketmq_storage_message_reserve_time</td><td>millisecond</td><td>Message retention time.</td><td>cluster,node_type,node_id</td></tr><tr><td>gauge</td><td>rocketmq_storage_dispatch_behind_bytes</td><td>byte</td><td>Undispatched message size.</td><td>cluster,node_type,node_id</td></tr><tr><td>gauge</td><td>rocketmq_storage_flush_behind_bytes</td><td>byte</td><td>Unflushed message size.</td><td>cluster,node_type,node_id</td></tr><tr><td>gauge</td><td>rocketmq_thread_pool_wartermark</td><td>count</td><td>The number of tasks queued in the thread pool.</td><td>cluster,node_type,node_id,name</td></tr><tr><td>histogram</td><td>rocketmq_topic_create_execution_time</td><td>millisecond</td><td>The execution time for creating topic:  le_10_ms le_100_ms le_1_s le_3_s le_5_s le_overflow</td><td>cluster,node_type,node_id,invocation_status,is_system</td></tr><tr><td>histogram</td><td>rocketmq_consumer_group_create_execution_time</td><td>millisecond</td><td>The execution time for creating consumer group:  le_10_ms le_100_ms le_1_s le_3_s le_5_s le_overflow</td><td>cluster,node_type,node_id,invocation_status</td></tr><tr><td>gauge</td><td>rocketmq_topic_number</td><td>count</td><td>The number of topics</td><td>cluster,node_type,node_id</td></tr><tr><td>gauge</td><td>rocketmq_consumer_group_number</td><td>count</td><td>The number of consumer group</td><td>cluster,node_type,node_id</td></tr></tbody></table>
<a id="observability-01metrics--producer-metrics"></a>

### Producer metrics

The following table describes the labels of the metrics that are related to the producers in Message Queue for Apache RocketMQ.

- cluster: RocketMQ cluster name.
- node\_type: the type of service node, whitch includes the following:proxy,broker,nameserver.
- node\_id: the ID of the service node.
- topic: the topic of Message Queue for Apache RocketMQ.
- message\_type: the type of a message, which includes the following: normal:normal messages; fifo:ordered messages; transaction:Transactional messages; delay:scheduled or delayed messages.
- client\_id: the ID of the client.
- invocation\_status: the result of the API call for sending messages, which includes success and failure.

<table><thead><tr><th>Type</th><th>Name</th><th>Unit</th><th>Description</th><th>Label</th></tr></thead><tbody><tr><td>Histogram</td><td>rocketmq_send_cost_time</td><td>millisecond</td><td>The distribution of production API call time. The following shows the distribution ranges:  le_1_ms  le_5_ms le_10_ms le_20_ms  le_50_ms  le_200_ms le_500_ms  le_overflow</td><td>topic,client_id,invocation_status</td></tr></tbody></table>
<a id="observability-01metrics--consumer-metrics"></a>

### Consumer metrics

The following table describes the labels of the metrics that are related to the consumers in Message Queue for Apache RocketMQ.

- topic: the topic of Message Queue for Apache RocketMQ.
- consumer\_group: the ID of the consumer group.
- client\_id: the ID of the client.
- invocation\_status: the result of the API call for consuming messages, which includes success and failure.

<table><thead><tr><th>Type</th><th>Name</th><th>Unit</th><th>Description</th><th>Label</th></tr></thead><tbody><tr><td>Histogram</td><td>rocketmq_process_time</td><td>millisecond</td><td>The distribution of message process time.The following shows the distribution ranges:  le_1_ms  le_5_ms   le_10_ms le_100_ms  le_10000_ms le_60000_ms  le_overflow</td><td>topic,consumer_group,client_id,invocation_status</td></tr><tr><td>gauge</td><td>rocketmq_consumer_cached_messages</td><td>message</td><td>The number of messages in the local buffer queue of PushConsumer.</td><td>topic,consumer_group,client_id</td></tr><tr><td>gauge</td><td>rocketmq_consumer_cached_bytes</td><td>byte</td><td>The total size of messages in the local buffer queue of PushConsumer.</td><td>topic,consumer_group,client_id</td></tr><tr><td>Histogram</td><td>rocketmq_await_time</td><td>millisecond</td><td>The distribution of queuing time for messages in the local buffer queue of PushConsumer. The following shows the distribution ranges: le_1_ms  le_5_ms le_20_ms le_100_ms  le_1000_ms  le_5000_ms  le_10000_ms le_overflow</td><td>topic,consumer_group,client_id</td></tr></tbody></table>
<a id="observability-01metrics--background-information"></a>

## Background information

RocketMQ defines metrics based on the following business scenarios.

<a id="observability-01metrics--message-accumulation-scenarios"></a>

### Message accumulation scenarios

![rocketmq queue meesage stuatus](assets/images/message-accumulation-4a033c0e12019e8da39e570e02247318_410dc4e918b6f490.png) The above figure shows the number and duration of messages in different stages. By monitoring these metrics, you can determine whether the business consumption is abnormal. The following table describes the meaning of these metrics and the formulas that are used to calculate these metrics.

<table><thead><tr><th>Name</th><th>Description</th><th>Formula</th></tr></thead><tbody><tr><td>Inflight messages</td><td>The number of messages being processed by consumer but not acked yet</td><td>Offset of the latest pulled message - Offset of the latest committed message</td></tr><tr><td>Ready messages</td><td>The number of messages that are ready for consumption.</td><td>Maximum offset - Offset of the latest pulled message</td></tr><tr><td>Ready time</td><td>normal message or ordered message:the time when the message is stored to the broker.    Scheduled message:timing end time.    Transactional message: transaction commit time.</td><td>--</td></tr><tr><td>Ready message queue time</td><td>The time interval between the ready time of the earliest ready message and the current time. This time reflects the timeliness of consumers pulling messages.</td><td>Current time - Ready time of the earliest ready message</td></tr><tr><td>Consumer lag time</td><td>The time difference between the ready time of the earliest unacked message and the current moment. This time reflects the timeliness of the consumer to complete message processing.</td><td>Current time - Ready time of the earliest unacked message</td></tr></tbody></table>
<a id="observability-01metrics--pushconsumer-consumption-scenarios"></a>

### PushConsumer consumption scenarios

In PushConsumer, real-time message processing capability is implemented based on the typical Reactor thread model inside the SDK.As shown below, the SDK has a built-in long polling thread that asynchronously pulls messages into the SDK's built-in buffer queue and then separately commits them to the consumer thread, triggering the listener to execute the local consumption logic. ![PushConsumer client](assets/images/pushconsumer-consumption-1e24bd7ab8e28a1f165635bd5a49637f_198042c36db6b681.png) The metrics of local buffer queues in the PushConsumer scenario are as follows:

- Number of messages in the local buffer queue: Total number of messages in the local buffer queue.
- Message size in the local buffer queue: The sum of all message sizes in the local buffer queue.
- Message waiting time: the time that the message is temporarily cached in the local buffer queue waiting to be processed.

<a id="observability-01metrics--how-to-obtain-metrics"></a>

## How to Obtain Metrics

Currently, two exporters are supported: gRPC OTLP and Prometheus.

<a id="observability-01metrics--grpc-otlp-exporter"></a>

### gRPC OTLP Exporter

The gRPC OTLP exporter periodically reports metrics to the specified OpenTelemetry Collector.

Prerequisites: Deploy an OpenTelemetry Collector that supports the [GRPC OpenTelemetry Protocol](https://github.com/open-telemetry/oteps/blob/main/text/0035-opentelemetry-protocol.md).

To enable the gRPC OTLP exporter of Broker metrics, do the following:

1. Set `metricsExporterType` to `OTLP_GRPC`.
2. Set `metricsGrpcExporterTarget` to the endpoint provided by the OpenTelemetry Collector.

Optional configurations:

1. `metricsGrpcExporterHeader`: Attach request headers to the gRPC OTLP exporter in the format of key1:value1,key2:value2.
2. `metricGrpcExporterTimeOutInMills`: Set the request timeout for the gRPC OTLP exporter.
3. `metricGrpcExporterIntervalInMills`: Set the reporting interval for the gRPC OTLP exporter.

<a id="observability-01metrics--prometheus-exporter"></a>

### Prometheus Exporter

The Prometheus exporter only supports Pull mode and Cumulative aggregation. See [OpenTelemetry Metrics Exporter - Prometheus](https://opentelemetry.io/docs/reference/specification/metrics/sdk_exporters/prometheus/) for more information.

To enable the Prometheus exporter of Broker metrics, do the following:

1. Set `metricsExporterType` to `PROM`.

Visit `http://<broker-ip>:5557/metrics` to view metrics. Configure service discovery or manually configure a pull task in Prometheus to collect metrics.

Optional configurations:

1. `metricsPromExporterPort`: The port number on which Broker exposes the metrics service. The default is `5557`.
2. `metricGrpcExporterTimeOutInMills`: The hostname for the exposed metrics service. The default is the IP to which Broker registers with NameServer, brokerIP1.

- [Details of metrics](#observability-01metrics--details-of-metrics)
  - [Metric types](#observability-01metrics--metric-types)
  - [Broker metrics](#observability-01metrics--broker-metrics)
  - [Producer metrics](#observability-01metrics--producer-metrics)
  - [Consumer metrics](#observability-01metrics--consumer-metrics)
- [Background information](#observability-01metrics--background-information)
  - [Message accumulation scenarios](#observability-01metrics--message-accumulation-scenarios)
  - [PushConsumer consumption scenarios](#observability-01metrics--pushconsumer-consumption-scenarios)
- [How to Obtain Metrics](#observability-01metrics--how-to-obtain-metrics)
  - [gRPC OTLP Exporter](#observability-01metrics--grpc-otlp-exporter)
  - [Prometheus Exporter](#observability-01metrics--prometheus-exporter)

---

<a id="sdk-01overview"></a>

<!-- source_url: https://rocketmq.apache.org/docs/sdk/01overview/ -->

<!-- page_index: 33 -->

# Overview

Version: 5.0

# Overview

This section introduces the evolution history, selection comparison, and best practices of the Apache RocketMQ 5.x client SDK.

<a id="sdk-01overview--history-and-choice"></a>

## History and Choice

Since its inception, the Apache RocketMQ project has evolved to the current version 5.x. Currently, rocketmq mainly supporting two series of client SDKs based on differences in underlying communication protocols, namely the Remoting protocol and the gRPC protocol.

As the default communication protocol between early components, the Remoting protocol has an embedded client SDK that has been evolving and iterating in sync with the main repository. The Remoting protocol SDK has always been bound with the server code version iteration and mainly supports Java-based languages.

The gRPC protocol was newly introduced in version 5.0, aimed at evolving a more lightweight, standardized, and easily extensible client-server communication protocol with mainstream cloud native technologies. The gRPC protocol SDK evolves as an independent repository  [RocketMQ Clients](https://github.com/apache/rocketmq-clients) , supporting languages such as Java/C++/.NET/Go/Rust. There is a relatively decoupled relationship between the client and the server, following the RocketMQ API protocol interface agreement.

> [!TIP]
> How to quickly distinguish whether the SDK used is the Remoting protocol or the gRPC protocol?
>
> Method 1: Check the repository coordinates
>
> - For Java language: If the repository coordinate is rocketmq-client, it is the Remoting protocol. If it is rocketmq-client-java, it is the gRPC protocol.
> - For other languages: Other gRPC languages are also named in the format of rocketmq-client-{language}.
>
> Method 2: Check the keywords
>
> - If the code package or classpath contains the keyword 'remoting', it is the Remoting protocol. Otherwise, it is the gRPC protocol SDK.

The comparison between the Remoting protocol SDK and the gRPC protocol SDK, please refer to the following:

<table><thead><tr><th><strong>Contrast term</strong></th><th><strong>Remoting SDK</strong></th><th><strong>gRPC SDK</strong></th></tr></thead><tbody><tr><td>Multi-language support</td><td>Java/Go</td><td>Java/C/C++/.NET/Go/Rust  Details for <a href="https://github.com/apache/rocketmq-clients" rel="noopener noreferrer" target="_blank">Link</a></td></tr><tr><td>Feature and Interface</td><td>Producer PushConsumer PullConsumer LitePullConsumer Admin</td><td>Producer PushConsumer（Only Java） SimpleConsumer PullConsumer（working）</td></tr><tr><td>Compatible version</td><td>Support 4.x and 5.x server</td><td>Only support server versions 5.0</td></tr><tr><td>Evolution</td><td>The Remoting protocol is mainly used for communication evolution of internal components within the server</td><td>The gRPC protocol is the preferred lightweight multi-language client, and subsequent promotion will gradually fill in all capabilities</td></tr></tbody></table>
<a id="sdk-01overview--remoting-sdk"></a>

## Remoting SDK

The Remoting protocol SDK, as the initial SDK evolution of Apache RocketMQ, uses the Remoting communication protocol of internal components of RocketMQ. It's used for communication of internal components of services and also supports API communication for client message sending and control operations.

<a id="sdk-01overview--sdk-info"></a>

### SDK Info

The currently supported programming languages and code repositories are as follows:

<table><thead><tr><th><strong>Language</strong></th><th><strong>ReleaseNote</strong></th><th><strong>SDK Repo</strong></th></tr></thead><tbody><tr><td>Java</td><td><a href="https://github.com/apache/rocketmq/releases" rel="noopener noreferrer" target="_blank">ReleaseNote from main repo</a></td><td><a href="https://github.com/apache/rocketmq" rel="noopener noreferrer" target="_blank">Main repo</a></td></tr><tr><td>Go</td><td><a href="https://github.com/apache/rocketmq-client-go/releases" rel="noopener noreferrer" target="_blank">ReleaseNote from main repo</a></td><td><a href="https://github.com/apache/rocketmq-client-go" rel="noopener noreferrer" target="_blank">Main repo</a></td></tr></tbody></table>
<a id="sdk-01overview--features"></a>

### Features

Waiting updates.

<a id="sdk-01overview--grpc-sdk"></a>

## gRPC SDK

The gRPC protocol SDK, introduced in Apache RocketMQ version 5.0, aims to provide a cloud-native, robust client solution for all major programming languages, including Java, C++, C#, Golang, JavaScript, and Rust. The gRPC SDK adheres to the [rocketmq-apis](https://github.com/apache/rocketmq-apis) constraints and uses Protocol Buffers and gRPC to replace the old protocol in version 4.x.

The gRPC SDK has the following advantages over the earlier Remoting protocol SDK:

- More concise interface design, easier to understand and less prone to error.
- Better interface design with clear parameters and exception types.
- Immutable interface design to avoid business exceptions caused by parameter and information leakage.
- Better support for multiple languages, as the gRPC protocol has the advantage of supporting multiple languages and enables lower cost evolution to achieve consistent behavior in multiple language SDKs.

Want the detailed design thinking and evolutionary direction, refer to [RIP-37: New and Unified APIs](https://docs.qq.com/doc/DUkNwdkdQUU15V1Fr) and [RIP-39: Support gRPC protocol](https://shimo.im/docs/gXqmeEPYgdUw5bqo).

<a id="sdk-01overview--sdk-info-1"></a>

### SDK Info

The currently supported programming languages and code repositories, refer to [rocketmq-clients](https://github.com/apache/rocketmq-clients#features-and-status).

<a id="sdk-01overview--features-1"></a>

### Features

Waiting updates.

<a id="sdk-01overview--faq"></a>

## FAQ

The following sections list some recommended selection strategies for certain scenarios.

1. **Can gRPC SDK be used with a server version of 4.x?**

   No, gRPC SDK is only supported by server versions equal to or greater than 5.0. It is recommended to first smoothly upgrade the server to version 5.0 and then replace the SDK.
2. **Is it necessary to modify the code when switching from Remoting SDK to gRPC SDK?**

   Yes, it is necessary. The client API of gRPC SDK has been redesigned and is not compatible with the Remoting SDK API. Therefore, it is necessary to modify the code accordingly.
3. **What's the best choice of sdk when use rocketmq in new system？**

   If a new business system is integrating with RocketMQ, it is recommended to use gRPC SDK, as it provides a better user experience and support for multiple language environments.

- [History and Choice](#sdk-01overview--history-and-choice)
- [Remoting SDK](#sdk-01overview--remoting-sdk)
  - [SDK Info](#sdk-01overview--sdk-info)
  - [Features](#sdk-01overview--features)
- [gRPC SDK](#sdk-01overview--grpc-sdk)
  - [SDK Info](#sdk-01overview--sdk-info-1)
  - [Features](#sdk-01overview--features-1)
- [FAQ](#sdk-01overview--faq)

---

<a id="sdk-02java"></a>

<!-- source_url: https://rocketmq.apache.org/docs/sdk/02java/ -->

<!-- page_index: 34 -->

# Java Client SDK

Version: 5.0

# Java Client SDK

<a id="sdk-02java--info"></a>

## Info

This section introduces sending and receiving messages using Apache RocketMQ 5.0 gRPC protocol Java SDK.

> [!INFO]
> - This sample code is built based on the gRPC protocol SDK. Therefore, the server needs to be upgraded to at least version 5.0 and enable gRPC Proxy to be compatible. Please refer to the [quick start guide](#quickstart-01quickstart) for deploying Proxy.
> - If you are using the Remoting protocol SDK, it is recommended to refer to the example code of the previous version 4.x for running. To identify the type of SDK you are using, please refer to the [overview](#sdk-01overview).

<a id="sdk-02java--codeexample"></a>

## CodeExample

Here is the link to the sample code for message sending and receiving using the Apache RocketMQ gRPC protocol Java SDK. The complete code project and runtime environment can be found in the [rocketmq-clients](https://github.com/apache/rocketmq-clients) repository. Please refer to it for configuration and running.

<table><thead><tr><th><strong>MessageTypes</strong></th><th><strong>Producer Examples</strong></th><th><strong>PushConsumer Examples</strong></th><th><strong>SimpleConsumer Examples</strong></th></tr></thead><tbody><tr><td><a href="#featurebehavior-01normalmessage">NormalMessage</a></td><td>Sync Send Example:<a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/ProducerNormalMessageExample.java" rel="noopener noreferrer" target="_blank">ProducerNormalMessageExample.java</a>  Async Send Example:<a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/AsyncProducerExample.java" rel="noopener noreferrer" target="_blank">AsyncProducerExample.java</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/PushConsumerExample.java" rel="noopener noreferrer" target="_blank">PushConsumerExample.java</a></td><td>Sync Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/SimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.java</a>  Async Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/AsyncSimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">AsyncSimpleConsumerExample.java</a></td></tr><tr><td><a href="#featurebehavior-03fifomessage">FIFOMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/ProducerFifoMessageExample.java" rel="noopener noreferrer" target="_blank">ProducerFifoMessageExample.java</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/PushConsumerExample.java" rel="noopener noreferrer" target="_blank">PushConsumerExample.java</a></td><td>Sync Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/SimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.java</a>  Async Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/AsyncSimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">AsyncSimpleConsumerExample.java</a></td></tr><tr><td><a href="#featurebehavior-02delaymessage">DelayMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/ProducerDelayMessageExample.java" rel="noopener noreferrer" target="_blank">ProducerDelayMessageExample.java</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/PushConsumerExample.java" rel="noopener noreferrer" target="_blank">PushConsumerExample.java</a></td><td>Sync Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/SimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.java</a>  Async Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/AsyncSimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">AsyncSimpleConsumerExample.java</a></td></tr><tr><td><a href="#featurebehavior-04transactionmessage">TransactionMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/ProducerTransactionMessageExample.java" rel="noopener noreferrer" target="_blank">ProducerTransactionMessageExample.java</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/PushConsumerExample.java" rel="noopener noreferrer" target="_blank">PushConsumerExample.java</a></td><td>Sync Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/SimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.java</a>  Async Sub Message: <a href="https://github.com/apache/rocketmq-clients/blob/master/java/client/src/main/java/org/apache/rocketmq/client/java/example/AsyncSimpleConsumerExample.java" rel="noopener noreferrer" target="_blank">AsyncSimpleConsumerExample.java</a></td></tr></tbody></table>

- [Info](#sdk-02java--info)
- [CodeExample](#sdk-02java--codeexample)

---

<a id="sdk-03cplusplus"></a>

<!-- source_url: https://rocketmq.apache.org/docs/sdk/03cplusplus/ -->

<!-- page_index: 35 -->

# C++ Client SDK

Version: 5.0

# C++ Client SDK

<a id="sdk-03cplusplus--info"></a>

## Info

This section introduces sending and receiving messages using Apache RocketMQ 5.0 gRPC protocol C++ SDK.

> [!INFO]
> - This sample code is built based on the gRPC protocol SDK. Therefore, the server needs to be upgraded to at least version 5.0 and enable gRPC Proxy to be compatible. Please refer to the [quick start guide](#quickstart-01quickstart) for deploying Proxy.
> - If you are using the Remoting protocol SDK, it is recommended to refer to the example code of the previous version 4.x for running. To identify the type of SDK you are using, please refer to the [overview](#sdk-01overview).

<a id="sdk-03cplusplus--codeexample"></a>

## CodeExample

Here is the link to the sample code for message sending and receiving using the Apache RocketMQ gRPC protocol C++ SDK. The complete code project and runtime environment can be found in the [rocketmq-clients](https://github.com/apache/rocketmq-clients) repository. Please refer to it for configuration and running.

<table><thead><tr><th><strong>MessageTypes</strong></th><th><strong>Producer Examples</strong></th><th><strong>PushConsumer Examples</strong></th><th><strong>SimpleConsumer Examples</strong></th></tr></thead><tbody><tr><td><a href="#featurebehavior-01normalmessage">NormalMessage</a></td><td>Sync Send Example:<a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleProducer.cpp" rel="noopener noreferrer" target="_blank">ExampleProducer.cpp</a>  Async Send Example:<a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleProducerWithAsync.cpp" rel="noopener noreferrer" target="_blank">ExampleProducerWithAsync.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExamplePushConsumer.cpp" rel="noopener noreferrer" target="_blank">ExamplePushConsumer.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleSimpleConsumer.cpp" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.cpp</a></td></tr><tr><td><a href="#featurebehavior-03fifomessage">FIFOMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleProducerWithFifoMessage.cpp" rel="noopener noreferrer" target="_blank">ExampleProducerWithFifoMessage.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExamplePushConsumer.cpp" rel="noopener noreferrer" target="_blank">ExamplePushConsumer.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleSimpleConsumer.cpp" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.cpp</a></td></tr><tr><td><a href="#featurebehavior-02delaymessage">DelayMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleProducerWithTimedMessage.cpp" rel="noopener noreferrer" target="_blank">ExampleProducerWithTimedMessage.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExamplePushConsumer.cpp" rel="noopener noreferrer" target="_blank">ExamplePushConsumer.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleSimpleConsumer.cpp" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.cpp</a></td></tr><tr><td><a href="#featurebehavior-04transactionmessage">TransactionMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleProducerWithTransactionalMessage.cpp" rel="noopener noreferrer" target="_blank">ExampleProducerWithTransactionalMessage.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExamplePushConsumer.cpp" rel="noopener noreferrer" target="_blank">ExamplePushConsumer.cpp</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/cpp/examples/ExampleSimpleConsumer.cpp" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.cpp</a></td></tr></tbody></table>

- [Info](#sdk-03cplusplus--info)
- [CodeExample](#sdk-03cplusplus--codeexample)

---

<a id="sdk-04csharp"></a>

<!-- source_url: https://rocketmq.apache.org/docs/sdk/04csharp/ -->

<!-- page_index: 36 -->

# C# Client SDK

Version: 5.0

# C# Client SDK

<a id="sdk-04csharp--info"></a>

## Info

This section introduces sending and receiving messages using Apache RocketMQ 5.0 gRPC protocol C# SDK.

> [!INFO]
> - This sample code is built based on the gRPC protocol SDK. Therefore, the server needs to be upgraded to at least version 5.0 and enable gRPC Proxy to be compatible. Please refer to the [quick start guide](#quickstart-01quickstart) for deploying Proxy.
> - If you are using the Remoting protocol SDK, it is recommended to refer to the example code of the previous version 4.x for running. To identify the type of SDK you are using, please refer to the [overview](#sdk-01overview).

<a id="sdk-04csharp--codeexample"></a>

## CodeExample

Here is the link to the sample code for message sending and receiving using the Apache RocketMQ gRPC protocol C# SDK. The complete code project and runtime environment can be found in the [rocketmq-clients](https://github.com/apache/rocketmq-clients) repository. Please refer to it for configuration and running.

<table><thead><tr><th><strong>MessageTypes</strong></th><th><strong>Producer Examples</strong></th><th><strong>SimpleConsumer Examples</strong></th></tr></thead><tbody><tr><td><a href="#featurebehavior-01normalmessage">NormalMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/ProducerNormalMessageExample.cs" rel="noopener noreferrer" target="_blank">ProducerNormalMessageExample.cs</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/SimpleConsumerExample.cs" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.cs</a></td></tr><tr><td><a href="#featurebehavior-03fifomessage">FIFOMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/ProducerFifoMessageExample.cs" rel="noopener noreferrer" target="_blank">ProducerFifoMessageExample.cs</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/SimpleConsumerExample.cs" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.cs</a></td></tr><tr><td><a href="#featurebehavior-02delaymessage">DelayMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/ProducerDelayMessageExample.cs" rel="noopener noreferrer" target="_blank">ProducerDelayMessageExample.cs</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/SimpleConsumerExample.cs" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.cs</a></td></tr><tr><td><a href="#featurebehavior-04transactionmessage">TransactionMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/ProducerTransactionMessageExample.cs" rel="noopener noreferrer" target="_blank">ProducerTransactionMessageExample.cs</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/master/csharp/examples/SimpleConsumerExample.cs" rel="noopener noreferrer" target="_blank">SimpleConsumerExample.cs</a></td></tr></tbody></table>

- [Info](#sdk-04csharp--info)
- [CodeExample](#sdk-04csharp--codeexample)

---

<a id="sdk-05go"></a>

<!-- source_url: https://rocketmq.apache.org/docs/sdk/05go/ -->

<!-- page_index: 37 -->

# Go Client SDK

Version: 5.0

# Go Client SDK

<a id="sdk-05go--info"></a>

## Info

This section introduces sending and receiving messages using Apache RocketMQ 5.0 gRPC protocol Go SDK.

> [!INFO]
> - This sample code is built based on the gRPC protocol SDK. Therefore, the server needs to be upgraded to at least version 5.0 and enable gRPC Proxy to be compatible. Please refer to the [quick start guide](#quickstart-01quickstart) for deploying Proxy.
> - If you are using the Remoting protocol SDK, it is recommended to refer to the example code of the previous version 4.x for running. To identify the type of SDK you are using, please refer to the [overview](#sdk-01overview).

<a id="sdk-05go--codeexample"></a>

## CodeExample

Here is the link to the sample code for message sending and receiving using the Apache RocketMQ gRPC protocol Go SDK. The complete code project and runtime environment can be found in the [rocketmq-clients](https://github.com/apache/rocketmq-clients) repository. Please refer to it for configuration and running.

<table><thead><tr><th><strong>MessageTypes</strong></th><th><strong>Producer Examples</strong></th><th><strong>SimpleConsumer Examples</strong></th></tr></thead><tbody><tr><td><a href="#featurebehavior-01normalmessage">NormalMessage</a></td><td>Sync producer:<a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/producer/normal/main.go" rel="noopener noreferrer" target="_blank">ExampleProducerNormalMessage.go</a>  Async producer:<a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/producer/async/main.go" rel="noopener noreferrer" target="_blank">AsyncExampleProducerNormalMessage.go</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/consumer/simple_consumer/main.go" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.go</a></td></tr><tr><td><a href="#featurebehavior-03fifomessage">FIFOMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/producer/fifo/main.go" rel="noopener noreferrer" target="_blank">ExampleProducerWithFifoMessage.go</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/consumer/simple_consumer/main.go" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.go</a></td></tr><tr><td><a href="#featurebehavior-02delaymessage">DelayMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/producer/delay/main.go" rel="noopener noreferrer" target="_blank">ExampleProducerDelayMessage.go</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/consumer/simple_consumer/main.go" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.go</a></td></tr><tr><td><a href="#featurebehavior-04transactionmessage">TransactionMessage</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/producer/transaction/main.go" rel="noopener noreferrer" target="_blank">ExampleProducerWithTransactionalMessage.go</a></td><td><a href="https://github.com/apache/rocketmq-clients/blob/rocketmq-client-golang-5.0.0/golang/example/consumer/simple_consumer/main.go" rel="noopener noreferrer" target="_blank">ExampleSimpleConsumer.go</a></td></tr></tbody></table>

- [Info](#sdk-05go--info)
- [CodeExample](#sdk-05go--codeexample)

---

<a id="bestpractice-01bestpractice"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/01bestpractice/ -->

<!-- page_index: 38 -->

# Basic Best Practices

Version: 5.0

# Basic Best Practices

<a id="bestpractice-01bestpractice--producer"></a>

## Producer

<a id="bestpractice-01bestpractice--precautions-for-sending-messages"></a>

### Precautions for sending messages

<a id="bestpractice-01bestpractice--the-use-of-tags"></a>

#### The use of Tags

An application can be identified as a Topic, and message subtypes can be identified as tags. tags can be set freely by the application. Only when the producer sets tags when sending messages, the consumer can use tags to filter messages through the broker when subscribing messages.
5.x SDK can call messageBuilder.setTag("messageTag") and historical versions can call message.setTags("messageTag").

<a id="bestpractice-01bestpractice--the-use-of-keys"></a>

#### The use of Keys

At the service level, it is recommended that each message be mapped to a unique service identifier and set to the keys field to locate message loss problems in the future. The server creates an index (hash index) for each message, and the application can query the content of the message by topic and key, and by whom the message was consumed. Since it is a hash index, make sure that the key is as unique as possible to avoid potential hash collisions. Common setup policies use discrete unique identifiers such as order Id, user Id, and request Id.

<a id="bestpractice-01bestpractice--printing-logs"></a>

#### Printing Logs

If the message is sent successfully or fails, you need to print message logs for troubleshooting services. Send Indicates that the message is sent successfully as long as no exception is thrown.

<a id="bestpractice-01bestpractice--handling-method-for-message-sending-failure"></a>

### Handling method for message sending failure

The send method of the Producer itself supports internal retry,5.x Retry logic reference [Send retry policy](#featurebehavior-05sendretrypolicy)：

The above strategies also guarantee the success of message sending to a certain extent. If the business requires that the message be sent without loss, you still need to cover for possible exceptions, such as when the send synchronization method is called and fails to send, then try to store the message to the db and retry periodically by the background thread to ensure that the message reaches the Broker.

The reason why the above DB retry method is not integrated into the MQ client, but requires the application to complete by itself, is mainly based on the following considerations: First, the MQ client is designed as a stateless mode, convenient for arbitrary horizontal expansion, and the consumption of machine resources is only cpu, memory, network. Secondly, if the MQ client is internally integrated with a KV storage module, the data can only be reliable if the synchronous disk fall, and the synchronous disk fall itself has a large performance overhead, so it usually uses asynchronous disk fall, and because the application closure process is not controlled by MQ operation and maintenance personnel, it may often happen kill -9 such violent closure. Resulting in data not timely drop disk and loss. Third, the machine where the Producer resides has low reliability and is generally virtual machines, which are not suitable for storing important data. In summary, it is recommended that the retry process be controlled by the application.

<a id="bestpractice-01bestpractice--consumer"></a>

## Consumer

<a id="bestpractice-01bestpractice--the-consumption-process-is-idempotent"></a>

### The consumption process is idempotent

RocketMQ cannot avoid message duplications (Exactly Once), so if the business is very sensitive to consumption duplications, it is important to de-process at the business level.
This can be done with the help of relational databases. You first need to determine a unique key for the message, either an msgId or a unique identifying field in the message content, such as an order id.
Determine if the unique key exists in the relational database before consumption. If not, insert and consume, otherwise skip. (The actual process should consider the atomicity problem, determine whether there is a primary key conflict, then the insertion failed, directly skip)

MsgId must be a globally unique identifier, but in practice, there may be cases where the same message has two different msgIds (consumer active retransmission, duplication due to client reinvestment mechanism, etc.), which necessitates repeated consumption of business fields.

<a id="bestpractice-01bestpractice--a-slow-process-of-consumption"></a>

### A slow process of consumption

<a id="bestpractice-01bestpractice--increase-consumption-parallelism"></a>

### Increase consumption parallelism

The vast majority of message consumption is IO intensive, that is, it may be operating on a database or calling an RPC, and the rate of consumption for this type of consumption depends on the throughput of the back-end database or external system.
By increasing consumption parallelism, the total consumption throughput can be improved, but when the parallelism increases to a certain degree, it will decrease.
Therefore, the application must set a reasonable degree of parallelism. There are several ways to modify consumption parallelism:

- In the same ConsumerGroup, we increase the number of Consumer instances to improve parallelism (note that Consumer instances exceeding the subscription queue are invalid). You can add a machine, or start multiple processes on an existing machine.
- Improve the individual Consumer's consumption parallel threads, 5.x PushConsumer SDK can PushConsumerBuilder.setConsumptionThreadCount() sets the number of threads, SimpleConsumer is free to increase concurrency from business threads, and the underlying thread is safe; The historical SDK PushConsumer can be implemented by modifying parameters consumeThreadMin and consumeThreadMax.

<a id="bestpractice-01bestpractice--consumption-in-bulk"></a>

### Consumption in bulk

If some business processes support bulk consumption, consumption throughput can be greatly improved. For example, the application of order deduction takes 1 s to process one order at a time, and it may only take 2 s to process 10 orders at a time, so the consumption throughput can be greatly improved. It is recommended to use SimpleConsumer from the 5.x SDK, set the batch size per interface call, and pull multiple messages at once.

<a id="bestpractice-01bestpractice--reset-site-to-skip-non-important-messages"></a>

### Reset site to skip non-important messages

In case of message pile-up, if the consumption rate cannot keep up with the delivery rate, and if the business is not demanding enough data, you can choose to discard unimportant messages. You are advised to use the reset site function to directly adjust the consumption site to a specified time or location.

<a id="bestpractice-01bestpractice--optimize-the-per-message-consumption-process"></a>

#### Optimize the per-message consumption process

For example, the consumption process of a message is as follows:

- Query [data 1] from DB according to message
- Query [data 2] from DB according to message
- Complex business calculations
- Insert [data 3] into DB
- Insert [data 4] into DB

There are four interactions with DB during the consumption of this message. If we calculate each interaction as 5ms, the total time is 20ms.
Assuming that the service computation takes 5ms, the total time is 25ms. Therefore, if the four DB interactions can be optimized to two, the total time can be optimized to 15ms, which means that the overall performance is improved by 40%.
Therefore, if the application is sensitive to delay, the DB can be deployed on SSD disks. Compared with SCSI disks, the RT of the former is much smaller.

<a id="bestpractice-01bestpractice--consumption-print-log"></a>

### Consumption print log

If the number of messages is small, you are advised to print messages in the consumption entry method, which takes a long time to consume.

```java
   new MessageListener() {
        @Override
        public ConsumeResult consume(MessageView messageView) {
            LOGGER.info("Consume message={}", messageView);
            //Do your consume process
            return ConsumeResult.SUCCESS;
            }
    }
```

If you can print each message consuming time, it will be more convenient to troubleshoot online problems such as slow consumption.

<a id="bestpractice-01bestpractice--broker"></a>

## Broker

<a id="bestpractice-01bestpractice--broker-role"></a>

### Broker Role

Broker roles are classified into ASYNC\_MASTER, SYNC\_MASTER, and SLAVE.
If you have strict requirements on message reliability, deploy SYNC\_MASTER plus SLAVE.
If message reliability is not required, deploy ASYNC\_MASTER plus SLAVE.
If testing is only convenient, you can select ASYNC\_MASTER only or SYNC\_MASTER only deployment.

<a id="bestpractice-01bestpractice--flushdisktype"></a>

### FlushDiskType

Compared with ASYNC\_FLUSH, SYNC\_FLUSH suffers from performance loss but is more reliable. Therefore, the trade-off must be made based on the actual service scenario.

<a id="bestpractice-01bestpractice--broker-configuration"></a>

### Broker Configuration

<table><thead><tr><th>Parameter</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td>listenPort</td><td>10911</td><td>A listening port that accepts client connections</td></tr><tr><td>namesrvAddr</td><td>null</td><td>nameServer address</td></tr><tr><td>brokerIP1</td><td>The network InetAddress</td><td>The IP address on which the broker is currently listening</td></tr><tr><td>brokerIP2</td><td>same to brokerIP1</td><td>When a master/slave broker exists, if the brokerIP2 property is configured on the broker master node, the broker slave node will connect to the brokerIP2 configured on the master node for synchronization</td></tr><tr><td>brokerName</td><td>null</td><td>broker name</td></tr><tr><td>brokerClusterName</td><td>DefaultCluster</td><td>The Cluster name to which this broker belongs</td></tr><tr><td>brokerId</td><td>0</td><td>broker id 0 indicates master, and other positive integers indicate slave</td></tr><tr><td>storePathCommitLog</td><td>$HOME/store/commitlog/</td><td>Path to store the commit log</td></tr><tr><td>storePathConsumerQueue</td><td>$HOME/store/consumequeue/</td><td>A path that consumes queue is stored</td></tr><tr><td>mappedFileSizeCommitLog</td><td>1024 <!-- -->*<!-- --> 1024 <!-- -->*<!-- --> 1024(1G)</td><td>commit log mapping file size</td></tr><tr><td>deleteWhen</td><td>04</td><td>At what time of day should I delete the commit log whose file retention time has exceeded</td></tr><tr><td>fileReservedTime</td><td>72</td><td>File retention time in hours</td></tr><tr><td>brokerRole</td><td>ASYNC_MASTER</td><td>SYNC_MASTER/ASYNC_MASTER/SLAVE</td></tr><tr><td>flushDiskType</td><td>ASYNC_FLUSH</td><td>SYNC_FLUSH/ASYNC_FLUSH The broker in SYNC_FLUSH mode guarantees to flush messages before receiving the acknowledged producer. ASYNC_FLUSH brokers use the flush mode to flush a group of messages for better performance.</td></tr></tbody></table>
<a id="bestpractice-01bestpractice--broker-log-management"></a>

### Broker Log Management

The default log path for the Broker is located at ${user.home}/logs/rocketmqlogs/. You can change the log level and path by editing the xx.logback.xml file in the conf directory of the binary package.

> Note: Please ensure your logs are properly secured to prevent sensitive information leaks.

- [Producer](#bestpractice-01bestpractice--producer)
  - [Precautions for sending messages](#bestpractice-01bestpractice--precautions-for-sending-messages)
  - [Handling method for message sending failure](#bestpractice-01bestpractice--handling-method-for-message-sending-failure)
- [Consumer](#bestpractice-01bestpractice--consumer)
  - [The consumption process is idempotent](#bestpractice-01bestpractice--the-consumption-process-is-idempotent)
  - [A slow process of consumption](#bestpractice-01bestpractice--a-slow-process-of-consumption)
  - [Increase consumption parallelism](#bestpractice-01bestpractice--increase-consumption-parallelism)
  - [Consumption in bulk](#bestpractice-01bestpractice--consumption-in-bulk)
  - [Reset site to skip non-important messages](#bestpractice-01bestpractice--reset-site-to-skip-non-important-messages)
  - [Consumption print log](#bestpractice-01bestpractice--consumption-print-log)
- [Broker](#bestpractice-01bestpractice--broker)
  - [Broker Role](#bestpractice-01bestpractice--broker-role)
  - [FlushDiskType](#bestpractice-01bestpractice--flushdisktype)
  - [Broker Configuration](#bestpractice-01bestpractice--broker-configuration)
  - [Broker Log Management](#bestpractice-01bestpractice--broker-log-management)

---

<a id="bestpractice-02dledger"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/02dledger/ -->

<!-- page_index: 39 -->

# DLedger

Version: 5.0

# DLedger

<a id="bestpractice-02dledger--dledger-quick-deployment"></a>

## DLedger Quick Deployment

<a id="bestpractice-02dledger--preface"></a>

### Preface

DLedger is a set of distributed log storage components based on Raft protocol. When deploying RocketMQ, you can choose to use DLedger to replace the native replica storage mechanism. This document is mainly introduced for how to build and deploy auto failover RocketMQ cluster based on DLedger.

<a id="bestpractice-02dledger--1-build-from-source-code"></a>

### 1. Build from source code

The build phase is divided into two parts, DLedger should be built first, and then build RocketMQ.

<a id="bestpractice-02dledger--11-build-dledger"></a>

#### 1.1 Build DLedger

```shell
$ git clone https://github.com/openmessaging/dledger.git
$ cd dledger
$ mvn clean install -DskipTests
```

<a id="bestpractice-02dledger--12-build-rocketmq"></a>

#### 1.2 Build RocketMQ

```shell
$ git clone https://github.com/apache/rocketmq.git
$ cd rocketmq
$ git checkout -b store_with_dledger origin/store_with_dledger
$ mvn -Prelease-all -DskipTests clean install -U
```

<a id="bestpractice-02dledger--2-quick-deployment"></a>

### 2. Quick Deployment

After building successfully

```shell
#{rocketmq-version} replace with rocketmq actual version. example: 5.1.0
$ cd distribution/target/rocketmq-{rocketmq-version}/rocketmq-{rocketmq-version}
$ sh bin/dledger/fast-try.sh start
```

If the above commands executed successfully, then check cluster status by using mqadmin operation commands.

```shell
$ sh bin/mqadmin clusterList -n 127.0.0.1:9876
```

If everything goes well, the following content will appear:

![ClusterList](assets/images/tb11z_434e8c481412a55f.ZyCzqK1RjSZFLXXcn2XXa)

（BID is 0 indicate Master, the others are Follower）

After the startup is successful, producer can produce message, and then test failover scenario.

Execute the following command to stop the cluster quickly:

```shell
$ sh bin/dledger/fast-try.sh stop
```

Quick deployment, default configuration is in directory conf/dledger, default storage path is /tmp/rmqstore.

<a id="bestpractice-02dledger--3-failover"></a>

### 3. Failover

After the successful deployment, kill the Leader process(as the above example, kill process that binds port 30931), then wait for 10 seconds, use clusterList command to check cluster status, and you could find that the Leader has been switched to another node.

<a id="bestpractice-02dledger--dledger-cluster-deployment"></a>

## Dledger cluster deployment

This document introduces how to deploy auto failover RocketMQ-on-DLedger Group.

RocketMQ-on-DLedger Group is a broker group with **same name**, needs at least 3 nodes, elect a Leader by Raft algorithm automatically, the others as Follower, replicating data between Leader and Follower for system high available.
RocketMQ-on-DLedger Group can failover automatically, and maintains consistent.
RocketMQ-on-DLedger Group can scale up horizontal, that is, can deploy any RocketMQ-on-DLedger Groups providing services external.

<a id="bestpractice-02dledger--1-new-cluster-deployment"></a>

### 1. New cluster deployment

<a id="bestpractice-02dledger--11-write-the-configuration"></a>

#### 1.1 Write the configuration

Each RocketMQ-on-DLedger Group needs at least 3 machines.(assuming 3 in this document)
write 3 configuration files, advising refer to the directory of conf/dledger 's example configuration file.
key configuration items:

<table><thead><tr><th>name</th><th>meaning</th><th>example</th></tr></thead><tbody><tr><td>enableDLegerCommitLog</td><td>whether enable DLedger</td><td>true</td></tr><tr><td>dLegerGroup</td><td>DLedger Raft Group's name, advising maintain consistent to brokerName</td><td>RaftNode00</td></tr><tr><td>dLegerPeers</td><td>DLedger Group's nodes port infos, each node's configuration stay consistent in the same group.</td><td>n0-127.0.0.1:40911;n1-127.0.0.1:40912;n2-127.0.0.1:40913</td></tr><tr><td>dLegerSelfId</td><td>node id, must belongs to dLegerPeers; each node is unique in the same group.</td><td>n0</td></tr><tr><td>sendMessageThreadPoolNums</td><td>the count of sending thread, advising set equal to the cpu cores.</td><td>16</td></tr></tbody></table>

The following presents an example configuration conf/dledger/broker-n0.conf.

```text
brokerClusterName = RaftCluster
brokerName=RaftNode00
listenPort=30911
namesrvAddr=127.0.0.1:9876
storePathRootDir=/tmp/rmqstore/node00
storePathCommitLog=/tmp/rmqstore/node00/commitlog
enableDLegerCommitLog=true
dLegerGroup=RaftNode00
dLegerPeers=n0-127.0.0.1:40911;n1-127.0.0.1:40912;n2-127.0.0.1:40913
## must be unique
dLegerSelfId=n0
sendMessageThreadPoolNums=16
```

<a id="bestpractice-02dledger--12-start-broker"></a>

### 1.2 Start Broker

Startup stays consistent with the old version.

`nohup sh bin/mqbroker -c conf/dledger/xxx-n0.conf &`
`nohup sh bin/mqbroker -c conf/dledger/xxx-n1.conf &`
`nohup sh bin/mqbroker -c conf/dledger/xxx-n2.conf &`

<a id="bestpractice-02dledger--2-upgrade-old-cluster"></a>

## 2. Upgrade old cluster

If old cluster deployed in Master mode, then each Master needs to be transformed into a RocketMQ-on-DLedger Group.
If old cluster deployed in Master-Slave mode, then each Master-Slave group needs to be transformed into a RocketMQ-on-DLedger Group.

<a id="bestpractice-02dledger--21-kill-old-broker"></a>

### 2.1 Kill old Broker

Execute kill command, or call `bin/mqshutdown broker`.

<a id="bestpractice-02dledger--22-check-old-commitlog"></a>

### 2.2 Check old Commitlog

Each node in RocketMQ-on-DLedger group is compatible with old Commitlog, but Raft replicating process works on the adding message only. So, to avoid occurring exceptions, old Commitlog must be consistent.
If old cluster deployed in Master-Slave mode, it maybe inconsistent after shutdown. Advising use md5sum to check at least 2 recently Commitlog file, if occur inconsistent, maintain consistent by copy.

Although RocketMQ-on-DLedger Group can deployed with 2 nodes, it lacks failover ability(at least 3 nodes can tolerate one node fail).
Make sure that both Master and Slave's Commitlog is consistent, then prepare 3 machines, copy old Commitlog from Master to this 3 machines(BTW, copy the config directory).

Then, go ahead to set configurations.

<a id="bestpractice-02dledger--23-modify-configuration"></a>

### 2.3 Modify configuration

Refer to New cluster deployment.

<a id="bestpractice-02dledger--24-restart-broker"></a>

### 2.4 Restart Broker

Refer to New cluster deployment.

- [DLedger Quick Deployment](#bestpractice-02dledger--dledger-quick-deployment)
  - [Preface](#bestpractice-02dledger--preface)
  - [1. Build from source code](#bestpractice-02dledger--1-build-from-source-code)
  - [2. Quick Deployment](#bestpractice-02dledger--2-quick-deployment)
  - [3. Failover](#bestpractice-02dledger--3-failover)
- [Dledger cluster deployment](#bestpractice-02dledger--dledger-cluster-deployment)
  - [1. New cluster deployment](#bestpractice-02dledger--1-new-cluster-deployment)
  - [1.2 Start Broker](#bestpractice-02dledger--12-start-broker)
- [2. Upgrade old cluster](#bestpractice-02dledger--2-upgrade-old-cluster)
  - [2.1 Kill old Broker](#bestpractice-02dledger--21-kill-old-broker)
  - [2.2 Check old Commitlog](#bestpractice-02dledger--22-check-old-commitlog)
  - [2.3 Modify configuration](#bestpractice-02dledger--23-modify-configuration)
  - [2.4 Restart Broker](#bestpractice-02dledger--24-restart-broker)

---

<a id="bestpractice-03access"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/03access/ -->

<!-- page_index: 40 -->

# Access Control 2.0

Version: 5.0

# Access Control 2.0

> [!INFO]
> **Version Notice**
> This document describes **Access Control 2.0 (ACL 2.0)**, applicable to **RocketMQ 5.3.0** and above.
>
> - If you are using **RocketMQ 4.x, 5.0-5.2, or 5.3.0-5.3.2**, please refer to [ACL 1.0 Documentation](https://rocketmq.apache.org/docs/bestPractice/07access-1.0)
> - **Starting from RocketMQ 5.3.3, ACL 1.0 is no longer supported**. It is recommended to upgrade to ACL 2.0
> - If you are migrating from ACL 1.0 to 2.0, please refer to the [ACL 1.0 Migration](#bestpractice-03access--5-migrating-from-acl-10-to-acl-20) section

> [!DANGER]
> **Security Notice**
> ⚠️ **All usernames and passwords in this document are for demonstration purposes only. DO NOT use them in production environments!**
>
> For production deployment, please ensure:
>
> - Use strong passwords (at least 16 characters, including uppercase, lowercase, numbers, and special characters)
> - Strictly control the scope of super user usage
> - Properly secure authentication credentials and do not commit them in plain text to code repositories

<a id="bestpractice-03access--introduction"></a>

## Introduction

<a id="bestpractice-03access--what-is-access-control-20"></a>

### What is Access Control 2.0?

Access Control 2.0 (ACL 2.0) is an upgraded version of Apache RocketMQ's Access Control List, providing comprehensive authentication and authorization mechanisms to protect the data security of RocketMQ clusters.

<a id="bestpractice-03access--core-features"></a>

### Core Features

- **Dual Security Mechanisms**: Supports independent configuration of authentication and authorization
- **Flexible Resource Matching**: Supports exact match, prefix match, and wildcard match
- **Fine-grained Permission Control**: Covers multiple resource types including Cluster, Namespace, Topic, and Group
- **Multiple Strategy Options**: Provides stateless and stateful authentication/authorization strategies
- **Inter-component Secure Communication**: Supports access control between components such as Broker, Proxy, and NameServer

<a id="bestpractice-03access--core-concepts"></a>

### Core Concepts

<table><thead><tr><th>Concept</th><th>Description</th></tr></thead><tbody><tr><td><strong>User</strong></td><td>Entity accessing RocketMQ resources, divided into Super users and Normal users</td></tr><tr><td><strong>Resource</strong></td><td>Objects requiring access control, such as Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>Action</strong></td><td>Operations performed on resources, such as Pub, Sub, Create, Update, Delete, Get, List</td></tr><tr><td><strong>Decision</strong></td><td>Authorization result, Allow or Deny</td></tr><tr><td><strong>Environment</strong></td><td>Access environment information, such as source IP address</td></tr></tbody></table>

---

<a id="bestpractice-03access--quick-start"></a>

## Quick Start

<a id="bestpractice-03access--5-minute-quick-experience"></a>

### 5-Minute Quick Experience

This section helps you quickly start a RocketMQ cluster with ACL enabled in 5 minutes.

> **Prerequisites**:
>
> - RocketMQ version ≥ 5.3.0
> - RocketMQ basic installation completed
>
> **Version Check**:
>
>
```bash
# Check RocketMQ version sh bin/mqbroker -v
```

> **Note**: This example uses integrated storage-compute architecture (single Broker mode), suitable for quick experience and testing environments. For production deployment, refer to the [Configuration](#bestpractice-03access--configuration) section.

<a id="bestpractice-03access--step-1-configure-broker"></a>

#### Step 1: Configure Broker

Edit the `conf/broker.conf` file and add the following configuration:

```properties
# Enable authentication
authenticationEnabled = true
authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider

# Enable authorization
authorizationEnabled = true
authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider

# Initialize admin user (auto-created on first startup)
initAuthenticationUser = {"username":"rocketmq","password":"12345678"}

# Inter-component authentication credentials (for Broker master-slave sync, internal cluster communication, etc.)
innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"}
```

> **Configuration Notes**:
>
> - Only required items need to be configured for quick start; other items have default values
> - For production environments, it is recommended to configure `authenticationStrategy` and `authorizationStrategy` to stateful strategy for better performance

<a id="bestpractice-03access--step-2-start-cluster"></a>

#### Step 2: Start Cluster

```bash
# 1. Start NameServer nohup sh bin/mqnamesrv &

# 2. Start Broker (using the above configuration file) nohup sh bin/mqbroker -n localhost:9876 -c conf/broker.conf &
```

<a id="bestpractice-03access--step-3-configure-mqadmin-tool"></a>

#### Step 3: Configure mqadmin Tool

After enabling ACL, you need to configure authentication credentials for the mqadmin tool to execute management commands.

Edit the `conf/tools.yml` file:

```yaml
# Use the initialized admin user credentials
accessKey: rocketmq
secretKey: 12345678
```

<a id="bestpractice-03access--step-4-create-business-users-and-grant-permissions"></a>

#### Step 4: Create Business Users and Grant Permissions

```bash
# Create producer user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u producer_user \ -p producer123 \ -t Normal

# Grant Topic publish permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:producer_user \ -r Topic:TestTopic \ -a Pub \ -d Allow
```

<a id="bestpractice-03access--step-5-verify-configuration"></a>

#### Step 5: Verify Configuration

Send a test message using Java client:

```java
SessionCredentials credentials = new SessionCredentials("producer_user", "producer123");
StaticSessionCredentialsProvider credentialsProvider =
    new StaticSessionCredentialsProvider(credentials);

ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
    .setEndpoints("127.0.0.1:10911")
    .setCredentialProvider(credentialsProvider)
    .build();
// ... Create Producer and send message
```

✅ Congratulations! You have successfully started a RocketMQ cluster with ACL enabled.

<a id="bestpractice-03access--different-deployment-architecture-configurations"></a>

### Different Deployment Architecture Configurations

RocketMQ supports two deployment architectures. Choose the appropriate configuration based on your scenario.

<a id="bestpractice-03access--integrated-storage-compute-architecture"></a>

#### Integrated Storage-Compute Architecture

Broker handles both computation and storage, suitable for small to medium-scale clusters and testing environments.

**Configuration Example**:

```properties
# broker.conf
authenticationEnabled = true
authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider
authenticationStrategy = org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy

authorizationEnabled = true
authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider
authorizationStrategy = org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy

initAuthenticationUser = {"username":"rocketmq","password":"12345678"}
innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"}
```

<a id="bestpractice-03access--separated-storage-compute-architecture-recommended"></a>

#### Separated Storage-Compute Architecture (Recommended)

Proxy handles computation and authentication/authorization, while Broker only handles storage and metadata management. Suitable for large-scale production environments.

**Broker Configuration** (`broker.conf`):

```properties
# Broker only acts as metadata provider, does not handle client authentication/authorization
authenticationEnabled = false
authorizationEnabled = false

# Configure metadata providers
authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider
authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider

# Initialize admin user
initAuthenticationUser = {"username":"rocketmq","password":"12345678"}
```

**Proxy Configuration** (`rmq-proxy.json`):

```json
{
  "authenticationEnabled": true,
  "authenticationProvider": "org.apache.rocketmq.auth.authentication.provider.DefaultAuthenticationProvider",
  "authenticationMetadataProvider": "org.apache.rocketmq.proxy.auth.ProxyAuthenticationMetadataProvider",
  "authenticationStrategy": "org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy",

  "authorizationEnabled": true,
  "authorizationProvider": "org.apache.rocketmq.auth.authorization.provider.DefaultAuthorizationProvider",
  "authorizationMetadataProvider": "org.apache.rocketmq.proxy.auth.ProxyAuthorizationMetadataProvider",
  "authorizationStrategy": "org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy"
}
```

**Startup Sequence**:

```bash
# 1. Start NameServer nohup sh bin/mqnamesrv &

# 2. Start Broker (storage node) nohup sh bin/mqbroker -n localhost:9876 -c conf/broker.conf &

# 3. Start Proxy (compute node) nohup sh bin/mqproxy -n localhost:9876 -pc conf/rmq-proxy.json &
```

---

<a id="bestpractice-03access--configuration"></a>

## Configuration

<a id="bestpractice-03access--authentication-configuration-parameters"></a>

### Authentication Configuration Parameters

<table><thead><tr><th>Parameter</th><th>Type</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td><code>authenticationEnabled</code></td><td>boolean</td><td><code>false</code></td><td>Whether to enable authentication</td></tr><tr><td><code>authenticationProvider</code></td><td>String</td><td><code>org.apache.rocketmq.auth.authentication.provider.DefaultAuthenticationProvider</code></td><td>Authentication provider implementation class (optional, uses default)</td></tr><tr><td><code>authenticationMetadataProvider</code></td><td>String</td><td>-</td><td>Authentication metadata provider implementation class <strong>Required</strong></td></tr><tr><td><code>authenticationStrategy</code></td><td>String</td><td><code>org.apache.rocketmq.auth.authentication.strategy.StatelessAuthenticationStrategy</code></td><td>Authentication strategy (optional, uses default)
Production recommendation: stateful strategy
<code>org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy</code></td></tr><tr><td><code>initAuthenticationUser</code></td><td>JSON</td><td>-</td><td><strong>Recommended</strong>: System initialization user (auto-created on first startup)
Format: <code>{"username":"xxx","password":"xxx"}</code>
If not configured, admin user must be created manually</td></tr><tr><td><code>innerClientAuthenticationCredentials</code></td><td>JSON</td><td>-</td><td><strong>Conditional</strong>: Inter-component authentication credentials for Broker master-slave sync, Proxy-Broker access, Controller election, etc.
Format: <code>{"accessKey":"xxx","secretKey":"xxx"}</code>
⚠️ All components must use identical credentials if inter-component communication exists</td></tr><tr><td><code>authenticationWhitelist</code></td><td>String</td><td>-</td><td>Authentication whitelist (comma-separated IP list)</td></tr></tbody></table>
<a id="bestpractice-03access--authorization-configuration-parameters"></a>

### Authorization Configuration Parameters

<table><thead><tr><th>Parameter</th><th>Type</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td><code>authorizationEnabled</code></td><td>boolean</td><td><code>false</code></td><td>Whether to enable authorization</td></tr><tr><td><code>authorizationProvider</code></td><td>String</td><td><code>org.apache.rocketmq.auth.authorization.provider.DefaultAuthorizationProvider</code></td><td>Authorization provider implementation class (optional, uses default)</td></tr><tr><td><code>authorizationMetadataProvider</code></td><td>String</td><td>-</td><td>Authorization metadata provider implementation class <strong>Required</strong></td></tr><tr><td><code>authorizationStrategy</code></td><td>String</td><td><code>org.apache.rocketmq.auth.authorization.strategy.StatelessAuthorizationStrategy</code></td><td>Authorization strategy (optional, uses default)
Production recommendation: stateful strategy
<code>org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy</code></td></tr><tr><td><code>authorizationWhitelist</code></td><td>String</td><td>-</td><td>Authorization whitelist (comma-separated IP list)</td></tr></tbody></table>
<a id="bestpractice-03access--cache-configuration-parameters"></a>

### Cache Configuration Parameters

<table><thead><tr><th>Parameter</th><th>Type</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td><code>userCacheMaxNum</code></td><td>int</td><td><code>1000</code></td><td>Maximum user cache size</td></tr><tr><td><code>userCacheExpiredSecond</code></td><td>int</td><td><code>600</code></td><td>User cache expiration time (seconds)</td></tr><tr><td><code>userCacheRefreshSecond</code></td><td>int</td><td><code>60</code></td><td>User cache refresh time (seconds)</td></tr><tr><td><code>aclCacheMaxNum</code></td><td>int</td><td><code>1000</code></td><td>Maximum ACL cache size</td></tr><tr><td><code>aclCacheExpiredSecond</code></td><td>int</td><td><code>600</code></td><td>ACL cache expiration time (seconds)</td></tr><tr><td><code>aclCacheRefreshSecond</code></td><td>int</td><td><code>60</code></td><td>ACL cache refresh time (seconds)</td></tr><tr><td><code>statefulAuthenticationCacheMaxNum</code></td><td>int</td><td><code>10000</code></td><td>Maximum stateful authentication cache size</td></tr><tr><td><code>statefulAuthenticationCacheExpiredSecond</code></td><td>int</td><td><code>60</code></td><td>Stateful authentication cache expiration time (seconds)</td></tr><tr><td><code>statefulAuthorizationCacheMaxNum</code></td><td>int</td><td><code>10000</code></td><td>Maximum stateful authorization cache size</td></tr><tr><td><code>statefulAuthorizationCacheExpiredSecond</code></td><td>int</td><td><code>60</code></td><td>Stateful authorization cache expiration time (seconds)</td></tr></tbody></table>
<a id="bestpractice-03access--authentication-and-authorization-strategies"></a>

### Authentication and Authorization Strategies

<a id="bestpractice-03access--stateless-strategy-default"></a>

#### Stateless Strategy - Default

- **Characteristics**: Performs complete authentication and authorization check for every request
- **Advantages**: High security, permission changes take effect immediately
- **Disadvantages**: Higher performance overhead
- **Use Cases**: Environments with extremely high security requirements
- **Default**: ✅ System uses this strategy by default

**Configuration Example**:

```properties
# Default values, can be omitted
authenticationStrategy = org.apache.rocketmq.auth.authentication.strategy.StatelessAuthenticationStrategy
authorizationStrategy = org.apache.rocketmq.auth.authorization.strategy.StatelessAuthorizationStrategy
```

<a id="bestpractice-03access--stateful-strategy-recommended-for-production"></a>

#### Stateful Strategy - Recommended for Production

- **Characteristics**: First request performs authentication/authorization, subsequent requests use cached results
- **Advantages**: Lower performance overhead, higher throughput
- **Disadvantages**: Permission changes have delay (takes effect after cache expires)
- **Use Cases**: High throughput scenarios, recommended for production environments
- **Recommendation**: ⭐ Explicitly configure this strategy for production environments

**Configuration Example**:

```properties
# Recommended for production
authenticationStrategy = org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy
authorizationStrategy = org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy
```

---

<a id="bestpractice-03access--user-management"></a>

## User Management

<a id="bestpractice-03access--user-type-description"></a>

### User Type Description

<table><thead><tr><th>User Type</th><th>Description</th><th>Permission Scope</th><th>Use Case</th></tr></thead><tbody><tr><td><strong>Super</strong></td><td>Super user</td><td>Has all permissions on all resources, no separate authorization needed</td><td>System administrator, operations personnel</td></tr><tr><td><strong>Normal</strong></td><td>Normal user</td><td>Requires explicit authorization to access resources</td><td>Business applications, services</td></tr></tbody></table>
<a id="bestpractice-03access--mqadmin-tool-configuration"></a>

### mqadmin Tool Configuration

Before using the mqadmin command-line tool, configure admin credentials.

**Configuration File**: `conf/tools.yml`

```yaml
# Use super user's username and password
accessKey: rocketmq
secretKey: 12345678
```

**Verify Configuration**:

```bash
# Test if mqadmin tool can connect normally sh bin/mqadmin listUser -n 127.0.0.1:9876 -c DefaultCluster
```

<a id="bestpractice-03access--user-management-commands"></a>

### User Management Commands

<a id="bestpractice-03access--create-user"></a>

#### Create User

```bash
# Create normal user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster -u username -p password -t Normal

# Create super user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster -u rocketmq -p 12345678 -t Super
```

<a id="bestpractice-03access--update-user"></a>

#### Update User

```bash
# Update user password sh bin/mqadmin updateUser -n 127.0.0.1:9876 -c DefaultCluster -u username -p newpassword

# Update user type sh bin/mqadmin updateUser -n 127.0.0.1:9876 -c DefaultCluster -u username -t Super
```

<a id="bestpractice-03access--query-user"></a>

#### Query User

```bash
# Query user details sh bin/mqadmin getUser -n 127.0.0.1:9876 -c DefaultCluster -u username

# Query user list sh bin/mqadmin listUser -n 127.0.0.1:9876 -c DefaultCluster

# Query user list with filter sh bin/mqadmin listUser -n 127.0.0.1:9876 -c DefaultCluster -f producer
```

<a id="bestpractice-03access--delete-user"></a>

#### Delete User

```bash
sh bin/mqadmin deleteUser -n 127.0.0.1:9876 -c DefaultCluster -u username
```

<a id="bestpractice-03access--command-parameters"></a>

### Command Parameters

<table><thead><tr><th>Parameter</th><th>Required</th><th>Description</th><th>Default</th></tr></thead><tbody><tr><td><code>-n</code></td><td>Yes</td><td>NameServer address</td><td>-</td></tr><tr><td><code>-c</code></td><td>No</td><td>Cluster name (choose one with <code>-b</code>)</td><td>-</td></tr><tr><td><code>-b</code></td><td>No</td><td>Broker address (choose one with <code>-c</code>)</td><td>-</td></tr><tr><td><code>-u</code></td><td>Yes</td><td>Username</td><td>-</td></tr><tr><td><code>-p</code></td><td>No</td><td>Password (used for create/update)</td><td>-</td></tr><tr><td><code>-t</code></td><td>No</td><td>User type: Super or Normal</td><td>Normal</td></tr><tr><td><code>-f</code></td><td>No</td><td>Filter condition (used for query)</td><td>-</td></tr></tbody></table>

---

<a id="bestpractice-03access--permission-management"></a>

## Permission Management

<a id="bestpractice-03access--core-concepts-1"></a>

### Core Concepts

<a id="bestpractice-03access--resource-types"></a>

#### Resource Types

<table><thead><tr><th>Resource Type</th><th>Format</th><th>Example</th><th>Description</th></tr></thead><tbody><tr><td><strong>Any</strong></td><td><code>*</code></td><td><code>*</code></td><td>All resources</td></tr><tr><td><strong>Cluster</strong></td><td><code>Cluster:cluster_name</code></td><td><code>Cluster:DefaultCluster</code></td><td>Cluster-level resource</td></tr><tr><td><strong>Namespace</strong></td><td><code>Namespace:namespace</code></td><td><code>Namespace:test</code></td><td>Namespace</td></tr><tr><td><strong>Topic</strong></td><td><code>Topic:topic_name</code></td><td><code>Topic:TestTopic</code></td><td>Message topic</td></tr><tr><td><strong>Group</strong></td><td><code>Group:group_name</code></td><td><code>Group:TestGroup</code></td><td>Consumer group</td></tr></tbody></table>
<a id="bestpractice-03access--resource-matching-modes"></a>

#### Resource Matching Modes

<table><thead><tr><th>Matching Mode</th><th>Description</th><th>Example</th><th>Match Result</th></tr></thead><tbody><tr><td><strong>Exact Match (LITERAL)</strong></td><td>Exact resource name match</td><td><code>Topic:OrderTopic</code></td><td>Matches only <code>Topic:OrderTopic</code></td></tr><tr><td><strong>Prefix Match (PREFIXED)</strong></td><td>Matches resources with specified prefix</td><td><code>Topic:Order*</code></td><td>Matches <code>Topic:OrderTopic</code>, <code>Topic:OrderDLQTopic</code>, etc.</td></tr><tr><td><strong>Wildcard Match (ANY)</strong></td><td>Matches all resources of the type</td><td><code>Topic:*</code></td><td>Matches all Topics</td></tr></tbody></table>
<a id="bestpractice-03access--action-types"></a>

#### Action Types

<table><thead><tr><th>Action</th><th>Description</th><th>Applicable Resources</th></tr></thead><tbody><tr><td><strong>Pub</strong></td><td>Publish messages</td><td>Topic</td></tr><tr><td><strong>Sub</strong></td><td>Subscribe messages</td><td>Topic, Group</td></tr><tr><td><strong>Create</strong></td><td>Create resource</td><td>Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>Update</strong></td><td>Update resource</td><td>Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>Delete</strong></td><td>Delete resource</td><td>Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>Get</strong></td><td>Query resource details</td><td>Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>List</strong></td><td>Query resource list</td><td>Cluster, Namespace, Topic, Group</td></tr><tr><td><strong>All</strong></td><td>All operations</td><td>All resources</td></tr></tbody></table>
<a id="bestpractice-03access--decision-types"></a>

#### Decision Types

<table><thead><tr><th>Decision</th><th>Description</th></tr></thead><tbody><tr><td><strong>Allow</strong></td><td>Allow operation</td></tr><tr><td><strong>Deny</strong></td><td>Deny operation (higher priority than Allow)</td></tr></tbody></table>
<a id="bestpractice-03access--permission-priority-rules"></a>

### Permission Priority Rules

When multiple permission policies match the same request, the final result is determined by the following priority.

<a id="bestpractice-03access--priority-rules"></a>

#### Priority Rules

<table><thead><tr><th>Resource Priority (High→Low)</th><th>Decision Priority</th></tr></thead><tbody><tr><td>1. Specific resource type &gt; Any resource type (<code>*</code>)
2. Exact match &gt; Prefix match &gt; Wildcard match
3. Longer resource name &gt; Shorter resource name</td><td><strong>Deny &gt; Allow</strong> (Deny has higher priority than Allow)</td></tr></tbody></table>
<a id="bestpractice-03access--priority-example"></a>

#### Priority Example

<table><thead><tr><th>Policy</th><th>Resource Definition</th><th>Action</th><th>Decision</th><th>Priority</th></tr></thead><tbody><tr><td>1</td><td><code>Topic:test-abc-1</code></td><td>Pub,Sub</td><td>Deny</td><td>Highest</td></tr><tr><td>2</td><td><code>Topic:test-abc</code></td><td>Pub,Sub</td><td>Allow</td><td>High</td></tr><tr><td>3</td><td><code>Topic:test-*</code></td><td>Pub,Sub</td><td>Allow</td><td>Medium</td></tr><tr><td>4</td><td><code>Topic:*</code></td><td>Pub,Sub</td><td>Allow</td><td>Low</td></tr><tr><td>5</td><td><code>*</code></td><td>All</td><td>Deny</td><td>Lowest</td></tr></tbody></table>

**Match Results**:

<table><thead><tr><th>Access Resource</th><th>Matched Policy</th><th>Final Decision</th></tr></thead><tbody><tr><td><code>Topic:test-abc-1</code></td><td>Policy 1 (exact match)</td><td>❌ Deny</td></tr><tr><td><code>Topic:test-abc</code></td><td>Policy 2 (exact match)</td><td>✅ Allow</td></tr><tr><td><code>Topic:test-123</code></td><td>Policy 3 (prefix match)</td><td>✅ Allow</td></tr><tr><td><code>Topic:other</code></td><td>Policy 4 (wildcard match)</td><td>✅ Allow</td></tr><tr><td><code>Group:TestGroup</code></td><td>Policy 5 (any resource)</td><td>❌ Deny</td></tr></tbody></table>
<a id="bestpractice-03access--permission-management-commands"></a>

### Permission Management Commands

<a id="bestpractice-03access--create-permission"></a>

#### Create Permission

**Basic Usage Examples**:

```bash
# Example 1: Grant publish permission for a single Topic sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:producer_user -r Topic:TestTopic -a Pub -d Allow

# Example 2: Grant subscribe permission for a single Topic (need to specify both Topic and Group) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:consumer_user -r Topic:TestTopic,Group:TestGroup -a Sub -d Allow

# Example 3: Grant multiple operation permissions sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:admin_user -r Topic:TestTopic -a Create,Update,Delete,Get,List -d Allow
```

**Resource Matching Mode Examples**:

```bash
# Example 4: Exact match - precise resource name match sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:order_service -r Topic:OrderTopic -a Pub,Sub -d Allow

# Example 5: Prefix match - matches all Topics starting with order_ sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:order_service -r Topic:order_* -a Pub -d Allow

# Example 6: Wildcard match - matches all Topics sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:monitor_user -r Topic:* -a Get,List -d Allow

# Example 7: Match all resource types sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:super_admin -r * -a All -d Allow
```

**IP Whitelist Examples**:

```bash
# Example 8: Restrict single IP access sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:producer_user -r Topic:TestTopic -a Pub -i 192.168.1.100 -d Allow

# Example 9: Restrict IP range access (CIDR format) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:internal_user -r Topic:InternalTopic -a Pub,Sub -i 192.168.1.0/24 -d Allow

# Example 10: No IP restriction (do not specify -i parameter) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:public_user -r Topic:PublicTopic -a Pub -d Allow
```

**Deny Policy Examples**:

```bash
# Example 11: Deny access to sensitive Topic sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:normal_user -r Topic:SensitiveTopic -a Pub,Sub -d Deny

# Example 12: Grant most permissions first, then deny specific resources (Deny has higher priority)
# Step 1: Grant access to all Topics sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:normal_user -r Topic:* -a Pub,Sub -d Allow
# Step 2: Deny sensitive Topic (overrides above Allow) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:normal_user -r Topic:SensitiveTopic -a Pub,Sub -d Deny
```

**Cluster Management Permission Examples**:

```bash
# Example 13: Grant cluster query permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:monitor_user -r Cluster:DefaultCluster -a Get,List -d Allow

# Example 14: Grant Topic management permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:topic_admin -r Topic:* -a Create,Update,Delete,Get,List -d Allow

# Example 15: Grant Group management permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:group_admin -r Group:* -a Create,Update,Delete,Get,List -d Allow
```

<a id="bestpractice-03access--update-permission"></a>

#### Update Permission

```bash
sh bin/mqadmin updateAcl -n 127.0.0.1:9876 -c DefaultCluster \
  -s User:producer_user -r Topic:TestTopic -a Pub,Sub -d Allow
```

<a id="bestpractice-03access--query-permission"></a>

#### Query Permission

```bash
# Query all permissions of a user sh bin/mqadmin getAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:producer_user

# Query all permission list sh bin/mqadmin listAcl -n 127.0.0.1:9876 -c DefaultCluster

# Query permission list with filter sh bin/mqadmin listAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:producer_user -r Topic:TestTopic
```

<a id="bestpractice-03access--delete-permission"></a>

#### Delete Permission

```bash
# Delete all permissions of a user sh bin/mqadmin deleteAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:producer_user

# Delete user's permission for specific resource sh bin/mqadmin deleteAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:producer_user -r Topic:TestTopic
```

<a id="bestpractice-03access--command-parameters-1"></a>

### Command Parameters

<table><thead><tr><th>Parameter</th><th>Required</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td><code>-n</code></td><td>Yes</td><td>NameServer address</td><td><code>127.0.0.1:9876</code></td></tr><tr><td><code>-c</code></td><td>No</td><td>Cluster name (choose one with <code>-b</code>)</td><td><code>DefaultCluster</code></td></tr><tr><td><code>-b</code></td><td>No</td><td>Broker address (choose one with <code>-c</code>)</td><td><code>192.168.1.1:10911</code></td></tr><tr><td><code>-s</code></td><td>Yes</td><td>Subject name</td><td><code>User:producer_user</code></td></tr><tr><td><code>-r</code></td><td>No</td><td>Resource definition (comma-separated)</td><td><code>Topic:TestTopic</code>
<code>Topic:*</code>
<code>Topic:Order*,Group:Order*</code></td></tr><tr><td><code>-a</code></td><td>No</td><td>Action type (comma-separated)</td><td><code>Pub</code>
<code>Pub,Sub</code>
<code>Create,Update,Delete</code></td></tr><tr><td><code>-i</code></td><td>No</td><td>IP whitelist (supports IP or IP range)</td><td><code>192.168.1.100</code>
<code>192.168.1.0/24</code></td></tr><tr><td><code>-d</code></td><td>No</td><td>Decision result</td><td><code>Allow</code> or <code>Deny</code></td></tr></tbody></table>

---

<a id="bestpractice-03access--client-usage"></a>

## Client Usage

<a id="bestpractice-03access--java-client-configuration"></a>

### Java Client Configuration

<a id="bestpractice-03access--maven-dependency"></a>

#### Maven Dependency

```xml
<dependency>
    <groupId>org.apache.rocketmq</groupId>
    <artifactId>rocketmq-client-java</artifactId>
    <version>5.4.0</version>
</dependency>
```

<a id="bestpractice-03access--message-producer"></a>

### Message Producer

```java
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.SessionCredentials;
import org.apache.rocketmq.client.apis.StaticSessionCredentialsProvider;
import org.apache.rocketmq.client.apis.producer.Producer;
import org.apache.rocketmq.client.apis.message.Message;

public class ProducerWithACL {
    public static void main(String[] args) throws Exception {
        // 1. Create credentials provider
        SessionCredentials credentials = new SessionCredentials(
            "producer_user",  // AccessKey (username)
            "producer123"     // SecretKey (password)
        );
        StaticSessionCredentialsProvider credentialsProvider =
            new StaticSessionCredentialsProvider(credentials);

        // 2. Configure client
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints("127.0.0.1:8081")  // Proxy or Broker address
            .setCredentialProvider(credentialsProvider)
            .build();

        // 3. Create producer
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        Producer producer = provider.newProducerBuilder()
            .setClientConfiguration(clientConfiguration)
            .setTopics("TestTopic")
            .build();

        // 4. Send message
        Message message = provider.newMessageBuilder()
            .setTopic("TestTopic")
            .setBody("Hello RocketMQ with ACL".getBytes())
            .build();

        producer.send(message);
        System.out.println("Message sent successfully");

        // 5. Close producer
        producer.close();
    }
}
```

<a id="bestpractice-03access--message-consumer"></a>

### Message Consumer

```java
import org.apache.rocketmq.client.apis.ClientConfiguration;
import org.apache.rocketmq.client.apis.ClientServiceProvider;
import org.apache.rocketmq.client.apis.SessionCredentials;
import org.apache.rocketmq.client.apis.StaticSessionCredentialsProvider;
import org.apache.rocketmq.client.apis.consumer.PushConsumer;
import org.apache.rocketmq.client.apis.consumer.FilterExpression;
import org.apache.rocketmq.client.apis.consumer.FilterExpressionType;
import org.apache.rocketmq.client.apis.consumer.ConsumeResult;

import java.util.Collections;

public class ConsumerWithACL {
    public static void main(String[] args) throws Exception {
        // 1. Create credentials provider
        SessionCredentials credentials = new SessionCredentials(
            "consumer_user",  // AccessKey (username)
            "consumer123"     // SecretKey (password)
        );
        StaticSessionCredentialsProvider credentialsProvider =
            new StaticSessionCredentialsProvider(credentials);

        // 2. Configure client
        ClientConfiguration clientConfiguration = ClientConfiguration.newBuilder()
            .setEndpoints("127.0.0.1:8081")
            .setCredentialProvider(credentialsProvider)
            .build();

        // 3. Create consumer
        ClientServiceProvider provider = ClientServiceProvider.loadService();
        FilterExpression filterExpression = new FilterExpression("*", FilterExpressionType.TAG);

        PushConsumer consumer = provider.newPushConsumerBuilder()
            .setClientConfiguration(clientConfiguration)
            .setConsumerGroup("TestGroup")
            .setSubscriptionExpressions(Collections.singletonMap("TestTopic", filterExpression))
            .setMessageListener(messageView -> {
                System.out.println("Received message: " + new String(messageView.getBody().array()));
                return ConsumeResult.SUCCESS;
            })
            .build();

        System.out.println("Consumer started successfully");

        // Keep running
        Thread.sleep(Long.MAX_VALUE);
    }
}
```

<a id="bestpractice-03access--spring-boot-integration"></a>

### Spring Boot Integration

```yaml
# application.yml
rocketmq:
  name-server: 127.0.0.1:9876
  producer:
    group: producer-group
    access-key: producer_user
    secret-key: producer123
  consumer:
    group: consumer-group
    access-key: consumer_user
    secret-key: consumer123
    topics:
      - TestTopic
```

---

<a id="bestpractice-03access--common-scenarios"></a>

## Common Scenarios

<a id="bestpractice-03access--scenario-1-separate-producer-and-consumer"></a>

### Scenario 1: Separate Producer and Consumer

**Requirement**: Producer can only send messages, consumer can only consume messages

```bash
# Create producer user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u producer_user -p producer123 -t Normal

# Create consumer user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u consumer_user -p consumer123 -t Normal

# Grant producer publish permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:producer_user -r Topic:TestTopic -a Pub -d Allow

# Grant consumer subscribe permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:consumer_user -r Topic:TestTopic,Group:TestGroup -a Sub -d Allow
```

<a id="bestpractice-03access--scenario-2-permissions-by-business-module"></a>

### Scenario 2: Permissions by Business Module

**Requirement**: Different business modules use different Topic prefixes, each module can only access its own Topics

```bash
# Create order module user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u order_service -p order123 -t Normal

# Grant order module permission (can access all Topics starting with order_) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:order_service -r Topic:order_* -a Pub,Sub -d Allow

# Create payment module user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u payment_service -p payment123 -t Normal

# Grant payment module permission (can access all Topics starting with payment_) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:payment_service -r Topic:payment_* -a Pub,Sub -d Allow
```

<a id="bestpractice-03access--scenario-3-ip-whitelist-restriction"></a>

### Scenario 3: IP Whitelist Restriction

**Requirement**: Only allow specific IP ranges to access

```bash
# Create user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u internal_user -p internal123 -t Normal

# Grant permission but restrict to internal IP access only sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:internal_user \ -r Topic:InternalTopic \ -a Pub,Sub \ -i 192.168.1.0/24,10.0.0.0/8 \ -d Allow
```

<a id="bestpractice-03access--scenario-4-administrator-permission"></a>

### Scenario 4: Administrator Permission

**Requirement**: Administrator needs to manage Topic and Group creation, update, deletion

```bash
# Create admin user sh bin/mqadmin createUser -n 127.0.0.1:9876 -c DefaultCluster \ -u admin_user -p admin_user123 -t Normal

# Grant cluster management permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:admin_user \ -r Cluster:DefaultCluster \ -a Create,Update,Delete,Get,List \ -d Allow

# Grant all Topic management permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:admin_user \ -r Topic:* \ -a Create,Update,Delete,Get,List \ -d Allow

# Grant all Group management permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:admin_user \ -r Group:* \ -a Create,Update,Delete,Get,List \ -d Allow
```

<a id="bestpractice-03access--scenario-5-deny-access-to-sensitive-topic"></a>

### Scenario 5: Deny Access to Sensitive Topic

**Requirement**: Explicitly deny certain users from accessing sensitive Topics

```bash
# Grant user access to most Topics sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:normal_user \ -r Topic:* \ -a Pub,Sub \ -d Allow

# Deny access to sensitive Topic (Deny has higher priority than Allow) sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:normal_user \ -r Topic:SensitiveTopic \ -a Pub,Sub \ -d Deny
```

---

<a id="bestpractice-03access--troubleshooting"></a>

## Troubleshooting

<a id="bestpractice-03access--common-errors"></a>

### Common Errors

<a id="bestpractice-03access--1-mqadmin-tool-command-execution-failed"></a>

#### 1. mqadmin Tool Command Execution Failed

**Error Message**:

```text
CODE: 17  DESC: No user
or
CODE: 16  DESC: Authentication failed
```

**Possible Causes**:

- `conf/tools.yml` file not configured
- Credentials in `tools.yml` are incorrect
- Configured user is not a super user

**Solution**:

```bash
# 1. Check if tools.yml file exists ls conf/tools.yml

# 2. Configure admin credentials cat > conf/tools.yml << EOF accessKey: rocketmq secretKey: 12345678 EOF

# 3. Verify configuration sh bin/mqadmin listUser -n 127.0.0.1:9876 -c DefaultCluster
```

<a id="bestpractice-03access--2-client-authentication-failed"></a>

#### 2. Client Authentication Failed

**Error Message**:

```text
[AUTHENTICATION] User:xxx is authenticated failed with Signature = xxx
```

**Possible Causes**:

- Incorrect username or password
- User does not exist
- User is disabled

**Troubleshooting Steps**:

```bash
# 1. Check if user exists sh bin/mqadmin getUser -n 127.0.0.1:9876 -c DefaultCluster -u username

# 2. Verify client configuration has correct username and password

# 3. Reset user password sh bin/mqadmin updateUser -n 127.0.0.1:9876 -c DefaultCluster -u username -p newpassword
```

<a id="bestpractice-03access--3-authorization-failed"></a>

#### 3. Authorization Failed

**Error Message**:

```text
[AUTHORIZATION] Subject = User:xxx is Deny Action = Pub from sourceIp = xxx on resource = Topic:xxx
```

**Possible Causes**:

- User does not have permission for the resource
- IP not in whitelist
- Deny rule exists

**Troubleshooting Steps**:

```bash
# 1. Check user's permission configuration sh bin/mqadmin getAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:username

# 2. Check if Deny rules exist sh bin/mqadmin listAcl -n 127.0.0.1:9876 -c DefaultCluster -s User:username

# 3. Grant appropriate permission sh bin/mqadmin createAcl -n 127.0.0.1:9876 -c DefaultCluster \ -s User:username -r Topic:TestTopic -a Pub -d Allow
```

<a id="bestpractice-03access--4-inter-component-communication-failed"></a>

#### 4. Inter-component Communication Failed

**Error Message**:

```text
Slave Broker connect to Master failed
or
Proxy connect to Broker failed
```

**Possible Causes**:

- `innerClientAuthenticationCredentials` misconfigured
- Inconsistent authentication credentials between components
- Master/Slave credential configuration mismatch

**Solution**:

```bash
# Check if all component configurations are consistent grep "innerClientAuthenticationCredentials" conf/*.conf conf/*.json

# Modify to unified credentials innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"}
```

<a id="bestpractice-03access--view-audit-logs"></a>

### View Audit Logs

All authentication and authorization operations are logged in Broker/Proxy logs.

**View Authentication Logs**:

```bash
grep "AUTHENTICATION" logs/rocketmqlogs/broker.log

# Authentication success example
# [AUTHENTICATION] User:producer_user is authenticated success with Signature = xxx

# Authentication failure example
# [AUTHENTICATION] User:producer_user is authenticated failed with Signature = xxx
```

**View Authorization Logs**:

```bash
grep "AUTHORIZATION" logs/rocketmqlogs/broker.log

# Authorization success example
# [AUTHORIZATION] Subject = User:producer_user is Allow Action = Pub from sourceIp = 192.168.1.100 on resource = Topic:TestTopic

# Authorization failure example
# [AUTHORIZATION] Subject = User:producer_user is Deny Action = Sub from sourceIp = 192.168.1.100 on resource = Topic:TestTopic
```

---

<a id="bestpractice-03access--best-practices"></a>

## Best Practices

<a id="bestpractice-03access--1-user-management"></a>

### 1. User Management

✅ **Recommended Practices**:

- Create independent users for different applications or services
- Use strong passwords (at least 8 characters, including letters and numbers)
- Super users should only be used for system initialization and emergency operations

❌ **Avoid**:

- Multiple applications sharing the same user
- Using weak passwords (e.g., 123456)
- Excessive use of super users in production

<a id="bestpractice-03access--2-permission-configuration"></a>

### 2. Permission Configuration

✅ **Recommended Practices**:

- Follow the principle of least privilege, grant only necessary permissions
- Use prefix matching to simplify permission management for similar resources
- Use Deny rules to protect sensitive resources
- Producers should only be granted Pub permission, consumers should only be granted Sub permission

❌ **Avoid**:

- Granting all users All permission on `*` resource
- Excessive use of wildcard matching
- Ignoring IP whitelist configuration

<a id="bestpractice-03access--3-strategy-selection"></a>

### 3. Strategy Selection

**Choose Stateless Strategy for**:

- Finance, payment, and other scenarios with extremely high security requirements
- Scenarios where permission changes need to take effect immediately
- Low throughput scenarios

**Choose Stateful Strategy for**:

- E-commerce, logging, and other high throughput scenarios
- Scenarios where permission changes are infrequent
- Scenarios with high performance requirements

<a id="bestpractice-03access--4-production-environment-deployment-tuning"></a>

### 4. Production Environment Deployment Tuning

For production deployment, in addition to basic configuration (refer to [Quick Start](#bestpractice-03access--quick-start)), pay attention to the following parameter tuning.

<a id="bestpractice-03access--integrated-storage-compute-architecture-tuning"></a>

#### Integrated Storage-Compute Architecture Tuning

```properties
# broker.conf
# Basic configuration
authenticationEnabled = true
authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider
authorizationEnabled = true
authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider
initAuthenticationUser = {"username":"rocketmq","password":"12345678"}
innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"}

# Production performance tuning: use stateful strategy (default is stateless)
authenticationStrategy = org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy
authorizationStrategy = org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy

# Cache configuration (adjust based on number of users and QPS)
userCacheMaxNum = 5000
userCacheExpiredSecond = 3600
userCacheRefreshSecond = 300
aclCacheMaxNum = 5000
aclCacheExpiredSecond = 3600
aclCacheRefreshSecond = 300
statefulAuthenticationCacheMaxNum = 20000
statefulAuthenticationCacheExpiredSecond = 60
statefulAuthorizationCacheMaxNum = 20000
statefulAuthorizationCacheExpiredSecond = 60
```

<a id="bestpractice-03access--separated-storage-compute-architecture-tuning-recommended"></a>

#### Separated Storage-Compute Architecture Tuning (Recommended)

**Broker Configuration** (`broker.conf`):

```properties
# Broker only acts as metadata provider
authenticationEnabled = false
authorizationEnabled = false
authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider
authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider
initAuthenticationUser = {"username":"rocketmq","password":"12345678"}
innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"}
```

**Proxy Configuration** (`rmq-proxy.json`):

```json
{
  "authenticationEnabled": true,
  "authenticationProvider": "org.apache.rocketmq.auth.authentication.provider.DefaultAuthenticationProvider",
  "authenticationMetadataProvider": "org.apache.rocketmq.proxy.auth.ProxyAuthenticationMetadataProvider",
  "authenticationStrategy": "org.apache.rocketmq.auth.authentication.strategy.StatefulAuthenticationStrategy",
  "innerClientAuthenticationCredentials": "{\"accessKey\":\"rocketmq\", \"secretKey\":\"12345678\"}",

  "authorizationEnabled": true,
  "authorizationProvider": "org.apache.rocketmq.auth.authorization.provider.DefaultAuthorizationProvider",
  "authorizationMetadataProvider": "org.apache.rocketmq.proxy.auth.ProxyAuthorizationMetadataProvider",
  "authorizationStrategy": "org.apache.rocketmq.auth.authorization.strategy.StatefulAuthorizationStrategy",

  "userCacheMaxNum": 5000,
  "userCacheExpiredSecond": 3600,
  "userCacheRefreshSecond": 300,
  "aclCacheMaxNum": 5000,
  "aclCacheExpiredSecond": 3600,
  "aclCacheRefreshSecond": 300,
  "statefulAuthenticationCacheMaxNum": 20000,
  "statefulAuthenticationCacheExpiredSecond": 60,
  "statefulAuthorizationCacheMaxNum": 20000,
  "statefulAuthorizationCacheExpiredSecond": 60
}
```

**Tuning Recommendations**:

<table><thead><tr><th>Parameter</th><th>Recommended Value</th><th>Description</th></tr></thead><tbody><tr><td><code>userCacheMaxNum</code></td><td>Number of users × 1.5</td><td>Avoid frequent loading of user data</td></tr><tr><td><code>aclCacheMaxNum</code></td><td>Number of users × 1.5</td><td>Avoid frequent loading of permission data</td></tr><tr><td><code>statefulAuthenticationCacheMaxNum</code></td><td>Number of connections × 2</td><td>Cache authentication result for each connection</td></tr><tr><td><code>statefulAuthorizationCacheMaxNum</code></td><td>Number of connections × resources × 2</td><td>Cache authorization result for each connection on each resource</td></tr></tbody></table>
<a id="bestpractice-03access--5-migrating-from-acl-10-to-acl-20"></a>

### 5. Migrating from ACL 1.0 to ACL 2.0

**Migration Steps**:

```bash
# 1. Backup ACL 1.0 configuration cp conf/plain_acl.yml conf/plain_acl.yml.backup

# 2. Enable migration in Broker configuration echo "migrateAuthFromV1Enabled = true" >> conf/broker.conf

# 3. Enable ACL 2.0 cat >> conf/broker.conf << EOF authenticationEnabled = true authenticationMetadataProvider = org.apache.rocketmq.auth.authentication.provider.LocalAuthenticationMetadataProvider authorizationEnabled = true authorizationMetadataProvider = org.apache.rocketmq.auth.authorization.provider.LocalAuthorizationMetadataProvider initAuthenticationUser = {"username":"rocketmq","password":"12345678"} innerClientAuthenticationCredentials = {"accessKey":"rocketmq","secretKey":"12345678"} EOF

# 4. Restart Broker (migration will execute automatically on startup) sh bin/mqbroker -n localhost:9876 -c conf/broker.conf

# 5. Verify migration results sh bin/mqadmin listUser -n 127.0.0.1:9876 -c DefaultCluster sh bin/mqadmin listAcl -n 127.0.0.1:9876 -c DefaultCluster

# 6. After successful migration, disable migration switch
# migrateAuthFromV1Enabled = false

# 7. Delete old configuration file (optional) rm conf/plain_acl.yml
```

**Notes**:

- ACL 1.0 IP whitelist will not be migrated (behavior inconsistency)
- Existing users and permissions will not be overwritten
- It is recommended to verify migration results in test environment first
- After successful migration, it is recommended to delete `plain_acl.yml` file to avoid confusion

<a id="bestpractice-03access--6-expanding-new-broker"></a>

### 6. Expanding New Broker

When expanding the cluster with new Brokers, you need to synchronize user and permission data.

**Copy all users from old Broker to new Broker**:

```bash
# Copy all users sh bin/mqadmin copyUser -n 127.0.0.1:9876 -f 192.168.0.1:10911 -t 192.168.0.2:10911

# Copy all permissions sh bin/mqadmin copyAcl -n 127.0.0.1:9876 -f 192.168.0.1:10911 -t 192.168.0.2:10911
```

**Copy specific user from old Broker to new Broker**:

```bash
# Copy specific user sh bin/mqadmin copyUser -n 127.0.0.1:9876 -f 192.168.0.1:10911 -t 192.168.0.2:10911 -u producer_user

# Copy permissions for this user sh bin/mqadmin copyAcl -n 127.0.0.1:9876 -f 192.168.0.1:10911 -t 192.168.0.2:10911 -s User:producer_user
```

<a id="bestpractice-03access--7-monitoring-and-alerting"></a>

### 7. Monitoring and Alerting

**Recommended Monitoring Metrics**:

- Authentication failure count
- Authorization denial count
- Cache hit rate
- User count
- ACL rule count

**Log Monitoring Script Example**:

```bash
#!/bin/bash
# Monitor authentication failure count auth_fail_count=$(grep "authenticated failed" logs/rocketmqlogs/broker.log | wc -l) if [ $auth_fail_count -gt 100 ]; then echo "Alert: Too many authentication failures: $auth_fail_count" fi

# Monitor authorization denial count authz_deny_count=$(grep "is Deny" logs/rocketmqlogs/broker.log | wc -l) if [ $authz_deny_count -gt 100 ]; then echo "Alert: Too many authorization denials: $authz_deny_count" fi
```

- [Introduction](#bestpractice-03access--introduction)
  - [What is Access Control 2.0?](#bestpractice-03access--what-is-access-control-20)
  - [Core Features](#bestpractice-03access--core-features)
  - [Core Concepts](#bestpractice-03access--core-concepts)
- [Quick Start](#bestpractice-03access--quick-start)
  - [5-Minute Quick Experience](#bestpractice-03access--5-minute-quick-experience)
  - [Different Deployment Architecture Configurations](#bestpractice-03access--different-deployment-architecture-configurations)
- [Configuration](#bestpractice-03access--configuration)
  - [Authentication Configuration Parameters](#bestpractice-03access--authentication-configuration-parameters)
  - [Authorization Configuration Parameters](#bestpractice-03access--authorization-configuration-parameters)
  - [Cache Configuration Parameters](#bestpractice-03access--cache-configuration-parameters)
  - [Authentication and Authorization Strategies](#bestpractice-03access--authentication-and-authorization-strategies)
- [User Management](#bestpractice-03access--user-management)
  - [User Type Description](#bestpractice-03access--user-type-description)
  - [mqadmin Tool Configuration](#bestpractice-03access--mqadmin-tool-configuration)
  - [User Management Commands](#bestpractice-03access--user-management-commands)
  - [Command Parameters](#bestpractice-03access--command-parameters)
- [Permission Management](#bestpractice-03access--permission-management)
  - [Core Concepts](#bestpractice-03access--core-concepts-1)
  - [Permission Priority Rules](#bestpractice-03access--permission-priority-rules)
  - [Permission Management Commands](#bestpractice-03access--permission-management-commands)
  - [Command Parameters](#bestpractice-03access--command-parameters-1)
- [Client Usage](#bestpractice-03access--client-usage)
  - [Java Client Configuration](#bestpractice-03access--java-client-configuration)
  - [Message Producer](#bestpractice-03access--message-producer)
  - [Message Consumer](#bestpractice-03access--message-consumer)
  - [Spring Boot Integration](#bestpractice-03access--spring-boot-integration)
- [Common Scenarios](#bestpractice-03access--common-scenarios)
  - [Scenario 1: Separate Producer and Consumer](#bestpractice-03access--scenario-1-separate-producer-and-consumer)
  - [Scenario 2: Permissions by Business Module](#bestpractice-03access--scenario-2-permissions-by-business-module)
  - [Scenario 3: IP Whitelist Restriction](#bestpractice-03access--scenario-3-ip-whitelist-restriction)
  - [Scenario 4: Administrator Permission](#bestpractice-03access--scenario-4-administrator-permission)
  - [Scenario 5: Deny Access to Sensitive Topic](#bestpractice-03access--scenario-5-deny-access-to-sensitive-topic)
- [Troubleshooting](#bestpractice-03access--troubleshooting)
  - [Common Errors](#bestpractice-03access--common-errors)
  - [View Audit Logs](#bestpractice-03access--view-audit-logs)
- [Best Practices](#bestpractice-03access--best-practices)
  - [1. User Management](#bestpractice-03access--1-user-management)
  - [2. Permission Configuration](#bestpractice-03access--2-permission-configuration)
  - [3. Strategy Selection](#bestpractice-03access--3-strategy-selection)
  - [4. Production Environment Deployment Tuning](#bestpractice-03access--4-production-environment-deployment-tuning)
  - [5. Migrating from ACL 1.0 to ACL 2.0](#bestpractice-03access--5-migrating-from-acl-10-to-acl-20)
  - [6. Expanding New Broker](#bestpractice-03access--6-expanding-new-broker)
  - [7. Monitoring and Alerting](#bestpractice-03access--7-monitoring-and-alerting)

---

<a id="bestpractice-04jvmos"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/04JVMOS/ -->

<!-- page_index: 41 -->

# JVM/OS Configuration

Version: 5.0

# JVM/OS Configuration

This section focuses on system (JVM/OS) related configuration.

<a id="bestpractice-04jvmos--1jvm-options"></a>

## 1.JVM Options

The latest release of JDK 1.8 is recommended. Prevent the JVM from adjusting the heap size for better performance by setting the same Xms and Xmx values. The production JVM configuration is as follows:

```text
-server -Xms8g -Xmx8g -Xmn4g
```

When the JVM is 8-byte aligned by default, it is recommended that the maximum heap memory not exceed 32 G. Otherwise, the pointer compression technology of the JVM will be affected and memory will be wasted.

If you don't care about the startup time of the RocketMQ Broker, a better option is to "pre-touch" the Java heap to ensure that every page will be allocated during JVM initialization. Those who don't care about startup time can enable it:

```text
-XX:+AlwaysPreTouch
```

Disabling bias locking may reduce JVM pauses:

```text
-XX:-UseBiasedLocking
```

Garbage collection, we recommend using the G1 collector that came with JDK 1.8:

```text
-XX:+UseG1GC
-XX:G1HeapRegionSize=16m
-XX:G1ReservePercent=25
-XX:InitiatingHeapOccupancyPercent=30
```

These GC options may seem aggressive, but they proved to perform well in our production environment.

Also, don't set the value of -XX:MaxGCPauseMillis too small, or the JVM will use a small young generation to achieve this goal, which will result in very frequent minor GCS, so rolling GC log files are recommended:

```text
-XX:+UseGCLogFileRotation
-XX:NumberOfGCLogFiles=5
-XX:GCLogFileSize=30m
```

If writing to GC files increases the agent's latency, consider redirecting GC log files to the in-memory file system:

```text
-Xloggc:/dev/shm/mq_gc_%p.log123
```

<a id="bestpractice-04jvmos--2linux-kernel-parameters"></a>

## 2.Linux Kernel Parameters

The os.sh script lists many kernel parameters in the bin folder, which can be changed slightly and then used for production purposes. Note the following parameters, for more details, see [Documentation](assets/files/vm_0033172d6bf249c6.txt) in /proc/sys/vm/\*

- **vm.extra\_free\_kbytes** The VM is told to keep extra available memory between the threshold at which background reclamation (kswapd) starts and the threshold at which it is directly reclaimed (by allocating processes). RocketMQ uses this parameter to avoid long delays in memory allocation. (depending on the kernel version)
- **vm.min\_free\_kbytes** If it is set below 1024 KB, it will subtly break the system, and the system is prone to deadlock under high load.
- **vm.max\_map\_count** Limits the maximum number of memory mapped regions that a process can have. RocketMQ will load CommitLog and ConsumeQueue using MMAP, so it is recommended to set this parameter to a large value.
- **vm.swappiness** Defines how aggressively the kernel swaps memory pages. Higher values increase aggression, lower values decrease exchange volume. A value of 10 is recommended to avoid exchange delays.
- **File descriptor limits** RocketMQ needs to open file descriptors for files (CommitLog and ConsumeQueue) and network connections. We recommend setting the file descriptor value to 655350.
- [Disk scheduler](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/ch06s04s02.html) RocketMQ recommends the use of an I/O deadline scheduler, which attempts to provide a guaranteed delay for requests.

- [1.JVM Options](#bestpractice-04jvmos--1jvm-options)
- [2.Linux Kernel Parameters](#bestpractice-04jvmos--2linux-kernel-parameters)

---

<a id="bestpractice-05subscribe"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/05subscribe/ -->

<!-- page_index: 42 -->

# Consistent Subscription Relationship

Version: 5.0

# Consistent Subscription Relationship

<a id="bestpractice-05subscribe--introduction"></a>

## Introduction

Subscription relationships are a very important part of the RocketMQ domain model, used to express the control metadata for consumer consumption of messages. For a complete concept, please refer to [Subscription Relationship Model](#domainmodel-09subscription).

Subscription relationships are consistent when all Consumer instances in the same consumer group have exactly the same subscriptions to Topic and Tag. If the subscription relationships (consumer group name-Topic-Tag) are not consistent, it can lead to confusion in consuming messages and even loss of messages.

<a id="bestpractice-05subscribe--1-examples-of-correct-subscription-relationships"></a>

## 1 Examples of correct subscription relationships

<a id="bestpractice-05subscribe--11-topics-subscribed-to-are-the-same-and-the-filter-expressions-are-consistent"></a>

### 1.1 Topics subscribed to are the same and the filter expressions are consistent

As shown in the following figure, the three Consumer instances C1, C2, and C3 in the same ConsumerGroup have all subscribed to TopicA, and the subscriptions to TopicA's Tag are all Tag1, which meets the principle of subscription relationship consistency.

![1658453577894-0e64b114-cb4a-4220-a09a-62bc1f2943c6](assets/images/5-0-e8-ae-a2-e9-98-85-e5-85-b3-e7-b3-bb-e4-b8-80-e8-87-b4-1-4cbab04c03d85562d7d144edfeb86aa6_96b6dc87de118624.jpeg)

**Correct example code 1:**

C1, C2, and C3's subscription relationships are consistent, meaning that C1, C2, and C3's code for subscribing to messages must be exactly the same, and the code example is as follows:

```java
PushConsumer consumer1 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer1.subscribe("TopicA", new FilterExpression("TagA", FilterExpressionType.TAG));

PushConsumer consumer2 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer2.subscribe("TopicA", new FilterExpression("TagA", FilterExpressionType.TAG));

PushConsumer consumer3 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer3.subscribe("TopicA", new FilterExpression("TagA", FilterExpressionType.TAG));
```

> [!INFO]
> RocketMQ emphasizes consistency in subscription relationships, which means that every Consumer within the same ConsumerGroup should be consistent, because from the perspective of the server, all Consumers in a Group should be the same logical copy.
>
> Emphasis on consistency in subscription relationships does not mean that a Consumer cannot subscribe to multiple Topics, and each Consumer can still subscribe to multiple Topics as needed, but the premise is that Consumers within the same consumer group must be consistent.

<a id="bestpractice-05subscribe--2-troubleshooting-inconsistent-subscription-relationships"></a>

## 2 Troubleshooting inconsistent subscription relationships

**Problem description**

When using the RocketMQ version of the message queue, it is possible to have inconsistent subscription relationships. The specific problems are as follows:

- The consistency of subscription relationships in the RocketMQ version of the message queue console is displayed as no.
- Consumer instances do not receive subscribed messages.

**Please refer to the following steps for checking**

You can check whether the subscription relationship of the specified Group is consistent in the Apache RocketMQ console or CLi tool. If the query result is inconsistent, please refer to the common subscription relationship inconsistency problems in this article to troubleshoot the consumption code of the Consumer instance.

1. Check the configuration code related to subscription in your Consumer instance to ensure that all Consumer instances in the same ConsumerGroup subscribe to the same Topic and Tag.
2. Use the console or Cli command ConsumerConnection to check if the effective subscription relationship is consistent.
3. Test and confirm that the message can be consumed by the expected Consumer instance.

<a id="bestpractice-05subscribe--3-common-issues-with-inconsistent-subscription-relationships"></a>

## 3 Common issues with inconsistent subscription relationships

<a id="bestpractice-05subscribe--31-in-the-same-consumergroup-the-consumer-instances-have-different-topics-subscribed-to-applicable-to-3x-4x-sdk"></a>

### 3.1 In the same ConsumerGroup, the Consumer instances have different Topics subscribed to (applicable to 3.x, 4.x SDK)

In the early 3.x/4.x versions of the SDK, as shown in the following figure, three Consumer instances C1, C2, and C3 in the same ConsumerGroup have subscribed to TopicA, TopicB, and TopicC respectively, and their subscribed Topics are inconsistent, which does not conform to the principle of consistent subscription.

> [!NOTE]
> The 5.x version of the SDK now supports Consumer instances in the same ConsumerGroup subscribing to different topics.

![image-20220722102131073](assets/images/5-0-e8-ae-a2-e9-98-85-e5-85-b3-e7-b3-bb-e4-b8-80-e8-87-b4-2-41010fd8c9c21c928807228caaf2d621_553199dbb9ac3ecf.jpeg)

<a id="bestpractice-05subscribe--32-consumer-instances-in-the-same-consumergroup-subscribe-to-the-same-topic-but-the-subscribed-tags-are-different"></a>

### 3.2 Consumer instances in the same ConsumerGroup subscribe to the same topic, but the subscribed tags are different.

As shown in the following figure, the Consumer instances C1, C2, and C3 in the same ConsumerGroup all subscribe to TopicA, but C1 subscribes to Tag1 of TopicA, while C2 and C3 subscribe to Tag2 of TopicA. The subscribed tags of the same topic are inconsistent and do not conform to the consistency principle of subscription relationship.

![image-20220722102926055](assets/images/5-0-e8-ae-a2-e9-98-85-e5-85-b3-e7-b3-bb-e4-b8-80-e8-87-b4-3-514888130c9907fb857a159181ff71cc_714d056f9bc54e58.jpeg)

**Error example code 2:**

- Consumer example 2-1：


```java
PushConsumer consumer1 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer1.subscribe("TopicA", new FilterExpression("Tag1", FilterExpressionType.TAG));
```

- Consumer example 2-2：


```java
PushConsumer consumer2 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer2.subscribe("TopicA", new FilterExpression("Tag2", FilterExpressionType.TAG));
```

- Consumer example 2-3：


```java
PushConsumer consumer3 = provider.newPushConsumerBuilder().setConsumerGroup("GroupA").build();
consumer3.subscribe("TopicA", new FilterExpression("Tag2", FilterExpressionType.TAG));
```

- [Introduction](#bestpractice-05subscribe--introduction)
- [1 Examples of correct subscription relationships](#bestpractice-05subscribe--1-examples-of-correct-subscription-relationships)
  - [1.1 Topics subscribed to are the same and the filter expressions are consistent](#bestpractice-05subscribe--11-topics-subscribed-to-are-the-same-and-the-filter-expressions-are-consistent)
- [2 Troubleshooting inconsistent subscription relationships](#bestpractice-05subscribe--2-troubleshooting-inconsistent-subscription-relationships)
- [3 Common issues with inconsistent subscription relationships](#bestpractice-05subscribe--3-common-issues-with-inconsistent-subscription-relationships)
  - [3.1 In the same ConsumerGroup, the Consumer instances have different Topics subscribed to (applicable to 3.x, 4.x SDK)](#bestpractice-05subscribe--31-in-the-same-consumergroup-the-consumer-instances-have-different-topics-subscribed-to-applicable-to-3x-4x-sdk)
  - [3.2 Consumer instances in the same ConsumerGroup subscribe to the same topic, but the subscribed tags are different.](#bestpractice-05subscribe--32-consumer-instances-in-the-same-consumergroup-subscribe-to-the-same-topic-but-the-subscribed-tags-are-different)

---

<a id="bestpractice-06faq"></a>

<!-- source_url: https://rocketmq.apache.org/docs/bestPractice/06FAQ/ -->

<!-- page_index: 43 -->

# FAQs

Version: 5.0

# FAQs

Common questions about the RocketMQ project:

<a id="bestpractice-06faq--1-basic"></a>

## 1 Basic

1. **Why should we use RocketMQ instead of choosing other products?**

   Please refer to [why choose RocketMQ](http://rocketmq.apache.org/docs/motivation/)
2. **Do I need to install any other software in order to use RocketMQ, such as ZooKeeper?**

   No，RocketMQ can run on independent。

<a id="bestpractice-06faq--2-use"></a>

## 2 Use

1. **Where does the newly created ConsumerGroup start consuming messages?**

   1）When the 5.x SDK is first online, it will consume from the latest message on the server, starting from the tail of the queue. After restarting again, it will continue to consume from the last consumption position.

   2）The 3.x/4.x SDK is more complicated. If the first start is within three days of the sent message, the consumer will start consuming from the first saved message on the server. If the sent message is more than three days, the consumer will start consuming from the latest message on the server, starting from the tail of the queue. After restarting again, it will continue to consume from the last consumption position.
2. **When consumption fails, how can the message be consumed again?**

   1）In cluster mode, the consumption business logic code will return a consumption failure status, or throw an exception. If a message consumption fails, it will be retried according to the maximum retry count set, and then the message will be discarded.

   2）In broadcast consumption mode, broadcast consumption still guarantees that the message is consumed at least once, but does not provide resend options.
3. **When consumption fails, how can the failed message be found?**

   1）Using a time-based topic query can query messages within a period of time.

   2）Use the topic and message ID to accurately query the message.

   3）Use the topic and message Key to accurately query all messages with the same message Key.
4. **Is the message only delivered once?**

   RocketMQ ensures that all messages are delivered at least once. In most cases, messages are not repeated.
5. **How can a new Broker be added?**

   1）Start a new Broker and register it in the Broker list of the NameServer.

   2）By default, only internal system Topics and Consumer Groups are automatically created. If you want to have your business topic and consumer group on the new node, copy them from the existing Broker. We provide management tools and command line to handle this.

<a id="bestpractice-06faq--3-configuration-dependent"></a>

## 3 Configuration dependent

The following answers are default values, which can be modified through configuration.

1. **How long can messages be saved on the server?**

   Messages will be stored for a maximum of 3 days. Messages that have not been used for more than 3 days will be deleted.
2. **What is the size limit for message bodies?**

   Typically, it is 256KB.
3. **How do you set the number of consumer threads?**

   When you start the consumer, you can set the property. The parameter name varies by version.

<a id="bestpractice-06faq--4-error"></a>

## 4 Error

1. **APPLY\_TOPIC\_URL**

   - **exception information**


```java
topic[xxx] not exist, apply first please!
```

   - **reason**

     1）When a Producer sends a message or a Consumer consumes a message, this exception will occur if the routing information for the Topic cannot be obtained.
   - **solution**

     1）Make sure that the NameServer indeed contains the routing information for the Topic. You can use the management tool or the Web console to query the routing information from the NameServer through the TopicRoute;

     2）Make sure that the Broker and Consumer are connected to the same NameServer cluster;

     3）Make sure that the queue permissions for the topic are 6 (rw-) for the Producer or at least 2 (-w-) for the Consumer;

     If the topic cannot be found, create it on the Broker through the management tool command updateTopic or the Web console.
2. **NAME\_SERVER\_ADDR\_NOT\_EXIST\_URL**

   - **exception information**


```java
No name server address, please set it
```

     or


```java
connect to xxx failed, maybe the domain name xxx not bind in /etc/hosts
```

   - **reason**

     1）Producer or Consumer, there is an error in obtaining the NameServer address information.
   - **solution**

     1）Please refer to：[5.1 Client addressing](https://github.com/apache/rocketmq/blob/develop/docs/cn/best_practice.md)
3. **GROUP\_NAME\_DUPLICATE\_URL**

   - **exception information**


```java
The producer group[xxx] has been created before, specify another name please.
```

   - **reason**

     1）A Consumer Group with the same name has already been started and registration failed.
   - **solution**

     1）Rename a new Consumer Group.

     2）A Consumer Group with the same name was normally closed and then started again.
4. **CLIENT\_PARAMETER\_CHECK\_URL**

   - **exception information**


```text
consumerGroup can not equal ...
```

     or


```java
allocateMessageQueueStrategy is null ...
```

     or


```java
Long polling mode, the consumer consumerTimeoutMillisWhenSuspend must greater than brokerSuspendMaxTimeMillis ...
```

     In addition to the above exceptions, there may be other exceptions that are not listed here.
   - **reason**

     1）Consumer parameter verification failed.
   - **solution**

     1）Please refer to： [5.2 Client configuration](https://github.com/apache/rocketmq/blob/develop/docs/cn/best_practice.md)
5. **SUBSCRIPTION\_GROUP\_NOT\_EXIST**

   - **exception information**


```java
subscription group not exist
```

   - **reason**

     1）If the Consumer Group or DelayQueue encounters an error while getting subscription information.
   - **solution**

     1）Ensure the Consumer's subscription to the Topic information is consistent with the Topic information in the NameServer.

     2）Make sure the Broker and Consumer are connected to the same NameServer cluster.

     3）Ensure the queue permissions for the Topic are 6 (rw-) for the Producer, or at least 2 (-w-) for the Consumer
6. **CLIENT\_SERVICE\_NOT\_OK**

   - **exception information**


```java
The xxx service state not OK, maybe started once
```

   - **reason**

     1）Starting multiple Producer/Consumer instances in the same JVM using the same Producer/Consumer Group may cause the client to fail to start.
   - **solution**

     1）Make sure only one Producer/Consumer instance is started for a given Producer/Consumer Group JVM.
7. **NO\_TOPIC\_ROUTE\_INFO**

   - **exception information**


```java
No route info of this topic:
```

   - **reason**

     1）If a message is sent to a topic that is not available to the producer，that's what happens.
   - **solution**

     1）Ensure the producer is able to connect to the name server and retrieve routing metadata from it.

     2）Ensure the name server contains routing metadata for the topic. You can use a management tool or the Web console to query the routing metadata from the name server using TopicRoute.

     3）Make sure your Broker is sending heartbeats to the same NameServer list that your producer is connected to.

     4）Ensure the topic has permission 6 (rw-), or at least 2 (-w-).

     If the topic is not found, create it on the Broker via the management tool command updateTopic or the Web console.
8. **LOAD\_JSON\_EXCEPTION**

   - **exception information**


```java
readLocalOffset Exception
```

   - **reason**

     1）In broadcast mode, consumers have an error when loading the local offsets.json file.

     2）A damaged fastjson file can also cause the same problem.
   - **solution**

     1）Check if the fastjson version and RocketMQ version in use are consistent.

     2）Upgrade fastjson version.
9. **SAME\_GROUP\_DIFFERENT\_TOPIC**

   - **exception information**


```java
the consumer's group info/subscription not exist
```

   - **reason**
     1）Consumer subscription to Topic information does not exist.
   - **solution**

     1）Check if the Consumer Group where the Consumer belongs exists.

     2）Check if the Topic subscribed to by the Consumer exists.
10. **MQLIST\_NOT\_EXIST**

    - **exception information**


```java
Can not find Message Queue for this topic
```

    - **reason**
      1）For the Producer, the corresponding Queue information could not be obtained based on the Topic.
    - **solution**

      1）Ensure that the Queue information has been correctly configured for the Topic.

      2）Ensure that the Queue corresponding to the Topic has at least 2 (-w-) permissions.
11. **SEND\_MSG\_FAILED**

    - **exception information**


```java
Send [xxx] times, still failed, cost [xxx]ms, Topic: xxx, BrokersSent ...
```

    - **reason**
      1）The Producer message sending is abnormal. A total of 3 times are sent in SYNC mode, and 1 time is sent in ASYNC and ONEWAY.
    - **solution**
      1）Whether the timeout parameter of the Producer sending message is too small.

      2）Ensure that the Broker is normal.

      3）Ensure that the connection between the Producer and Broker is normal.
12. **UNKNOWN\_HOST\_EXCEPTION**

    - **exception information**


```java
InetAddress java.net.InetAddress.getLocalHost() throws UnknownHostException
```

    - **reason**

      1）There may be many network interfaces on the host, and one interface may be bound to multiple IP addresses.
    - **solution**

      1）Ensure that the IP corresponding to the host can be accessed normally, and use network commands such as Ping to check the network situation.

<a id="bestpractice-06faq--5-others"></a>

## 5 Others

1. What is the impact of the Broker crashing？

   1）Master node crashes

   Messages can no longer be sent to the Broker cluster, but if you have another available Broker cluster, messages can still be sent as long as the topic exists. Messages can still be consumed from the Slave node.

   2）Some Slave nodes crash

   Sending messages will not be affected as long as there is another working Slave. Consuming messages will not be affected unless the consumer group is set to consume from the Slave first. By default, the consumer group consumes from the Master.

   3）All Slave nodes crash

   Sending messages to the Master will not be affected, but if the Master is SYNC\_MASTER, the Producer will get a SLAVE\_NOT\_AVAILABLE indicating that the message was not sent to any Slave. Consuming messages will not be affected unless the consumer group is set to consume from the Slave first. By default, the consumer group consumes from the Master.

- [1 Basic](#bestpractice-06faq--1-basic)
- [2 Use](#bestpractice-06faq--2-use)
- [3 Configuration dependent](#bestpractice-06faq--3-configuration-dependent)
- [4 Error](#bestpractice-06faq--4-error)
- [5 Others](#bestpractice-06faq--5-others)

---

<a id="eventbridge-01rocketmqeventbridgeconcepts"></a>

<!-- source_url: https://rocketmq.apache.org/docs/eventbridge/01RocketMQEventBridgeConcepts/ -->

<!-- page_index: 44 -->

# RocketMQ EventBridge Core Concept

Version: 5.0

# RocketMQ EventBridge Core Concept

Understanding the core concepts in EventBridge can help us better analyze and use EventBridge. This article focuses on introducing the terms included in EventBridge:

- EventSource: the source of the event. Used to manage events sent to EventBridge, all events sent to EventBridge must be marked with the source name information, corresponding to the source field in the CloudEvent event body.
- EventBus: the event bus. Used to store events sent to EventBridge.
- EventRule: event rule. When a consumer needs to subscribe to events, they can configure filtering and transformation information through rules to push events to the designated target endpoint.
- FilterPattern: event filtering pattern, used to configure filtering of target endpoints in rules.
- Transform: event transformation, converting the event format to the data format required by the target endpoint.
- EventTarget: the target endpoint of the event, which is the actual event consumer.

Next, we will expand on these concepts in more detail.

<a id="eventbridge-01rocketmqeventbridgeconcepts--eventsource"></a>

## EventSource

Event source represents the origin of the event and is used to describe a category of events, generally corresponding one-to-one with microservice systems. For example: transaction event source, attendance event source, etc. Event source is a large classification for events, and a single event source often contains multiple event types (type), such as a transaction event source may contain: order events, payment events, refund events, etc.

Additionally, it is worth noting that event source is not used to describe the entity that caused the event. Instead, in CloudEvent, we generally use subject to represent the entity resource that caused the event. The event source is similar to the large category divisions in a market economy department store, such as fresh food area, daily necessities area, household appliances area, etc. In the event center "department store", we can quickly find the event we need through the event source.

<a id="eventbridge-01rocketmqeventbridgeconcepts--eventbus"></a>

## EventBus

The event bus is where events are stored, and it can have multiple implementations including Local, RocketMQ, Kafka, etc.

When the event producer sends an event, they must specify the event bus. The event bus is a first-class citizen in EventBridge, and all other resources form logical isolation around the event bus, that is: event sources and event rules must belong to a specific event bus. Event sources and event rules under different event buses can have the same name, but event sources and rules under the same event bus must have unique names.

<a id="eventbridge-01rocketmqeventbridgeconcepts--eventrule"></a>

## EventRule

When a consumer needs to subscribe to events, they can configure filtering and transformation information through event rules, and push events to the designated target endpoint. Therefore, event rules include three parts: event filtering + event transformation + event target.

![img_1.png](assets/images/eventrule-c822b08589be43f273884c8b21bcb7de_a86fdc90ebc63c42.png)

<a id="eventbridge-01rocketmqeventbridgeconcepts--filterpattern"></a>

## FilterPattern

By using event filtering patterns, we can filter events on the event bus and only push the events that the target endpoint needs, thus reducing unnecessary opening and relieving the pressure on the consumer's target endpoint. Currently, EventBridge supports the following event filtering capabilities:

- Specified value matching
- Prefix matching
- Suffix matching
- Exclusion matching
- Numeric matching
- Array matching
- And complex combination logic matching

(Details will be covered in other articles)

<a id="eventbridge-01rocketmqeventbridgeconcepts--transform"></a>

## Transform

Event producers' events may be subscribed to by multiple consumers, but the data format needed by different consumers is often different. In this case, it is necessary to convert the event produced by the producer into the event format that the consumer target end needs. Currently, EventBridge supports the following event conversion capabilities:

- Complete events: No conversion, directly delivering the original CloudEvents;
- Partial events: Extracting the content that needs to be delivered to the event target through JsonPath syntax from CloudEvents;
- Constants: The event only serves as a trigger, and the delivered content is a constant;
- Template converter: Flexibly rendering the delivered event format through the definition of a template.

(Details to be seen in other articles)

<a id="eventbridge-01rocketmqeventbridgeconcepts--eventtarget"></a>

## EventTarget

The event target is the event consumer in the EventBridge architecture. In this architecture, consumers only need to design their own business models and provide a common API (this API can be used to receive events and also for front-end management operations). EventBridge will then safely and reliably push events to the target consumer according to the data format defined by the API.

- [EventSource](#eventbridge-01rocketmqeventbridgeconcepts--eventsource)
- [EventBus](#eventbridge-01rocketmqeventbridgeconcepts--eventbus)
- [EventRule](#eventbridge-01rocketmqeventbridgeconcepts--eventrule)
- [FilterPattern](#eventbridge-01rocketmqeventbridgeconcepts--filterpattern)
- [Transform](#eventbridge-01rocketmqeventbridgeconcepts--transform)
- [EventTarget](#eventbridge-01rocketmqeventbridgeconcepts--eventtarget)

---

<a id="eventbridge-02rocketmqeventbridgeoverview"></a>

<!-- source_url: https://rocketmq.apache.org/docs/eventbridge/02RocketMQEventBridgeOverview/ -->

<!-- page_index: 45 -->

# RocketMQ EventBridge Overview

Version: 5.0

# RocketMQ EventBridge Overview

RocketMQ EventBridge is dedicated to helping users build high-reliability, low-coupling, and high-performance event-driven architectures. In event-driven architecture, microservices do not need to actively subscribe to external messages, but can instead centralize all entries that trigger changes in the microservice system to the API, and only need to focus on the current microservice's own business domain model definition and design of the API, without having to adapt and parse external service messages through a lot of glue code. EventBridge is responsible for safely and reliably adapting and delivering external service-generated events to the API designed by the current microservice.

When do we use RocketMQ messages and when do we use EventBridge events? What is the meaning of events, and what is the difference with messages?

<a id="eventbridge-02rocketmqeventbridgeoverview--message-event"></a>

## Message & Event

We have defined events as follows:

```text
Events refer to things that have already happened, especially important things.
```

The relationship between events and messages is as follows：

![image](assets/images/messagewithevent-e09f120787a45a119bdff9104d391a25_9ef40f5ad3c63f47.png)

Messages include Command messages and Event messages. Command messages are operation commands sent by external systems to this system (as shown in the left part of the figure); Event messages are events that occur after the system receives a Command operation request and internal changes (as shown in the right part of the figure);

<a id="eventbridge-02rocketmqeventbridgeoverview--four-characteristics-of-an-event"></a>

## Four characteristics of an event

<a id="eventbridge-02rocketmqeventbridgeoverview--1-happened"></a>

### 1. Happened

Events are always "already happened." "Already happened" also means they are immutable. This feature is very important, when we process events and analyze events, it means that we can absolutely trust these events, as long as we receive the events, they must be true behaviors of the system.

Command represents an operation request, whether it truly happens or not cannot be known. For example：

```text
* Turning on the kitchen lights
* Someone pressed the doorbell
* Account A received 100,000.
```

An event is a clear occurrence that has already happened, such as

```text
* The kitchen light being turned on
* Someone pressing the doorbell
* Account A receiving 100,000
```

<a id="eventbridge-02rocketmqeventbridgeoverview--2-no-expectation"></a>

### 2. No expectation

```text
An event is an objective description of a change in the state or attribute value of a thing, but it does not make any expectations about how to handle the event itself. In contrast, both Command and Query have expectations, they hope the system will make changes or return results, but the Event is just an objective description of a change in the system.
```

For example: the traffic signal, from green to yellow, just describes an objective fact, and there is no objective expectation in itself. In different countries and regions, different expectations are given to this event. For example, in Japan, yellow is equivalent to red, while in Russia, running a yellow light is tolerated.

Compared to Command messages：

- Events: are a bit like "market economy", goods are produced and placed in the large window of the shopping mall, consumers buy them back if they feel good, if no one buys them, the goods may expire and be wasted.
- Command message: is a bit like "planned economy", production is based on demand, designated distribution objects, and there is little waste.

<a id="eventbridge-02rocketmqeventbridgeoverview--3-naturally-ordered-and-unique"></a>

### 3. Naturally ordered and unique

```text
The same entity cannot have both A and B occur at the same time, there must be a temporal relationship; if so, these two events must belong to different event types.
```

For example: for the same traffic light, it can't turn green and red at the same time, it can only turn into one state at a given moment. If we see two events with the same content, then it must have occurred twice and one happened before the other. This is valuable for processing data consistency and system behavior analysis (such as ABA scenarios): we not only see the final result of the system, but also the intermediate process that led to that result.

<a id="eventbridge-02rocketmqeventbridgeoverview--4-materialize"></a>

### 4. Materialize

Events try to record the "crime scene" as completely as possible, because events do not know how consumers will use them, so they will be as detailed as possible. Including:

```text
When did the event occur?
Who generated it?
What type of event is it?
What is the content of the event? What is the structure of the content?
... ...
```

Compared to common messages we see, as the upstream and downstream are generally determined, often in order to improve performance and transmission efficiency, messages will be as concise as possible, as long as it meets the consumer's needs specified by the "planned economy".

<a id="eventbridge-02rocketmqeventbridgeoverview--rocketmq-eventbridges-typical-application-scenarios"></a>

## RocketMQ EventBridge's typical application scenarios

<a id="eventbridge-02rocketmqeventbridgeoverview--scenario-1-event-notification"></a>

### Scenario 1: Event Notification

In microservices, we often encounter situations where messages produced in one microservice need to be notified to other consumers. Here we compare three ways:

**A: Strong dependency method**

The producer actively calls the consumer's microservice and adapts the consumer's API. This design is undoubtedly very bad, the producer is strongly dependent on the consumer, deeply coupled. If a call to a consumer has an exception and no effective isolation is done, it is very likely to cause the entire microservice to hang. It is very poor when new consumers come in.

**B: Semi-decoupling method**

The producer sends the message to the message service, and the consumer subscribes to the message service to get the message and converts the message into the data format required by its own business domain model. This method achieved decoupling on the call chain, greatly reducing system risks, but for consumers, they still need to understand and parse the producer's business semantics and convert the message into the format needed for their own business domain. Under this method, when the consumer needs to subscribe to data from multiple producers, a large amount of glue code is needed to adapt to each message produced by the producer. In addition, when the upstream producer's message format changes, there is also a risk and operational cost.

**C: Complete decoupling method**

Under this method, consumers do not need to introduce SDK to subscribe to Broker, they only need to design API according to their own business domain model, and the message service will filter and convert upstream

![image](assets/images/threestages-840b209d165587c9fe2e3e5d6b942ead_4a81f5772e53825a.png)

<a id="eventbridge-02rocketmqeventbridgeoverview--scenario-2-inter-system-integration"></a>

### Scenario 2: Inter-system integration

Scenario 1 mainly focuses on the event communication between microservices within a single product. Scenario 2 mainly focuses on event communication between multiple products. In an enterprise, we often use multiple products, and many of these products may not be developed by ourselves, but are purchased as external SaaS services. In this case, it is difficult to make events flow between different external SaaS products, because these external SaaS products are not developed by ourselves and it is not easy to modify their code. The event center capability provided by EventBridge can help collect events generated by various products and organize and manage them well, just like the goods in a department store window, carefully arranged and equipped with instructions, for consumers to choose from, and also providing home delivery service.

![image](assets/images/eventcenter-850d3b5bbc18655758b155d3e610a73d_20246678d9ce32f2.png)

<a id="eventbridge-02rocketmqeventbridgeoverview--how-rocketmq-eventbridge-works"></a>

## How RocketMQ EventBridge works?

In order to address the problems mentioned in the above two scenarios, EventBridge approaches from five aspects:

**1. Determine event standards:**

Because events are not for oneself, but for everyone. It has no clear consumer, and all are potential consumers. Therefore, we need to standardize the definition of events, so that everyone can understand, and be easy to understand. Currently, CloudEvent under CNCF has gradually become a widely recognized factual standard, so we choose CloudEvent as our EventBridge event standard.

**2. Establish event center:**

The event center contains all the events registered by various systems. This is like the market economy department store we mentioned above, which has a variety of events classified and arranged, and everyone can come in to see which events may be needed, and then buy them back.

**3. Define event format:**

Event format is used to describe the specific contents of events. This is equivalent to a sales contract in a market economy. The event format sent by the producer must be determined and cannot always change; the format in which the consumer receives events must also be determined, otherwise the entire market will be in chaos.

**4. Subscription "rules":**

We need to give consumers the ability to deliver events to the target end, and filter and transform events before delivery so that it can adapt to the format of the target end API receiving parameters. We call this process creating a subscription rule.

**5. Event Bus:**
Finally, we also need a place to store events, that is the event bus in the middle of the diagram.

![image](assets/images/howeventbridgework-f7ce646f4bfc0d5f26b9261673009ce9_e9cc63bc04c4b0b9.png)

- [Message & Event](#eventbridge-02rocketmqeventbridgeoverview--message-event)
- [Four characteristics of an event](#eventbridge-02rocketmqeventbridgeoverview--four-characteristics-of-an-event)
  - [1. Happened](#eventbridge-02rocketmqeventbridgeoverview--1-happened)
  - [2. No expectation](#eventbridge-02rocketmqeventbridgeoverview--2-no-expectation)
  - [3. Naturally ordered and unique](#eventbridge-02rocketmqeventbridgeoverview--3-naturally-ordered-and-unique)
  - [4. Materialize](#eventbridge-02rocketmqeventbridgeoverview--4-materialize)
- [RocketMQ EventBridge's typical application scenarios](#eventbridge-02rocketmqeventbridgeoverview--rocketmq-eventbridges-typical-application-scenarios)
  - [Scenario 1: Event Notification](#eventbridge-02rocketmqeventbridgeoverview--scenario-1-event-notification)
  - [Scenario 2: Inter-system integration](#eventbridge-02rocketmqeventbridgeoverview--scenario-2-inter-system-integration)
- [How RocketMQ EventBridge works?](#eventbridge-02rocketmqeventbridgeoverview--how-rocketmq-eventbridge-works)

---

<a id="eventbridge-03rocketmqeventbridgequickstart"></a>

<!-- source_url: https://rocketmq.apache.org/docs/eventbridge/03RocketMQEventBridgeQuickStart/ -->

<!-- page_index: 46 -->

# RocketMQ EventBridge Quick Start

Version: 5.0

# RocketMQ EventBridge Quick Start

RocketMQ EventBridge requires a message service to store events and a runtime to subscribe and push events. In this case, we choose Apache RocketMQ as our message service and Apache RocketMQ Connect as our runtime for subscribing and pushing events. Of course, you can also choose other message services instead, EventBridge does not impose any restrictions on this. In the future, EventBridge also plans to implement its own runtime based on OpenMessaging Connect API in order to better provide event-driven services.

System requirements:

- 64-bit operating system, Linux/Unix/macOS is recommended
- 64-bit JDK 1.8+

<a id="eventbridge-03rocketmqeventbridgequickstart--deploy-apache-rocketmq"></a>

## Deploy Apache RocketMQ

Apache RocketMQ is a great message service and we choose it as the default storage for EventBus. You can quickly deploy it according to this manual: [Apache RocketMQ Quick Start](https://rocketmq.apache.org/docs/quick-start/)

<a id="eventbridge-03rocketmqeventbridgequickstart--deploy-apache-rocketmq-connect"></a>

## Deploy Apache RocketMQ Connect

We use Apache RocketMQ Connect as our default runtime to connect to external upstream and downstream services. You can complete the deployment according to the manual: [RocketMQ Connect Quick Start](https://github.com/apache/rocketmq-connect). Before deploying Apache RocketMQ Connect, you should download the following plugins and put them in the directory defined by the "pluginPaths" configuration parameter in rocketmq-connect.

- [rocketmq-connect-eventbridge-jar-with-dependencies.jar](assets/files/rocketmq-connect-eventbridge-0-0-1-snapshot-jar-with-dependencies_afbcb836e7b1fe20.jar)
- [rocketmq-connect-dingtalk-jar-with-dependencies.jar](assets/files/rocketmq-connect-dingtalk-1-0-snapshot-jar-with-dependencies_16c194f83547f64d.jar)
- [connect-cloudevent-transform-jar-with-dependencies.jar](assets/files/connect-cloudevent-transform-1-0-0-snapshot-jar-with-dependencies_fc2e9690d70faf49.jar)
- [connect-filter-transform-jar-with-dependencies.jar](assets/files/connect-filter-transform-1-0-0-snapshot-jar-with-dependencies_efc32f9e9c75908a.jar)
- [connect-eventbridge-transform-jar-with-dependencies.jar](assets/files/connect-eventbridge-transform-1-0-0-snapshot-jar-with-dependencies_d6e1614b5e8b3812.jar)

<a id="eventbridge-03rocketmqeventbridgequickstart--deploy-rocketmq-eventbridge"></a>

## Deploy RocketMQ EventBridge

- Download EventBridge

  You can download the binary package of EventBridge from [here](https://www.apache.org/dyn/closer.cgi?path=rocketmq/rocketmq-eventbridge/1.0.0/rocketmq-eventbridge-1.0.0-bin-release.zip) : rocketmq-eventbridge-xxx-bin-release.zip. After downloading, unzip it and you will get a directory as follows:


```text
/rocketmq-eventbridge-xxx-bin-release/
|——bin
|   |——runserver.sh
|   |——eventbridge.sh
|——config
|   |——application.properties
|——jar
|   |——rocketmq-eventbridge.jar
```

- Configuring EventBridge

  Before running, we need to configure the runtime environment for EventBridge by modifying the config/application.properties file, as follows：


```text
# Mysql database address
spring.datasource.url=jdbc:mysql://xxxx:3306/xxxx?characterEncoding=utf8
spring.datasource.username=xxx
spring.datasource.password=xxxx

# RocketMQ nameserver address
rocketmq.namesrvAddr=xxxxx:9876

# RocketMQ cluster name
rocketmq.cluster.name=DefaultCluster

# RocketMQ Connect address
rocketmq.connect.endpoint=xxxxxx:8082

# log default configuration
log.path=～
log.level=INFO
app.name=rocketmq-eventbridge
```

- Start EventBridge


```shell
sh bin/eventbridge.sh start
```

  The log directory by default is located at ~ /rocketmq-eventbridge/rocketmq-eventbridge.log, it can be modified by changing the log.path and app.name. The log can be used to check if the service has started properly.：
  ![img.png](assets/images/started-284e7a8c9a25eecdff4498d093654fac_77c58d17cd976cac.png)
- Test EventBridge

Once the service is started, we can use the following demo cases to test and verify EventBridge.

<a id="eventbridge-03rocketmqeventbridgequickstart--demo"></a>

## Demo

- Create Event Bus


```text
POST /bus/createEventBus HTTP/1.1
Host: demo.eventbridge.com
Content-Type: application/json; charset=utf-8
{
"eventBusName":"demo-bus",
"description":"a demo bus."
}
```

- Create Source Event


```text
POST /source/createEventSource HTTP/1.1
Host: demo.eventbridge.com
Content-Type: application/json; charset=utf-8
{
"eventBusName":"demo-bus",
"eventSourceName":"demo-source",
"description":"A demo source."
}
```

- Create Event Rules


```text
POST /rule/createEventRule HTTP/1.1
Host: demo.eventbridge.com
Content-Type: application/json; charset=utf-8
{
  "eventBusName":"demo-bus",
  "eventRuleName":"demo-rule",
  "description":"A demo rule.",
  "filterPattern":"{}"
}
```

- Create Event Target

  Create an event target that delivers to EventBridge in the cloud.


```text
POST /target/createEventTargets HTTP/1.1
Host: demo.eventbridge.com
Content-Type: application/json; charset=utf-8
{
    "eventBusName":"demo-bus",
    "eventRuleName":"demo-rule",
    "eventTargets":[
            {
            "eventTargetName":"eventbridge-target",
            "className":"acs.eventbridge",
                "config":{
                "RegionId":"cn-hangzhou",
                "AliyunEventBus":"rocketmq-eventbridge"
                }
            }
        ]
}
```

  Creating an event target that delivers notifications to a DingTalk robot：


```text
POST /target/createEventTargets HTTP/1.1
Host: demo.eventbridge.com
Content-Type: application/json; charset=utf-8
{
    "eventBusName":"demo-bus",
    "eventRuleName":"demo-rule",
    "eventTargets":[
        {
            "eventTargetName":"dingtalk-target",
            "className":"acs.dingtalk",
            "config":{
            "WebHook":"https://oapi.dingtalk.com/robot/send?access_token=b43a54b702314415c2acdae97eda1e092528b7a9dddb31510a5b4430be2ef867",
            "SecretKey":"SEC53483bf496b8f9e0b4ab0ab669d422208e6ccfaedfd5120ea6b8426b9ecd47aa",
            "Body":"{\"template\":\"{\\\"text\\\":{\\\"content\\\":\\\"${content}\\\"},\\\"msgtype\\\":\\\"text\\\"}\",\"form\":\"TEMPLATE\",\"value\":\"{\\\"content\\\":\\\"$.data.body\\\"}\"}"
            }
        }
    ]
}
```

- Send Event to EventBus

  Finally, we will send an event through the API and verify if the Target endpoint receives the corresponding event as expected.


```text
POST /putEvents HTTP/1.1
Host: demo.eventbridge.com
Content-Type:"application/cloudevents+json; charset=UTF-8"
{
  "specversion" : "1.0",
  "type" : "com.github.pull_request.opened",
  "source" : "https://github.com/cloudevents/spec/pull",
  "subject" : "123",
  "id" : "A234-1234-1234",
  "time" : "2018-04-05T17:31:00Z",
  "datacontenttype" : "application/json",
  "data" : {
    "body":"demo"
  },
  "aliyuneventbusname":"demo-bus"
}
```

- [Deploy Apache RocketMQ](#eventbridge-03rocketmqeventbridgequickstart--deploy-apache-rocketmq)
- [Deploy Apache RocketMQ Connect](#eventbridge-03rocketmqeventbridgequickstart--deploy-apache-rocketmq-connect)
- [Deploy RocketMQ EventBridge](#eventbridge-03rocketmqeventbridgequickstart--deploy-rocketmq-eventbridge)
- [Demo](#eventbridge-03rocketmqeventbridgequickstart--demo)

---

<a id="mqtt-01rocketmqmqttoverview"></a>

<!-- source_url: https://rocketmq.apache.org/docs/mqtt/01RocketMQMQTTOverview/ -->

<!-- page_index: 47 -->

# RocketMQ MQTT Overview

Version: 5.0

# RocketMQ MQTT Overview

The traditional message queue MQ is mainly used for message communication between services (ends), such as transaction messages, payment messages, logistics messages, etc. in the e-commerce field. However, under the general category of messages, there is another very important and common message field, that is, IoT terminal device messages. In recent years, we have seen the explosive growth of IoT device-oriented news arising from smart home and industrial interconnection, and the news on the mobile APP side of the mobile Internet, which has been developed for more than ten years, is still orders of magnitude huge. The order of magnitude of messages for terminal devices is many orders of magnitude larger than that of traditional servers and is still growing rapidly.

If there is a unified message system (product) to provide multi-scenario computing (such as stream, event) and multi-scenario (IoT, APP) access, it is actually very valuable, because messages are also important data. There is only one system, which can minimize storage costs and effectively avoid the consistency problems and challenges caused by data synchronization between different systems.

![image](assets/images/eone-9371a21bf82b3b3af8b90dd1a703a851_7af2c27291f5b648.png)

Based on this, we introduced the RocketMQ-MQTT extension project to realize RocketMQ's unified access to the messages of IoT devices and servers, and provide integrated message storage and intercommunication capabilities.

<a id="mqtt-01rocketmqmqttoverview--mqtt-protocol-introduction"></a>

## MQTT Protocol Introduction

In IoT terminal scenarios, the MQTT protocol is widely adopted across the industry. MQTT originated in IoT contexts as a lightweight message transport protocol based on the publish/subscribe (Pub/Sub) model, specifically designed for low-bandwidth and unreliable network environments. It was originally developed by IBM and is now maintained as an open standard by the OASIS consortium. MQTT is extensively used in IoT, smart hardware, vehicle networking, smart cities, telemedicine, power, oil & energy, and other domains.

Its core communication model is also Pub/Sub—similar to RocketMQ. But it provides greater flexibility in subscription patterns, supporting multi-level topic subscriptions (e.g., `/t/t1/t2`) and wildcard subscriptions (e.g., `/t/t1/+`). With MQTT, you can easily implement message broadcasting, multicasting, and unicasting.

<a id="mqtt-01rocketmqmqttoverview--rocketmq-mqtt-architecture-design"></a>

## RocketMQ MQTT Architecture Design

The goal of the RocketMQ MQTT architecture is to achieve unified management of message storage and distribution while enabling multi-protocol integration without intruding into the core logic of the RocketMQ broker. To this end, we have designed two fundamental models: the queue storage model and the push-pull model.

<a id="mqtt-01rocketmqmqttoverview--queue-storage-model"></a>

### Queue Storage Model

![image](assets/images/cq-0346fd04c437e267721dca190f30c49d_83b2b2afe317e6ef.png)

We have designed a topic queue model for multi-dimensional distribution. As shown in the figure above, messages can come from various access scenarios (such as MQ/AMQP on the server side and MQTT on the client side), but only one copy will be written and stored in the commitlog, and then Distribute the queue index (ConsumerQueue) of multiple demand scenarios. For example, the server-side scenario (MQ/AMQP) can perform traditional server-side consumption according to the first-level Topic queue, and the client-side MQTT scenario can consume according to MQTT multi-level Topic and wildcard subscription.

Such a queue model can support the access and message sending and receiving of the server and terminal scenarios at the same time, achieving the goal of integration.

<a id="mqtt-01rocketmqmqttoverview--push-pull-model"></a>

### Push-Pull Model

![image](assets/images/epushpull-680e9c01bf450138c834983c671e1c81_13020e30b837c438.png)

The above figure shows a push-pull model. The P node in the figure is a protocol gateway or broker plug-in, and the terminal device is connected to the gateway node through the MQTT protocol. Messages can be sent from a variety of scenarios (MQ/AMQP/MQTT). After being stored in the Topic queue, there will be a notify logic module to sense the arrival of the new message in real time, and then a message event (that is, the topic name of the message) will be generated. The event is pushed to the gateway node, and the gateway node performs internal matching according to the subscription status of the connected terminal devices, finds which terminal devices can be matched, and then triggers a pull request to the storage layer to read the message and push it to the terminal device.

<a id="mqtt-01rocketmqmqttoverview--architecture-overview"></a>

## Architecture Overview

![image](assets/images/earch-0625e2c129ed2b9b453abcdfa9998f90_c4f41725a3438ee8.png)
Our goal is to achieve an integrated and self-closed loop based on RocketMQ, but we don't want Broker to be invaded into more scenario logic. We abstract a protocol computing layer, which can be a gateway or a broker plug-in. Broker focuses on solving Queue issues and doing some Queue storage adaptation or transformation to meet the above computing needs. The protocol computing layer is responsible for protocol access and must be pluggable and deployed.

- [MQTT Protocol Introduction](#mqtt-01rocketmqmqttoverview--mqtt-protocol-introduction)
- [RocketMQ MQTT Architecture Design](#mqtt-01rocketmqmqttoverview--rocketmq-mqtt-architecture-design)
  - [Queue Storage Model](#mqtt-01rocketmqmqttoverview--queue-storage-model)
  - [Push-Pull Model](#mqtt-01rocketmqmqttoverview--push-pull-model)
- [Architecture Overview](#mqtt-01rocketmqmqttoverview--architecture-overview)

---

<a id="mqtt-02rocketmqmqttquickstart"></a>

<!-- source_url: https://rocketmq.apache.org/docs/mqtt/02RocketMQMQTTQuickStart/ -->

<!-- page_index: 48 -->

# RocketMQ MQTT QuickStart

Version: 5.0

# RocketMQ MQTT QuickStart

<a id="mqtt-02rocketmqmqttquickstart--system-requirements"></a>

## System Requirements

- 64-bit operating system, Linux/Unix/macOS recommended
- 64-bit JDK 1.8+

<a id="mqtt-02rocketmqmqttquickstart--deployment-instructions"></a>

## Deployment Instructions

Since the RocketMQ-MQTT project relies on the underlying multi-queue distribution of RocketMQ, RocketMQ supports this feature from version 4.9.3, so you need to confirm that the version of RocketMQ is upgraded to 4.9.3 or later, and ensure that the following configuration items are enabled:

```text
enableLmq = true
enableMultiDispatch = true
```

For the deployment of RocketMQ-MQTT, refer to the project description, download the project release version or build it directly from the source code.

```text
git clone https://github.com/apache/rocketmq-mqtt
cd rocketmq-mqtt
mvn -Prelease-all -DskipTests clean install -U
cd distribution/target/
```

After the source code is built, edit conf/service.conf to complete the MQTT related configuration, as follows

```text
username=xxx    // Authorization verification account configuration
secretKey=xxx    // Authorization verification account configuration
NAMESRV_ADDR=xxx  //namesrv access point
eventNotifyRetryTopic=xx   //notify retry topic, created in advance
clientRetryTopic=xx  //Client message retry topic, created in advance
```

Other launch configuration and pre-step reference projects [README.md](https://github.com/apache/rocketmq-mqtt/blob/main/README.md)

Finally start the meta service and then the mqtt broker. Go to the distribution/target/bin directory and start the process.

```text
sh meta.sh start
sh mqtt.sh start
```

<a id="mqtt-02rocketmqmqttquickstart--example-description"></a>

## Example Description

The basic code is provided in the project engineering code, see the code [example](https://github.com/apache/rocketmq-mqtt/tree/main/mqtt-example)

```text
MqttConsumer.java  // MQTT client initiates subscription message
MqttProducer.java   // MQTT client starts publishing messages
RocketMQConsumer.java // RocketMQ client starts subscription message
RocketMQProducer.java  // RocketMQ client starts publishing messages
```

- [System Requirements](#mqtt-02rocketmqmqttquickstart--system-requirements)
- [Deployment Instructions](#mqtt-02rocketmqmqttquickstart--deployment-instructions)
- [Example Description](#mqtt-02rocketmqmqttquickstart--example-description)

---

<a id="connect-01rocketmq-connect-overview"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/01RocketMQ%20Connect%20Overview/ -->

<!-- page_index: 49 -->

# RocketMQ Connect Overview

Version: 5.0

# RocketMQ Connect Overview

RocketMQ Connect is an important component of RocketMQ data integration, which can transfer data in and out of RocketMQ from various systems efficiently and reliably. It is a separate, distributed, scalable, and fault-tolerant system that has low latency, high reliability, high performance, low code, and strong scalability. It can achieve various heterogeneous data system connections, data pipeline building, ETL, CDC, and data lake capabilities.

![RocketMQ Connect Overview](assets/images/overview-195cf6b6249dc8488e721970527cc533_7dd4a3608050fc58.png)

<a id="connect-01rocketmq-connect-overview--connector-working-principle"></a>

### Connector working principle

RocketMQ Connect is a standalone, distributed, scalable, and fault-tolerant system that mainly provides RocketMQ with the ability to flow data in and out of various external systems. Users do not need programming, they only need simple configuration to use RocketMQ Connect, such as synchronizing data from MySQL to RocketMQ, only need to configure the account password, connection address, and the need to synchronize the database and table name.

<a id="connect-01rocketmq-connect-overview--connector-use-cases"></a>

### Connector use cases

**Building a streaming data pipeline**

![RocketMQ Connect使用场景](assets/images/scene-3406354e6f18c416f4676634945f8fdd_3823f58c9b57a2fb.png)

In business systems, MySQL's excellent transaction support is used to handle data addition, deletion, and modification, ElasticSearch and Solr are used to achieve powerful search capabilities, or the generated business data is synchronized to the data analysis system and data lake (such as Hudi) for further processing, thus making the data generate higher value. Using RocketMQ Connect, it is easy to realize such data pipeline capabilities. Only three tasks need to be configured: the first task is to get data from MySQL, the second and third tasks are to consume data from RocketMQ to ElasticSearch and Hudi. Configuring these three tasks has realized two data pipelines from MySQL to ElasticSearch and MySQL to Hudi, which can not only meet the needs of transactions in business but also the needs of search, and also can construct a data lake.

<a id="connect-01rocketmq-connect-overview--cdc"></a>

##### CDC

CDC, as one of the ETL patterns, can capture the database's INSERT, UPDATE, DELETE changes in near real-time, RocketMQ Connect flow data transmission, with high availability and low latency characteristics, through connector easily realize CDC.

<a id="connect-01rocketmq-connect-overview--connector-deployment"></a>

### Connector deployment

When creating a Connector, it is generally completed through configuration. Connector generally includes the logical Connector and the Task that performs data replication, which is the physical thread, as shown in the following figure, two Connector connectors and their corresponding running Task tasks.

![RocketMQ Connect任务模型1](data:image/png;base64,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)

A Connector can also run multiple tasks at the same time to increase the parallelism of the Connector. For example, the Hudi Sink Connector in the figure below has 2 tasks, each task handles different shard data, thus increasing the parallelism of the Connector and improving processing performance.

![RocketMQ Connect任务模型2](data:image/png;base64,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)

RocketMQ Connect Worker supports two running modes, cluster and single-machine. In cluster mode, as the name implies, there are multiple Worker nodes, it is recommended to have at least 2 Worker nodes to form a highly available cluster. Cluster configuration information, offset information, and status information are stored in a specified RocketMQ Topic. A new Worker node will also obtain these configuration, offset, and status information and trigger load balancing to re-allocate tasks in the cluster to achieve a balanced state, and reduce the number of Worker nodes or when a Worker node goes down, it will also trigger load balancing to ensure that all tasks in the cluster can run normally on the surviving nodes of the cluster.

![RocketMQ Connect部署模型集群](assets/images/deploy3-879eb285035b5f869646a5707885d874_28c3d05b63b57462.png)

In standalone mode, Connector tasks run on a single machine and Worker itself does not have high availability, task offset information is persisted locally. It is suitable for scenarios where there is no high availability requirement or does not require Worker to ensure high availability, such as deployment in K8s clusters, which are guaranteed by K8s clusters.

![RocketMQ Connect部署模型单机](data:image/png;base64,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)

- [Connector working principle](#connect-01rocketmq-connect-overview--connector-working-principle)
- [Connector use cases](#connect-01rocketmq-connect-overview--connector-use-cases)
- [Connector deployment](#connect-01rocketmq-connect-overview--connector-deployment)

---

<a id="connect-02rocketmq-connect-concept"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/02RocketMQ%20Connect%20Concept/ -->

<!-- page_index: 50 -->

# RocketMQ Connect Concept

Version: 5.0

# RocketMQ Connect Concept

<a id="connect-02rocketmq-connect-concept--connector"></a>

## Connector

The connector defines where the data is copied from and where it is copied to. It reads data from the source system and writes it to RocketMQ, which is the SourceConnector, or reads data from RocketMQ and writes it to the target system, which is the SinkConnector. The Connector decides the number of tasks to be created, and receives configuration from the Worker and passes it to the task.

<a id="connect-02rocketmq-connect-concept--task"></a>

## Task

Task is the minimum allocation unit of Connector task sharding, which is responsible for actually copying the source data to RocketMQ (SourceTask), or reading data from RocketMQ and writing it to the target system (SinkTask). Tasks are stateless, and can be started and stopped dynamically. Multiple tasks can be executed in parallel, and the parallelism of data copying by the Connector is mainly reflected in the number of tasks.

![RocketMQ Basic Model](assets/images/connector-task-concept-2b559eafc66fb942242d970224426270_6dc34e6cf3cd3c54.png)

Through Connect's API, you can also see the responsibilities of Connector and Task, Connector has determined the data copy flow when it is implemented, Connector receives data source related configuration, taskClass obtains the type of task to be created, and taskConfigs specifies the maximum number of tasks, and allocates configuration for tasks. After task gets the configuration, it reads data from the data source and writes it to the target storage.

From the following two diagrams, it is clear to see the basic flow of processing for Connector and Task.

![RocketMQ Basic Model](assets/images/connector-task-process-deec60b757a7689d932d86e7cfcadfaa_1993ad5af2adeefd.png)

<a id="connect-02rocketmq-connect-concept--worker"></a>

## Worker

The worker process is the running environment for Connector and Task, it provides RESTful capabilities, accepts HTTP requests, and passes the obtained configuration to Connector and Task. In addition, it is responsible for starting Connector and Task, saving Connector configuration information, saving the position information of Task's synchronized data, and load balancing capability. High availability, scaling and fault handling of Connect clusters mainly rely on the load balancing capability of Worker.

![RocketMQ Basic Model](assets/images/worker-d578aa53e7f0d91e6448ddc0fa1478e3_8ba566d92ff5f4c7.png)

From the above diagram, it can be seen that the Worker receives http requests through the provided REST API, and passes the received configuration information to the configuration management service. The configuration management service saves the configuration locally and synchronizes it with other worker nodes, while also triggering load balancing.

- [Connector](#connect-02rocketmq-connect-concept--connector)
- [Task](#connect-02rocketmq-connect-concept--task)
- [Worker](#connect-02rocketmq-connect-concept--worker)

---

<a id="connect-03rocketmq-connect-quick-start"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/03RocketMQ%20Connect%20Quick%20Start/ -->

<!-- page_index: 51 -->

# RocketMQ Connect Quick Start

Version: 5.0

# RocketMQ Connect Quick Start

# Quick Start

This tutorial will start a RocketMQ Connector example project "rocketmq-connect-sample" in standalone mode to help you understand the working principle of connectors.
The example project provides a source connector that reads data from source files and sends it to the RocketMQ cluster.
It also provides a sink connector that reads messages from the RocketMQ cluster and writes them to destination files.

<a id="connect-03rocketmq-connect-quick-start--1-preparation-start-rocketmq"></a>

## 1. Preparation: Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start RocketMQ. Either [RocketMQ 4.x](https://rocketmq.apache.org/docs/4.x/) or
   [RocketMQ 5.x](#quickstart-01quickstart) 5.x version can be used;
5. Test RocketMQ message sending and receiving using the tool.

Here, use the environment variable NAMESRV\_ADDR to inform the tool client of the NameServer address of RocketMQ as localhost:9876.

```shell
#$ cd distribution/target/rocketmq-4.9.7/rocketmq-4.9.7
$ cd distribution/target/rocketmq-5.1.4/rocketmq-5.1.4

$ export NAMESRV_ADDR=localhost:9876
$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer SendResult [sendStatus=SEND_OK, msgId= ...

$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer ConsumeMessageThread_%d Receive New Messages: [MessageExt...
```

**Note**: RocketMQ has the feature of automatically creating Topic and Group. When sending or subscribing to messages, if the corresponding Topic or Group does not exist, RocketMQ will automatically create them. Therefore, there is no need to create Topic and Group in advance.

<a id="connect-03rocketmq-connect-quick-start--2-build-connector-runtime"></a>

## 2. Build Connector Runtime

```shell
git clone https://github.com/apache/rocketmq-connect.git

cd  rocketmq-connect

export RMQ_CONNECT_HOME=`pwd`

mvn -Prelease-connect -Dmaven.test.skip=true clean install -U
```

**Note**: The project already includes the code for rocketmq-connect-sample by default, so there is no need to build the rocketmq-connect-sample plugin separately.

<a id="connect-03rocketmq-connect-quick-start--3-run-connector-worker-in-standalone-mode"></a>

## 3. Run Connector Worker in Standalone Mode

<a id="connect-03rocketmq-connect-quick-start--modify-configuration"></a>

### Modify Configuration

Modify the `connect-standalone.conf` file to configure the RocketMQ connection
address and other information. Please refer to [9. Configuration File Instructions](#connect-03rocketmq-connect-quick-start--9-configuration-file-instructions) for details.

```text
cd $RMQ_CONNECT_HOME/distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

vim conf/connect-standalone.conf
```

In standalone mode, RocketMQ Connect persists the synchronization checkpoint information
to the local file directory storePathRootDir.

> storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

If you want to reset the synchronization checkpoint, you need to delete the persisted
checkpoint file.

```shell
rm -rf /Users/YourUsername/rocketmqconnect/storeRoot/*
```

<a id="connect-03rocketmq-connect-quick-start--start-connector-worker-in-standalone-mode"></a>

### Start Connector Worker in Standalone Mode

```shell
sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

**tips**: You can modify `docker/connect/bin/runconnect.sh` to adjust JVM startup
parameters as needed.

> JAVA\_OPT="${JAVA\_OPT} -server -Xms256m -Xmx256m"

To view the startup log file:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

If the runtime starts successfully, you will see the following print in the log file:

> The standalone worker boot success.

To exit the log tracking mode of `tail -f` command, you can press the `Ctrl + C` key combination.

<a id="connect-03rocketmq-connect-quick-start--4-start-source-connector"></a>

## 4. Start Source Connector

<a id="connect-03rocketmq-connect-quick-start--create-source-file-and-write-test-data"></a>

### Create Source File and Write Test Data

```shell
mkdir -p /Users/YourUsername/rocketmqconnect/
cd /Users/YourUsername/rocketmqconnect/
touch test-source-file.txt

echo "Hello \r\nRocketMQ\r\n Connect" >> test-source-file.txt
```

**Note**: There should be no empty lines (the demo program will throw an error if it
encounters empty lines). The source connector will continuously read the source file
and convert each line of data into a message body to be sent to RocketMQ for consumption
by the sink connector.

<a id="connect-03rocketmq-connect-quick-start--start-source-connector"></a>

### Start Source Connector

```shell
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/fileSourceConnector -d '{
    "connector.class": "org.apache.rocketmq.connect.file.FileSourceConnector",
    "filename": "/Users/YourUsername/rocketmqconnect/test-source-file.txt",
    "connect.topicname": "fileTopic"
}'
```

If the curl request returns status 200, it indicates successful creation. Example response:

> {"status":200,"body":{"connector.class":"org.apache.rocketmq.connect.file.FileSourceConnector","filename":"/Users/YourUsername/rocketmqconnect/test-source-file.txt","connect.topicname":"fileTopic"}}

View the log file:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

If you see the following log, it means the file source connector has started successfully:

> Start connector fileSourceConnector and set target state STARTED successed!!

<a id="connect-03rocketmq-connect-quick-start--source-connector-configuration-instructions"></a>

#### Source Connector Configuration Instructions

<table><thead><tr><th>key</th><th>nullable</th><th>default</th><th>description</th></tr></thead><tbody><tr><td>connector.class</td><td>false</td><td></td><td>The class name (including the package name) that implements the Connector interface</td></tr><tr><td>filename</td><td>false</td><td></td><td>The name of the source file (recommended to use absolute path)</td></tr><tr><td>connect.topicname</td><td>false</td><td></td><td>Topic required for synchronizing file data</td></tr></tbody></table>
<a id="connect-03rocketmq-connect-quick-start--5-start-sink-connector"></a>

## 5. Start sink connector

```shell
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/fileSinkConnector -d '{
    "connector.class": "org.apache.rocketmq.connect.file.FileSinkConnector",
    "filename": "/Users/YourUsername/rocketmqconnect/test-sink-file.txt",
    "connect.topicnames": "fileTopic"
}'
```

If the curl request returns status 200, it indicates successful creation. Example response:

> {"status":200,"body":{"connector.class":"org.apache.rocketmq.connect.file.FileSinkConnector","filename":"/Users/YourUsername/rocketmqconnect/test-sink-file.txt","connect.topicnames":"fileTopic"}}

View the log file:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

If you see the following log, it means the file sink connector has started successfully:

> Start connector fileSinkConnector and set target state STARTED successed!!

Check if the sink connector has written data to the destination file:

```shell
cat /Users/YourUsername/rocketmqconnect/test-sink-file.txt
```

If the test-sink-file.txt file is generated and its content is the same as the
test-source-file.txt, it means the entire process is running correctly.

Continue writing test data to the source file test-source-file.txt:

```shell
cd /Users/YourUsername/rocketmqconnect/

echo "Say Hi to\r\nRMQ Connector\r\nAgain" >> test-source-file.txt

# Wait a few seconds, check if rocketmq-connect replicate data to sink file succeed sleep 10 cat /Users/YourUsername/rocketmqconnect/test-sink-file.txt
```

**Note**: The order of file contents may vary because the `rocketmq-connect-sample` uses `normal message` when
sending and receiving messages to/from a RocketMQ topic. This is different from `ordered message`, and consuming
`normal messages` does not guarantee the order.

<a id="connect-03rocketmq-connect-quick-start--sink-connector-configuration-instructions"></a>

#### sink connector configuration instructions

<table><thead><tr><th>key</th><th>nullable</th><th>default</th><th>description</th></tr></thead><tbody><tr><td>connector.class</td><td>false</td><td></td><td>The class name (including the package name) that implements the Connector interface</td></tr><tr><td>filename</td><td>false</td><td></td><td>The sink pulls data and saves it to a file(recommended to use absolute path)</td></tr><tr><td>connect.topicnames</td><td>false</td><td></td><td>The topics of the data messages that the sink needs to process</td></tr></tbody></table>

**Tips**：The configuration file instructions for the sample rocketmq-connect-sample are for reference only, different source/sink connectors have different configurations, please refer to the specific source/sink connector.

<a id="connect-03rocketmq-connect-quick-start--6-stop-connector"></a>

## 6. Stop connector

The RESTful command format for stopping connectors is
`http://(your worker ip):(port)/connectors/(connector name)/stop`

To stop the two connectors in the demo, you can use the following commands:

```shell
curl http://127.0.0.1:8082/connectors/fileSinkConnector/stop
curl http://127.0.0.1:8082/connectors/fileSourceConnector/stop
```

If the curl request returns a status of 200, it indicates successful stopping of the connectors.
Example response:

> {"status":200,"body":"Connector [fileSinkConnector] deleted successfully"}

If you see the following log message, it means the file sink connector has been
successfully shut down:

```shell
tail -100f ~/logs/rocketmqconnect/connect_default.log
```

> Completed shutdown for connectorName:fileSinkConnector

<a id="connect-03rocketmq-connect-quick-start--7-stop-the-worker-process"></a>

## 7. Stop the Worker process

```shell
cd $RMQ_CONNECT_HOME/distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT
sh bin/connectshutdown.sh
```

<a id="connect-03rocketmq-connect-quick-start--8-log-directory"></a>

## 8. Log directory

You can use the following commands to view the log directory:

```shell
ls $HOME/logs/rocketmqconnect
ls ~/logs/rocketmqconnect
```

<a id="connect-03rocketmq-connect-quick-start--9-configuration-file-instructions"></a>

## 9. Configuration File Instructions

Modify the RESTful port, storeRoot path, Nameserver address, and other information based on your usage.

Here is an example of a configuration file:

```shell
#current cluster node uniquely identifies
workerId=DEFAULT_WORKER_1

# Http prot for user to access REST API httpPort=8082

# Local file dir for config store storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

#You need to modify it to your own rocketmq nameserver endpoint.
# RocketMQ namesrvAddr namesrvAddr=127.0.0.1:9876

# Plugin path for loading Source/Sink Connectors
# The rocketmq-connect project already includes the rocketmq-connect-sample module by default, so no configuration is needed here. pluginPaths=
```

Explanation of storePathRootDir configuration:

In standalone mode, RocketMQ Connect persists the synchronization checkpoint information
to the local file directory specified by storePathRootDir. The persistent files include:

<table><thead><tr><th>key</th><th>description</th></tr></thead><tbody><tr><td>connectorConfig.json</td><td>Connector configuration persistence files</td></tr><tr><td>position.json</td><td>Source connect data processing progress persistence files</td></tr><tr><td>taskConfig.json</td><td>Task configuration persistence files</td></tr><tr><td>offset.json</td><td>Sink connect data consumption progress persistence files</td></tr><tr><td>connectorStatus.json</td><td>Connector status persistence files</td></tr><tr><td>taskStatus.json</td><td>Task status persistence files</td></tr></tbody></table>

- [1. Preparation: Start RocketMQ](#connect-03rocketmq-connect-quick-start--1-preparation-start-rocketmq)
- [2. Build Connector Runtime](#connect-03rocketmq-connect-quick-start--2-build-connector-runtime)
- [3. Run Connector Worker in Standalone Mode](#connect-03rocketmq-connect-quick-start--3-run-connector-worker-in-standalone-mode)
  - [Modify Configuration](#connect-03rocketmq-connect-quick-start--modify-configuration)
  - [Start Connector Worker in Standalone Mode](#connect-03rocketmq-connect-quick-start--start-connector-worker-in-standalone-mode)
- [4. Start Source Connector](#connect-03rocketmq-connect-quick-start--4-start-source-connector)
  - [Create Source File and Write Test Data](#connect-03rocketmq-connect-quick-start--create-source-file-and-write-test-data)
  - [Start Source Connector](#connect-03rocketmq-connect-quick-start--start-source-connector)
- [5. Start sink connector](#connect-03rocketmq-connect-quick-start--5-start-sink-connector)
- [6. Stop connector](#connect-03rocketmq-connect-quick-start--6-stop-connector)
- [7. Stop the Worker process](#connect-03rocketmq-connect-quick-start--7-stop-the-worker-process)
- [8. Log directory](#connect-03rocketmq-connect-quick-start--8-log-directory)
- [9. Configuration File Instructions](#connect-03rocketmq-connect-quick-start--9-configuration-file-instructions)

---

<a id="connect-04rocketmq-connect-in-action1"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/04RocketMQ%20Connect%20In%20Action1/ -->

<!-- page_index: 52 -->

# RocketMQ Connect in Action 1

Version: 5.0

# RocketMQ Connect in Action 1

MySQL Source(CDC) - >RocketMQ Connect -> MySQL Sink(JDBC)

<a id="connect-04rocketmq-connect-in-action1--preparation"></a>

## Preparation

<a id="connect-04rocketmq-connect-in-action1--start-rocketmq"></a>

### Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start [RocketMQ](https://rocketmq.apache.org/docs/quick-start/);

**tips** : ${ROCKETMQ\_HOME} locational instructions

> bin-release.zip version：/rocketmq-all-4.9.4-bin-release
>
> source-release.zip version：/rocketmq-all-4.9.4-source-release/distribution

<a id="connect-04rocketmq-connect-in-action1--start-connect"></a>

### Start Connect

<a id="connect-04rocketmq-connect-in-action1--compiling-connector-plugin"></a>

#### Compiling Connector Plugin

Debezium RocketMQ Connector

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-debezium/
$ mvn clean package -Dmaven.test.skip=true
```

Move the compiled Debezium MySQL RocketMQ Connector package into the Runtime loading directory. The command is as follows：

```shell
mkdir -p /usr/local/connector-plugins
cp rocketmq-connect-debezium-mysql/target/rocketmq-connect-debezium-mysql-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

JDBC Connector

Move the compiled JDBC Connector package into the Runtime loading directory. The command is as follows：

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-jdbc/
$ mvn clean package -Dmaven.test.skip=true
cp rocketmq-connect-jdbc/target/rocketmq-connect-jdbc-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

<a id="connect-04rocketmq-connect-in-action1--start-connect-runtime"></a>

#### Start Connect Runtime

```text
cd  rocketmq-connect

mvn -Prelease-connect -DskipTests clean install -U
```

Modify the configuration `connect-standalone.conf`, the main configuration is as follows

```shell
$ cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT
$ vim conf/connect-standalone.conf
```

```text
workerId=standalone-worker
storePathRootDir=/tmp/storeRoot

## Http port for user to access REST API
httpPort=8082

# Rocketmq namesrvAddr
namesrvAddr=localhost:9876

# RocketMQ acl
aclEnable=false
accessKey=rocketmq
secretKey=12345678

autoCreateGroupEnable=false
clusterName="DefaultCluster"

# Core configuration, configure the plugin directory of the previously compiled debezium package here
# Source or sink connector jar file dir,The default value is rocketmq-connect-sample
pluginPaths=/usr/local/connector-plugins
```

```text
cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

<a id="connect-04rocketmq-connect-in-action1--mysql-image"></a>

### MySQL image

Use debezium's MySQL docker environment to set up the MySQL database

```text
docker run -it --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw quay.io/debezium/example-mysql:1.9
```

MySQL information

Port：3306

Account：root/debezium

slave:debezium/dbz

<a id="connect-04rocketmq-connect-in-action1--test-data"></a>

### Test data

Log in to the database with the root/debezium account

Source database table：inventory.employee

```text
CREATE database inventory;

use inventory;
CREATE TABLE `employee` (
`id` bigint NOT NULL AUTO_INCREMENT,
`name` varchar(128) DEFAULT NULL,
`howold` int DEFAULT NULL,
`male` int DEFAULT NULL,
`company` varchar(128) DEFAULT NULL,
`money` double DEFAULT NULL,
`begin_time` datetime DEFAULT NULL,
`modify_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'modify time',
`decimal_test` decimal(11,2) DEFAULT NULL COMMENT 'test decimal type',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;



INSERT INTO `employee` VALUES (1, 'name-01', 24, 6, 'company', 9987, '2021-12-22 08:00:00', '2022-06-14 18:20:11', 321.11);
INSERT INTO `employee` VALUES (2, 'name-02', 19, 7, 'company', 32232, '2021-12-29 08:00:00', '2022-06-14 18:18:47', 77.12);
INSERT INTO `employee` VALUES (8, 'name-03', 20, 1, NULL, 0, NULL, '2022-06-14 18:26:05', 11111.00);
INSERT INTO `employee` VALUES (9, 'name-04', 21, 1, 'company', 12345, '2021-12-24 20:44:10', '2022-06-14 18:20:02', 123.12);
INSERT INTO `employee` VALUES (11, 'name-05', 50, 2, 'company', 33333, '2021-12-24 22:14:52', '2022-06-14 18:19:58', 123.12);
INSERT INTO `employee` VALUES (12, 'name-06', 19, 3, NULL, 0, NULL, '2022-06-14 18:26:12', 111233.00);
INSERT INTO `employee` VALUES (13, 'name-07', 20, 4, 'company', 3237, '2021-12-29 01:31:03', '2022-06-14 18:19:27', 52.00);
INSERT INTO `employee` VALUES (14, 'name-08', 25, 15, 'company', 32255, '2022-02-08 19:06:39', '2022-06-14 18:18:32', 0.00);
INSERT INTO `employee` VALUES (15, NULL, 0, 0, NULL, 0, NULL, '2022-06-14 20:13:29', NULL);
```

Target database：inventory\_2.employee

```text
CREATE database inventory_2;
use inventory_2;
CREATE TABLE `employee` (
`id` bigint NOT NULL AUTO_INCREMENT,
`name` varchar(128) DEFAULT NULL,
`howold` int DEFAULT NULL,
`male` int DEFAULT NULL,
`company` varchar(128) DEFAULT NULL,
`money` double DEFAULT NULL,
`begin_time` datetime DEFAULT NULL,
`modify_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
`decimal_test` decimal(11,2) DEFAULT NULL COMMENT 'test decimal type',
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
```

<a id="connect-04rocketmq-connect-in-action1--start-connector"></a>

## Start Connector

<a id="connect-04rocketmq-connect-in-action1--start-debezium-source-connector"></a>

### Start Debezium source connector

Synchronize original table data：inventory.employee
Purpose: Parse MySQL binlog and encapsulate into a generic ConnectRecord object and send to RocketMQ Topic.

```shell
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/MySQLCDCSource -d '{
"connector.class": "org.apache.rocketmq.connect.debezium.mysql.DebeziumMysqlConnector",
"max.task": "1",
"connect.topicname": "debezium-mysql-source-topic",
"kafka.transforms": "Unwrap",
"kafka.transforms.Unwrap.delete.handling.mode": "none",
"kafka.transforms.Unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
"kafka.transforms.Unwrap.add.headers": "op,source.db,source.table",
"database.history.skip.unparseable.ddl": true,
"database.history.name.srv.addr": "localhost:9876",
"database.history.rocketmq.topic": "db-history-debezium-topic",
"database.history.store.only.monitored.tables.ddl": true,
"include.schema.changes": false,
"database.server.name": "dbserver1",
"database.port": 3306,
"database.hostname": "database ip",
"database.connectionTimeZone": "UTC",
"database.user": "debezium",
"database.password": "dbz",
"table.include.list": "inventory.employee",
"max.batch.size": 50,
"database.include.list": "inventory",
"snapshot.mode": "when_needed",
"database.server.id": "184054",
"key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
"value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

<a id="connect-04rocketmq-connect-in-action1--start-jdbc-sink-connector"></a>

### Start JDBC sink connector

Purpose: Consume data from the Topic and write to the destination table through the JDBC protocol.

```shell
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/jdbcmysqlsinktest -d '{
  "connector.class": "org.apache.rocketmq.connect.jdbc.connector.JdbcSinkConnector",
  "max.task": "2",
  "connect.topicnames": "debezium-mysql-source",
  "connection.url": "jdbc:mysql://database ip:3306/inventory_2",
  "connection.user": "root",
  "connection.password": "debezium",
  "pk.fields": "id",
  "table.name.from.header": "true",
  "pk.mode": "record_key",
  "insert.mode": "UPSERT",
  "db.timezone": "UTC",
  "table.types": "TABLE",
  "errors.deadletterqueue.topic.name": "dlq-topic",
  "errors.log.enable": "true",
  "errors.tolerance": "ALL",
  "delete.enabled": "true",
  "key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
  "value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

After the above two Connector tasks are successfully created, log in to the database with the root/debezium account.

Insert, delete or update data to the source database table: inventory.employee, then the data will be synchronized to the destination table inventory\_2.employee.

- [Preparation](#connect-04rocketmq-connect-in-action1--preparation)
  - [Start RocketMQ](#connect-04rocketmq-connect-in-action1--start-rocketmq)
  - [Start Connect](#connect-04rocketmq-connect-in-action1--start-connect)
  - [MySQL image](#connect-04rocketmq-connect-in-action1--mysql-image)
  - [Test data](#connect-04rocketmq-connect-in-action1--test-data)
- [Start Connector](#connect-04rocketmq-connect-in-action1--start-connector)
  - [Start Debezium source connector](#connect-04rocketmq-connect-in-action1--start-debezium-source-connector)
  - [Start JDBC sink connector](#connect-04rocketmq-connect-in-action1--start-jdbc-sink-connector)

---

<a id="connect-05rocketmq-connect-in-action2"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/05RocketMQ%20Connect%20In%20Action2/ -->

<!-- page_index: 53 -->

# RocketMQ Connect in Action 2

Version: 5.0

# RocketMQ Connect in Action 2

PostgreSQL Source(CDC) - >RocketMQ Connect -> MySQL Sink(JDBC)

<a id="connect-05rocketmq-connect-in-action2--preparation"></a>

## Preparation

<a id="connect-05rocketmq-connect-in-action2--start-rocketmq"></a>

### Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start [RocketMQ](https://rocketmq.apache.org/docs/quick-start/);

**tips** : ${ROCKETMQ\_HOME} locational instructions

> bin-release.zip version：/rocketmq-all-4.9.4-bin-release
>
> source-release.zip version：/rocketmq-all-4.9.4-source-release/distribution

<a id="connect-05rocketmq-connect-in-action2--start-connect"></a>

### Start Connect

<a id="connect-05rocketmq-connect-in-action2--compiling-connector-plugin"></a>

#### Compiling Connector Plugin

Debezium RocketMQ Connector

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-debezium/
$ mvn clean package -Dmaven.test.skip=true
```

Move the compiled Debezium PostgreSQL RocketMQ Connector package into the Runtime loading directory. The command is as follows ：

```text
mkdir -p /usr/local/connector-plugins
cp rocketmq-connect-debezium-postgresql/target/rocketmq-connect-debezium-postgresql-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

JDBC Connector

Move the compiled JDBC Connector package into the Runtime loading directory. The command is as follows：

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-jdbc/
$ mvn clean package -Dmaven.test.skip=true
cp rocketmq-connect-jdbc/target/rocketmq-connect-jdbc-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

<a id="connect-05rocketmq-connect-in-action2--start-connect-runtime"></a>

#### Start Connect Runtime

```text
cd  rocketmq-connect

mvn -Prelease-connect -DskipTests clean install -U
```

Modify the configuration `connect-standalone.conf`, the main configuration is as follows

```shell
$ cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT
$ vim conf/connect-standalone.conf
```

```text
$ cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT
$ vim conf/connect-standalone.conf
```

```text
workerId=standalone-worker
storePathRootDir=/tmp/storeRoot

## Http port for user to access REST API
httpPort=8082

# Rocketmq namesrvAddr
namesrvAddr=localhost:9876

# RocketMQ acl
aclEnable=false
accessKey=rocketmq
secretKey=12345678

autoCreateGroupEnable=false
clusterName="DefaultCluster"

# Core configuration, configure the plugin directory of the previously compiled debezium package here
# Source or sink connector jar file dir,The default value is rocketmq-connect-sample
pluginPaths=/usr/local/connector-plugins
```

```text
cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

<a id="connect-05rocketmq-connect-in-action2--postgres-image"></a>

### Postgres image

Use debezium's Postgres docker environment to set up the Postgres database

```text
# starting a pg instance
docker run -d --name postgres -p 5432:5432 -e POSTGRES_USER=start_data_engineer -e POSTGRES_PASSWORD=password debezium/postgres:14

# bash into postgres instance
docker exec -ti postgres /bin/bash
```

Postgres information
Port：5432
Aaccount：start\_data\_engineer/password
Synchronize original database：bank.holding
Target database table：bank1.holding

<a id="connect-05rocketmq-connect-in-action2--mysql-image"></a>

### MySQL image

Use debezium's MySQL docker environment to set up the MySQL database.

```text
docker run -it --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw quay.io/debezium/example-mysql:1.9
```

MySQL information

Port：3306

Account：root/debezium

<a id="connect-05rocketmq-connect-in-action2--test-data"></a>

### Test data

Log in to the database with the start\_data\_engineer/password account

Source database table：bank.holding

```text
CREATE SCHEMA bank;
SET search_path TO bank,public;
CREATE TABLE bank.holding (
                              holding_id int,
                              user_id int,
                              holding_stock varchar(8),
                              holding_quantity int,
                              datetime_created timestamp,
                              datetime_updated timestamp,
                              primary key(holding_id)
);
ALTER TABLE bank.holding replica identity FULL;
insert into bank.holding values (1000, 1, 'VFIAX', 10, now(), now());
\q
insert into bank.holding values (1000, 1, 'VFIAX', 10, now(), now());
insert into bank.holding values (1001, 2, 'SP500', 1, now(), now());
insert into bank.holding values (1003, 3, 'SP500', 1, now(), now());
update bank.holding set holding_quantity = 300 where holding_id=1000;
```

Target database table：bank1.holding

```text
create database bank1;
CREATE TABLE holding (
                          holding_id int,
                          user_id int,
                          holding_stock varchar(8),
                          holding_quantity int,
                          datetime_created bigint,
                          datetime_updated bigint,
                          primary key(holding_id)
);
```

<a id="connect-05rocketmq-connect-in-action2--start-connector"></a>

## Start Connector

<a id="connect-05rocketmq-connect-in-action2--start-debezium-source-connector"></a>

### Start Debezium source connector

Synchronize original table data：bank.holding
Purpose: Parse Postgres binlog and encapsulate it into a common ConnectRecord object, which is sent to the RocketMQ Topic.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/postgres-connector -d  '{
  "connector.class": "org.apache.rocketmq.connect.debezium.postgres.DebeziumPostgresConnector",
  "max.task": "1",
  "connect.topicname": "debezium-postgres-source-01",
  "kafka.transforms": "Unwrap",
  "kafka.transforms.Unwrap.delete.handling.mode": "none",
  "kafka.transforms.Unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
  "kafka.transforms.Unwrap.add.headers": "op,source.db,source.table",
  "database.history.skip.unparseable.ddl": true,
  "database.server.name": "bankserver1",
  "database.port": 5432,
  "database.hostname": "database ip",
  "database.connectionTimeZone": "UTC",
  "database.user": "start_data_engineer",
  "database.dbname": "start_data_engineer",
  "database.password": "password",
  "table.whitelist": "bank.holding",
  "key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
  "value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

<a id="connect-05rocketmq-connect-in-action2--start-jdbc-sink-connector"></a>

### Start JDBC sink connector

Purpose: Consume data from the Topic and write it to the target table through JDBC protocol.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/jdbcmysqlsinktest201 -d '{
  "connector.class": "org.apache.rocketmq.connect.jdbc.connector.JdbcSinkConnector",
  "max.task": "2",
  "connect.topicnames": "debezium-postgres-source-01",
  "connection.url": "jdbc:mysql://database ip:3306/bank1",
  "connection.user": "root",
  "connection.password": "debezium",
  "pk.fields": "holding_id",
  "table.name.from.header": "true",
  "pk.mode": "record_key",
  "insert.mode": "UPSERT",
  "db.timezone": "UTC",
  "table.types": "TABLE",
  "errors.deadletterqueue.topic.name": "dlq-topic",
  "errors.log.enable": "true",
  "errors.tolerance": "ALL",
  "delete.enabled": "true",
  "key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
  "value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

After the creation of the above two Connector tasks, log in to the database using the start\_data\_engineer/password account.

Any add, delete, or modification made to the source database table `bankholding` will be synced to the target table `bank1.holding`.

- [Preparation](#connect-05rocketmq-connect-in-action2--preparation)
  - [Start RocketMQ](#connect-05rocketmq-connect-in-action2--start-rocketmq)
  - [Start Connect](#connect-05rocketmq-connect-in-action2--start-connect)
  - [Postgres image](#connect-05rocketmq-connect-in-action2--postgres-image)
  - [MySQL image](#connect-05rocketmq-connect-in-action2--mysql-image)
  - [Test data](#connect-05rocketmq-connect-in-action2--test-data)
- [Start Connector](#connect-05rocketmq-connect-in-action2--start-connector)
  - [Start Debezium source connector](#connect-05rocketmq-connect-in-action2--start-debezium-source-connector)
  - [Start JDBC sink connector](#connect-05rocketmq-connect-in-action2--start-jdbc-sink-connector)

---

<a id="connect-06rocketmq-connect-in-action3"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/06RocketMQ%20Connect%20In%20Action3/ -->

<!-- page_index: 54 -->

# RocketMQ Connect in Action 3

Version: 5.0

# RocketMQ Connect in Action 3

![RocketMQ Connect Overview](assets/images/rocketmq-connect-integration-demo-71911f69343ac89f172b014950cb12e6_4eb9a62eb6cff0f6.jpg)

<a id="connect-06rocketmq-connect-in-action3--preparation"></a>

## Preparation

<a id="connect-06rocketmq-connect-in-action3--start-rocketmq"></a>

### Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start [RocketMQ](https://rocketmq.apache.org/docs/quick-start/);

**tips** : ${ROCKETMQ\_HOME} locational instructions

> bin-release.zip version：/rocketmq-all-4.9.4-bin-release
>
> source-release.zip version：/rocketmq-all-4.9.4-source-release/distribution

<a id="connect-06rocketmq-connect-in-action3--start-connect"></a>

### Start Connect

<a id="connect-06rocketmq-connect-in-action3--compiling-connector-plugin"></a>

#### Compiling Connector Plugin

Debezium RocketMQ Connector

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-debezium/
$ mvn clean package -Dmaven.test.skip=true
```

Compile the Debezium MySQL, PostgreSQL, and RocketMQ Connector packages and place them in the Runtime loading directory. The command is as follows：

```text
mkdir -p /usr/local/connector-plugins
cp rocketmq-connect-debezium-postgresql/target/rocketmq-connect-debezium-postgresql-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins

cp rocketmq-connect-debezium-mysql/target/rocketmq-connect-debezium-mysql-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

JDBC Connector

Move the compiled JDBC Connector package into the Runtime loading directory. The command is as follows：

```text
$ cd rocketmq-connect/connectors/rocketmq-connect-jdbc/
$ mvn clean package -Dmaven.test.skip=true
cp rocketmq-connect-jdbc/target/rocketmq-connect-jdbc-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/local/connector-plugins
```

<a id="connect-06rocketmq-connect-in-action3--start-connect-runtime"></a>

#### Start Connect Runtime

```text
cd  rocketmq-connect

mvn -Prelease-connect -DskipTests clean install -U
```

Modify the configuration `connect-standalone.conf`, the main configuration is as follows

```text
$ cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT
$ vim conf/connect-standalone.conf
```

```text
workerId=standalone-worker
storePathRootDir=/tmp/storeRoot

## Http port for user to access REST API
httpPort=8082

# Rocketmq namesrvAddr
namesrvAddr=localhost:9876

# RocketMQ acl
aclEnable=false
accessKey=rocketmq
secretKey=12345678

autoCreateGroupEnable=false
clusterName="DefaultCluster"

#  Core configuration, configure the plugin directory of the previously compiled debezium package here
# Source or sink connector jar file dir,The default value is rocketmq-connect-sample
pluginPaths=/usr/local/connector-plugins
```

```text
cd distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

<a id="connect-06rocketmq-connect-in-action3--postgres-image"></a>

### Postgres image

Use debezium's Postgres docker environment to set up the Postgres database

```text
# starting a pg instance
docker run -d --name postgres -p 5432:5432 -e POSTGRES_USER=start_data_engineer -e POSTGRES_PASSWORD=password debezium/postgres:14

# bash into postgres instance
docker exec -ti postgres /bin/bash
```

Postgres information
Port：5432
Account：start\_data\_engineer/password
Synchronize the source database：bank.user

<a id="connect-06rocketmq-connect-in-action3--mysql-image"></a>

### MySQL image

Use debezium's MySQL docker environment to set up the MySQL database

```text
docker run -it --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw quay.io/debezium/example-mysql:1.9
```

```text
docker run -it --rm --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=debezium -e MYSQL_USER=mysqluser -e MYSQL_PASSWORD=mysqlpw quay.io/debezium/example-mysql:1.9
```

MySQL information

Port：3306

Account：root/debezium
Synchronize the source database：bank.user

Target database：bank1.user

<a id="connect-06rocketmq-connect-in-action3--test-data"></a>

### Test data

Login to the database using the root/debezium account

Source database table：bank.user

```text
create database bank;
use bank;

create table bank.user
(
    id       bigint NOT NULL AUTO_INCREMENT,
    user_id          integer,
    name    varchar(8),
    age integer,
    birthday date,
    datetime_created timestamp(3),
    datetime_updated timestamp(3),
    height           decimal(11, 2) null,
    PRIMARY KEY (`id`)
);

insert into bank.user values (1003, 1, 'lilei2', 10, now(), now(), now(), 1.72);
update bank.user set user_id = 1003 where id = 1003;
```

Login to the PostgreSQL database using the start\_data\_engineer/password account.

Source database table: bank.user

```text
CREATE SCHEMA bank;
SET search_path TO bank,public;
create table bank.user
(
    id       integer not null
        constraint user_pkey
            primary key,
    user_id          integer,
    name    varchar(8),
    age integer,
    birthday date,
    datetime_created timestamp(3),
    datetime_updated timestamp(3),
    height           numeric(11, 2)
);

insert into bank.user values (1001, 1, 'lilei1', 10, now(), now(), now(), 1.72);
update bank.user set user_id = 1001 where id = 1001;
```

Target database table: bank1.user

```text
create database bank1;
create table bank1.user
(
    id               bigint auto_increment
        primary key,
    user_id          int            null,
    name             varchar(8)     null,
    age              int            null,
    birthday         date           null,
    datetime_created timestamp(3)   null,
    datetime_updated timestamp(3)   null,
    height           decimal(11, 2) null
);
```

<a id="connect-06rocketmq-connect-in-action3--start-connector"></a>

## Start Connector

<a id="connect-06rocketmq-connect-in-action3--start-debezium-source-connector"></a>

### Start Debezium source connector

Synchronize the original table：bank.user
Purpose：Parse the MySQL binlog and encapsulate it into a common ConnectRecord object, sent to the RocketMQ Topic.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/MySQLCDCSource1000 -d '{
"connector.class": "org.apache.rocketmq.connect.debezium.mysql.DebeziumMysqlConnector",
"max.task": "1",
"connect.topicname": "debezium-source-topic1000",
"kafka.transforms": "Unwrap",
"kafka.transforms.Unwrap.delete.handling.mode": "none",
"kafka.transforms.Unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
"kafka.transforms.Unwrap.add.headers": "op,source.db,source.table",
"database.history.skip.unparseable.ddl": true,
"database.history.name.srv.addr": "localhost:9876",
"database.history.rocketmq.topic": "db-history-debezium-topic1000",
"database.history.store.only.monitored.tables.ddl": true,
"include.schema.changes": false,
"database.server.name": "dbserver1",
"database.port": 3306,
"database.hostname": "database ip",
"database.connectionTimeZone": "UTC",
"database.user": "debezium",
"database.password": "dbz",
"table.include.list": "bank.user",
"max.batch.size": 50,
"database.include.list": "bank",
"snapshot.mode": "when_needed",
"database.server.id": "184054",
"key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
"value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

Synchronize the original table：bank.user
Purpose: Parse the Postgres binlog and encapsulate it into a common ConnectRecord object, sent to the RocketMQ Topic.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/postgres-connector1000 -d  '{
  "connector.class": "org.apache.rocketmq.connect.debezium.postgres.DebeziumPostgresConnector",
  "max.task": "1",
  "connect.topicname": "debezium-source-topic1000",
  "kafka.transforms": "Unwrap",
  "kafka.transforms.Unwrap.delete.handling.mode": "none",
  "kafka.transforms.Unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
  "kafka.transforms.Unwrap.add.headers": "op,source.db,source.table",
  "database.history.skip.unparseable.ddl": true,
  "database.server.name": "bankserver1",
  "database.port": 5432,
  "database.hostname": "database ip",
  "database.connectionTimeZone": "UTC",
  "database.user": "start_data_engineer",
  "database.dbname": "start_data_engineer",
  "database.password": "password",
  "table.whitelist": "bank.user",
  "key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
  "value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

<a id="connect-06rocketmq-connect-in-action3--start-jdbc-sink-connector"></a>

### Start JDBC sink connector

Purpose: Consume the data in the Topic and write it to the target table through JDBC protocol.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/jdbcmysqlsinktest1000 -d '{
  "connector.class": "org.apache.rocketmq.connect.jdbc.connector.JdbcSinkConnector",
  "max.task": "2",
  "connect.topicnames": "debezium-source-topic1000",
  "connection.url": "jdbc:mysql://database ip:3306/bank1",
  "connection.user": "root",
  "connection.password": "debezium",
  "pk.fields": "id",
  "table.name.from.header": "true",
  "pk.mode": "record_key",
  "insert.mode": "UPSERT",
  "db.timezone": "UTC",
  "table.types": "TABLE",
  "errors.deadletterqueue.topic.name": "dlq-topic",
  "errors.log.enable": "true",
  "errors.tolerance": "ALL",
  "delete.enabled": "true",
  "key.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
  "value.converter": "org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

After the above three Connector tasks are created successfully, login to the PostgreSQL database using the start\_data\_engineer/password account or login to the MySQL database using the root/debezium account.

Modifying, deleting, or adding to the source database table bank.user will synchronize to the target MySQL table bank1.user.

- [Preparation](#connect-06rocketmq-connect-in-action3--preparation)
  - [Start RocketMQ](#connect-06rocketmq-connect-in-action3--start-rocketmq)
  - [Start Connect](#connect-06rocketmq-connect-in-action3--start-connect)
  - [Postgres image](#connect-06rocketmq-connect-in-action3--postgres-image)
  - [MySQL image](#connect-06rocketmq-connect-in-action3--mysql-image)
  - [Test data](#connect-06rocketmq-connect-in-action3--test-data)
- [Start Connector](#connect-06rocketmq-connect-in-action3--start-connector)
  - [Start Debezium source connector](#connect-06rocketmq-connect-in-action3--start-debezium-source-connector)
  - [Start JDBC sink connector](#connect-06rocketmq-connect-in-action3--start-jdbc-sink-connector)

---

<a id="connect-07rocketmq-connect-in-action4"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/07RocketMQ%20Connect%20In%20Action4/ -->

<!-- page_index: 55 -->

# RocketMQ Connect in Action 4

Version: 5.0

# RocketMQ Connect in Action 4

SFTP Server (File Data) -> RocketMQ Connect -> SFTP Server (File)

<a id="connect-07rocketmq-connect-in-action4--preparation"></a>

## Preparation

<a id="connect-07rocketmq-connect-in-action4--start-rocketmq"></a>

### Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start RocketMQ. Either [RocketMQ 4.x](https://rocketmq.apache.org/docs/4.x/) or
   [RocketMQ 5.x](#quickstart-01quickstart) 5.x version can be used;
5. Test RocketMQ message sending and receiving using the tool.

Here, use the environment variable NAMESRV\_ADDR to inform the tool client of the NameServer address of RocketMQ as localhost:9876.

```shell
#$ cd distribution/target/rocketmq-4.9.7/rocketmq-4.9.7
$ cd distribution/target/rocketmq-5.1.4/rocketmq-5.1.4

$ export NAMESRV_ADDR=localhost:9876
$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer SendResult [sendStatus=SEND_OK, msgId= ...

$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer ConsumeMessageThread_%d Receive New Messages: [MessageExt...
```

**Note**: RocketMQ has the feature of automatically creating Topic and Group. When sending or subscribing to messages, if the corresponding Topic or Group does not exist, RocketMQ will automatically create them. Therefore, there is no need to create Topic and Group in advance.

<a id="connect-07rocketmq-connect-in-action4--build-connector-runtime"></a>

### Build Connector Runtime

```shell
git clone https://github.com/apache/rocketmq-connect.git

cd  rocketmq-connect

export RMQ_CONNECT_HOME=`pwd`

mvn -Prelease-connect -Dmaven.test.skip=true clean install -U
```

<a id="connect-07rocketmq-connect-in-action4--build-sftp-connector-plugin"></a>

### Build SFTP Connector Plugin

```text
cd $RMQ_CONNECT_HOME/connectors/rocketmq-connect-sftp/

mvn clean package -Dmaven.test.skip=true
```

Put the compiled jar of the SFTP RocketMQ Connector into the Plugin directory for runtime loading.

```text
mkdir -p /Users/YourUsername/rocketmqconnect/connector-plugins
cp target/rocketmq-connect-sftp-0.0.1-SNAPSHOT-jar-with-dependencies.jar /Users/YourUsername/rocketmqconnect/connector-plugins
```

<a id="connect-07rocketmq-connect-in-action4--run-connector-worker-in-standalone-mode"></a>

### Run Connector Worker in Standalone Mode

Modify the `connect-standalone.conf` file to configure the RocketMQ connection
address and other information.

```text
cd $RMQ_CONNECT_HOME/distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

vim conf/connect-standalone.conf
```

Example configuration information is as follows:

```text
workerId=standalone-worker
storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

## Http port for user to access REST API
httpPort=8082

# Rocketmq namesrvAddr
namesrvAddr=localhost:9876

# RocketMQ acl
aclEnable=false
#accessKey=rocketmq
#secretKey=12345678

clusterName="DefaultCluster"

# Plugin path for loading Source/Sink Connectors
pluginPaths=/Users/YourUsername/rocketmqconnect/connector-plugins
```

In standalone mode, RocketMQ Connect persistently stores the synchronization checkpoint information
in the local file directory specified by storePathRootDir.

> storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

If you want to reset the synchronization checkpoint, you need to delete the persisted checkpoint information files.

```shell
rm -rf /Users/YourUsername/rocketmqconnect/storeRoot/*
```

To start Connector Worker in standalone mode:

```text
sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

<a id="connect-07rocketmq-connect-in-action4--set-up-an-sftp-server"></a>

### Set up an SFTP server

SFTP (SSH File Transfer Protocol) is a file transfer protocol used for secure file transfers between computers.
SFTP is built on top of the SSH (Secure Shell) protocol and utilizes encryption and authentication.

We will use the built-in SFTP service in macOS (by enabling "Remote Login" access).
For detailed instructions, please refer to the
[Allow a remote computer to access your Mac](https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac)document.

<a id="connect-07rocketmq-connect-in-action4--create-source-test-file"></a>

### Create Source Test File

Create a test file named `source.txt` and write some test data to it:

```shell
mkdir -p /Users/YourUsername/rocketmqconnect/sftp-test/

cd /Users/YourUsername/rocketmqconnect/sftp-test/

touch source.txt

echo 'John Doe|100000202211290001|20221129001|30000.00|2022-11-28|03:00:00|7.00
Jane Smith|100000202211290002|20221129002|40000.00|2022-11-28|04:00:00|9.00
Bob Johnson|100000202211290003|20221129003|50000.00|2022-11-28|05:00:00|12.00' >> source.txt
```

Log in to the SFTP service to verify that you can access it normally. Enter the following command, then enter your
password :

```shell
# sftp -P port YourUsername@hostname sftp -P 22 YourUsername@127.0.0.1
```

**Note**: Since this is the SFTP service provided by your local MAC OS, the address is `127.0.0.1` and the port is the default 22.

```shell
sftp> cd /Users/YourUsername/rocketmqconnect/sftp-test/
sftp> ls source.txt
sftp> bye
```

<a id="connect-07rocketmq-connect-in-action4--start-connector"></a>

## Start Connector

<a id="connect-07rocketmq-connect-in-action4--start-sftp-source-connector"></a>

### Start SFTP Source Connector

Run the following command to start the SFTP source connector. This connector will connect to the
SFTP service to read from the `source.txt` file. For each line of text in the file, the connector
will parse and package the contents into a generic ConnectRecord object, which will then be sent
to a RocketMQ topic for consumption by sink connectors.

```shell
curl -X POST --location "http://localhost:8082/connectors/SftpSourceConnector" --http1.1 \
    -H "Host: localhost:8082" \
    -H "Content-Type: application/json" \
    -d '{
          "connector.class": "org.apache.rocketmq.connect.http.sink.SftpSourceConnector",
          "host": "127.0.0.1",
          "port": 22,
          "username": "YourUsername",
          "password": "yourPassword",
          "filePath": "/Users/YourUsername/rocketmqconnect/sftp-test/source.txt",
          "connect.topicname": "sftpTopic",
          "fieldSeparator": "|",
          "fieldSchema": "username|idCardNo|orderNo|orderAmount|trxDate|trxTime|profit"
        }'
```

If the curl request returns status: 200, it indicates that the connector was successfully
created. An example response would look like this:

```json
{"status":200,"body":{"connector.class":"...
```

To confirm that the file source connector has started successfully, run the following command:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

> Start connector SftpSourceConnector and set target state STARTED successed!!

<a id="connect-07rocketmq-connect-in-action4--start-sftp-sink-connector"></a>

### Start SFTP Sink Connector

Run the following command to start the SFTP sink connector. This connector will subscribe to the RocketMQ topic
to consume messages and convert each one into a single line of text, which will then be written to the destination
file `sink.txt` using the SFTP protocol:

```shell
curl -X POST --location "http://localhost:8082/connectors/SftpSinkConnector" --http1.1 \
    -H "Host: localhost:8082" \
    -H "Content-Type: application/json" \
    -d '{
          "connector.class": "org.apache.rocketmq.connect.http.sink.SftpSinkConnector",
          "host": "127.0.0.1",
          "port": 22,
          "username": "YourUsername",
          "password": "yourPassword",
          "filePath": "/Users/YourUsername/rocketmqconnect/sftp-test/sink.txt",
          "connect.topicnames": "sftpTopic",
          "fieldSeparator": "|",
          "fieldSchema": "username|idCardNo|orderNo|orderAmount|trxDate|trxTime|profit"
        }'
```

If the curl request returns status: 200, it indicates that the connector was successfully
created. An example response would look like this:

```json
{"status":200,"body":{"connector.class":"...
```

Check the logs to confirm successful startup of the SFTP sink connector:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

> Start connector SftpSinkConnector and set target state STARTED successed!!

Confirm that the data has been written to the destination file by running the following command:

```shell
cat /Users/YourUsername/rocketmqconnect/sftp-test/sink.txt
```

If the `sink.txt` file has been generated and its contents match those of the `source.txt` file, the entire process is working correctly.

Write more test data to the `source.txt` file to continue testing:

```shell
cd /Users/YourUsername/rocketmqconnect/sftp-test/

echo 'John Doe|100000202211290001|20221129001|30000.00|2022-11-28|03:00:00|7.00
Jane Smith|100000202211290002|20221129002|40000.00|2022-11-28|04:00:00|9.00
Bob Johnson|100000202211290003|20221129003|50000.00|2022-11-28|05:00:00|12.00' >> source.txt

# Wait a few seconds to give the connector time to replicate data to the sink file. sleep 10

cat /Users/YourUsername/rocketmqconnect/sftp-test/sink.txt
```

**Note**: The order of file contents may vary because the `rocketmq-connect-sftp` uses `normal message` when
sending and receiving messages to/from a RocketMQ topic. This is different from `ordered message`, and consuming
`normal messages` does not guarantee the order.

- [Preparation](#connect-07rocketmq-connect-in-action4--preparation)
  - [Start RocketMQ](#connect-07rocketmq-connect-in-action4--start-rocketmq)
  - [Build Connector Runtime](#connect-07rocketmq-connect-in-action4--build-connector-runtime)
  - [Build SFTP Connector Plugin](#connect-07rocketmq-connect-in-action4--build-sftp-connector-plugin)
  - [Run Connector Worker in Standalone Mode](#connect-07rocketmq-connect-in-action4--run-connector-worker-in-standalone-mode)
  - [Set up an SFTP server](#connect-07rocketmq-connect-in-action4--set-up-an-sftp-server)
  - [Create Source Test File](#connect-07rocketmq-connect-in-action4--create-source-test-file)
- [Start Connector](#connect-07rocketmq-connect-in-action4--start-connector)
  - [Start SFTP Source Connector](#connect-07rocketmq-connect-in-action4--start-sftp-source-connector)
  - [Start SFTP Sink Connector](#connect-07rocketmq-connect-in-action4--start-sftp-sink-connector)

---

<a id="connect-08rocketmq-connect-in-action5-es"></a>

<!-- source_url: https://rocketmq.apache.org/docs/connect/08RocketMQ%20%20Connect%20In%20Action5-ES/ -->

<!-- page_index: 56 -->

# RocketMQ Connect in Action 5

Version: 5.0

# RocketMQ Connect in Action 5

Elasticsearch Source -> RocketMQ Connect -> Elasticsearch Sink

<a id="connect-08rocketmq-connect-in-action5-es--preparatory-work"></a>

## preparatory work

<a id="connect-08rocketmq-connect-in-action5-es--start-rocketmq"></a>

### Start RocketMQ

1. Linux/Unix/Mac
2. 64bit JDK 1.8+;
3. Maven 3.2.x+;
4. Start RocketMQ. Either [RocketMQ 4.x](https://rocketmq.apache.org/docs/4.x/) or
   [RocketMQ 5.x](#quickstart-01quickstart) 5.x version can be used;
5. Test RocketMQ message sending and receiving using the tool.

Here, use the environment variable NAMESRV\_ADDR to inform the tool client of the NameServer address of RocketMQ as localhost:9876.

```shell
#$ cd distribution/target/rocketmq-4.9.7/rocketmq-4.9.7
$ cd distribution/target/rocketmq-5.1.4/rocketmq-5.1.4

$ export NAMESRV_ADDR=localhost:9876
$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer SendResult [sendStatus=SEND_OK, msgId= ...

$ sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer ConsumeMessageThread_%d Receive New Messages: [MessageExt...
```

**Note**: RocketMQ has the feature of automatically creating Topic and Group. When sending or subscribing to messages, if the corresponding Topic or Group does not exist, RocketMQ will automatically create them. Therefore, there is no need to create Topic and Group in advance.

Here's the English translation of the content:

<a id="connect-08rocketmq-connect-in-action5-es--building-the-connector-runtime"></a>

### Building the Connector Runtime

Clone the repository and build the RocketMQ Connect project:

```shell
git clone https://github.com/apache/rocketmq-connect.git

cd rocketmq-connect

export RMQ_CONNECT_HOME=`pwd`

mvn -Prelease-connect -Dmaven.test.skip=true clean install -U
```

<a id="connect-08rocketmq-connect-in-action5-es--build-elasticsearch-connector-plugin"></a>

### Build Elasticsearch Connector Plugin

Build the Elasticsearch RocketMQ Connector plugin:

```shell
cd $RMQ_CONNECT_HOME/connectors/rocketmq-connect-elasticsearch/

mvn clean package -Dmaven.test.skip=true
```

Copy the compiled Elasticsearch RocketMQ Connector plugin JAR file into the plugin directory used by the runtime:

```shell
mkdir -p /Users/YourUsername/rocketmqconnect/connector-plugins

cp target/rocketmq-connect-elasticsearch-1.0.0-jar-with-dependencies.jar /Users/YourUsername/rocketmqconnect/connector-plugins
```

<a id="connect-08rocketmq-connect-in-action5-es--run-connector-worker-in-standalone-mode"></a>

### Run Connector Worker in Standalone Mode

Modify the `connect-standalone.conf` file to configure the RocketMQ connection
address and other information.

```shell
cd $RMQ_CONNECT_HOME/distribution/target/rocketmq-connect-0.0.1-SNAPSHOT/rocketmq-connect-0.0.1-SNAPSHOT

vim conf/connect-standalone.conf
```

Example configuration information is as follows:

```text
workerId=standalone-worker
storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

## Http port for user to access REST API
httpPort=8082

# Rocketmq namesrvAddr
namesrvAddr=localhost:9876

# RocketMQ acl
aclEnable=false
#accessKey=rocketmq
#secretKey=12345678

clusterName="DefaultCluster"

# Plugin path for loading Source/Sink Connectors
pluginPaths=/Users/YourUsername/rocketmqconnect/connector-plugins
```

In standalone mode, RocketMQ Connect persistently stores the synchronization checkpoint information
in the local file directory specified by storePathRootDir.

> storePathRootDir=/Users/YourUsername/rocketmqconnect/storeRoot

If you want to reset the synchronization checkpoint, delete the persistence files:

```shell
rm -rf /Users/YourUsername/rocketmqconnect/storeRoot/*
```

To start Connector Worker in standalone mode:

```text
sh bin/connect-standalone.sh -c conf/connect-standalone.conf &
```

<a id="connect-08rocketmq-connect-in-action5-es--set-up-elasticsearch-services"></a>

### Set Up Elasticsearch Services

Elasticsearch is an open-source search and analytics engine.

We'll use two separate Docker instances of Elasticsearch to serve as our source and destination databases:

```text
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.15.1

docker run --name es1 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
-v /Users/YourUsername/rocketmqconnect/es/es1_data:/usr/share/elasticsearch/data \
-d docker.elastic.co/elasticsearch/elasticsearch:7.15.1

docker run --name es2 -p 9201:9200 -p 9301:9300 -e "discovery.type=single-node" -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
-v /Users/YourUsername/rocketmqconnect/es/es2_data:/usr/share/elasticsearch/data \
-d docker.elastic.co/elasticsearch/elasticsearch:7.15.1
```

Explanation of Docker commands:

- `--name es2`: Specifies a name for the container, e.g., `es2`.
- `-p 9201:9200 -p 9301:9300`: Maps ports 9200 and 9300 on the Elasticsearch container to host ports 9201 and 9301 so that the Elasticsearch service can be accessed via the host.
- `-e discovery.type=single-node`: configures Elasticsearch to work on a single node without discovering other nodes in a cluster, suitable for single-server deployment.
- `-v /Users/YourUsername/rocketmqconnect/es/es2_data:/usr/share/elasticsearch/data`: Mounts a directory on the host to `/usr/share/elasticsearch/data` within the container for persistent storage of Elasticsearch data.

This runs a custom-configured instance of Elasticsearch with persistent data storage on a container accessible through port 9200 on the host machine, making it useful for development or testing environments on a local machine.

View the Elasticsearch logs:

```text
docker logs -f es1

docker logs -f es2
```

Verify that Elasticsearch has started successfully:

```text
# Check Elasticsearch instance 1
curl -XGET http://localhost:9200

# Check Elasticsearch instance 2
curl -XGET http://localhost:9201
```

A successful connection and correct operation will result in JSON responses containing information
about Elasticsearch and its version number.

<a id="connect-08rocketmq-connect-in-action5-es--set-up-kibana-services"></a>

### Set Up Kibana Services

Kibana is an open-source data visualization tool that allows users to interactively explore
and understand data stored within Elasticsearch clusters. It offers rich features such as charts, graphs, and dashboards.

For convenience, we'll set up two separate instances of Kibana in Docker and link them to
our previously established Elasticsearch containers using the following command:

```text
docker pull docker.elastic.co/kibana/kibana:7.15.1

docker run --name kibana1 --link es1:elasticsearch -p 5601:5601 -d docker.elastic.co/kibana/kibana:7.15.1

docker run --name kibana2 --link es2:elasticsearch -p 5602:5601 -d docker.elastic.co/kibana/kibana:7.15.1
```

Explanation of Docker Commands:

- `--name kibana2`: Assigns a name to the new container, e.g., kibana2
- `--link es2:elasticsearch`: Links the container to another named Elasticsearch instance (in this case, 'es2'). This enables communication between Kibana and Elasticsearch.
- `-p 5602:5601`: Maps Kibana's default port (5601) to the same port on the host machine to make it accessible through the browser.
- `-d`: runs the Docker container in detached mode.

Once the container has launched, you can monitor its log output:

```text
docker logs -f kibana1

docker logs -f kibana2
```

To access Kibana console pages, simply visit following addresses in your browser

- kibana1: http://localhost:5601
- kibana2：http://localhost:5602

If they load correctly, it indicates successful startup of the respective Kibana instances.

<a id="connect-08rocketmq-connect-in-action5-es--write-test-data-to-the-source-elasticsearch"></a>

### Write Test Data to the Source Elasticsearch

Kibana's Dev Tools can help you interact and operate directly with Elasticsearch in Kibana.
You can execute various queries and operations, analyze and understand the returned data.
Refer to the documentation [console-kibana](https://www.elastic.co/guide/en/kibana/8.9/console-kibana.html).

<a id="connect-08rocketmq-connect-in-action5-es--bulk-write-test-data"></a>

#### Bulk Write Test Data

Access the Kibana1 console through the browser, find Dev Tools from the left menu, and enter the following commands on the page to write test data:

```text
POST /_bulk
{ "index" : { "_index" : "connect_es" } }
{ "id": "1", "field1": "value1", "field2": "value2" }
{ "index" : { "_index" : "connect_es" } }
{ "id": "2", "field1": "value3", "field2": "value4" }
```

**Note**:

- connect\_es: The index name for the data.
- id/field1/field2: These are field names, and 1, value1, value2 represent the values for the fields.

**Note**: There is a limitation in `rocketmq-connect-elasticsearch`, which requires a field in the data that
can be used for >= comparison operations (string or number). This field will be used to record the
synchronization checkpoint. In the above example, the `id` field is a globally unique, incrementing numerical field.

<a id="connect-08rocketmq-connect-in-action5-es--query-data"></a>

#### Query Data

To query data within an index, use the following command:

```text
GET /connect_es/_search
{
  "size": 100
}
```

If there is no data available, the response will be:

```text
{
  "error" : {
    ...
    "type" : "index_not_found_exception",
    "reason" : "no such index [connect_es]",
    "resource.type" : "index_or_alias",
    "resource.id" : "connect_es",
    "index_uuid" : "_na_",
    "index" : "connect_es"
  },
  "status" : 404
}
```

If there is data available, the response will be:

```text
{
  ...
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "connect_es",
        "_type" : "_doc",
        "_id" : "_dx49osBb46Z9cN4hYCg",
        "_score" : 1.0,
        "_source" : {
          "id" : "1",
          "field1" : "value1",
          "field2" : "value2"
        }
      },
      {
        "_index" : "connect_es",
        "_type" : "_doc",
        "_id" : "_tx49osBb46Z9cN4hYCg",
        "_score" : 1.0,
        "_source" : {
          "id" : "2",
          "field1" : "value3",
          "field2" : "value4"
        }
      }
    ]
  }
}
```

<a id="connect-08rocketmq-connect-in-action5-es--delete-data"></a>

#### Delete Data

If you need to delete data within an index due to repeated testing or other reasons, you can use the following command:

```text
DELETE /connect_es
```

<a id="connect-08rocketmq-connect-in-action5-es--start-connector"></a>

## Start Connector

<a id="connect-08rocketmq-connect-in-action5-es--start-elasticsearch-source-connector"></a>

### Start Elasticsearch Source Connector

Run the following command to start the ES source connector. The connector will connect to Elasticsearch
and read document data from the connect\_es index. It will parse the Elasticsearch document data and
package it into a generic ConnectRecord object, which will be sent to a RocketMQ topic for consumption by the Sink Connector.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/elasticsearchSourceConnector -d  '{
  "connector.class":"org.apache.rocketmq.connect.elasticsearch.connector.ElasticsearchSourceConnector",
    "elasticsearchHost":"localhost",
    "elasticsearchPort":9200,
    "index":{
        "connect_es": {
            "primaryShards":1,
            "id":1
        }
    },
    "max.tasks":2,
    "connect.topicname":"ConnectEsTopic",
    "value.converter":"org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
    "key.converter":"org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

**Note**: The startup command specifies that the source ES should synchronize the connect\_es index, and the incrementing field in the index is id. Data will be fetched starting from id=1.

If the curl request returns status:200, it indicates a successful creation, and the sample response will be:

> {"status":200,"body":{"connector.class":"...

If you see the following logs, it indicates that the file source connector has started successfully.

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

> Start connector elasticsearchSourceConnector and set target state STARTED successed!!

<a id="connect-08rocketmq-connect-in-action5-es--start-elasticsearch-sink-connector"></a>

### Start Elasticsearch Sink Connector

Run the following command to start the ES sink connector. The connector will subscribe to data from
the RocketMQ topic and consume it. It will convert each message into document data and write it to the destination ES.

```text
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8082/connectors/elasticsearchSinkConnector -d '{
  "connector.class":"org.apache.rocketmq.connect.elasticsearch.connector.ElasticsearchSinkConnector",
    "elasticsearchHost":"localhost",
    "elasticsearchPort":9201,
    "max.tasks":2,
    "connect.topicnames":"ConnectEsTopic",
    "value.converter":"org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter",
    "key.converter":"org.apache.rocketmq.connect.runtime.converter.record.json.JsonConverter"
}'
```

**Note**: The startup command specifies the address and port of the destination ES, which corresponds to
the previously started ES2 in Docker.

If the curl request returns status:200, it indicates a successful creation, and the sample response will be:

> {"status":200,"body":{"connector.class":"...

If you see the following logs, it indicates that the file source connector has started successfully:

```shell
tail -100f ~/logs/rocketmqconnect/connect_runtime.log
```

> Start connector elasticsearchSinkConnector and set target state STARTED successed!!

To check if the sink connector has written data to the destination ES index:

1. Access the Kibana2 console address in the browser: http://localhost:5602
2. In the Kibana2 Dev Tools page, query the data within the index. If it matches the data in the source ES1, it means the connector is running properly.

```text
GET /connect_es/_search
{
  "size": 100
}
```

- [preparatory work](#connect-08rocketmq-connect-in-action5-es--preparatory-work)
  - [Start RocketMQ](#connect-08rocketmq-connect-in-action5-es--start-rocketmq)
  - [Building the Connector Runtime](#connect-08rocketmq-connect-in-action5-es--building-the-connector-runtime)
  - [Build Elasticsearch Connector Plugin](#connect-08rocketmq-connect-in-action5-es--build-elasticsearch-connector-plugin)
  - [Run Connector Worker in Standalone Mode](#connect-08rocketmq-connect-in-action5-es--run-connector-worker-in-standalone-mode)
  - [Set Up Elasticsearch Services](#connect-08rocketmq-connect-in-action5-es--set-up-elasticsearch-services)
  - [Set Up Kibana Services](#connect-08rocketmq-connect-in-action5-es--set-up-kibana-services)
  - [Write Test Data to the Source Elasticsearch](#connect-08rocketmq-connect-in-action5-es--write-test-data-to-the-source-elasticsearch)
- [Start Connector](#connect-08rocketmq-connect-in-action5-es--start-connector)
  - [Start Elasticsearch Source Connector](#connect-08rocketmq-connect-in-action5-es--start-elasticsearch-source-connector)
  - [Start Elasticsearch Sink Connector](#connect-08rocketmq-connect-in-action5-es--start-elasticsearch-sink-connector)

---

<a id="streams-01rocketmq-streams-overview"></a>

<!-- source_url: https://rocketmq.apache.org/docs/streams/01RocketMQ%20Streams%20Overview/ -->

<!-- page_index: 57 -->

# RocketMQ Streams Overview

Version: 5.0

# RocketMQ Streams Overview

RocketMQ Streams is a lightweight stream computing engine based on RocketMQ. It can be applied as an SDK dependency without the need for deploying complex stream computing servers, making it resource-efficient, easily extensible, and rich in stream computing operators.

<a id="streams-01rocketmq-streams-overview--architecture"></a>

## Architecture

![总体架构](assets/images/e6-80-bb-e4-bd-93-1-83fd1dda4e3d43b6852f1805845b9a22_4131c5b8b8b8044e.png)

Data is consumed from RocketMQ by RocketMQ-streams, processed, and ultimately written back to RocketMQ.

![总体架构](assets/images/e6-80-bb-e4-bd-93-2-2890a8f2fef9eebee54da9edff1fdc94_80ebc5d71cbecb02.png)

Data is consumed by the RocketMQ Consumer, enters the processing topology to be processed by operators. If the stream processing task contains the keyBy operator, the data needs to be grouped by Key and written to a shuffle topic. Subsequent operators consume from the shuffle topic. If there are also stateful operators such as count, the calculation requires reading and writing to the state topic. After the calculation is finished, the result is written back to RocketMQ.

<a id="streams-01rocketmq-streams-overview--consume-model"></a>

## Consume model

![img_2.png](assets/images/e6-b6-88-e8-b4-b9-e6-a8-a1-e5-9e-8b-d98dfe7e30b9762714b160f2e473cd74_7f325bf60c835d26.png)

The calculation instances actually depend on the client of the Rocket-streams SDK. Therefore, the calculation instances consume MQ, dependent on the RocketMQ rebalance allocation. The total number of calculation instances cannot be greater than the total number of consuming MQ, otherwise, some calculation instances will be in a waiting state, unable to consume data.

One calculation instance can consume multiple MQs, and within one instance, there is only one calculation topology graph.

<a id="streams-01rocketmq-streams-overview--state"></a>

## State

![img_3.png](assets/images/state-cdeb5a31134120b49cd60a94d0415b7d_6e03b1becf214f42.png)

For stateful operators, such as count, grouping must be done first before summing. The grouping operator keyBy will re-write the data to RocketMQ based on the grouping key, and ensures that data with the same key is written to the same partition (this process is called shuffle), to ensure that data with the same key is consumed by the same consumer. The state is locally accelerated by RocksDB, and remotely persisted by RocketMQ.

<a id="streams-01rocketmq-streams-overview--expansionshrinkage-capacity"></a>

## Expansion/shrinkage capacity

![img.png](assets/images/scale-1b24d0731e3288382ce42624afe932d3_2a3c717c7e5de675.png)

When the calculation instances are reduced from 3 to 2, with the help of the rebalance function under the RocketMQ cluster consumption mode, the consumed MQ will be re-allocated among the calculation instances. The MQ2 and MQ3 consumed by Instance1 are allocated to Instance2 and Instance3, and the state data of these two MQs also needs to be migrated to Instance2 and Instance3. This also implies that the state data is saved according to the original data partition MQ; expansion is just the opposite process.

- [Architecture](#streams-01rocketmq-streams-overview--architecture)
- [Consume model](#streams-01rocketmq-streams-overview--consume-model)
- [State](#streams-01rocketmq-streams-overview--state)
- [Expansion/shrinkage capacity](#streams-01rocketmq-streams-overview--expansionshrinkage-capacity)

---

<a id="streams-02rocketmq-streams-concept"></a>

<!-- source_url: https://rocketmq.apache.org/docs/streams/02RocketMQ%20Streams%20Concept/ -->

<!-- page_index: 58 -->

# RocketMQ Streams Core Concept

Version: 5.0

# RocketMQ Streams Core Concept

<a id="streams-02rocketmq-streams-concept--domain-model"></a>

## Domain model

<a id="streams-02rocketmq-streams-concept--streambuilder"></a>

### StreamBuilder

![img_2.png](assets/images/e9-a2-86-e5-9f-9f-e6-a8-a1-e5-9e-8b-1-d0e1ee0b63e037d14c2ce13488a8eb65_c1f36c67766ea750.png)

- An instance of StreamBuilder has 1 to N pipelines, where a pipeline represents a data processing path.
- A pipeline can contain 1 to N processing nodes, called GroupNodes.
- An instance of StreamBuilder also has a TopologyBuilder, which can construct data processors.
- Each JobId corresponds to one instance of StreamBuilder.

<a id="streams-02rocketmq-streams-concept--rocketmqstream"></a>

### RocketMQStream

![img_2.png](assets/images/e9-a2-86-e5-9f-9f-e6-a8-a1-e5-9e-8b-2-4b2fc60e1b5ded400548aa3f25861dd8_50e99cb94226b815.png)

- An instance of RocketMQStream has a TopologyBuilder for building topologies
- An instance of RocketMQStream can instantiate 1 to N worker threads
- Each thread, represented by a WorkerThread instance, contains an engine
- An engine contains all the logic for executing data processing and includes a consumer instance, a producer instance, and a StateStore instance.

<a id="streams-02rocketmq-streams-concept--stream-processing-instance"></a>

### Stream Processing Instance

A Stream Processing Instance represents a process running RocketMQ Streams;

- An instance of Stream Processing contains one StreamBuilder, one RocketMQStream, one topology, and one or multiple pipelines.

<a id="streams-02rocketmq-streams-concept--streambuilder-1"></a>

## StreamBuilder

- `StreamBuilder(jobId)` build instance；
- `<OUT> RStream<OUT> source(topicName, deserializer)`  define source topic and deserialization method；

<a id="streams-02rocketmq-streams-concept--rstream"></a>

## RStream

- `<K> GroupedStream<K, T> keyBy(selectAction)` group the data by specific field；
- `<O> RStream<O> map(mapperAction)` transform data one-to-one；
- `RStream<T> filter(predictor)` filter the data
- `<VR> RStream<T> flatMap(mapper)`transform data one-to-many；
- `<T2> JoinedStream<T, T2> join(rightStream)` Perform a two-stream join；
- `sink(topicName, serializer)` output the results to a specific topic；

<a id="streams-02rocketmq-streams-concept--groupedstream"></a>

## GroupedStream

Operations on data that has the same key

- `<OUT> GroupedStream<K, Integer> count(selectAction)` counts the number of data entries that contain a certain field.
- `GroupedStream<K, V> min(selectAction)` calculates the minimum value of a certain field.
- `GroupedStream<K, V> max(selectAction)` calculates the maximum value of a certain field.
- `GroupedStream<K, ? extends Number> sum(selectAction)` calculates the sum of a certain field.
- `GroupedStream<K, V> filter(predictor)` filters a certain field.
- `<OUT> GroupedStream<K, OUT> map(valueMapperAction)` performs one-to-one data transformation.
- `<OUT> GroupedStream<K, OUT> aggregate(accumulator)` performs aggregate operations on the data, and supports second-order aggregation, such as adding data before a window triggers and calculating results when the window triggers.
- `WindowStream<K, V> window(windowInfo)` defines a window for the stream.
- `GroupedStream<K, V> addGraphNode(name, supplier)` adds a custom operator to the stream processing topology at a low-level interface.
- `RStream<V> toRStream()` converts to RStream, only converting in terms of interface and not affecting the data.
- `sink(topicName, serializer)` writes the results to a topic in a custom serialization format.

<a id="streams-02rocketmq-streams-concept--windowstream"></a>

## WindowStream

Operations on data that has been divided into windows

- `WindowStream<K, Integer> count()` counts the number of data entries in the window.
- `WindowStream<K, V> filter(predictor)` filters the data in the window.
- `<OUT> WindowStream<K, OUT> map(mapperAction)` performs one-to-one data transformation on the data in the window.
- `<OUT> WindowStream<K, OUT> aggregate(aggregateAction)` performs many-to-one data transformation on the data in the window.
- `<OUT> WindowStream<K, OUT> aggregate(accumulator)` performs aggregate operations on the data in the window, and supports second-order aggregation, such as adding data before a window triggers and calculating results when the window triggers.
- `void sink(topicName, serializer)` writes the results to a topic in a custom serialization format.

- [Domain model](#streams-02rocketmq-streams-concept--domain-model)
  - [StreamBuilder](#streams-02rocketmq-streams-concept--streambuilder)
  - [RocketMQStream](#streams-02rocketmq-streams-concept--rocketmqstream)
  - [Stream Processing Instance](#streams-02rocketmq-streams-concept--stream-processing-instance)
- [StreamBuilder](#streams-02rocketmq-streams-concept--streambuilder-1)
- [RStream](#streams-02rocketmq-streams-concept--rstream)
- [GroupedStream](#streams-02rocketmq-streams-concept--groupedstream)
- [WindowStream](#streams-02rocketmq-streams-concept--windowstream)

---

<a id="streams-03rocketmq-streams-quick-start"></a>

<!-- source_url: https://rocketmq.apache.org/docs/streams/03RocketMQ%20Streams%20Quick%20Start/ -->

<!-- page_index: 59 -->

# RocketMQ Streams Quick Start

Version: 5.0

# RocketMQ Streams Quick Start

<a id="streams-03rocketmq-streams-quick-start--run-in-the-rocketmq-streams-project"></a>

## Run in the RocketMQ Streams project

Refer to the RocketMQ Streams project rocketmq-streams-examples module for programs that can be run directly. Steps to run the example:

- Start RocketMQ 5.0 or above locally.
- Use mqAdmin to create the data source topic in the example.
- Start the example.
- Write appropriate data to the source topic of RocketMQ (as determined by the example).

<a id="streams-03rocketmq-streams-quick-start--rocketmq-streams-is-applied-as-a-dependency-in-sdk-form"></a>

## RocketMQ Streams is applied as a dependency in SDK form

<a id="streams-03rocketmq-streams-quick-start--prepare-the-environment"></a>

### Prepare the environment

- 64bit JDK 1.8+
- Maven 3.2+
- Start RocketMQ locally，[Startup documentation](https://rocketmq.apache.org/docs/quick-start/)

<a id="streams-03rocketmq-streams-quick-start--build-rocketmq-streams"></a>

### Build RocketMQ Streams

<a id="streams-03rocketmq-streams-quick-start--add-pom-dependency"></a>

### Add pom dependency

```xml
 <dependencies>
    <dependency>
        <groupId>org.apache.rocketmq</groupId>
        <artifactId>rocketmq-streams</artifactId>
            <!-- Modify as needed -->
        <version>1.1.0</version>
    </dependency>
</dependencies>
```

<a id="streams-03rocketmq-streams-quick-start--write-stream-computing-program"></a>

### Write stream computing program

```java
public class WordCount {
    public static void main(String[] args) {
        StreamBuilder builder = new StreamBuilder("wordCount");

        builder.source("sourceTopic", total -> {
                    String value = new String(total, StandardCharsets.UTF_8);
                    return new Pair<>(null, value);
                })
                .flatMap((ValueMapperAction<String, List<String>>) value -> {
                    String[] splits = value.toLowerCase().split("\\W+");
                    return Arrays.asList(splits);
                })
                .keyBy(value -> value)
                .count()
                .toRStream()
                .print();

        TopologyBuilder topologyBuilder = builder.build();

        Properties properties = new Properties();
        properties.put(MixAll.NAMESRV_ADDR_PROPERTY, "127.0.0.1:9876");

        RocketMQStream rocketMQStream = new RocketMQStream(topologyBuilder, properties);

        final CountDownLatch latch = new CountDownLatch(1);

        Runtime.getRuntime().addShutdownHook(new Thread("wordcount-shutdown-hook") {
            @Override
            public void run() {
                rocketMQStream.stop();
                latch.countDown();
            }
        });

        try {
            rocketMQStream.start();
            latch.await();
        } catch (final Throwable e) {
            System.exit(1);
        }
        System.exit(0);
    }
}
```

<a id="streams-03rocketmq-streams-quick-start--write-data-to-the-rocketmq-sourcetopic-and-observe-the-results"></a>

### Write data to the RocketMQ sourceTopic and observe the results

If the data written to the sourceTopic is as follows: each line of data is sent as a message;

```xml
"To be, or not to be,--that is the question:--",
"Whether 'tis nobler in the mind to suffer",
"The slings and arrows of outrageous fortune",
"Or to take arms against a sea of troubles,",
"And by opposing end them?--To die,--to sleep,--",
"No more; and by a sleep to say we end",
"The heartache, and the thousand natural shocks",
"That flesh is heir to,--'tis a consummation",
```

Count the frequency of words, and the calculation results are as follows:

```xml
(key=to, value=1)
(key=be, value=1)
(key=or, value=1)
(key=not, value=1)
(key=to, value=2)
(key=be, value=2)
(key=that, value=1)
(key=is, value=1)
(key=the, value=1)
(key=whether, value=1)
(key=tis, value=1)
(key=nobler, value=1)
(key=mind, value=1)
(key=against, value=1)
(key=troubles, value=1)
(key=slings, value=1)
(key=die, value=1)
(key=natural, value=1)
(key=flesh, value=1)
(key=sea, value=1)
(key=fortune, value=1)
(key=shocks, value=1)
(key=consummation, value=1)
(key=to, value=3)
(key=to, value=4)
(key=to, value=5)
(key=say, value=1)
(key=end, value=1)
(key=end, value=2)
(key=to, value=6)
(key=to, value=7)
(key=to, value=8)
(key=or, value=2)
(key=them, value=1)
(key=take, value=1)
(key=arms, value=1)
(key=of, value=1)
(key=and, value=1)
(key=of, value=2)
(key=and, value=2)
(key=by, value=1)
(key=sleep, value=1)
(key=and, value=3)
(key=by, value=2)
(key=sleep, value=2)
(key=and, value=4)
(key=that, value=2)
(key=arrows, value=1)
(key=heir, value=1)
(key=question, value=1)
(key=is, value=2)
(key=the, value=2)
(key=suffer, value=1)
(key=a, value=1)
(key=the, value=3)
(key=no, value=1)
(key=a, value=2)
(key=opposing, value=1)
(key=the, value=4)
(key=the, value=5)
(key=a, value=3)
(key=in, value=1)
(key=more, value=1)
(key=heartache, value=1)
(key=outrageous, value=1)
(key=we, value=1)
(key=thousand, value=1)
(key=tis, value=2)
```

- [Run in the RocketMQ Streams project](#streams-03rocketmq-streams-quick-start--run-in-the-rocketmq-streams-project)
- [RocketMQ Streams is applied as a dependency in SDK form](#streams-03rocketmq-streams-quick-start--rocketmq-streams-is-applied-as-a-dependency-in-sdk-form)
  - [Prepare the environment](#streams-03rocketmq-streams-quick-start--prepare-the-environment)
  - [Build RocketMQ Streams](#streams-03rocketmq-streams-quick-start--build-rocketmq-streams)
  - [Add pom dependency](#streams-03rocketmq-streams-quick-start--add-pom-dependency)
  - [Write stream computing program](#streams-03rocketmq-streams-quick-start--write-stream-computing-program)
  - [Write data to the RocketMQ sourceTopic and observe the results](#streams-03rocketmq-streams-quick-start--write-data-to-the-rocketmq-sourcetopic-and-observe-the-results)

---

<a id="contributionguide-01how-to-contribute"></a>

<!-- source_url: https://rocketmq.apache.org/docs/contributionGuide/01how-to-contribute/ -->

<!-- page_index: 60 -->

# How to Contribute

Version: 5.0

# How to Contribute

Apache RocketMQ —— Open and sharing open source community, sincerely invite you to join.

Ways of community communication and contribution:

- Ask questions
- Submitting an error report
- Introduce new feature
- Participate in discussions on mailing lists
- Contribute code or documentation
- Optimize the site
- Test pre-release versions

<a id="contributionguide-01how-to-contribute--request-to-answer-questions"></a>

## Request to answer questions

Apache RocketMQ community provides a complete process to help you answer your questions.

You can ask questions through [User mailing list](mailto:users@rocketmq.apache.org) and [Stack Overflow #rocketmq](https://stackoverflow.com/questions/tagged/rocketmq) .

<a id="contributionguide-01how-to-contribute--submitting-an-error-report"></a>

## Submitting an error report

If you have problems using RocketMQ,You can file an error report on [GitHub Issue](https://github.com/apache/rocketmq/issues).

<a id="contributionguide-01how-to-contribute--propose-improvements-or-new-features"></a>

## Propose improvements or new features

The community is constantly looking for feedback to improve Apache RocketMQ,Your need for improvements or new features will benefit all RocketMQ users, Please create an issue on [GitHub Issue](https://github.com/apache/rocketmq/issues)。

Proposals need to include appropriate details and scope of impact. Please elaborate as much as possible on the requirements.We hope to get more complete information for the following reasons:

- The improvements and new features implemented ultimately fit your needs
- Evaluate input costs and design solutions based on your needs
- To facilitate constructive community discussion around the proposal

If you plan to implement your proposal to contribute to the community, you will also need to provide detailed description information,And follow [code-guidelines](#contributionguide-02code-guidelines) Code specification

We recommend building community consensus before implementing features. By discussing the need for new features and how to implement them, proposals that are outside the scope of the project can be spotted early.

<a id="contributionguide-01how-to-contribute--participate-in-discussions-and-help-others"></a>

## Participate in discussions and help others

Members of the Apache RocketMQ community communicate through the following two types of email:

- [User mailing list](mailto:users@rocketmq.apache.org) ：Apache RocketMQ users use the mailing list to ask for help or advice.

  You can contribute to the community by subscribing to the email system to help others solve problems;

  You can also retrieve on Stackoverflow [rocketmq](https://stackoverflow.com/questions/tagged/rocketmq) tag answer user questions and get more insights.
- [Development mailing list](mailto:dev@rocketmq.apache.org) : Apache RocketMQ developers use this mailing list to communicate new features, pre-releases, general development processes, etc.

  If you are interested in contributing code to the RocketMQ community, you can join the mailing list.

You can also by subscribing to [mailing lists](https://rocketmq.apache.org/contact) get more info about the community.

<a id="contributionguide-01how-to-contribute--test-pre-release-versions"></a>

## Test pre-release versions

Apache RocketMQ continues to grow with the help of its active community. Every few weeks we release a new version of RocketMQ to fix bugs, improve performance, add features, etc. The process for releasing a new version is as follows:

1. Launch a new pre-release version and start the voting process (72 hours)
2. Test pre-release versions and score (+1 no problem found, -1 test problem)
3. If the pre-release version is not tested, release it; otherwise, go back to Step 1

We have compiled the [release-manual](#contributionguide-04release-manual) release guide on the website.
Testing a pre-release is a big job, and we need to get more people involved. The RocketMQ community encourages everyone to participate in testing the new version. By testing the pre-release version, you will be confident that the new RocketMQ version will still service your program properly and is indeed supporting version upgrades.

<a id="contributionguide-01how-to-contribute--contribute-code"></a>

## Contribute code

Apache RocketMQ has been and will continue to be maintained, optimized, and extended.
So Apache RocketMQ encourages everyone to contribute source code.To give code contributors and reviewers a great code contribution experience and provide a high quality code repository, the community follows the contribution process in [code-guidelines](#contributionguide-02code-guidelines).The coding manual contains guidelines for building a development environment, community coding guidelines and coding styles, and describes how to submit contributed code.

\*\*Be sure to read it carefully before coding [code-guidelines](#contributionguide-02code-guidelines)

And please read [Apache Software Foundation contributor license](https://www.apache.org/licenses/contributor-agreements.html) to submit electronic signature.

How to find the right issue?

[GitHub Issue](https://github.com/apache/rocketmq/issues) lists the improvements and recommended features that have been proposed so far.

<a id="contributionguide-01how-to-contribute--contribution-to-the-document"></a>

## Contribution to the document

Good documentation is essential to any kind of software. The Apache RocketMQ community is committed to providing concise, accurate, and complete technical documentation. The community invites all contributions to help refine and improve the RocketMQ documentation.

- Please report missing, incorrect, expired documents on [GitHub Issue](https://github.com/apache/rocketmq/issues)
- The RocketMQ technical documentation is written in Markdown form and stored in [RocketMQ Official Website Repository](https://github.com/apache/rocketmq-site/tree/new-official-website/) `/docs`

Read [Q&A](https://github.com/apache/rocketmq-site/tree/new-official-website)to learn how to contribute by updating and refining documents.

<a id="contributionguide-01how-to-contribute--optimize-the-website"></a>

## Optimize the website

The Apache RocketMQ website represents Apache RocketMQ and the Apache RocketMQ community. Its main functions are as follows:

- Become familiar with the visitor Apache RocketMQ and the features of Apache RocketMQ
- Support visitors to download and use RocketMQ
- Guide visitors to participate and contribute to the RocketMQ community

The community accepts any contribution that will help improve the site.

Please provide your suggestions and ideas about the site by creating [Github Issue](https://github.com/apache/rocketmq-site/issues)

If you would like to update or optimize the website, please visit [apache/rocketmq-site new-official-website](https://github.com/apache/rocketmq-site/tree/new-official-website#qa%E3%80%82)

<a id="contributionguide-01how-to-contribute--more-ways-to-contribute"></a>

## More ways to contribute...

There are many more ways to contribute to the RocketMQ community that you can choose from:

- Introduce RocketMQ to as many partners as possible
- Organize offline communication meetings or online user groups
- Become the evangelist of RocketMQ
- ...

<a id="contributionguide-01how-to-contribute--how-do-i-become-a-committer"></a>

## How do I become a committer

Committers are members of a community's project repository who can modify code, documents, and websites or accept contributions from other members.

There is no strict protocol for becoming a committer, and candidates are usually active contributors in the community.

Being an active contributor means: participating in discussions on email lists, helping others solve problems, verifying pre-release versions, honoring the good people and continuously optimizing community management, which is part of the community in Apache.

Undoubtedly, contributing code and documentation to the project is equally important. A good place to start is by optimizing performance, developing new features, and fixing bugs. Either way, you are responsible for contributing code, providing test cases and documentation, and maintaining it continuously.

Candidates can be recommended by committer or PMC members in the community, and ultimately voted on by the PMC.

If you are interested in becoming a committer in the RocketMQ community, please actively engage with the community and contribute to Apache RocketMQ in any of the above ways

committer members in the community will be eager to share with you and give you advice and guidance as appropriate.

- [Request to answer questions](#contributionguide-01how-to-contribute--request-to-answer-questions)
- [Submitting an error report](#contributionguide-01how-to-contribute--submitting-an-error-report)
- [Propose improvements or new features](#contributionguide-01how-to-contribute--propose-improvements-or-new-features)
- [Participate in discussions and help others](#contributionguide-01how-to-contribute--participate-in-discussions-and-help-others)
- [Test pre-release versions](#contributionguide-01how-to-contribute--test-pre-release-versions)
- [Contribute code](#contributionguide-01how-to-contribute--contribute-code)
- [Contribution to the document](#contributionguide-01how-to-contribute--contribution-to-the-document)
- [Optimize the website](#contributionguide-01how-to-contribute--optimize-the-website)
- [More ways to contribute...](#contributionguide-01how-to-contribute--more-ways-to-contribute)
- [How do I become a committer](#contributionguide-01how-to-contribute--how-do-i-become-a-committer)

---

<a id="contributionguide-02code-guidelines"></a>

<!-- source_url: https://rocketmq.apache.org/docs/contributionGuide/02code-guidelines/ -->

<!-- page_index: 61 -->

# Code Guidelines

Version: 5.0

# Code Guidelines

<a id="contributionguide-02code-guidelines--introduction"></a>

## Introduction

This article introduces you to coding specifications and coding guidelines.

Research shows that 80% of software development time is spent on software maintenance, including source code interpretation, source code refactoring, source code maintenance, etc.

Agreeing on and enforcing code specifications and guidelines can help improve code readability, maintain code ownership by the development team,

help engineers understand new code quickly and deeply, and simplify maintenance costs.

<a id="contributionguide-02code-guidelines--idea-programming-template"></a>

## IDEA Programming Template

The following guides you to import the `rmq_codeStyle.xml` encoding specification file and `Apache.xml` contribution license file in IDEA.

<a id="contributionguide-02code-guidelines--import-code-style"></a>

### Import Code Style

1.File Path: `rocketmq/style/rmq_codestyle.xml`

2.Apple OS Import: `IntelliJ IDEA > File > Settings > Editor > Code Style` enter the `Code Style`, select the `Manage > Import` to import the `rmq_codestyle.xml` and name it `Scheme`

3.Windows OS Import: `IntelliJ IDEA > File > Settings > Editor > Code Style` enter the `Code Style`, select the `Show Scheme Actions > Import Scheme > Intellij IDEA code style XML` to import the `rmq_codestyle.xml`

![1656682140788](data:image/png;base64,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)

4.The imported `rmq_codeStyle.xml` specifies the code's indentation format, naming conventions, standard Java conventions, and so on

5.After IDEA is set, the code is automatically reformat to pass the code style validate of Travis CI

<a id="contributionguide-02code-guidelines--import-apache-v2"></a>

## Import Apache V2

1.File Path: `rocketmq/style/copyright/Apache.xml`

2.Import: `IntelliJ IDEA > File > Settings > Editor > Copyright > Copyright Profiles` enter the `Copyright Profiles`, select the `import` to import the `Apache.xml`

![1656683960857](assets/images/2-apachev2-540c72638cb4bd717aec875802b4a096_44077a0464524113.png)

3.License: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<a id="contributionguide-02code-guidelines--select-apache-copyright"></a>

## Select Apache Copyright

![1656684219109](data:image/png;base64,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)

Refer to [Five open source protocols(GPL,LGPL,BSD,MIT,Apache) - OSCHINA - Chinese open source technology exchange community](https://www.oschina.net/question/54100_9455) For details

<a id="contributionguide-02code-guidelines--remove-javadoc-label"></a>

## Remove Javadoc Label

1. select the `Settings > Editor > File and Code Templates > Includes`
2. enter the `File Header` , remove the Javadoc label from it

![1656684039505](data:image/png;base64,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)

- [Introduction](#contributionguide-02code-guidelines--introduction)
- [IDEA Programming Template](#contributionguide-02code-guidelines--idea-programming-template)
  - [Import Code Style](#contributionguide-02code-guidelines--import-code-style)
- [Import Apache V2](#contributionguide-02code-guidelines--import-apache-v2)
- [Select Apache Copyright](#contributionguide-02code-guidelines--select-apache-copyright)
- [Remove Javadoc Label](#contributionguide-02code-guidelines--remove-javadoc-label)

---

<a id="contributionguide-03pull-request"></a>

<!-- source_url: https://rocketmq.apache.org/docs/contributionGuide/03pull-request/ -->

<!-- page_index: 62 -->

# GitHub Submit PR

Version: 5.0

# GitHub Submit PR

This article walks you through contributing RocketMQ through Git

<a id="contributionguide-03pull-request--github-remote-repository"></a>

## GitHub Remote Repository

As a prerequisite, this section briefly explains the reasons for using Git to contribute RocketMQ. If you have related knowledge, you can skip it

First, you need to educate yourself about Git and GitHub

Think: From a developer's perspective, how do you collaborate with others to complete a project?

If you think of packaging, compression, and then copy and paste, think of expanding the scope of participants to the 10k+ level

This is the point of the remote repository: Developers can easily access the repository code from GitHub and submit development branches to the remote repository to communicate and share with others

![1656601484232](assets/images/1-github-84c9eac1be749cc78c0570e6e6b4fafe_2d5e50012483232c.png)

So, with this public repository, what then?

How do I download the code for a remote repository?

How do I commit a development branch to a remote repository?

<a id="contributionguide-03pull-request--git-contribution-guide"></a>

## Git Contribution Guide

① fork [apache/rocketmq](https://github.com/apache/rocketmq) to personal GitHub remote repository

```shell
https://github.com/cuser/rocketmq.git # cuser's rocketmq repo[repository] url
```

Notice: `cuser` GitHub username，after `Fork` you can find the copy repository through the personal home page Repositories, and view the address

② Install Git yourself and clone it to your local repository

```shell
git clone https://github.com/cuser/rocketmq.git # git clone [repo url]
```

Notice：The cloned local repository will use GitHub repository as the remote repository, and will be named `origin`

③ Get the latest code for the development branch

```shell
git rebase origin/develop # git rebase [branch]
```

Notice： [rebase `<branch>`](https://git-scm.com/docs/git-rebase) The basic term is base swapping, and you can see why this step is necessary by looking at the linked examples

④ Make changes in the local repository

```shell
git checkout -b RocketMQ-Vxx.0 # git checkout [-b] [new-branch]
git add /rocketmq/pom.xml # git add [dir/file]
git commit -a -m "pom"  # git commit [-all] [-msg] [message]
```

Notice： Reference [Git](https://git-scm.com/docs/git-add)，Use relative paths to switch to the same directory as `.git`

⑤ Push changes to the remote repository

```shell
git push --set-upstream apache RocketMQ-Vxx.0   # push branch to https://github.com/cuser/rocketmq-site.git
```

<a id="contributionguide-03pull-request--github-commit-pr"></a>

## GitHub Commit PR

As follows: Take submitting PR to the `new-official-website` branch as an example to illustrate the PR process

Reference `Git Contribution Guide`Modify the branch in the local repository and push it to the GitHub remote repository

```shell
git checkout new-official-website   # git checkout -b new-official-website
git push origin new-official-website    # push to https://github.com/cuser/rocketmq-site.git
```

① Switch the GitHub remote repository to the development branch new-official-website

② Create the pull request and click the open pull request under Contribute

③ compare across forks, Select the request branch and the development branch

![1656580236831](assets/images/2-compare-e6e43b6f317598e536eb244233a5e50e_c7f2195cde339c44.png)

base repository / base : Request repository and request branch

head repository / compare : Develop repository and branch

Be sure to correctly select the request branch and the development branch, and request merging only after obtaining permission from the branch owner

④ Fill in the PR summary with uppercase letters and briefly describe the PR content

![1656589498318](assets/images/3-write-531b30b458285686e95f5f1ad01f2f33_267fed9658345561.png)

Before submitting PR, please confirm as follows:

1. A [GitHub Issue]( [apache/rocketmq: Mirror of Apache RocketMQ (github.com)](https://github.com/apache/rocketmq/issues) ) corresponding to PR has been created
2. Modified content to comply with [Coding Guidelines](#contributionguide-02code-guidelines) programming specification
3. The PR summary begins with [ISSUE #XXX] and briefly describes the change requirements
4. Outline PR change requirements, change logs, and validation information,Reference [PR Demo](https://github.com/apache/rocketmq/pull/152)
5. Submit content with complete test cases and ensure that basic checks, unit tests, and integration tests pass

⑤ Click "Create pull request" , Request that the branch be merged

⑥ At this point, the PR is visible on the apache/rocketmq-site remote repository, and all collaborators can review the PR and make suggestions

You can make changes locally and commit multiple times based on comments. Information about the request to merge and the submission of changes is displayed simultaneously on the PR page, the issue list, and the RocketMQ mailing list, in order to remind the committer to review the PR in a timely manner

<a id="contributionguide-03pull-request--merge-pr"></a>

## Merge PR

Open source Project development branch mergers are performed by the committer.

① Merge contributor PR

```shell
git checkout develop    # switch to local develop branch
git pull apache develop # fast-forward to current remote HEAD
git pull --squash https://github.com/cuser/rocketmq.git RocketMQ-Vxx.0  # merge to branch
```

A pull request merge branch may contain multiple commits. It is recommended that the `--squash` directive compress the commit to a single commit

It is important to resolve merge conflicts and ensure that the current branch is synchronized to the remote branch before merging

Please read[Git pull]( [Git - git-pull Documentation (git-scm.com)](https://git-scm.com/docs/git-pull) ) to learn fast-forward and other info

② Merge committer PR

If committer merges its own PR, run the command [Git merge]( [Git - git-merge Documentation (git-scm.com)](https://git-scm.com/docs/git-merge) )

```shell
git checkout develop      # switch to local develop branch
git pull apache develop   # fast-forward to current remote HEAD
git merge --squash RocketMQ-Vxx.0   # merge to branch
```

③ Do regular patch checks, build projects with built-in test cases, and be sure to modify the changelog

④ Once all of the above is done, submit the merge with the following instructions, feedback the branch status to the developer, and close PR

```shell
git commit --author="contributor_name <contributor_email>" -a -m "RocketMQ-Vxx.0 description closes apache/rocketmq#ZZ"
```

For details of closing PR, reference [Close PR](https://docs.github.com/cn/issues/tracking-your-work-with-issues/closing-an-issue)

⑤ Push the merged branch to the apache/rocketmq remote repository

```shell
git push apache develop
```

⑥ Once a PR is submitted, it will remain in the GitHub remote repository, and you can also update your personal GitHub repository simultaneously

```shell
git push origin develop
```

Notice: squash discards the commit information of the development branch

<a id="contributionguide-03pull-request--reject-pr"></a>

## Reject PR

Reject PR: Means that no pull or merge is performed, but only the reject PR message is submitted

```SHELL
git commit --allow-empty -m "RocketMQ-Vxx.0 closes apache/rocketmq#ZZ *Won't fix*"
git push apache develop
```

Close PR #ZZ on GitHub

- [GitHub Remote Repository](#contributionguide-03pull-request--github-remote-repository)
- [Git Contribution Guide](#contributionguide-03pull-request--git-contribution-guide)
- [GitHub Commit PR](#contributionguide-03pull-request--github-commit-pr)
- [Merge PR](#contributionguide-03pull-request--merge-pr)
- [Reject PR](#contributionguide-03pull-request--reject-pr)

---

<a id="contributionguide-04release-manual"></a>

<!-- source_url: https://rocketmq.apache.org/docs/contributionGuide/04release-manual/ -->

<!-- page_index: 63 -->

# Release Manual

Version: 5.0

# Release Manual

<a id="contributionguide-04release-manual--1-introduction"></a>

## 1. Introduction

<a id="contributionguide-04release-manual--11-apache-release-documentation"></a>

#### 1.1 Apache release documentation

Refer to the following link to understand the ASF release process：

- [Apache Release Guide](http://www.apache.org/dev/release-publishing)
- [Apache Release Policy](http://www.apache.org/dev/release.html)
- [Maven Release Info](http://www.apache.org/dev/publishing-maven-artifacts.html)

<a id="contributionguide-04release-manual--12-pgp-signature"></a>

#### 1.2 PGP signature

Follow the Apache release guidelines to sign the release version, users can also use this to determine if the downloaded version has been tampered with.

Create a `pgp` key for version signing, use **\<your Apache ID>@apache.org** as the USER-ID for the key

For more details, refer to [Apache Releases Signing documentation](https://infra.apache.org/release-signing)，[Cryptography with OpenPGP](http://www.apache.org/dev/openpgp.html)

Brief process for generating a key：

- Generate a new `gpg` key using `gpg --gen-key`, set the key length to 4096 and set it to never expire
- Upload the key to the public key server using `gpg --keyserver keys.openpgp.org --send-key <your key id>`
- Export the public key to a text file using `gpg --armor --export <your key id> >> gpgapachekey.txt`
- Obtain the keys of other committers for signing (optional)
- Add the generated key to the [KEYS file](https://dist.apache.org/repos/dist/dev/rocketmq/KEYS) (uploaded to the svn repository by the release manager)

> [!TIP]
> Set the default public key. If you have multiple public keys, modify `~/.gnupg/gpg.conf`.

Refer to the example：

```shell
[root@localhost ~]# gpg --gen-key
gpg (GnuPG) 2.0.22; Copyright (C) 2013 Free Software Foundation, Inc.
...
# secret key generation directory gpg: directory `/root/.gnupg' created gpg: new configuration file `/root/.gnupg/gpg.conf' created gpg: WARNING: options in `/root/.gnupg/gpg.conf' are not yet active during this run gpg: keyring `/root/.gnupg/secring.gpg' created gpg: keyring `/root/.gnupg/pubring.gpg' created Please select what kind of key you want:(1) RSA and RSA (default) (2) DSA and Elgamal (3) DSA (sign only) (4) RSA (sign only) Your selection? RSA keys may be between 1024 and 4096 bits long. What keysize do you want? (2048) 4096 Requested keysize is 4096 bits Please specify how long the key should be valid. 0 = key does not expire <n> = key expires in n days <n>w = key expires in n weeks <n>m = key expires in n months <n>y = key expires in n years Key is valid for? (0) Key does not expire at all Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.
# set USER-ID Real name: rocketmq Email address: rocketmq@apache.org Comment: rocketmq You selected this USER-ID:"rocketmq (rocketmq) <rocketmq@apache.org>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

...
gpg: /root/.gnupg/trustdb.gpg: trustdb created
gpg: key 7DE280AF marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   4096R/7DE280AF 2022-07-05
      Key fingerprint = 421D C10E 9CC3 D261 9F89  C777 86BB 17AA 7DE2 80AF
uid                  rocketmq (rocketmq) <rocketmq@apache.org>
sub   4096R/65B9828A 2022-07-05
```

The generated public and private key addresses：

```shell
gpg: keyring `/root/.gnupg/secring.gpg' created
gpg: keyring `/root/.gnupg/pubring.gpg' created
```

Convert the generated public and private keys to ASCII form：

```shell
gpg --armor --output /root/gpgtest/public-key.txt --export 7DE280AF
gpg --armor --output /root/gpgtest/private-key.txt --export-secret-keys 7DE280AF
```

View the key list：

```shell
[root@localhost ~]# gpg --list-keys
/root/.gnupg/pubring.gpg
------------------------
pub   4096R/7DE280AF 2022-07-05
uid                  rocketmq (rocketmq) <rocketmq@apache.org>
sub   4096R/65B9828A 2022-07-05
```

Upload the public key to the public key server

```shell
[root@localhost gpgtest]# gpg --keyserver keys.openpgp.org --send-key 7DE280AF
gpg: sending key 7DE280AF to hkp server keys.openpgp.org
```

<a id="contributionguide-04release-manual--13-pom-setting"></a>

#### 1.3 POM setting

Configure the POM file to deploy the version to the ASF Nexus repository.

① Add Apache POM inheritance default settings

```XML
<parent>
    <groupId>org.apache</groupId>
    <artifactId>apache</artifactId>
    <version>XX</version>
</parent>
```

② Add key information to the Maven configuration file `settings.xml`.

```xml
<settings>
    <profiles>
        <profile>
            <id>signed_release</id>
            <properties>
                <mavenExecutorId>forked-path</mavenExecutorId>
                <gpg.keyname>yourKeyName</gpg.keyname>
                <deploy.url>https://dist.apache.org/repos/dist/dev/rocketmq/</deploy.url>
            </properties>
        </profile>
    </profiles>
    <servers>
        <!-- To publish a snapshot of some part of Maven -->
        <server>
            <id>apache.snapshots.https</id>
            <username>yourApacheID</username>
            <!-- Use the password encryption by maven -->
            <password>yourApachePassword</password>
        </server>
        <!-- To stage a release of some part of Maven -->
        <server>
            <id>apache.releases.https</id>
            <username>yourApacheID</username>
            <password>yourApachePassword</password>
        </server>
        <server>
            <id>gpg.passphrase</id>
            <passphrase>yourKeyPassword</passphrase>
        </server>
    </servers>
</settings>
```

> [!TIP]
> It is recommended to use [Maven's password encryption capabilities](http://maven.apache.org/guides/mini/guide-encryption.html) to encrypt `gpg.passphrase`.

③ Build artifacts and sign

```shell
mvn clean install -Papache-release
```

<a id="contributionguide-04release-manual--14-deal-with-issues"></a>

#### 1.4 Deal with issues

Resolve JIRA issues and GitHub issues related to this release version.

Check that MQVersion is consistent with the released version.

<a id="contributionguide-04release-manual--15-release-notes"></a>

#### 1.5 Release Notes

Generate Release Notes through [RocketMQ JIRA](https://issues.apache.org/jira/browse/ROCKETMQ/) and push to [rocketmq-site](https://github.com/apache/rocketmq-site), adding a link to the version voting email.

<a id="contributionguide-04release-manual--2-build-source-release"></a>

## 2. Build Source Release

Use the [Maven Release plugin](https://maven.apache.org/maven-release/maven-release-plugin/) version release plugin to release the Artifact to the ASF Nexus staging repository, and after version validation and version voting, copy it to the Apache SVN version repository.

<a id="contributionguide-04release-manual--21-check-rocketmq-version"></a>

#### 2.1 Check RocketMQ version

Confirm the MQVersion version and modify it to the correct form if it does not match the `release-4.5.0` form or is inconsistent, and push it to the `develop` branch.

```java
public static final int CURRENT_VERSION = Version.V4_5_0.ordinal();
```

<a id="contributionguide-04release-manual--22-staging-in-the-asf-nexus-repository"></a>

#### 2.2 Staging in the ASF Nexus repository

1. Switch to the `develop` branch and confirm that all GitHub PRs related to this version have been merged.

① Configure the `pom.xml` file

```xml
<scm>
    <url>git@github.com:apache/rocketmq.git</url>
    <connection>scm:git:git@github.com:apache/rocketmq.git</connection>
    <developerConnection>scm:git:git@github.com:apache/rocketmq.git</developerConnection>
    <tag>rocketmq-all-x.x.x</tag>
</scm>
```

② maven release plugin

```shell
mvn release:clean
mvn release:prepare
mvn release:perform
```

Follow this process to place the generated Artifacts in the staging repository.：

1. `mvn clean release:clean`: Clear failed builds and discarded versions.
2. `mvn release:prepare -Psigned_release -Darguments="-DskipTests"`：Update the tag based on the `SCM` property.
3. `mvn -Psigned_release release:perform -Darguments="-DskipTests"`：Stage the generated artifacts to the [Nexus repo](https://repository.apache.org/#stagingRepositories). You can add the `-DdryRun=true` parameter to perform a dry run.

After completing the above process, you can find the pre-release version Artifacts in the `target` directory of the local branch or in the [Nexus staging repo](https://repository.apache.org/#stagingRepositories).

> [!TIP]
> To only release the source code version, only keep the source code and related jar files, and use the `delete` option in the Nexus GUI to delete the other artifacts.

<a id="contributionguide-04release-manual--23-rc-version-files"></a>

#### 2.3 rc version files

- Before the pre-release version vote is passed, it will be staged in [/dev/rocketmq](https://dist.apache.org/repos/dist/dev/rocketmq/) and stored in the `x.x.x-rcx/` directory. The following files are required：

  > rocketmq-all-x1.x2.x3-bin-release.zip
  >
  > rocketmq-all-x1.x2.x3-bin-release.zip.asc
  >
  > rocketmq-all-x1.x2.x3-bin-release.zip.sha512
  >
  > rocketmq-all-x1.x2.x3-source-release.zip
  >
  > rocketmq-all-x1.x2.x3-source-release.zip.asc
  >
  > rocketmq-all-x1.x2.x3-source-release.zip.sha512

Generate signature and verification files using the `gpg` command：

- Generate `asc` file


```text
gpg --clearsign rocketmq-all-x1.x2.x3-bin-release.zip
gpg --clearsign rocketmq-all-x1.x2.x3-source-release.zip
```

- Generate `sha512` file


```text
gpg --print-md SHA512 rocketmq-all-x1.x2.x3-bin-release.zip > rocketmq-all-x1.x2.x3-bin-release.zip.sha512
gpg --print-md SHA512 rocketmq-all-x1.x2.x3-source-release.zip >  rocketmq-all-x1.x2.x3-source-release.zip.sha512
```

> [!TIP]
> The source code and binary versions should begin with `rocketmq-all` to facilitate the [RocketMQ Docker Build](https://github.com/apache/rocketmq-docker/blob/a2672f62cc5171263ffc856ab5657291efba1912/image-build/Dockerfile-centos#L58-L59).

<a id="contributionguide-04release-manual--24-roll-back-and-retry"></a>

#### 2.4 Roll back and retry

If there are problems with the staging process, roll back according to the following process：

- Delete the tag created in step 2.2

  - List all tags and find the most recently created one


```text
git tag -ln
```

  - Delete the tag from the local repository


```text
git tag -d rocketmq-all-x1.x2.x3
```

  - Push the update to GitHub


```text
git push origin :refs/tags/rocketmq-all-x1.x2.x3
```

- Delete the commit records in the development branch from step 2.2

  - List the git log


```text
git log
```

  - Find the most recent commit record and label it as follows：

    > des1: [maven-release-plugin] prepare release rocketmq-all-4.9.2]
    >
    > des2: [maven-release-plugin] prepare for next development iteration]
  - Delete commits


```text
git reset --hard commit-id
git push origin HEAD --force
```

- Delete the version to be rolled back in [Nexus](https://repository.apache.org/#welcome)
- Roll back to step 2.1 and redo

<a id="contributionguide-04release-manual--3-build-binary-release"></a>

## 3. Build binary release

Both the binary and source code versions are built from the same code branch, but you should be aware of the operating system version.

Some dependencies, such as `netty tc-native`, are sensitive to the operating system.

- Make sure you check out the pre-release version branch
- Make sure all unit tests pass with `mvn clean install`
- Make sure all integration tests pass with `mvn clean install -Pit-test`

After successful build, you also need to generate .asc and .sha512 files, and after verification and voting, finally copy them to the [svn](https://dist.apache.org/repos/dist/release/rocketmq/) repository.

<a id="contributionguide-04release-manual--4-version-verification"></a>

## 4. Version Verification

<a id="contributionguide-04release-manual--41-binary-release-verification-checklist"></a>

#### 4.1 Binary Release Verification Checklist

- Check the operating system for the build dependencies, netty-tcnative is sensitive to the operating system
- Ensure the license is Apache V2
- If third-party dependencies are introduced, update the NOTICE
- Extract the compressed file to check that the version is correct
- Validate the ASC signature, SHA512 digest
- Run the Quick-Start to start the nameserver and broker
- Run the clusterList command to check that the version is correct
- Make sure there are no nohup.out files

<a id="contributionguide-04release-manual--42-source-release-verification-checklist"></a>

#### 4.2 Source Release Verification Checklist

- Ensure the license is Apache V2
- If third-party dependencies are introduced, update the NOTICE
- Extract the compressed file to check that the version is correct
- Validate the ASC signature, SHA512 digest
- Compile the source code and run the Quick-Start to start the nameserver and broker
- Run the clusterList command to check the version is correct

<a id="contributionguide-04release-manual--43-verification-tool"></a>

#### 4.3 Verification tool

Follow the steps below to verify the GPG signature and SHA512 digest.

1. Download the release packages, the `.asc` file, and the `.sha512` file.
2. On a Unix system, run the following command：


```shell
for file in `find . -type f -iname '*.asc'`
do
    gpg --verify ${file}
done
```

   or


```shell
gpg --verify rocketmq-all-%version-number%-source-release.zip.asc rocketmq-all-%version-number%-bin-release.zip
```

   If you see `Good signature`, the signature is correct.


```text
gpg: Good signature from ... gpg: Signature made ...
```

3. Verify the consistency of the version based on the SHA512.


```shell
gpg --print-md SHA512 rocketmq-all-%version-number%-source-release.zip
gpg --print-md SHA512 rocketmq-all-%version-number%-bin-release.zip
```

<a id="contributionguide-04release-manual--5-close-staging-repo"></a>

## 5. Close staging repo

1. After the pre-release version has completed the checklist verification, close the Nexus staging repository and prepare for the version election.
2. Select the `orgapacherocketmq-XXX` pending release version on Nexus and click the `Close` icon to close the staging repository.
3. Before closing, Nexus will perform a series of signature verifications and text checks.
4. If the verification is successful, Nexus will close the repository and provide the staging repository URL, which is marked as "The staging repo" in the election email.
5. If the verification fails, fix the issues, roll back, and re-execute the release process.
6. If all of the above work is complete, use SVN to copy it to the [/dev/rocketmq](https://dist.apache.org/repos/dist/dev/rocketmq/) Apache remote repository.

<a id="contributionguide-04release-manual--6-version-election"></a>

## 6. Version election

The RocketMQ community conducts version elections through the **[dev@rocketmq.apache.org](mailto:dev@rocketmq.apache.org)** email list.

Refer to the [voting process](http://www.apache.org/foundation/voting.html) to understand the Apache voting process.

<a id="contributionguide-04release-manual--61-community-voting"></a>

### 6.1 Community voting

Email list：[dev list](mailto:dev@rocketmq.apache.org)

Email topic：**[VOTE]: Release Apache RocketMQ \<release-version> RC\<RC Number>**

> Hello RocketMQ Community,
>
> This is the vote for \<release version> of Apache RocketMQ.
>
> ${A brief introduction to RocketMQ and the features of this release.}
>
> **The artifacts:**
>
> [https://dist.apache.org/repos/dist/dev/rocketmq/${release](https://dist.apache.org/repos/dist/dev/rocketmq/$%7Brelease) version}
>
> **The staging repo:**
>
> <https://repository.apache.org/content/repositories/orgapacherocketmq-XXX/>
>
> **Git tag for the release:**
>
> \<link to the tag of GitHub repo>
>
> **Hash for the release tag:**
>
> \<Hash value of the release tag>
>
> **Release Notes:**
>
> \<insert link to the rocketmq release notes>
>
> The artifacts have been signed with Key : \<ID of signing key>, which can be found in the keys file:
>
> <https://dist.apache.org/repos/dist/dev/rocketmq/KEYS>
>
> The vote will be open for at least 72 hours or until necessary number of votes are reached.
>
> Please vote accordingly:
>
> [ ] +1 approve
>
> [ ] +0 no opinion
>
> [ ] -1 disapprove with the reason
>
> Thanks,
>
> The Apache RocketMQ Team

> [!TIP]
> Hash for the release tag: You can use the commit id.

<a id="contributionguide-04release-manual--62-result-announced"></a>

### 6.2 Result announced

After 72 hours, if there are at least 3 votes in favor and no votes against, send the following email to celebrate the release of the version.

Email topic：**[RESULT][VOTE]: Release Apache RocketMQ \<release-version> RC\<RC Number>**

> Hello RocketMQ Community,
>
> The Apache RocketMQ `<release version>` vote is now closed and has passed with [number] binding +1s, [number] non-binding +1s and no 0 or -1:
>
> **Binding votes +1s:**
>
> User Name (Apache ID)
>
> User Name (Apache ID)
>
> User Name (Apache ID)
>
> ....
>
> **Non-binding votes +1s:**
>
> User Name (Apache ID)
>
> ....
>
> The release will be published soon.
>
> Thanks,
>
> The Apache RocketMQ Team

If the vote does not pass, fix the issues, roll back, increase the RC number, restart the release process, and re-initiate the version voting process.

Update email topic：**[RESTART][VOTE][#]: Release Apache RocketMQ \<release-version> RC\<RC Number>**

<a id="contributionguide-04release-manual--7-release-version"></a>

## 7. Release version

After the Apache RocketMQ PMC vote passes, release the version to the Maven Nexus repository and the Apache version repository.

1. Publish to Nexus repository, select the **orgapacherocketmq-XXX** in the staging area and click the `Release` icon to publish.
2. Publish to the Apache version repository, use SVN to copy the version to [/release/rocketmq](https://dist.apache.org/repos/dist/release/rocketmq/)
3. Merge the `develop` branch of [Apache RocketMQ](https://github.com/apache/rocketmq) into the `master` branch.
4. Add release notes to [Releases · apache/rocketmq](https://github.com/apache/rocketmq/releases).
5. Create a new branch and name it `release-x.x.x`.
6. Update [apache/rocketmq-site](https://github.com/apache/rocketmq-site) Official Website Home Page
   - Add release note，refer to [4.9.3 release notes](https://github.com/apache/rocketmq-site/commit/4b662a197a0a77fd460614df9e231e6ffdd7c622)
   - Update release note，refer to [docs updates for 4.9.3](https://github.com/apache/rocketmq-site/commit/0fd4d231c06f1d641a0cc30f8ffe22775043e89d)

<a id="contributionguide-04release-manual--8-version-announcement"></a>

## 8. Version announcement

Email list：**[announce@apache.org](mailto:announce@apache.org)**, **[users@rocketmq.apache.org](mailto:users@rocketmq.apache.org)**,

**[private@rocketmq.apache.org](mailto:private@rocketmq.apache.org)**, **[dev@rocketmq.apache.org](mailto:dev@rocketmq.apache.org)**

Email topic： **[ANNOUNCE] Release Apache RocketMQ \<release-version>**

> Hi all,
>
> The Apache RocketMQ team would like to announce the release of Apache RocketMQ \<release version>.
>
> ${A brief introduction to RocketMQ and the features of this release.}
>
> More details regarding Apache RocketMQ can be found at:
>
> <http://rocketmq.apache.org/>
>
> The release artifacts can be downloaded here:
>
> [https://dist.apache.org/repos/dist/release/rocketmq/${release-version}](https://dist.apache.org/repos/dist/release/rocketmq/$%7Brelease-version%7D)
>
> The release notes can be found here:
>
> \<insert link to the rocketmq release notes>
>
> Thanks,
>
> The Apache RocketMQ Team

- [1. Introduction](#contributionguide-04release-manual--1-introduction)
- [2. Build Source Release](#contributionguide-04release-manual--2-build-source-release)
- [3. Build binary release](#contributionguide-04release-manual--3-build-binary-release)
- [4. Version Verification](#contributionguide-04release-manual--4-version-verification)
- [5. Close staging repo](#contributionguide-04release-manual--5-close-staging-repo)
- [6. Version election](#contributionguide-04release-manual--6-version-election)
  - [6.1 Community voting](#contributionguide-04release-manual--61-community-voting)
  - [6.2 Result announced](#contributionguide-04release-manual--62-result-announced)
- [7. Release version](#contributionguide-04release-manual--7-release-version)
- [8. Version announcement](#contributionguide-04release-manual--8-version-announcement)

---

<a id="security-01security"></a>

<!-- source_url: https://rocketmq.apache.org/docs/security/01security/ -->

<!-- page_index: 64 -->

# Security

Version: 5.0

# Security

<a id="security-01security--security-model"></a>

## Security Model

The Apache RocketMQ project itself provides security features such as ACL and TLS, but the final security effectiveness still depends on the operator's comprehensive protection of **network, hosts, accounts, and data**.

> **Important Note (Security Deployment Baseline)**: RocketMQ's authentication/authorization capabilities rely on ACL configuration. If ACL is not enabled/configured, RocketMQ will not enforce client identity verification at the protocol layer. Any entity that can access RocketMQ ports may initiate message sending/receiving or management operations.
> **Operators must**: Either enable and properly configure ACL (authentication + authorization), or strictly restrict RocketMQ components and ports within a trusted network (intranet/VPC/private network), rather than exposing them to untrusted networks.

<a id="security-01security--1-authentication-and-authorization-acl"></a>

### 1. Authentication and Authorization (ACL)

- ACL 1.0 has been supported since RocketMQ 4.4.0
- The more secure **ACL 2.0** was introduced in 5.3.0
- ACL 1.0 was removed in 5.3.3
- It is recommended that all users who use Apache RocketMQ ACL migrate to **ACL 2.0**

ACL is used for **authentication** and **authorization** control of RocketMQ requests. For production environments, it is recommended to:

- Enable ACL (authentication/authorization) unless RocketMQ is strictly isolated within a trusted network, and configure accounts with minimum privileges for applications
- Avoid using administrator accounts in business applications; implement tiered access keys, regular rotation, and audit changes

<a id="security-01security--2-dashboard-observability-exposure"></a>

### 2. Dashboard & Observability Exposure

RocketMQ Dashboard and some observability components (such as RocketMQ Prometheus Exporter) do **not** enable strong authentication by default; anyone who can access the HTTP port can read cluster metadata. Strongly recommended:

- Bind the Dashboard listening address to the intranet or a trusted VPC
- Configure ACL / IP allow-lists on the gateway / Ingress / reverse proxy
- If public-network operation and maintenance is required, be sure to add a VPN, HTTP Basic/OAuth authentication, or a WAF

> Otherwise, information-leakage risks may occur; such risks are the responsibility of the deployment side rather than RocketMQ vulnerabilities.

<a id="security-01security--3-transport-encryption-and-data-encryption"></a>

### 3. Transport Encryption and Data Encryption

- Clients and servers can communicate through **TLS** encryption; enable it if sensitive data is involved
- The message body is defined by the business; RocketMQ will **not** parse or persist decrypted content
- If messages contain sensitive information, perform field-level or overall encryption on the business side to avoid storing plaintext

<a id="security-01security--4-serialization-and-deserialization-risks"></a>

### 4. Serialization and Deserialization Risks

- RocketMQ only transmits byte arrays and does **not** perform object deserialization
- If consumers need to deserialize, they should choose secure formats (such as **JSON-Binding, Protobuf** etc.) and validate untrusted data

<a id="security-01security--5-sdk-and-version-management"></a>

### 5. SDK and Version Management

- Always use the latest official stable client to obtain the latest vulnerability fixes and improvements

<a id="security-01security--6-log-management"></a>

### 6. Log Management

- Properly keep RocketMQ-related logs (including **Broker, NameServer, Proxy, Client**, etc.) to avoid leakage of sensitive information

<a id="security-01security--security-policy"></a>

## Security Policy

Apache RocketMQ is a project of the Apache Software Foundation (ASF) and follows the ASF vulnerability handling process.

<a id="security-01security--reporting-a-vulnerability"></a>

### Reporting a Vulnerability

To report a new vulnerability you have discovered, please follow the ASF vulnerability reporting process:
<https://apache.org/security/#reporting-a-vulnerability>

To help us assess and address the issue, please include the affected component(s)/version(s), reproduction steps, impact analysis, and a PoC if available.

> Please do not disclose exploitable details via public issues, mailing lists, or social media before a fix is available.

<a id="security-01security--faq-regarding-no-authentication-requiredaccessible-when-acl-is-not-enabled"></a>

### FAQ: Regarding "No Authentication Required/Accessible When ACL is Not Enabled"

RocketMQ's authentication and authorization capabilities are provided by ACL; whether to enable it depends on deployment and configuration.
When ACL is not enabled or not configured, requests may be processed without identity verification. This is a deployment/configuration choice. Operators should enable ACL based on their threat model and ensure security through network isolation and other means.

- [Security Model](#security-01security--security-model)
  - [1. Authentication and Authorization (ACL)](#security-01security--1-authentication-and-authorization-acl)
  - [2. Dashboard & Observability Exposure](#security-01security--2-dashboard-observability-exposure)
  - [3. Transport Encryption and Data Encryption](#security-01security--3-transport-encryption-and-data-encryption)
  - [4. Serialization and Deserialization Risks](#security-01security--4-serialization-and-deserialization-risks)
  - [5. SDK and Version Management](#security-01security--5-sdk-and-version-management)
  - [6. Log Management](#security-01security--6-log-management)
- [Security Policy](#security-01security--security-policy)
  - [Reporting a Vulnerability](#security-01security--reporting-a-vulnerability)
  - [FAQ: Regarding "No Authentication Required/Accessible When ACL is Not Enabled"](#security-01security--faq-regarding-no-authentication-requiredaccessible-when-acl-is-not-enabled)

---
