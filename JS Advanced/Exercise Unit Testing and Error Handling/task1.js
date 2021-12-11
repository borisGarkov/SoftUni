function verifyRequest(object) {

    let validMethods = [
        'GET',
        'POST',
        'DELETE',
        'CONNECT',
    ];

    let validVersions = [
        'HTTP/0.9',
        'HTTP/1.0',
        'HTTP/1.1',
        'HTTP/2.0',
    ];

    let invalidMessageChars = [
        '<',
        '>',
        '\\',
        '&',
        '\'',
        '\"',
    ]

    let objectComponents = [
        'method',
        'uri',
        'version',
        'message',
    ]

    if (!validMethods.includes(object.method) || object.method == undefined) {
        throw Error('Invalid request header: Invalid Method');
    } else if (object.uri == undefined) {
        throw Error('Invalid request header: Invalid URI');
    } else if (!validVersions.includes(object.version) || object.version == undefined) {
        throw Error('Invalid request header: Invalid Version');
    } else if (invalidMessageChars.includes(object.message) || object.message == undefined) {
        throw Error('Invalid request header: Invalid Message');
    }

    return object
}


console.log(verifyRequest({
    method: 'OPTIONS',
    uri: 'git.master',
    version: 'HTTP/1.1',
    message: '-recursive'
  }  
))