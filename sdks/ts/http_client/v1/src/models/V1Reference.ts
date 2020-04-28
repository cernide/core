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
    V1DagReference,
    V1DagReferenceFromJSON,
    V1DagReferenceFromJSONTyped,
    V1DagReferenceToJSON,
    V1HubReference,
    V1HubReferenceFromJSON,
    V1HubReferenceFromJSONTyped,
    V1HubReferenceToJSON,
    V1PathReference,
    V1PathReferenceFromJSON,
    V1PathReferenceFromJSONTyped,
    V1PathReferenceToJSON,
    V1UrlReference,
    V1UrlReferenceFromJSON,
    V1UrlReferenceFromJSONTyped,
    V1UrlReferenceToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1Reference
 */
export interface V1Reference {
    /**
     * 
     * @type {V1HubReference}
     * @memberof V1Reference
     */
    hub_reference?: V1HubReference;
    /**
     * 
     * @type {V1DagReference}
     * @memberof V1Reference
     */
    dag_reference?: V1DagReference;
    /**
     * 
     * @type {V1UrlReference}
     * @memberof V1Reference
     */
    url_reference?: V1UrlReference;
    /**
     * 
     * @type {V1PathReference}
     * @memberof V1Reference
     */
    path_reference?: V1PathReference;
}

export function V1ReferenceFromJSON(json: any): V1Reference {
    return V1ReferenceFromJSONTyped(json, false);
}

export function V1ReferenceFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1Reference {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'hub_reference': !exists(json, 'hub_reference') ? undefined : V1HubReferenceFromJSON(json['hub_reference']),
        'dag_reference': !exists(json, 'dag_reference') ? undefined : V1DagReferenceFromJSON(json['dag_reference']),
        'url_reference': !exists(json, 'url_reference') ? undefined : V1UrlReferenceFromJSON(json['url_reference']),
        'path_reference': !exists(json, 'path_reference') ? undefined : V1PathReferenceFromJSON(json['path_reference']),
    };
}

export function V1ReferenceToJSON(value?: V1Reference | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'hub_reference': V1HubReferenceToJSON(value.hub_reference),
        'dag_reference': V1DagReferenceToJSON(value.dag_reference),
        'url_reference': V1UrlReferenceToJSON(value.url_reference),
        'path_reference': V1PathReferenceToJSON(value.path_reference),
    };
}


