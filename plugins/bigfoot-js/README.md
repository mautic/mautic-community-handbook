# Bigfoot.js Plugin

The **Bigfoot.js** Plugin is for [Grav CMS](http://github.com/getgrav/grav). Loads the Bigfoot.js script (and jQuery if required) to enable better Footnotes.

## Installation

Installing the Bigfoot Js plugin can be done in one of two ways. The GPM (Grav Package Manager) installation method enables you to quickly and easily install the plugin with a simple terminal command, while the manual method enables you to do so via a zip file.

### GPM Installation (Preferred)

The simplest way to install this plugin will be via the [Grav Package Manager (GPM)](http://learn.getgrav.org/advanced/grav-gpm) through your system's terminal (also called the command line). *Currently the plugin isn't available through GPM so you the manual option will have to be used in the short term.*  From the root of your Grav install type:

    bin/gpm install bigfoot-js

This will install the Bigfoot Js plugin into your `/user/plugins` directory within Grav. Its files can be found under `/your/site/grav/user/plugins/bigfoot-js`.

### Manual Installation

To install this plugin, just download the zip version of this repository and unzip it under `/your/site/grav/user/plugins`. Then, rename the folder to `bigfoot-js`. You can find these files on [GitHub](https://github.com/craig-phillips/grav-plugin-bigfoot-js) or via [GetGrav.org](http://getgrav.org/downloads/plugins#extras).

You should now have all the plugin files under

    /your/site/grav/user/plugins/bigfoot-js

> NOTE: This plugin is a modular component for Grav which requires [Grav](http://github.com/getgrav/grav) and the [Error](https://github.com/getgrav/grav-plugin-error) and [Problems](https://github.com/getgrav/grav-plugin-problems) to operate.

## Configuration
### Plugin settings
From the plugins settings screen in the Grav Admin you can:

- Enable/Disable the Bigfoot.js plugin
- Enable/Disable autoloading of Bigfoot.js
- Select from the 'Default', 'Number' or 'Bottom' style of footnotes

### Manual Configuration
Before configuring this plugin, you should copy the `user/plugins/bigfoot-js/bigfoot-js.yaml` to `user/config/plugins/bigfoot-js.yaml` and only edit that copy.

Here is the default configuration and an explanation of available options can be found below:

```yaml
enabled: true
include_jquery: false
auto_bigfootjs: true
style: default
```

## Usage

### Creating Footnotes in Markdown

Everyone know that Grav supports Markdown and [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/)?

Markdown Extra provides support for [Footnotes](https://michelf.ca/projects/php-markdown/extra/#footnotes) 😃

To enable Markdown Extra, login to your Grav websites Admin area and go to Configuration->System and turn on `Markdown Extra`.

Or enable it manually, in `user/config/system.yaml` set the `markdown:` -> `extra:` to `true`, the section should look something like this:

```yaml
  markdown:
    extra: true
    auto_line_breaks: false
    auto_url_links: false
    escape_markup: false
    special_chars:
      '>': gt
      '<': lt
```

Right now there's only two options, the first is to enable automatic detection of Markdown Extra style footnotes and add `Bigfoot.js` to the page when it does detect them. I recommend leaving this `On` right now as it won't work without being turned on.

The second option is to include jQuery, this defaults to off. You probably won't need this as most themes include jQuery and the Grav core includes it as well, but if you use a theme that doesn't load jQuery into your pages this will add it for you.



#### Footnote Syntax

The syntax for adding footnotes is suitably simple… in the Markdown style:

```md
This is some text with a footnote at the end.[^1]

[^1]: And this is the footnote.
```

Footnotes can contain a reasonable range of content and like any good footnote system you don't have to keep them in order (one can be after two for example). In fact most markdown will work in a footnote e.g.

```md
[^6]: You've already seen:
* links
* text styling
* and now lists
[^7]: It also support images… ![](Icon_Craig.jpg)
```

## Credits

Of course this wouldn't be possible without [Bigfoot.js](http://www.bigfootjs.com) and [Markdown Extra](https://michelf.ca/projects/php-markdown/extra/), all my efforts are trivial by comparison.

## To Do

 * settings for controlling the footnote mark option (right now its the default elipses [^3], soon you have numbers available as well)
 * the ability to add your own CSS styling to your theme for automatic overriding of the default style
 * and controls for changing the other options in Bigfoot.js
