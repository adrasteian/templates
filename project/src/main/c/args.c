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
#include <args.h>

static bool arg_debug = false;
static bool arg_usage = false;
static bool arg_verbose = false;
static bool arg_version = false;
static char *arg_input_file_name = NULL;
static FILE *arg_input_file = NULL;

// External API to parsed command-line args...

// Initialise arg values, useful for tests...
void initArgs() {
    arg_debug = false;
    arg_usage = false;
    arg_verbose = false;
    arg_version = false;
    arg_input_file_name = NULL;

    if (NULL!=arg_input_file) {
        fclose(arg_input_file);
    }
    arg_input_file = NULL;
}

// Getters/setters for each parsed arg...

bool getArgDebug() { return arg_debug; }
void setArgDebug(bool value) { arg_debug=value; }
bool getArgUsage() { return arg_usage; }
bool getArgVerbose() { return arg_verbose; }
bool getArgVersion() { return arg_version; }
bool getArgInputFileName() { return arg_input_file_name; }
FILE *getArgInputFile() { return arg_input_file; }

// Handle -version and -usage locally...

void print_version() {
    printf("someapp v0.1 (c) Simon R. Butler");
}

void print_usage() {
    printf("Usage:\n");
    printf("    someapp <input_file> [options]\n");
    printf("\n");
    printf("Options:\n");
    printf("    -d, --debug     Output additional debug logs\n");
    printf("    -h, --help      Print this usage information\n");
    printf("    -v, --verbose   Ouput additional details relating to the the stream\n");
    printf("        --version   Show version information\n");
    printf("\n");
}

/*
 * parse_args()
 *
 * Very simple command-line args parser for someapp
 *
 * IN:
 *      argc    Number of args provided to main
 *      argv    Each of the args
 *
 * OUT:
 *      -
 *
 * RETURNS:
 *      true    Sufficient well-formed args provided, stream may be processed
 *      false   Stream may not be processed
 *              - Insufficient or malformed args
 *              - Input file not found
 *              - User requested usage or version
 */
bool parse_args(int argc, char* argv[]) {

    if (arg_debug) printf("parse_args()...\n");

    initArgs();

    if (2>argc) {
        printf("ERROR: Insufficient command line arguments\n");
        printf("\n");
        print_usage();
        return false;
    } else {

        for (int a=1; a<argc; a++) {

            char *arg = argv[a];
            int argLen = strlen(arg);

            if (arg_debug) printf("%d <%s>\n",a,arg);

            // ...something of note.
            if (1<argLen && '-'==arg[0]) {

                // A command-line option.
                //
                // We could drive options parsing from a more generic/
                // configurable table but the command line is trivial
                // so just brute-force it for simplicity...

                if (strcmp("-d",arg)==0 || strcmp("--debug",arg)==0) {
                    arg_debug = true;
                } else if (strcmp("-h",arg)==0 || strcmp("--help",arg)==0) {
                    arg_usage = true;
                } else if (strcmp("-v",arg)==0 || strcmp("--verbose",arg)==0) {
                    arg_verbose = true;
                } else if (strcmp("--version",arg)==0) {
                    arg_version = true;
                } else {
                    printf("ERROR: Unsupported option <%s>\n", arg);
                    printf("\n");
                    print_usage();
                    return false;
                }
            } else {

                // The input file.
                arg_input_file_name = arg;
            }
        }
    }


    if (arg_usage) {
        print_version();
        printf("\n");
        print_usage();
        return false;
    }

    if (arg_version) {
        print_version();
        return false;
    }

    if (NULL==arg_input_file_name) {
        printf("ERROR: Input file not specified\n");
        printf("\n");
        print_usage();
        return false;
    }

    if (access(arg_input_file_name, R_OK)==0) {

        // File exists and we can read it so open it for the
        // caller and inidicate OK to begin processing...
        arg_input_file = fopen(arg_input_file_name, "rb");
        if (NULL!=arg_input_file) {
            return true;
        }
    }

    printf("ERROR: Unable to access input file\n");
    printf("\n");

    return false;
}