# ckeditor upload path
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_AutoMagicDeveloperConfig': [
            {
                'name': 'row1',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    '-',
                    'Image',
                    'CodeSnippet',
                    'Blockquote',
                    'NumberedList',
                    'BulletedList',
                    'Table',
                    'HorizontalRule',
                    'Iframe',
                    '-',
                    'Link',
                    'Unlink',
                    '-',
                    'Undo',
                    'Redo',
                ]
            },
            '/',
            {
                'name': 'row2',
                'items': [
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                    '-',
                    'TextColor',
                    'BGColor',
                    '-',
                    'Strike',
                    'Subscript',
                    'Superscript',
                    '-',
                    'BidiLtr',
                    'BidiRtl',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'Find',
                    'Replace',
                    '-',
                    'Templates',
                ]
            },
            '/',
            {
                'name': 'row3',
                'items': [
                    'Format',
                    'Styles',
                    '-',
                    'ShowBlocks',
                    '-',
                    'Smiley',
                    'SpecialChar',
                    '-',
                    'PageBreak',
                    # 'Print',
                    '-',
                    'Source',
                    '-',
                    'NewPage',
                    '-',
                    'Maximize',
                    '-',
                    'RemoveFormat',
                ]
            },
        ],
        'toolbar': 'AutoMagicDeveloperConfig',
        'height': 300,
        'width': '100%',
        'tabSpaces': 4,
        "removePlugins": "exportpdf",
        'extraPlugins': ','.join([
            'uploadimage',
            'codesnippet',
            'autolink',
            'embedsemantic',
            'widget',
            'lineutils',
            # 'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
        'contentsCss': """ 
            html{
                font-size: 100%;
            }
            body{
                font-family: 'Open Sans', 'arial' , system-ui, sans-serif;
            }

            a {
                text-decoration: none;
            }
            h1, h2, h3, h4, h5, h6{
                color: #222;
                font-weight: bold;
            }
            h1 {
                font-size: 2rem;
            }
            h2 {
                font-size: 1.8rem;
            }
            h3 {
                font-size: 1.6rem;
            }
            h4 {
                font-size: 1.4rem;
            }
            h5 {
                font-size: 1.2rem;
            }
            h6 {
                font-size: 1rem;
            }

            p{
                font-size: 1.1rem;
                color: #222;
            }
            .marker {
                display: inline;
                padding: 0.1em 0.1em;
                background-color: Yellow;
            }
            blockquote {
                border-left: 3px solid #f56e213b;
                font-style: italic;
                line-height: 1.8em;
                margin: 1.1em 1em;
                padding: 0 2rem;
                position: relative;
            }
            table {
                text-align: center;
                width: auto !important;
                max-width: 100%;
                caption-side: top;
                border-collapse: unset;
            }
            table caption {
                text-align: center;
                color: #222;
                text-transform: capitalize;
            }
            tbody, td, tfoot, th, thead, tr {
                padding: 0.4rem 1.5rem;
                border: 1px solid #ccc;
            }
            a {
                color: blue;
                text-decoration: underline;
            }
            img {
                max-width: 100%;
                height: auto !important;
            }
            img.cke_reset.cke_widget_mask {
                display: none;
            }
            .cke_widget_wrapper {
                overflow: auto;
            }
            .cke_widget_wrapper:hover>.cke_widget_element {
                width: 100%;
            }
            pre {
                margin-top: 1rem;
            }
            a {
                text-decoration: none;
                color: #ff3c00;
            }
            a:hover{
                color: #F56E21;
            }
        """,
    }
}
