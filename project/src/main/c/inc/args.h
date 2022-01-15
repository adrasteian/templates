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
#if !defined(__ARGS__)
#define __ARGS__

// External API to parsed command-line args...

void initArgs();
bool getArgDebug();
void setArgDebug(bool value);
bool getArgUsage();
bool getArgVerbose();
bool getArgVersion();
bool getArgInputFileName();
FILE *getArgInputFile();

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
bool parse_args(int argc, char* argv[]);

#endif