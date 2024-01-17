import json

# some JSON:


def output_jenkins():
    value = 'OOsucessOO'

    x = {
      "name": "John",
      "age": 30,
      "city": "New York"
    }

    # convert into JSON:
    y = json.dumps(x)
    return(x)



if __name__=='__main__':
    output_jenkins()