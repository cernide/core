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

/*
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.1.8-rc4
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.openapitools.client.model.V1CronSchedule;
import org.openapitools.client.model.V1ExactTimeSchedule;
import org.openapitools.client.model.V1IntervalSchedule;
import org.openapitools.client.model.V1RepeatableSchedule;

/**
 * V1Schedule
 */

public class V1Schedule {
  public static final String SERIALIZED_NAME_CRON = "cron";
  @SerializedName(SERIALIZED_NAME_CRON)
  private V1CronSchedule cron;

  public static final String SERIALIZED_NAME_EXACT_TIME = "exact_time";
  @SerializedName(SERIALIZED_NAME_EXACT_TIME)
  private V1ExactTimeSchedule exactTime;

  public static final String SERIALIZED_NAME_INTERVAL = "interval";
  @SerializedName(SERIALIZED_NAME_INTERVAL)
  private V1IntervalSchedule interval;

  public static final String SERIALIZED_NAME_REPEATABLE = "repeatable";
  @SerializedName(SERIALIZED_NAME_REPEATABLE)
  private V1RepeatableSchedule repeatable;


  public V1Schedule cron(V1CronSchedule cron) {
    
    this.cron = cron;
    return this;
  }

   /**
   * Get cron
   * @return cron
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1CronSchedule getCron() {
    return cron;
  }


  public void setCron(V1CronSchedule cron) {
    this.cron = cron;
  }


  public V1Schedule exactTime(V1ExactTimeSchedule exactTime) {
    
    this.exactTime = exactTime;
    return this;
  }

   /**
   * Get exactTime
   * @return exactTime
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1ExactTimeSchedule getExactTime() {
    return exactTime;
  }


  public void setExactTime(V1ExactTimeSchedule exactTime) {
    this.exactTime = exactTime;
  }


  public V1Schedule interval(V1IntervalSchedule interval) {
    
    this.interval = interval;
    return this;
  }

   /**
   * Get interval
   * @return interval
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1IntervalSchedule getInterval() {
    return interval;
  }


  public void setInterval(V1IntervalSchedule interval) {
    this.interval = interval;
  }


  public V1Schedule repeatable(V1RepeatableSchedule repeatable) {
    
    this.repeatable = repeatable;
    return this;
  }

   /**
   * Get repeatable
   * @return repeatable
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1RepeatableSchedule getRepeatable() {
    return repeatable;
  }


  public void setRepeatable(V1RepeatableSchedule repeatable) {
    this.repeatable = repeatable;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1Schedule v1Schedule = (V1Schedule) o;
    return Objects.equals(this.cron, v1Schedule.cron) &&
        Objects.equals(this.exactTime, v1Schedule.exactTime) &&
        Objects.equals(this.interval, v1Schedule.interval) &&
        Objects.equals(this.repeatable, v1Schedule.repeatable);
  }

  @Override
  public int hashCode() {
    return Objects.hash(cron, exactTime, interval, repeatable);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1Schedule {\n");
    sb.append("    cron: ").append(toIndentedString(cron)).append("\n");
    sb.append("    exactTime: ").append(toIndentedString(exactTime)).append("\n");
    sb.append("    interval: ").append(toIndentedString(interval)).append("\n");
    sb.append("    repeatable: ").append(toIndentedString(repeatable)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

