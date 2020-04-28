// Copyright 2018-2020 Polyaxon, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/* tslint:disable */
/* eslint-disable */
/**
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.0.83
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    SparkDeployMode,
    SparkDeployModeFromJSON,
    SparkDeployModeFromJSONTyped,
    SparkDeployModeToJSON,
    V1SparkReplica,
    V1SparkReplicaFromJSON,
    V1SparkReplicaFromJSONTyped,
    V1SparkReplicaToJSON,
    V1SparkType,
    V1SparkTypeFromJSON,
    V1SparkTypeFromJSONTyped,
    V1SparkTypeToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1Spark
 */
export interface V1Spark {
    /**
     * 
     * @type {string}
     * @memberof V1Spark
     */
    kind?: string;
    /**
     * 
     * @type {Array<string>}
     * @memberof V1Spark
     */
    connections?: Array<string>;
    /**
     * Volumes is a list of volumes that can be mounted.
     * @type {Array<object>}
     * @memberof V1Spark
     */
    volumes?: Array<object>;
    /**
     * 
     * @type {V1SparkType}
     * @memberof V1Spark
     */
    type?: V1SparkType;
    /**
     * Spark version is the version of Spark the application uses.
     * @type {string}
     * @memberof V1Spark
     */
    spark_version?: string;
    /**
     * Spark version is the version of Spark the application uses.
     * @type {string}
     * @memberof V1Spark
     */
    python_version?: string;
    /**
     * 
     * @type {SparkDeployMode}
     * @memberof V1Spark
     */
    deploy_mode?: SparkDeployMode;
    /**
     * MainClass is the fully-qualified main class of the Spark application. This only applies to Java/Scala Spark applications.
     * @type {string}
     * @memberof V1Spark
     */
    main_class?: string;
    /**
     * MainFile is the path to a bundled JAR, Python, or R file of the application.
     * @type {string}
     * @memberof V1Spark
     */
    main_application_file?: string;
    /**
     * Arguments is a list of arguments to be passed to the application.
     * @type {Array<string>}
     * @memberof V1Spark
     */
    arguments?: Array<string>;
    /**
     * HadoopConf carries user-specified Hadoop configuration properties as they would use the  the \"--conf\" option in spark-submit.  The SparkApplication controller automatically adds prefix \"spark.hadoop.\" to Hadoop configuration properties.
     * @type {{ [key: string]: string; }}
     * @memberof V1Spark
     */
    hadoop_conf?: { [key: string]: string; };
    /**
     * HadoopConf carries user-specified Hadoop configuration properties as they would use the  the \"--conf\" option in spark-submit.  The SparkApplication controller automatically adds prefix \"spark.hadoop.\" to Hadoop configuration properties.
     * @type {{ [key: string]: string; }}
     * @memberof V1Spark
     */
    spark_conf?: { [key: string]: string; };
    /**
     * SparkConfigMap carries the name of the ConfigMap containing Spark configuration files such as log4j.properties. The controller will add environment variable SPARK_CONF_DIR to the path where the ConfigMap is mounted to.
     * @type {string}
     * @memberof V1Spark
     */
    spark_config_map?: string;
    /**
     * HadoopConfigMap carries the name of the ConfigMap containing Hadoop configuration files such as core-site.xml. The controller will add environment variable HADOOP_CONF_DIR to the path where the ConfigMap is mounted to.
     * @type {string}
     * @memberof V1Spark
     */
    hadoop_config_map?: string;
    /**
     * 
     * @type {V1SparkReplica}
     * @memberof V1Spark
     */
    executor?: V1SparkReplica;
    /**
     * 
     * @type {V1SparkReplica}
     * @memberof V1Spark
     */
    driver?: V1SparkReplica;
}

export function V1SparkFromJSON(json: any): V1Spark {
    return V1SparkFromJSONTyped(json, false);
}

export function V1SparkFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1Spark {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'kind': !exists(json, 'kind') ? undefined : json['kind'],
        'connections': !exists(json, 'connections') ? undefined : json['connections'],
        'volumes': !exists(json, 'volumes') ? undefined : json['volumes'],
        'type': !exists(json, 'type') ? undefined : V1SparkTypeFromJSON(json['type']),
        'spark_version': !exists(json, 'spark_version') ? undefined : json['spark_version'],
        'python_version': !exists(json, 'python_version') ? undefined : json['python_version'],
        'deploy_mode': !exists(json, 'deploy_mode') ? undefined : SparkDeployModeFromJSON(json['deploy_mode']),
        'main_class': !exists(json, 'main_class') ? undefined : json['main_class'],
        'main_application_file': !exists(json, 'main_application_file') ? undefined : json['main_application_file'],
        'arguments': !exists(json, 'arguments') ? undefined : json['arguments'],
        'hadoop_conf': !exists(json, 'hadoop_conf') ? undefined : json['hadoop_conf'],
        'spark_conf': !exists(json, 'spark_conf') ? undefined : json['spark_conf'],
        'spark_config_map': !exists(json, 'spark_config_map') ? undefined : json['spark_config_map'],
        'hadoop_config_map': !exists(json, 'hadoop_config_map') ? undefined : json['hadoop_config_map'],
        'executor': !exists(json, 'executor') ? undefined : V1SparkReplicaFromJSON(json['executor']),
        'driver': !exists(json, 'driver') ? undefined : V1SparkReplicaFromJSON(json['driver']),
    };
}

export function V1SparkToJSON(value?: V1Spark | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'kind': value.kind,
        'connections': value.connections,
        'volumes': value.volumes,
        'type': V1SparkTypeToJSON(value.type),
        'spark_version': value.spark_version,
        'python_version': value.python_version,
        'deploy_mode': SparkDeployModeToJSON(value.deploy_mode),
        'main_class': value.main_class,
        'main_application_file': value.main_application_file,
        'arguments': value.arguments,
        'hadoop_conf': value.hadoop_conf,
        'spark_conf': value.spark_conf,
        'spark_config_map': value.spark_config_map,
        'hadoop_config_map': value.hadoop_config_map,
        'executor': V1SparkReplicaToJSON(value.executor),
        'driver': V1SparkReplicaToJSON(value.driver),
    };
}


