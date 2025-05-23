#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


class WebflowToAirbyteMapping:

    """
    The following disctionary is used for dynamically pulling the schema from Webflow, and mapping it to an Airbyte-compatible json-schema
        Webflow: https://developers.webflow.com/#get-collection-with-full-schema
        Airbyte/json-schema:  https://docs.airbyte.com/understanding-airbyte/supported-data-types/
    """

    webflow_to_airbyte_mapping = {
        "Bool": {"type": ["null", "boolean"]},
        "Switch": {"type": ["null", "boolean"]},
        "Date": {
            "type": ["null", "string"],
            "format": "date-time",
        },
        "Email": {
            "type": ["null", "string"],
        },
        "Phone": {
            "type": ["null", "string"],
        },
        "ImageRef": {"type": ["null", "object"], "additionalProperties": True},
        "Image": {"type": ["null", "object"], "additionalProperties": True},
        "MultiImage": {"type": ["null", "array"]},
        "ItemRef": {"type": ["null", "string"]},
        "ItemRefSet": {"type": ["null", "array"]},
        "Reference": {"type": ["null", "string"]},
        "Link": {"type": ["null", "string"]},
        "Color": {"type": ["null", "string"]},
        "Number": {"type": ["null", "number"]},
        "Option": {"type": ["null", "string"]},
        "PlainText": {"type": ["null", "string"]},
        "RichText": {"type": ["null", "string"]},
        "User": {"type": ["null", "string"]},
        "Price": {"type": ["null", "object"], "additionalProperties": True},
        "Video": {"type": ["null", "string"]},
        "FileRef": {"type": ["null", "object"]},
        "SkuValues": {"type": ["null", "object"], "additionalProperties": True},
    }
