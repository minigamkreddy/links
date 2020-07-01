/* DO NOT EDIT
 * This dissector is autogenerated
 */

/* packet-dcerpc-budb.c
 * Routines for BUDB packet disassembly
 *   ronnie sahlberg 2005
 *
 * $Id$
 *
 * Wireshark - Network traffic analyzer
 * By Gerald Combs <gerald@wireshark.org>
 * Copyright 1998 Gerald Combs
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

#include "config.h"

#include <glib.h>
#include <string.h>

#include <epan/packet.h>
#include "packet-dcerpc.h"
#include "packet-dcerpc-nt.h"
#include "packet-windows-common.h"
#include "packet-dcerpc-budb.h"

static int proto_budb = -1;
ETH_HF

ETH_ETT

static int
budb_dissect_NameString_t(tvbuff_t *tvb, int offset, packet_info *pinfo, proto_tree *tree, guint8 *drep, int hf_index, guint32 param _U_)
{
    offset=dissect_ndr_vstring(tvb, offset, pinfo, tree, drep, 1, hf_index, FALSE, NULL);
    return offset;
}

ETH_CODE

void
proto_register_budb(void)
{
        static hf_register_info hf[] = {

ETH_HFARR
	};

        static gint *ett[] = {
ETH_ETTARR
        };

        proto_budb = proto_register_protocol(
                "DCE/DFS BUDB", 
		"BUDB", "budb");
	proto_register_field_array(proto_budb, hf, array_length(hf));
        proto_register_subtree_array(ett, array_length(ett));
}

static dcerpc_sub_dissector function_dissectors[] = {
ETH_FT
	{ 0, NULL, NULL, NULL },
};

void
proto_reg_handoff_budb(void)
{
ETH_HANDOFF
}
