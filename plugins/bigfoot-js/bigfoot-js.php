<?php
namespace Grav\Plugin;

use Grav\Common\Assets;
use Grav\Common\Page\Page;
use Grav\Common\Plugin;
use RocketTheme\Toolbox\Event\Event;

/**
 * Class BigfootJSPlugin
 * @package Grav\Plugin
 */
class BigfootJSPlugin extends Plugin
{
    /**
     * @return array
     *
     * The getSubscribedEvents() gives the core a list of events
     *     that the plugin wants to listen to. The key of each
     *     array section is the event that the plugin listens to
     *     and the value (in the form of an array) contains the
     *     callable (or function) as well as the priority. The
     *     higher the number the higher the priority.
     */
    public static function getSubscribedEvents()
    {
        return [
            'onPluginsInitialized' => ['onPluginsInitialized', 0]
        ];
    }

    /**
     * Initialize the plugin
     */
    public function onPluginsInitialized()
    {
        // Don't proceed if we are in the admin plugin
        if ($this->isAdmin()) {
            return;
        }

        // Enable the main event we are interested in
        $this->enable([
            'onPageContentRaw' => ['onPageContentRaw', 0]
        ]);
    }

    /**
     * Do some work for this event, full details of events can be found
     * on the learn site: http://learn.getgrav.org/plugins/event-hooks
     *
     * @param Event $e
     */
    public function onPageContentRaw(Event $e)
    {
        // Get settings from the plugin configuration
        $add_jQuery        = $this->config->get('plugins.bigfoot-js.include_jquery', false);
        $autoAdd_BigfootJS = $this->config->get('plugins.bigfoot-js.auto_bigfootjs', true);
        $style             = $this->config->get('plugins.bigfoot-js.style', 'default');

        /** @var Assets $assets */
        $assets = $this->grav['assets'];

        // Check for Footnotes
        $pmResult = $this->checkForFootnotes($e);
        if ($pmResult == false || $pmResult === 0) return;

        // Do we need to add jQuery?
        if ($add_jQuery) {
            /** @var Page $page */
            $page = $e['page'];
            $assets->addJs('jquery');
        }

        // Now do we add BigfootJS
        if ($autoAdd_BigfootJS) {
            // Build our inline JS block to initialise BigfootJS
            $bf_init = <<<BFJS
var bigfoot = $.bigfoot()

window.addEventListener('message', function (event) {
    $('body').attr('data-footnote-style', event.data);
    bigfoot.updateSetting('positionContent', event.data !== 'bottom');
});
BFJS;

            $stylesheet = "plugins://bigfoot-js/css/bigfoot-$style.css";

            $assets->addJs('plugins://bigfoot-js/js/bigfoot.js');
            $assets->addCss($stylesheet);
            $assets->addInlineJs($bf_init);
        }
    }

    /**
     * @param Event $e
     * @return int
     */
    protected function checkForFootnotes(Event $e)
    {
// Get the current raw content
        $content = $e['page']->getRawContent();

        // Check for Markdown Footnotes
        $footnoteMatches = [];
        $pmResult = preg_match('/\[\^\d+\]?/', $content, $footnoteMatches);
        return $pmResult;
    }
}
