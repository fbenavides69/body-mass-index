#! /usr/bin/env python
# -*- coding: utf-8 -*-

from application import create_app

if __name__ == '__main__':
    app, _ = create_app('sqlite:////tmp/bmi.db')
    app.run(debug=True)
