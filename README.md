# Formeler SDK

Formeler SDK is a cloud language detection api SDK, It's design to make get started quick and easy with the ability to
scale up to complex applications.

## An Example

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
If the API call is successful,the `result` variable will contain the following JSON response:
```json
{
  "result": "success",
  "language": "de",
  "tokenCount": "4"
}
```
### More Example

You can find additional examples in the `examples` directory of this repository.

### API errors

The Formeler API may return an error in the response. You can identify these by checking the `result` field in the returned object.
An error response will follow this structure:
```json
{
  "result": "failed",
  "message": "unauthorized"
}
```