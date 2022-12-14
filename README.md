# Release light 💡 with LaunchDarkly and Home Assistant

Inspired by [this](https://www.youtube.com/watch?v=-n0weDGWTy8) LaunchDarkly introduction video to feature flags I decided to build an actual light switch controlled via LaunchDarkly feature flags to release light into the dark.

[![LaunchDarkly Feature Flags](https://img.youtube.com/vi/-n0weDGWTy8/0.jpg)](https://www.youtube.com/watch?v=-n0weDGWTy8)

The Python script presented evaluates a [LaunchDarkly](https://launchdarkly.com/) feature flag called `HomeAssistantLight` and uses the [Home Assistant](https://www.home-assistant.io/) home automation API to control a smart light switch based on the targeting status of the feature flag.

https://user-images.githubusercontent.com/18030370/198258660-579f4824-0812-4d3a-b5f8-2000c0a93636.mov

### Do I need Home Assistant to try it out?

To use the `HomeAssistantLight.py` script, a running Home Assistant instance with at least one `"light"` entity is reqiured! The script controls the `"light.launchdarkly"` entity by default.

If one does not own a Home Assistant home automation instance, a stripped down version of the script (`NoHomeAssistant.py`) is available which will simply give a visual representation of the light switch status as a console output.

### Required environment variables

The Python script reads the folllowing environment variables:
- `HA_API_KEY` - The API key to interact with the Home Assistant API (not required for `NoHomeAssistant.py`)
- `HA_IP` - The IP address of the Home Assistant instance (not required for `NoHomeAssistant.py`)
- `LAUNCHDARKLY_KEY` - The LaunchDarkly SDK key (always required)

### Required LaunchDarkly feature flags

The Python script evaluates the targeting status of a LaunchDarkly feature flag called `HomeAssistantLight`.

### But why...?!

tl;dr. Why not?

The slightly longer answer:

This little piece of Python code showcases how easily one can leverage LaunchDarkly feature flags to control which section of code will be executed.

In addition, this MVP provides a potential security benefit for Home Assistant users, as one does not need to expose it's Home Assistant API to the public internet to control select entities.
It is possible to leverage LaunchDarkly feature flags, e.g. via the LaunchDarkly Slack integration, to control a smart home system when outside of the private network.

By adding more complex LaunchDarkly features like "Individual targeting" and "Workflows" one could as well implement more advanced controls, like controlling opening percentages for roller shutters or defining when shutters will open in the morning / close in the evening

### todo

- Replace `while True:` loop by a more elegant solution which does not constantly hit the Home Assistant API
- Add some error handling at all...