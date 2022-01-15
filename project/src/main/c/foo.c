/*
 * Copyright (c) 2021 SIMON R. BUTLER
 * All rights reserved
 *
 * The present software is the confidential and proprietary information of
 * SIMON R. BUTLER. You shall not disclose the present software and shall
 * use it only in accordance with the terms of the license agreement you
 * entered into with SIMON R. BUTLER. This software may be subject to
 * export or import laws in certain countries.
 */
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>

#include <someapp.h>
#include <foo.h>

static bool db = false;
static bool vb = false;

char *foo() {
    return "barx"; // 'x' make test fail initially
}