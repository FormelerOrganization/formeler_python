# Formeler SDK

First, please check the documentation (https://formeler.com/lang-id/doc/) page to familiarize yourself with the basics of the API.
## Installation

Within the activated environment, use the following command to install `Formeler` SDK:
```sh
pip install formeler
```

To get started, create a new instance of `Formeler` and pass your API key as the first argument to the constructor. You can obtain a fresh API key from the [website](https://formeler.com/lang-id/overview/) that includes 10M tokens of free credit.
Once initialized, you can use the available `Formeler` methods. Currently, language detection via the LangID module is supported. Below are examples of how to use the LangID methods.
## Example

```python
from formeler import Formeler

def test_detect():
    api = Formeler("YOUR-API-KEY")
    result = api.lang_id.detect("Dies ist ein Test")
    print(result)

def main():
    test_detect()

if __name__ == "__main__":
    main()
```
If the API call is successful, the `result` variable will contain the following JSON response:
```json
{
  "result": "success",
  "language": "de",
  "tokenCount": "4"
}
```
### More Examples

You can find additional examples in the `examples` directory of this repository.

### API Errors

The Formeler API may return an error in the response. You can identify these by checking the `result` field in the returned object.
An error response will follow this structure:
```json
{
  "result": "failed",
  "message": "unauthorized"
}
```
