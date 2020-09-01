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
import org.openapitools.client.model.V1HpChoice;
import org.openapitools.client.model.V1HpGeomSpace;
import org.openapitools.client.model.V1HpLinSpace;
import org.openapitools.client.model.V1HpLogNormal;
import org.openapitools.client.model.V1HpLogSpace;
import org.openapitools.client.model.V1HpLogUniform;
import org.openapitools.client.model.V1HpNormal;
import org.openapitools.client.model.V1HpPChoice;
import org.openapitools.client.model.V1HpQLogNormal;
import org.openapitools.client.model.V1HpQLogUniform;
import org.openapitools.client.model.V1HpQNormal;
import org.openapitools.client.model.V1HpQUniform;
import org.openapitools.client.model.V1HpRange;
import org.openapitools.client.model.V1HpUniform;

/**
 * V1HpParams
 */

public class V1HpParams {
  public static final String SERIALIZED_NAME_CHOICE = "choice";
  @SerializedName(SERIALIZED_NAME_CHOICE)
  private V1HpChoice choice;

  public static final String SERIALIZED_NAME_PCHOICE = "pchoice";
  @SerializedName(SERIALIZED_NAME_PCHOICE)
  private V1HpPChoice pchoice;

  public static final String SERIALIZED_NAME_RANGE = "range";
  @SerializedName(SERIALIZED_NAME_RANGE)
  private V1HpRange range;

  public static final String SERIALIZED_NAME_LINSPACE = "linspace";
  @SerializedName(SERIALIZED_NAME_LINSPACE)
  private V1HpLinSpace linspace;

  public static final String SERIALIZED_NAME_LOGSPACE = "logspace";
  @SerializedName(SERIALIZED_NAME_LOGSPACE)
  private V1HpLogSpace logspace;

  public static final String SERIALIZED_NAME_GEOMSPACE = "geomspace";
  @SerializedName(SERIALIZED_NAME_GEOMSPACE)
  private V1HpGeomSpace geomspace;

  public static final String SERIALIZED_NAME_UNIFORM = "uniform";
  @SerializedName(SERIALIZED_NAME_UNIFORM)
  private V1HpUniform uniform;

  public static final String SERIALIZED_NAME_QUNIFORM = "quniform";
  @SerializedName(SERIALIZED_NAME_QUNIFORM)
  private V1HpQUniform quniform;

  public static final String SERIALIZED_NAME_LOGUNIFORM = "loguniform";
  @SerializedName(SERIALIZED_NAME_LOGUNIFORM)
  private V1HpLogUniform loguniform;

  public static final String SERIALIZED_NAME_QLOGUNIFORM = "qloguniform";
  @SerializedName(SERIALIZED_NAME_QLOGUNIFORM)
  private V1HpQLogUniform qloguniform;

  public static final String SERIALIZED_NAME_NORMAL = "normal";
  @SerializedName(SERIALIZED_NAME_NORMAL)
  private V1HpNormal normal;

  public static final String SERIALIZED_NAME_QNORMAL = "qnormal";
  @SerializedName(SERIALIZED_NAME_QNORMAL)
  private V1HpQNormal qnormal;

  public static final String SERIALIZED_NAME_LOGNORMAL = "lognormal";
  @SerializedName(SERIALIZED_NAME_LOGNORMAL)
  private V1HpLogNormal lognormal;

  public static final String SERIALIZED_NAME_QLOGNORMAL = "qlognormal";
  @SerializedName(SERIALIZED_NAME_QLOGNORMAL)
  private V1HpQLogNormal qlognormal;


  public V1HpParams choice(V1HpChoice choice) {
    
    this.choice = choice;
    return this;
  }

   /**
   * Get choice
   * @return choice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpChoice getChoice() {
    return choice;
  }


  public void setChoice(V1HpChoice choice) {
    this.choice = choice;
  }


  public V1HpParams pchoice(V1HpPChoice pchoice) {
    
    this.pchoice = pchoice;
    return this;
  }

   /**
   * Get pchoice
   * @return pchoice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpPChoice getPchoice() {
    return pchoice;
  }


  public void setPchoice(V1HpPChoice pchoice) {
    this.pchoice = pchoice;
  }


  public V1HpParams range(V1HpRange range) {
    
    this.range = range;
    return this;
  }

   /**
   * Get range
   * @return range
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpRange getRange() {
    return range;
  }


  public void setRange(V1HpRange range) {
    this.range = range;
  }


  public V1HpParams linspace(V1HpLinSpace linspace) {
    
    this.linspace = linspace;
    return this;
  }

   /**
   * Get linspace
   * @return linspace
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpLinSpace getLinspace() {
    return linspace;
  }


  public void setLinspace(V1HpLinSpace linspace) {
    this.linspace = linspace;
  }


  public V1HpParams logspace(V1HpLogSpace logspace) {
    
    this.logspace = logspace;
    return this;
  }

   /**
   * Get logspace
   * @return logspace
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpLogSpace getLogspace() {
    return logspace;
  }


  public void setLogspace(V1HpLogSpace logspace) {
    this.logspace = logspace;
  }


  public V1HpParams geomspace(V1HpGeomSpace geomspace) {
    
    this.geomspace = geomspace;
    return this;
  }

   /**
   * Get geomspace
   * @return geomspace
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpGeomSpace getGeomspace() {
    return geomspace;
  }


  public void setGeomspace(V1HpGeomSpace geomspace) {
    this.geomspace = geomspace;
  }


  public V1HpParams uniform(V1HpUniform uniform) {
    
    this.uniform = uniform;
    return this;
  }

   /**
   * Get uniform
   * @return uniform
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpUniform getUniform() {
    return uniform;
  }


  public void setUniform(V1HpUniform uniform) {
    this.uniform = uniform;
  }


  public V1HpParams quniform(V1HpQUniform quniform) {
    
    this.quniform = quniform;
    return this;
  }

   /**
   * Get quniform
   * @return quniform
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpQUniform getQuniform() {
    return quniform;
  }


  public void setQuniform(V1HpQUniform quniform) {
    this.quniform = quniform;
  }


  public V1HpParams loguniform(V1HpLogUniform loguniform) {
    
    this.loguniform = loguniform;
    return this;
  }

   /**
   * Get loguniform
   * @return loguniform
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpLogUniform getLoguniform() {
    return loguniform;
  }


  public void setLoguniform(V1HpLogUniform loguniform) {
    this.loguniform = loguniform;
  }


  public V1HpParams qloguniform(V1HpQLogUniform qloguniform) {
    
    this.qloguniform = qloguniform;
    return this;
  }

   /**
   * Get qloguniform
   * @return qloguniform
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpQLogUniform getQloguniform() {
    return qloguniform;
  }


  public void setQloguniform(V1HpQLogUniform qloguniform) {
    this.qloguniform = qloguniform;
  }


  public V1HpParams normal(V1HpNormal normal) {
    
    this.normal = normal;
    return this;
  }

   /**
   * Get normal
   * @return normal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpNormal getNormal() {
    return normal;
  }


  public void setNormal(V1HpNormal normal) {
    this.normal = normal;
  }


  public V1HpParams qnormal(V1HpQNormal qnormal) {
    
    this.qnormal = qnormal;
    return this;
  }

   /**
   * Get qnormal
   * @return qnormal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpQNormal getQnormal() {
    return qnormal;
  }


  public void setQnormal(V1HpQNormal qnormal) {
    this.qnormal = qnormal;
  }


  public V1HpParams lognormal(V1HpLogNormal lognormal) {
    
    this.lognormal = lognormal;
    return this;
  }

   /**
   * Get lognormal
   * @return lognormal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpLogNormal getLognormal() {
    return lognormal;
  }


  public void setLognormal(V1HpLogNormal lognormal) {
    this.lognormal = lognormal;
  }


  public V1HpParams qlognormal(V1HpQLogNormal qlognormal) {
    
    this.qlognormal = qlognormal;
    return this;
  }

   /**
   * Get qlognormal
   * @return qlognormal
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public V1HpQLogNormal getQlognormal() {
    return qlognormal;
  }


  public void setQlognormal(V1HpQLogNormal qlognormal) {
    this.qlognormal = qlognormal;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    V1HpParams v1HpParams = (V1HpParams) o;
    return Objects.equals(this.choice, v1HpParams.choice) &&
        Objects.equals(this.pchoice, v1HpParams.pchoice) &&
        Objects.equals(this.range, v1HpParams.range) &&
        Objects.equals(this.linspace, v1HpParams.linspace) &&
        Objects.equals(this.logspace, v1HpParams.logspace) &&
        Objects.equals(this.geomspace, v1HpParams.geomspace) &&
        Objects.equals(this.uniform, v1HpParams.uniform) &&
        Objects.equals(this.quniform, v1HpParams.quniform) &&
        Objects.equals(this.loguniform, v1HpParams.loguniform) &&
        Objects.equals(this.qloguniform, v1HpParams.qloguniform) &&
        Objects.equals(this.normal, v1HpParams.normal) &&
        Objects.equals(this.qnormal, v1HpParams.qnormal) &&
        Objects.equals(this.lognormal, v1HpParams.lognormal) &&
        Objects.equals(this.qlognormal, v1HpParams.qlognormal);
  }

  @Override
  public int hashCode() {
    return Objects.hash(choice, pchoice, range, linspace, logspace, geomspace, uniform, quniform, loguniform, qloguniform, normal, qnormal, lognormal, qlognormal);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class V1HpParams {\n");
    sb.append("    choice: ").append(toIndentedString(choice)).append("\n");
    sb.append("    pchoice: ").append(toIndentedString(pchoice)).append("\n");
    sb.append("    range: ").append(toIndentedString(range)).append("\n");
    sb.append("    linspace: ").append(toIndentedString(linspace)).append("\n");
    sb.append("    logspace: ").append(toIndentedString(logspace)).append("\n");
    sb.append("    geomspace: ").append(toIndentedString(geomspace)).append("\n");
    sb.append("    uniform: ").append(toIndentedString(uniform)).append("\n");
    sb.append("    quniform: ").append(toIndentedString(quniform)).append("\n");
    sb.append("    loguniform: ").append(toIndentedString(loguniform)).append("\n");
    sb.append("    qloguniform: ").append(toIndentedString(qloguniform)).append("\n");
    sb.append("    normal: ").append(toIndentedString(normal)).append("\n");
    sb.append("    qnormal: ").append(toIndentedString(qnormal)).append("\n");
    sb.append("    lognormal: ").append(toIndentedString(lognormal)).append("\n");
    sb.append("    qlognormal: ").append(toIndentedString(qlognormal)).append("\n");
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

