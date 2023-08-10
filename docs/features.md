# Features

The MkDocs-Nature theme supports a number of features which are configurable by
the end user.

* [Theme Variables](#theme-variables)
* [Search](#search)
* [Code Highlighting](#code-highlighting)

## Theme Variables

The theme includes support for a few variables which can be set by the user to
control the theme's behavior.

### theme.icon

Point this setting at an image file in your `docs_dir` to display an icon in
your documentation.

```yaml
theme:
    name: nature
    icon: icon.png
```

### theme.logo

Point this setting at an image file in your `docs_dir` to display logo in
your documentation.

```yaml
theme:
    name: nature
    logo: logo.png
```

### theme.release

Use this setting to include the version of the project you are documenting in
your documentation.

```yaml
theme:
    name: nature
    release: '2.1.3'
```

### theme.issue_tracker

Assign the URL for your issue tracker to this setting to include a "Report a
Bug" link on each page. For example, if you use GitHub to track issues:

```yaml
theme:
    name: nature
    issue_tracker: https://github.com/user/project/issues
```

### repo_url

Assign the URL for your repository to this setting to include a link on each
page. See MkDocs' [documentation][1] for more details.

[1]: https://www.mkdocs.org/user-guide/configuration/#repo_url

### edit_uri

When set, an "edit this page" link is included on each page. Note that if the
`repo_url` points to either GitHub or Bitbucket, this setting is automatically
configured and does not need to be set manually. See MkDocs' [documentation][2]
for more details.

[2]: https://www.mkdocs.org/user-guide/configuration/#edit_uri

### copyright

Assign the text to be used as a copyright notice in the footer of each page. For
example:

```yaml
copyright: "Copyright &copy; 2017"
```

### site_author

Assign the name to be included with the copyright notice on each page. This
setting is ignored if `copyright` is not also set.

## MetaData Variables

In addition to the [default metadata variables][meta] supported by MkDocs, the
McDocs-Nature theme includes support for the following variables defined in a
page's metadata.

[meta]: https://www.mkdocs.org/user-guide/writing-your-docs/#meta-data

### `toc_depth`

Set the depth of the table of contents to a unique value for a specific page.
Must be an integer. Defaults to `6`. Note that if the configuration option of
the same name is set for the `toc` Markdown extension, then this option must be
set to a lower value to have any effect.

## Search

The MkDocs-Nature theme includes support for MkDocs search plugin. As long as
the search plugin is enabled (MkDocs' default), a search page will be generated
and included in your site. If you would like to disable search, then disable the
search plugin by defining a `plugins` setting which does not include `search`.
If you have no other plugins, then set `plugins` to an empty list:

```yaml
plugins: []
```

## Permalinks

To enable permalinks to appear when hovering over any page or section headers,
you need to enable the relevant configuration setting for the TOC extension of
Python-Markdown.

```yaml
markdown_extensions:
    - toc:
        permalink: true
```

By default, the pilcrow or paragraph sign (&para;) is used for the permalink. If
you would like different text, set `permalink` to your desired string instead of
`true`. For example setting it to `§` would display the section sign.

## Admonitions

The appropriate CSS styles are defined to support the `admonition` extension to
Python-Markdown. To utilize admonitions, enable the extension in your config
file:

```yaml
markdown_extensions:
    - admonition
```

!!! attention

    See the Admonition Extension [documentation][3] for specifics on the syntax.

[3]: https://python-markdown.github.io/extensions/admonition#syntax

## Code Highlighting

By enabling the `codehilite` extension in your `mkdocs.yml` config file you get
syntax highlighting support using Pygments' Tango theme.

### Configuration

Enable the `codehilite` extension in your `mkdocs.yml` config file:

```yaml
markdown_extensions:
    - codehilite
```

### Usage

For best results, be sure to identify the language of each code block in your
Markdown files.

#### JavaScript Sample

For example, by using the following Markdown:

````text
```javascript
alert("A JavaScript Alert!");
```
````

Your codeblock will render as:

```javascript
alert("A JavaScript Alert!");
```

#### HTML Sample

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <title>Hello, World!</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```

#### Python Sample

```python
>>> def hello(name):
...     print u"Hello, {}!".format(name)
...
>>> hello('World')
u'Hello, World!'
```
