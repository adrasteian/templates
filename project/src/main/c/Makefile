# ------------------------------------------------------------------------
# Copyright (c) 2021 SIMON R. BUTLER
# All rights reserved
#
# The present software is the confidential and proprietary information of
# SIMON R. BUTLER. You shall not disclose the present
# software and shall use it only in accordance with the terms of the license
# agreement you entered into with SIMON R. BUTLER. This
# software may be subject to export or import laws in certain countries.
# ------------------------------------------------------------------------
#
# Simple makefile to build the final someapp executable. Run with:
#
#	make -fsomeapp.mk
#

# Folder for all artifacts generated during the build...
BUILD_DIR ?= ./_build

# Name of final executable, it will be in ${BUILD_DIR)...
TARGET_EXEC ?= someapp

# List of source files to be built...
SRCS := \
	someapp.c \
	args.c \
	foo.c

# ...corresponding list of objects following $(CC),,
OBJS := $(SRCS:%=$(BUILD_DIR)/%.o)

# Sort out header dependencies: .o depends on corresponding .d
# Requires -MMD -MP to generate phony targets for each local
# header file.
H_DEPS := $(OBJS:.o=.d)

# list of local folders containing header files...
INC_DIRS := ./inc

# ...and the corres[onding -I needed by $(CC)
INC_FLAGS := $(addprefix -I,$(INC_DIRS))

# -MMD: header deps only for local headers
# -MP: add phony target for each header dep
#      More detail here:
#  	   https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html
CPPFLAGS ?= $(INC_FLAGS) -MMD -MP

# Link the objs to get executable...
$(BUILD_DIR)/$(TARGET_EXEC): $(OBJS)
	$(CC) $(OBJS) -o $@ $(LDFLAGS)

# Generate objs for C sources. We give the objs ".c.o"
# extn in case we want to add similar rule for other
# langs e.g cpp, .s etc.
$(BUILD_DIR)/%.c.o: %.c
	$(MKDIR_P) $(dir $@)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@

# clean just needs to delete $(BUILD_DIR)
.PHONY: clean

clean:
	$(RM) -r $(BUILD_DIR)

# Phony targets for header deps, see above.
-include $(H_DEPS)

MKDIR_P ?= mkdir -p