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
    V1CronSchedule,
    V1CronScheduleFromJSON,
    V1CronScheduleFromJSONTyped,
    V1CronScheduleToJSON,
    V1ExactTimeSchedule,
    V1ExactTimeScheduleFromJSON,
    V1ExactTimeScheduleFromJSONTyped,
    V1ExactTimeScheduleToJSON,
    V1IntervalSchedule,
    V1IntervalScheduleFromJSON,
    V1IntervalScheduleFromJSONTyped,
    V1IntervalScheduleToJSON,
    V1RepeatableSchedule,
    V1RepeatableScheduleFromJSON,
    V1RepeatableScheduleFromJSONTyped,
    V1RepeatableScheduleToJSON,
} from './';

/**
 * 
 * @export
 * @interface V1Schedule
 */
export interface V1Schedule {
    /**
     * 
     * @type {V1CronSchedule}
     * @memberof V1Schedule
     */
    cron?: V1CronSchedule;
    /**
     * 
     * @type {V1ExactTimeSchedule}
     * @memberof V1Schedule
     */
    exact_time?: V1ExactTimeSchedule;
    /**
     * 
     * @type {V1IntervalSchedule}
     * @memberof V1Schedule
     */
    interval?: V1IntervalSchedule;
    /**
     * 
     * @type {V1RepeatableSchedule}
     * @memberof V1Schedule
     */
    repeatable?: V1RepeatableSchedule;
}

export function V1ScheduleFromJSON(json: any): V1Schedule {
    return V1ScheduleFromJSONTyped(json, false);
}

export function V1ScheduleFromJSONTyped(json: any, ignoreDiscriminator: boolean): V1Schedule {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'cron': !exists(json, 'cron') ? undefined : V1CronScheduleFromJSON(json['cron']),
        'exact_time': !exists(json, 'exact_time') ? undefined : V1ExactTimeScheduleFromJSON(json['exact_time']),
        'interval': !exists(json, 'interval') ? undefined : V1IntervalScheduleFromJSON(json['interval']),
        'repeatable': !exists(json, 'repeatable') ? undefined : V1RepeatableScheduleFromJSON(json['repeatable']),
    };
}

export function V1ScheduleToJSON(value?: V1Schedule | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'cron': V1CronScheduleToJSON(value.cron),
        'exact_time': V1ExactTimeScheduleToJSON(value.exact_time),
        'interval': V1IntervalScheduleToJSON(value.interval),
        'repeatable': V1RepeatableScheduleToJSON(value.repeatable),
    };
}


