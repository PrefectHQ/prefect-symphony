# generated by datamodel-codegen:
#   filename:  dlp.yaml
#   timestamp: 2022-09-07T03:04:02+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class V3DLPDictionaryMeta(BaseModel):
    """
    See source code for the fields' description.

    Identity of a dictionary.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    dict_id: str = Field(..., alias="dictId")
    name: str
    version: str


class V3DLPFileClassifierConfig(BaseModel):
    """
    See source code for the fields' description.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types that can be applied. Can be ["PDF", "WORD", "EXCEL",'
            ' "POWERPOINT", "ZIP", "CSV", "TXT"].'
        ),
    )
    classifiers: Dict[str, str] = Field(
        ...,
        description=(
            'Classifier is defined as a Key and its Value: e.g.: "classification":'
            ' "Internal".\nName and value can contain UTF-8 characters. Neither the'
            " name nor value cannot be left empty.\nMaximum 30 characters for the name"
            " and value, case insensitive.\nIf files contains k-v pairs in the"
            " classifers map, it means a match. Maximum 30 classifiers per policy.\n"
        ),
    )


class V3DLPFileExtensionConfig(BaseModel):
    """
    See source code for the fields' description.

    Extension detection config for allowed and blocked types of file extensions.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    allow_lists: List[str] = Field(
        ..., alias="allowLists", description="File extensions that are allowed."
    )
    block_lists: List[str] = Field(
        ..., alias="blockLists", description="File extensions that are blocked."
    )


class V3DLPFilePasswordConfig(BaseModel):
    """
    See source code for the fields' description.

    Password protected detection config for files that are password protected or not.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types that can be applied. Can be ["PDF", "WORD", "EXCEL",'
            ' "POWERPOINT", "ZIP", "CSV", "TXT"].'
        ),
    )
    match_criteria: str = Field(
        ...,
        alias="matchCriteria",
        description=(
            "Based on the criteria, whether a file is password protected or not means a"
            ' match.\nCan be ["PASSWORD_PROTECTED", "NOT_PASSWORD_PROTECTED"]. The'
            ' default is "NOT_PASSWORD_PROTECTED".\n'
        ),
    )


class V3DLPFileSizeConfig(BaseModel):
    """
    See source code for the fields' description.

    File size config defines maximum allowed size of file. Default max size limit is 20 MB.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    size_limit: Optional[int] = Field(None, alias="sizeLimit")


class V3DLPTextMatchConfig(BaseModel):
    """
    See source code for the fields' description.

        This is a configuration that can be used to match text or regex.
    Configuration that can be used by a rule. This is a configuration that can be used to match text or regex.
    This configuration also corresponds to V2 TextMatch/RegexMatch of dictionaries.

    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types must be applied only for rule type "FileContent", otherwise'
            ' must be empty.\nCan be ["PDF", "WORD", "EXCEL", "POWERPOINT", "ZIP",'
            ' "CSV", "TXT"].\n'
        ),
    )
    count_unique_occurrences: Optional[int] = Field(
        None, alias="countUniqueOccurrences"
    )
    dictionaries: List[V3DLPDictionaryMeta]


class V3DLPRule(BaseModel):
    """
    See source code for the fields' description.

        A Rule defines the actual matching specification for policies. It holds a type and a configuration
    for the rule, these properties should be used to build the corresponding matching implementation.
    Only one of the configuration property should be set [textMatchConfig, fileSizeConfig, fileExtensionConfig, filePasswordConfig, fileClassifierConfig].

    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    file_classifier_config: Optional[V3DLPFileClassifierConfig] = Field(
        None, alias="fileClassifierConfig"
    )
    file_extension_config: Optional[V3DLPFileExtensionConfig] = Field(
        None, alias="fileExtensionConfig"
    )
    file_password_config: Optional[V3DLPFilePasswordConfig] = Field(
        None, alias="filePasswordConfig"
    )
    file_size_config: Optional[V3DLPFileSizeConfig] = Field(
        None, alias="fileSizeConfig"
    )
    id: Optional[str] = None
    name: str = Field(..., description="Name for rule.")
    text_match_config: Optional[V3DLPTextMatchConfig] = Field(
        None, alias="textMatchConfig"
    )
    type: str = Field(
        ...,
        description=(
            'Type of a rule used by policy. Can be ["UNKNOWN", "TEXT_MATCH",'
            ' "FILE_EXTENSION", "FILE_SIZE", "FILE_PASSWORD", "FILE_CLASSIFIER"].'
        ),
    )


class V3DLPPolicyAppliesTo(BaseModel):
    """
    See source code for the fields' description.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    action: str = Field(
        ...,
        description=(
            'Action to be taken on violation detection.\nCan be ["Block", "Warn",'
            ' "LogOnly"]. The default is "LogOnly".\n'
        ),
    )
    data_type: str = Field(
        ...,
        alias="dataType",
        description=(
            "The list of data types that policy should apply to. Can't be empty.\nCan"
            ' be ["Messages","RoomMeta", "SignalMeta", "FileContent", "FileMeta"].\n'
        ),
    )
    rules: List[V3DLPRule]


# generated by datamodel-codegen:
#   filename:  dlp.yaml
#   timestamp: 2022-09-07T03:10:45+00:00


from typing import Dict, List, Optional

from pydantic import BaseModel, Extra, Field


class V3DLPDictionaryMeta(BaseModel):
    """
    See source code for the fields' description.

    Identity of a dictionary.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    dict_id: str = Field(..., alias="dictId")
    name: str
    version: str


class V3DLPFileClassifierConfig(BaseModel):
    """
    See source code for the fields' description.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types that can be applied. Can be ["PDF", "WORD", "EXCEL",'
            ' "POWERPOINT", "ZIP", "CSV", "TXT"].'
        ),
    )
    classifiers: Dict[str, str] = Field(
        ...,
        description=(
            'Classifier is defined as a Key and its Value: e.g.: "classification":'
            ' "Internal".\nName and value can contain UTF-8 characters. Neither the'
            " name nor value cannot be left empty.\nMaximum 30 characters for the name"
            " and value, case insensitive.\nIf files contains k-v pairs in the"
            " classifers map, it means a match. Maximum 30 classifiers per policy.\n"
        ),
    )


class V3DLPFileExtensionConfig(BaseModel):
    """
    See source code for the fields' description.

    Extension detection config for allowed and blocked types of file extensions.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    allow_lists: List[str] = Field(
        ..., alias="allowLists", description="File extensions that are allowed."
    )
    block_lists: List[str] = Field(
        ..., alias="blockLists", description="File extensions that are blocked."
    )


class V3DLPFilePasswordConfig(BaseModel):
    """
    See source code for the fields' description.

    Password protected detection config for files that are password protected or not.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types that can be applied. Can be ["PDF", "WORD", "EXCEL",'
            ' "POWERPOINT", "ZIP", "CSV", "TXT"].'
        ),
    )
    match_criteria: str = Field(
        ...,
        alias="matchCriteria",
        description=(
            "Based on the criteria, whether a file is password protected or not means a"
            ' match.\nCan be ["PASSWORD_PROTECTED", "NOT_PASSWORD_PROTECTED"]. The'
            ' default is "NOT_PASSWORD_PROTECTED".\n'
        ),
    )


class V3DLPFileSizeConfig(BaseModel):
    """
    See source code for the fields' description.

    File size config defines maximum allowed size of file. Default max size limit is 20 MB.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    size_limit: Optional[int] = Field(None, alias="sizeLimit")


class V3DLPTextMatchConfig(BaseModel):
    """
    See source code for the fields' description.

        This is a configuration that can be used to match text or regex.
    Configuration that can be used by a rule. This is a configuration that can be used to match text or regex.
    This configuration also corresponds to V2 TextMatch/RegexMatch of dictionaries.

    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    applicable_file_types: List[str] = Field(
        ...,
        alias="applicableFileTypes",
        description=(
            'File types must be applied only for rule type "FileContent", otherwise'
            ' must be empty.\nCan be ["PDF", "WORD", "EXCEL", "POWERPOINT", "ZIP",'
            ' "CSV", "TXT"].\n'
        ),
    )
    count_unique_occurrences: Optional[int] = Field(
        None, alias="countUniqueOccurrences"
    )
    dictionaries: List[V3DLPDictionaryMeta]


class V3DLPRule(BaseModel):
    """
    See source code for the fields' description.

        A Rule defines the actual matching specification for policies. It holds a type and a configuration
    for the rule, these properties should be used to build the corresponding matching implementation.
    Only one of the configuration property should be set [textMatchConfig, fileSizeConfig, fileExtensionConfig, filePasswordConfig, fileClassifierConfig].

    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    file_classifier_config: Optional[V3DLPFileClassifierConfig] = Field(
        None, alias="fileClassifierConfig"
    )
    file_extension_config: Optional[V3DLPFileExtensionConfig] = Field(
        None, alias="fileExtensionConfig"
    )
    file_password_config: Optional[V3DLPFilePasswordConfig] = Field(
        None, alias="filePasswordConfig"
    )
    file_size_config: Optional[V3DLPFileSizeConfig] = Field(
        None, alias="fileSizeConfig"
    )
    id: Optional[str] = None
    name: str = Field(..., description="Name for rule.")
    text_match_config: Optional[V3DLPTextMatchConfig] = Field(
        None, alias="textMatchConfig"
    )
    type: str = Field(
        ...,
        description=(
            'Type of a rule used by policy. Can be ["UNKNOWN", "TEXT_MATCH",'
            ' "FILE_EXTENSION", "FILE_SIZE", "FILE_PASSWORD", "FILE_CLASSIFIER"].'
        ),
    )


class V3DLPPolicyAppliesTo(BaseModel):
    """
    See source code for the fields' description.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    action: str = Field(
        ...,
        description=(
            'Action to be taken on violation detection.\nCan be ["Block", "Warn",'
            ' "LogOnly"]. The default is "LogOnly".\n'
        ),
    )
    data_type: str = Field(
        ...,
        alias="dataType",
        description=(
            "The list of data types that policy should apply to. Can't be empty.\nCan"
            ' be ["Messages","RoomMeta", "SignalMeta", "FileContent", "FileMeta"].\n'
        ),
    )
    rules: List[V3DLPRule]
