/* Extend jQuery with functions for PUT and DELETE requests. */
/* http://homework.nwsnet.de/releases/9132/ */

function _ajax_request(url, data, callback, type, method) {
    if (jQuery.isFunction(data)) {
        callback = data;
        data = {};
    }
    return jQuery.ajax({
        type: method,
        url: url,
        data: data,
        success: callback,
        dataType: type
        });
}

jQuery.extend({
    put: function(url, data, callback, type) {
        return _ajax_request(url, data, callback, type, 'PUT');
    },
    delete_: function(url, data, callback, type) {
        return _ajax_request(url, data, callback, type, 'DELETE');
    },
    putJSON: function(url, data, callback) {
        return _ajax_request(url, data, callback, 'json', 'PUT');
    },
    postJSON: function(url, data, callback) {
        return _ajax_request(url, data, callback, 'json', 'POST');
    },
    deleteJSON: function(url, data, callback, type) {
        return _ajax_request(url, data, callback, 'json', 'DELETE');
    }
});
