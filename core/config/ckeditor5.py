customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
    {"color": "hsl(120, 60%, 70%)", "label": "Light Green"},
    {"color": "hsl(60, 70%, 50%)", "label": "Yellow"},
    {"color": "hsl(30, 100%, 40%)", "label": "Orange"},
    {"color": "hsl(0, 0%, 20%)", "label": "Dark Grey"},
]

# Define predefined font sizes
customFontSizes = {
    "options": [
        "tiny",  # predefined size options
        "small",
        "default",
        "big",
        "huge",
    ]
}

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload",
            "mediaEmbed",  # Media Embed to support iframe embedding
            "codeBlock",
            "sourceEditing",
            "fileUpload",
            "|",
            "alignment",
            "fontSize",
            "fontColor",
            "fontBackgroundColor",
            "|",
            "undo",
            "redo",
        ],
        "extraAllowedContent": "iframe[*]",  # Allow all iframe attributes
        "allowedContent": True,  # Allow all content types
        "alignment": {
            "options": ["left", "center", "right", "justify"],
        },
        "fontSize": customFontSizes,
        "fontColor": {
            "colors": customColorPalette,
        },
        "fontBackgroundColor": {
            "colors": customColorPalette,
        },
        # Add iframe embedding functionality
        "mediaEmbed": {
            "previewsInData": True,
        },
    },
    "extends": {
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            "heading",
            "|",
            "outdent",
            "indent",
            "|",
            "bold",
            "italic",
            "link",
            "underline",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "codeBlock",
            "sourceEditing",
            "insertImage",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "imageUpload",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",  # Enable Media Embed in toolbar for iframes
            "removeFormat",
            "insertTable",
            "|",
            "alignment",
        ],
        "alignment": {
            "options": ["left", "center", "right", "justify"],
        },
        "fontSize": customFontSizes,
        "fontColor": {
            "colors": customColorPalette,
        },
        "fontBackgroundColor": {
            "colors": customColorPalette,
        },
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
                "resizeImage:50",
                "resizeImage:75",
                "resizeImage:original",
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
    },
    "list": {
        "properties": {
            "styles": "true",
            "startIndex": "true",
            "reversed": "true",
        }
    },
}
CKEDITOR_5_ALLOW_ALL_FILE_TYPES = True
CKEDITOR_5_MAX_FILE_SIZE = 5
CKEDITOR_5_UPLOAD_FILE_TYPES = [
    "jpeg",
    "png",
    "gif",
    "bmp",
    "webp",
    "tiff",
    "jpg",
    "pdf",
    "docx",
    "doc",
    "xls",
    "xlsx",
]
CKEDITOR_5_FILE_UPLOAD_PERMISSION = "any"
