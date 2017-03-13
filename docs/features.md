# Features

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

#### JavaScript Example

For example, by using the following Markdown:

    ```javascript
    alert("A JavaScript Alert!");
    ```

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
