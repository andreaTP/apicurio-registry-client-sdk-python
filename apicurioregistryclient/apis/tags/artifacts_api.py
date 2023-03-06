# coding: utf-8

"""
    Apicurio Registry API [v2]

    Apicurio Registry is a datastore for standard event schemas and API designs. Apicurio Registry enables developers to manage and share the structure of their data using a REST interface. For example, client applications can dynamically push or pull the latest updates to or from the registry without needing to redeploy. Apicurio Registry also enables developers to create rules that govern how registry content can evolve over time. For example, this includes rules for content validation and version compatibility.  The Apicurio Registry REST API enables client applications to manage the artifacts in the registry. This API provides create, read, update, and delete operations for schema and API artifacts, rules, versions, and metadata.   The supported artifact types include: - Apache Avro schema - AsyncAPI specification - Google protocol buffers - GraphQL schema - JSON Schema - Kafka Connect schema - OpenAPI specification - Web Services Description Language - XML Schema Definition   **Important**: The Apicurio Registry REST API is available from `https://MY-REGISTRY-URL/apis/registry/v2` by default. Therefore you must prefix all API operation paths with `../apis/registry/v2` in this case. For example: `../apis/registry/v2/ids/globalIds/{globalId}`.   # noqa: E501

    The version of the OpenAPI document: 2.4.x
    Contact: apicurio@lists.jboss.org
    Generated by: https://openapi-generator.tech
"""

from apicurioregistryclient.paths.groups_group_id_artifacts.post import CreateArtifact
from apicurioregistryclient.paths.groups_group_id_artifacts_artifact_id.delete import DeleteArtifact
from apicurioregistryclient.paths.groups_group_id_artifacts.delete import DeleteArtifactsInGroup
from apicurioregistryclient.paths.ids_global_ids_global_id.get import GetContentByGlobalId
from apicurioregistryclient.paths.ids_content_hashes_content_hash_.get import GetContentByHash
from apicurioregistryclient.paths.ids_content_ids_content_id_.get import GetContentById
from apicurioregistryclient.paths.groups_group_id_artifacts_artifact_id.get import GetLatestArtifact
from apicurioregistryclient.paths.groups_group_id_artifacts.get import ListArtifactsInGroup
from apicurioregistryclient.paths.ids_content_hashes_content_hash_references.get import ReferencesByContentHash
from apicurioregistryclient.paths.ids_content_ids_content_id_references.get import ReferencesByContentId
from apicurioregistryclient.paths.ids_global_ids_global_id_references.get import ReferencesByGlobalId
from apicurioregistryclient.paths.search_artifacts.get import SearchArtifacts
from apicurioregistryclient.paths.search_artifacts.post import SearchArtifactsByContent
from apicurioregistryclient.paths.groups_group_id_artifacts_artifact_id.put import UpdateArtifact
from apicurioregistryclient.paths.groups_group_id_artifacts_artifact_id_state.put import UpdateArtifactState


class ArtifactsApi(
    CreateArtifact,
    DeleteArtifact,
    DeleteArtifactsInGroup,
    GetContentByGlobalId,
    GetContentByHash,
    GetContentById,
    GetLatestArtifact,
    ListArtifactsInGroup,
    ReferencesByContentHash,
    ReferencesByContentId,
    ReferencesByGlobalId,
    SearchArtifacts,
    SearchArtifactsByContent,
    UpdateArtifact,
    UpdateArtifactState,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
