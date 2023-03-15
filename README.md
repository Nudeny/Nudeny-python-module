# Nudeny Python Package

*The Nudeny Rest-API is still not deployed.*

## Installation

```pip install nudeny```

## Classification use case

### Image file

```python
from nudeny import Classify

classify = Classify()

paths = [
    './sample.jpg',
    './sample2.png',
]

response = classify.imageClassify(paths=paths)
print(response)
```

### Output:
```json
{
  "Prediction": [
    {
      "filename": "sample.jpg",
      "class": "safe"
    },
    {
      "filename": "sample2.png",
      "class": "nude"
    }
  ]
}
```

### Image URL

```python
from nudeny import Classify

classify = Classify()

urls = [
    '...URL',
    '...URL'
]

response = classify.imageClassifyUrl(urls=urls)
print(response)
```

### Output:
```json
{
  "Prediction": [
    {
      "source": "...URL",
      "class": "nude"
    },
    {
      "source": "...URL",
      "class": "nude"
    }
  ]
}
```

## Detection use case

### Image file Detection

```python
from nudeny import Detect

detect = Detect()

paths = [
    './sample.jpg',
    './sample2.png',
]

response = detect.detectExposed(paths=paths)
print(response)
```
### Output:
```json
{
  "Prediction": [
    {
      "filename": "sample.jpg",
      "exposed_parts": {
        "female_breast": [],
        "female_genitalia": [],
        "male_genitalia": [
          {
            "confidence_score": 61.76939010620117,
            "top": 75,
            "left": 102,
            "bottom": 121,
            "right": 129
          }
        ],
        "buttocks": []
      }
    },
    {
      "filename": "sample2.png",
      "exposed_parts": {
        "female_breast": [],
        "female_genitalia": [],
        "male_genitalia": [],
        "buttocks": [
          {
            "confidence_score": 83.09783339500427,
            "top": 819,
            "left": 621,
            "bottom": 1100,
            "right": 925
          },
          {
            "confidence_score": 82.38601088523865,
            "top": 835,
            "left": 49,
            "bottom": 1125,
            "right": 381
          }
        ]
      }
    }
  ]
}
```

### Image URL Detection

```python
from nudeny import Detect

detect = Detect()

urls = [
    '...URL',
    '...URL'
]

response = detect.detectExposedFromUrl(urls=urls)
print(response)
```
### Output:
```json
{
  "Prediction": [
    {
      "source": "...URL",
      "exposed_parts": {
        "female_breast": [
          {
            "confidence_score": 81.59351348876953,
            "top": 293,
            "left": 87,
            "bottom": 413,
            "right": 390
          }
        ],
        "female_genitalia": [
          {
            "confidence_score": 66.92414283752441,
            "top": 446,
            "left": 183,
            "bottom": 533,
            "right": 255
          }
        ],
        "male_genitalia": [],
        "buttocks": []
      }
    },
    {
      "source": "...URL",
      "exposed_parts": {
        "female_breast": [
          {
            "confidence_score": 86.64460182189941,
            "top": 970,
            "left": 2387,
            "bottom": 1504,
            "right": 3099
          }
        ],
        "female_genitalia": [],
        "male_genitalia": [],
        "buttocks": []
      }
    }
  ]
}
```

### Image file Censor *(Save path is where you want to save/download the censored image)*

```python
from nudeny import Detect

detect = Detect()

paths = [
    './sample.jpg',
    './sample2.png',
]
save_path = './Path'

response = detect.censorExposed(paths=paths, save_path=save_path)
print(response)
```
### Output:
```json
{
  "Prediction": [
    {
      "filename": "sample.jpg",
      "url": "URL OF THE CENSORED IMAGE",
      "exposed_parts": {
        "female_breast": [],
        "female_genitalia": [],
        "male_genitalia": [
          {
            "confidence_score": 61.76939010620117,
            "top": 75,
            "left": 102,
            "bottom": 121,
            "right": 129
          }
        ],
        "buttocks": []
      }
    },
    {
      "filename": "sample.png",
      "url": "URL OF THE CENSORED IMAGE",
      "exposed_parts": {
        "female_breast": [],
        "female_genitalia": [],
        "male_genitalia": [],
        "buttocks": [
          {
            "confidence_score": 83.09783339500427,
            "top": 819,
            "left": 621,
            "bottom": 1100,
            "right": 925
          },
          {
            "confidence_score": 82.38601088523865,
            "top": 835,
            "left": 49,
            "bottom": 1125,
            "right": 381
          }
        ]
      }
    }
  ]
}
```

### Image URL Censor *(Save path is where you want to save/download the censored image)*

```python
from nudeny import Detect

detect = Detect()

urls = [
    '...URL',
    '...URL'
]
save_path = './Path'

response = detect.censorExposedFromUrl(urls=urls, save_path=save_path)
print(response)
```
### Output:
```json
{
  "Prediction": [
    {
      "source": "...URL",
      "url": "URL OF THE CENSORED IMAGE",
      "exposed_parts": {
        "female_breast": [
          {
            "confidence_score": 81.59351348876953,
            "top": 293,
            "left": 87,
            "bottom": 413,
            "right": 390
          }
        ],
        "female_genitalia": [
          {
            "confidence_score": 66.92414283752441,
            "top": 446,
            "left": 183,
            "bottom": 533,
            "right": 255
          }
        ],
        "male_genitalia": [],
        "buttocks": []
      }
    },
    {
      "source": "...URL",
      "url": "URL OF THE CENSORED IMAGE",
      "exposed_parts": {
        "female_breast": [
          {
            "confidence_score": 86.64460182189941,
            "top": 970,
            "left": 2387,
            "bottom": 1504,
            "right": 3099
          }
        ],
        "female_genitalia": [],
        "male_genitalia": [],
        "buttocks": []
      }
    }
  ]
}
```
