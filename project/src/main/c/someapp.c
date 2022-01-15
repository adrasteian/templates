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

#include <someapp.h>
#include <args.h>
#include <foo.h>

void main(int argc, char* argv[]) {

    if (parse_args(argc, argv)) {

        // Commandline is sufficient to proceed with processing the input

        // Stream source is a file...
        FILE *input = getArgInputFile();

        printf("foo(): <%s>\n",foo());

        fclose(input);
    }
}