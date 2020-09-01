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

/**
 * Polyaxon SDKs and REST API specification.
 * Polyaxon SDKs and REST API specification.
 *
 * The version of the OpenAPI document: 1.1.8-rc4
 * Contact: contact@polyaxon.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import RuntimeError from '../model/RuntimeError';
import V1ListOrganizationMembersResponse from '../model/V1ListOrganizationMembersResponse';
import V1ListOrganizationsResponse from '../model/V1ListOrganizationsResponse';
import V1Organization from '../model/V1Organization';
import V1OrganizationMember from '../model/V1OrganizationMember';

/**
* OrganizationsV1 service.
* @module api/OrganizationsV1Api
* @version 1.1.8-rc4
*/
export default class OrganizationsV1Api {

    /**
    * Constructs a new OrganizationsV1Api. 
    * Polyaxon sdk
    * @alias module:api/OrganizationsV1Api
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createOrganization operation.
     * @callback module:api/OrganizationsV1Api~createOrganizationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create organization
     * @param {module:model/V1Organization} body 
     * @param {module:api/OrganizationsV1Api~createOrganizationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    createOrganization(body, callback) {
      let postBody = body;
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling createOrganization");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/create', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the createOrganizationMember operation.
     * @callback module:api/OrganizationsV1Api~createOrganizationMemberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create organization member
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1OrganizationMember} body Organization body
     * @param {Object} opts Optional parameters
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~createOrganizationMemberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    createOrganizationMember(owner, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling createOrganizationMember");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling createOrganizationMember");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganization operation.
     * @callback module:api/OrganizationsV1Api~deleteOrganizationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete organization
     * @param {String} owner Owner of the namespace
     * @param {module:api/OrganizationsV1Api~deleteOrganizationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganization(owner, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling deleteOrganization");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationInvitation operation.
     * @callback module:api/OrganizationsV1Api~deleteOrganizationInvitationCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete organization invitation details
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {String} opts.member_user User.
     * @param {String} opts.member_user_email Read-only User email.
     * @param {String} opts.member_role Role.
     * @param {Date} opts.member_created_at Optional time when the entity was created.
     * @param {Date} opts.member_updated_at Optional last time the entity was updated.
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~deleteOrganizationInvitationCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationInvitation(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling deleteOrganizationInvitation");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'member.user': opts['member_user'],
        'member.user_email': opts['member_user_email'],
        'member.role': opts['member_role'],
        'member.created_at': opts['member_created_at'],
        'member.updated_at': opts['member_updated_at'],
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/invitations', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationMember operation.
     * @callback module:api/OrganizationsV1Api~deleteOrganizationMemberCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete organization member details
     * @param {String} owner Owner of the namespace
     * @param {String} user Memeber under namesapce
     * @param {module:api/OrganizationsV1Api~deleteOrganizationMemberCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationMember(owner, user, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling deleteOrganizationMember");
      }
      // verify the required parameter 'user' is set
      if (user === undefined || user === null) {
        throw new Error("Missing the required parameter 'user' when calling deleteOrganizationMember");
      }

      let pathParams = {
        'owner': owner,
        'user': user
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members/{user}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganization operation.
     * @callback module:api/OrganizationsV1Api~getOrganizationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get organization
     * @param {String} owner Owner of the namespace
     * @param {module:api/OrganizationsV1Api~getOrganizationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    getOrganization(owner, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getOrganization");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationInvitation operation.
     * @callback module:api/OrganizationsV1Api~getOrganizationInvitationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get organization invitation details
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {String} opts.member_user User.
     * @param {String} opts.member_user_email Read-only User email.
     * @param {String} opts.member_role Role.
     * @param {Date} opts.member_created_at Optional time when the entity was created.
     * @param {Date} opts.member_updated_at Optional last time the entity was updated.
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~getOrganizationInvitationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    getOrganizationInvitation(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getOrganizationInvitation");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'member.user': opts['member_user'],
        'member.user_email': opts['member_user_email'],
        'member.role': opts['member_role'],
        'member.created_at': opts['member_created_at'],
        'member.updated_at': opts['member_updated_at'],
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/invitations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationMember operation.
     * @callback module:api/OrganizationsV1Api~getOrganizationMemberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get organization member details
     * @param {String} owner Owner of the namespace
     * @param {String} user Memeber under namesapce
     * @param {module:api/OrganizationsV1Api~getOrganizationMemberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    getOrganizationMember(owner, user, callback) {
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getOrganizationMember");
      }
      // verify the required parameter 'user' is set
      if (user === undefined || user === null) {
        throw new Error("Missing the required parameter 'user' when calling getOrganizationMember");
      }

      let pathParams = {
        'owner': owner,
        'user': user
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members/{user}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationSettings operation.
     * @callback module:api/OrganizationsV1Api~getOrganizationSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get organization settings
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {String} opts.organization_user User.
     * @param {String} opts.organization_user_email Read-only User email.
     * @param {String} opts.organization_name Name.
     * @param {Boolean} opts.organization_is_public Optional flag to tell if this organization is public.
     * @param {Date} opts.organization_created_at Optional time when the entity was created.
     * @param {Date} opts.organization_updated_at Optional last time the entity was updated.
     * @param {String} opts.organization_role Current user's role in this org.
     * @param {module:api/OrganizationsV1Api~getOrganizationSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    getOrganizationSettings(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling getOrganizationSettings");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'organization.user': opts['organization_user'],
        'organization.user_email': opts['organization_user_email'],
        'organization.name': opts['organization_name'],
        'organization.is_public': opts['organization_is_public'],
        'organization.created_at': opts['organization_created_at'],
        'organization.updated_at': opts['organization_updated_at'],
        'organization.role': opts['organization_role']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/settings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listOrganizationMembers operation.
     * @callback module:api/OrganizationsV1Api~listOrganizationMembersCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListOrganizationMembersResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get organization members
     * @param {String} owner Owner of the namespace
     * @param {Object} opts Optional parameters
     * @param {Number} opts.offset Pagination offset.
     * @param {Number} opts.limit Limit size.
     * @param {String} opts.sort Sort to order the search.
     * @param {String} opts.query Query filter the search search.
     * @param {module:api/OrganizationsV1Api~listOrganizationMembersCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListOrganizationMembersResponse}
     */
    listOrganizationMembers(owner, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling listOrganizationMembers");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'offset': opts['offset'],
        'limit': opts['limit'],
        'sort': opts['sort'],
        'query': opts['query']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ListOrganizationMembersResponse;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listOrganizationNames operation.
     * @callback module:api/OrganizationsV1Api~listOrganizationNamesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListOrganizationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List organizations names
     * @param {module:api/OrganizationsV1Api~listOrganizationNamesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListOrganizationsResponse}
     */
    listOrganizationNames(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ListOrganizationsResponse;
      return this.apiClient.callApi(
        '/api/v1/orgs/names', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listOrganizations operation.
     * @callback module:api/OrganizationsV1Api~listOrganizationsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1ListOrganizationsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List organizations
     * @param {module:api/OrganizationsV1Api~listOrganizationsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1ListOrganizationsResponse}
     */
    listOrganizations(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = V1ListOrganizationsResponse;
      return this.apiClient.callApi(
        '/api/v1/orgs/list', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchOrganization operation.
     * @callback module:api/OrganizationsV1Api~patchOrganizationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch organization
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1Organization} body Organization body
     * @param {module:api/OrganizationsV1Api~patchOrganizationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    patchOrganization(owner, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchOrganization");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchOrganization");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchOrganizationInvitation operation.
     * @callback module:api/OrganizationsV1Api~patchOrganizationInvitationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch organization invitation
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1OrganizationMember} body Organization body
     * @param {Object} opts Optional parameters
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~patchOrganizationInvitationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    patchOrganizationInvitation(owner, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchOrganizationInvitation");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchOrganizationInvitation");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/invitations', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchOrganizationMember operation.
     * @callback module:api/OrganizationsV1Api~patchOrganizationMemberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch organization member
     * @param {String} owner Owner of the namespace
     * @param {String} member_user User
     * @param {module:model/V1OrganizationMember} body Organization body
     * @param {Object} opts Optional parameters
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~patchOrganizationMemberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    patchOrganizationMember(owner, member_user, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchOrganizationMember");
      }
      // verify the required parameter 'member_user' is set
      if (member_user === undefined || member_user === null) {
        throw new Error("Missing the required parameter 'member_user' when calling patchOrganizationMember");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchOrganizationMember");
      }

      let pathParams = {
        'owner': owner,
        'member.user': member_user
      };
      let queryParams = {
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members/{member.user}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the patchOrganizationSettings operation.
     * @callback module:api/OrganizationsV1Api~patchOrganizationSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch oranization settings
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1Organization} body Organization body
     * @param {module:api/OrganizationsV1Api~patchOrganizationSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    patchOrganizationSettings(owner, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling patchOrganizationSettings");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling patchOrganizationSettings");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/settings', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganization operation.
     * @callback module:api/OrganizationsV1Api~updateOrganizationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update organization
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1Organization} body Organization body
     * @param {module:api/OrganizationsV1Api~updateOrganizationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    updateOrganization(owner, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateOrganization");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateOrganization");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationInvitation operation.
     * @callback module:api/OrganizationsV1Api~updateOrganizationInvitationCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update organization invitation
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1OrganizationMember} body Organization body
     * @param {Object} opts Optional parameters
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~updateOrganizationInvitationCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    updateOrganizationInvitation(owner, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateOrganizationInvitation");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateOrganizationInvitation");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/invitations', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationMember operation.
     * @callback module:api/OrganizationsV1Api~updateOrganizationMemberCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1OrganizationMember} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update organization member
     * @param {String} owner Owner of the namespace
     * @param {String} member_user User
     * @param {module:model/V1OrganizationMember} body Organization body
     * @param {Object} opts Optional parameters
     * @param {String} opts.email Optional email.
     * @param {module:api/OrganizationsV1Api~updateOrganizationMemberCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1OrganizationMember}
     */
    updateOrganizationMember(owner, member_user, body, opts, callback) {
      opts = opts || {};
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateOrganizationMember");
      }
      // verify the required parameter 'member_user' is set
      if (member_user === undefined || member_user === null) {
        throw new Error("Missing the required parameter 'member_user' when calling updateOrganizationMember");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateOrganizationMember");
      }

      let pathParams = {
        'owner': owner,
        'member.user': member_user
      };
      let queryParams = {
        'email': opts['email']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1OrganizationMember;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/members/{member.user}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationSettings operation.
     * @callback module:api/OrganizationsV1Api~updateOrganizationSettingsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/V1Organization} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update organization settings
     * @param {String} owner Owner of the namespace
     * @param {module:model/V1Organization} body Organization body
     * @param {module:api/OrganizationsV1Api~updateOrganizationSettingsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/V1Organization}
     */
    updateOrganizationSettings(owner, body, callback) {
      let postBody = body;
      // verify the required parameter 'owner' is set
      if (owner === undefined || owner === null) {
        throw new Error("Missing the required parameter 'owner' when calling updateOrganizationSettings");
      }
      // verify the required parameter 'body' is set
      if (body === undefined || body === null) {
        throw new Error("Missing the required parameter 'body' when calling updateOrganizationSettings");
      }

      let pathParams = {
        'owner': owner
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKey'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = V1Organization;
      return this.apiClient.callApi(
        '/api/v1/orgs/{owner}/settings', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
