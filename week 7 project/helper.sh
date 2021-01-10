#!/bin/bash

grep ERROR syslog.log > error.log

grep INFO syslog.log > info.log