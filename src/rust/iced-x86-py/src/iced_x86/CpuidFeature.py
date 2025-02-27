# SPDX-License-Identifier: MIT
# Copyright (C) 2018-present iced project and contributors

# ⚠️This file was generated by GENERATOR!🦹‍♂️

# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

"""
``CPUID`` feature flags
"""

import typing
if typing.TYPE_CHECKING:
	from ._iced_x86_py import CpuidFeature
else:
	CpuidFeature = int

INTEL8086: CpuidFeature = 0 # type: ignore
"""
8086 or later
"""
INTEL8086_ONLY: CpuidFeature = 1 # type: ignore
"""
8086 only
"""
INTEL186: CpuidFeature = 2 # type: ignore
"""
80186 or later
"""
INTEL286: CpuidFeature = 3 # type: ignore
"""
80286 or later
"""
INTEL286_ONLY: CpuidFeature = 4 # type: ignore
"""
80286 only
"""
INTEL386: CpuidFeature = 5 # type: ignore
"""
80386 or later
"""
INTEL386_ONLY: CpuidFeature = 6 # type: ignore
"""
80386 only
"""
INTEL386_A0_ONLY: CpuidFeature = 7 # type: ignore
"""
80386 A0-B0 stepping only (``XBTS``, ``IBTS`` instructions)
"""
INTEL486: CpuidFeature = 8 # type: ignore
"""
Intel486 or later
"""
INTEL486_A_ONLY: CpuidFeature = 9 # type: ignore
"""
Intel486 A stepping only (``CMPXCHG``)
"""
UMOV: CpuidFeature = 10 # type: ignore
"""
UMOV (80386 and Intel486)
"""
IA64: CpuidFeature = 11 # type: ignore
"""
IA-64
"""
X64: CpuidFeature = 12 # type: ignore
"""
: CPUID.80000001H:EDX.LM[bit 29]
"""
ADX: CpuidFeature = 13 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.ADX[bit 19]
"""
AES: CpuidFeature = 14 # type: ignore
"""
: CPUID.01H:ECX.AES[bit 25]
"""
AVX: CpuidFeature = 15 # type: ignore
"""
: CPUID.01H:ECX.AVX[bit 28]
"""
AVX2: CpuidFeature = 16 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX2[bit 5]
"""
AVX512_4FMAPS: CpuidFeature = 17 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AVX512_4FMAPS[bit 3]
"""
AVX512_4VNNIW: CpuidFeature = 18 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AVX512_4VNNIW[bit 2]
"""
AVX512_BF16: CpuidFeature = 19 # type: ignore
"""
: CPUID.(EAX=07H, ECX=1H):EAX.AVX512_BF16[bit 5]
"""
AVX512_BITALG: CpuidFeature = 20 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.AVX512_BITALG[bit 12]
"""
AVX512_IFMA: CpuidFeature = 21 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512_IFMA[bit 21]
"""
AVX512_VBMI: CpuidFeature = 22 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.AVX512_VBMI[bit 1]
"""
AVX512_VBMI2: CpuidFeature = 23 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.AVX512_VBMI2[bit 6]
"""
AVX512_VNNI: CpuidFeature = 24 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.AVX512_VNNI[bit 11]
"""
AVX512_VP2INTERSECT: CpuidFeature = 25 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AVX512_VP2INTERSECT[bit 08]
"""
AVX512_VPOPCNTDQ: CpuidFeature = 26 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.AVX512_VPOPCNTDQ[bit 14]
"""
AVX512BW: CpuidFeature = 27 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512BW[bit 30]
"""
AVX512CD: CpuidFeature = 28 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512CD[bit 28]
"""
AVX512DQ: CpuidFeature = 29 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512DQ[bit 17]
"""
AVX512ER: CpuidFeature = 30 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512ER[bit 27]
"""
AVX512F: CpuidFeature = 31 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512F[bit 16]
"""
AVX512PF: CpuidFeature = 32 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512PF[bit 26]
"""
AVX512VL: CpuidFeature = 33 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.AVX512VL[bit 31]
"""
BMI1: CpuidFeature = 34 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.BMI1[bit 3]
"""
BMI2: CpuidFeature = 35 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.BMI2[bit 8]
"""
CET_IBT: CpuidFeature = 36 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.CET_IBT[bit 20]
"""
CET_SS: CpuidFeature = 37 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.CET_SS[bit 7]
"""
CL1INVMB: CpuidFeature = 38 # type: ignore
"""
``CL1INVMB`` instruction (Intel SCC = Single-Chip Computer)
"""
CLDEMOTE: CpuidFeature = 39 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.CLDEMOTE[bit 25]
"""
CLFLUSHOPT: CpuidFeature = 40 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.CLFLUSHOPT[bit 23]
"""
CLFSH: CpuidFeature = 41 # type: ignore
"""
: CPUID.01H:EDX.CLFSH[bit 19]
"""
CLWB: CpuidFeature = 42 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.CLWB[bit 24]
"""
CLZERO: CpuidFeature = 43 # type: ignore
"""
: CPUID.80000008H:EBX.CLZERO[bit 0]
"""
CMOV: CpuidFeature = 44 # type: ignore
"""
: CPUID.01H:EDX.CMOV[bit 15]
"""
CMPXCHG16B: CpuidFeature = 45 # type: ignore
"""
: CPUID.01H:ECX.CMPXCHG16B[bit 13]
"""
CPUID: CpuidFeature = 46 # type: ignore
"""
``RFLAGS.ID`` can be toggled
"""
CX8: CpuidFeature = 47 # type: ignore
"""
: CPUID.01H:EDX.CX8[bit 8]
"""
D3NOW: CpuidFeature = 48 # type: ignore
"""
: CPUID.80000001H:EDX.3DNOW[bit 31]
"""
D3NOWEXT: CpuidFeature = 49 # type: ignore
"""
: CPUID.80000001H:EDX.3DNOWEXT[bit 30]
"""
OSS: CpuidFeature = 50 # type: ignore
"""
: CPUID.(EAX=12H, ECX=0H):EAX.OSS[bit 5]
"""
ENQCMD: CpuidFeature = 51 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.ENQCMD[bit 29]
"""
F16C: CpuidFeature = 52 # type: ignore
"""
: CPUID.01H:ECX.F16C[bit 29]
"""
FMA: CpuidFeature = 53 # type: ignore
"""
: CPUID.01H:ECX.FMA[bit 12]
"""
FMA4: CpuidFeature = 54 # type: ignore
"""
: CPUID.80000001H:ECX.FMA4[bit 16]
"""
FPU: CpuidFeature = 55 # type: ignore
"""
: 8087 or later (CPUID.01H:EDX.FPU[bit 0])
"""
FPU287: CpuidFeature = 56 # type: ignore
"""
80287 or later
"""
FPU287XL_ONLY: CpuidFeature = 57 # type: ignore
"""
80287XL only
"""
FPU387: CpuidFeature = 58 # type: ignore
"""
80387 or later
"""
FPU387SL_ONLY: CpuidFeature = 59 # type: ignore
"""
80387SL only
"""
FSGSBASE: CpuidFeature = 60 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.FSGSBASE[bit 0]
"""
FXSR: CpuidFeature = 61 # type: ignore
"""
: CPUID.01H:EDX.FXSR[bit 24]
"""
CYRIX_D3NOW: CpuidFeature = 62 # type: ignore
"""
Cyrix (AMD Geode GX/LX) 3DNow! instructions
"""
GFNI: CpuidFeature = 63 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.GFNI[bit 8]
"""
HLE: CpuidFeature = 64 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.HLE[bit 4]
"""
HLE_OR_RTM: CpuidFeature = 65 # type: ignore
"""
:class:`HLE` or :class:`RTM`
"""
INVEPT: CpuidFeature = 66 # type: ignore
"""
IA32_VMX_EPT_VPID_CAP[bit 20]
"""
INVPCID: CpuidFeature = 67 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.INVPCID[bit 10]
"""
INVVPID: CpuidFeature = 68 # type: ignore
"""
IA32_VMX_EPT_VPID_CAP[bit 32]
"""
LWP: CpuidFeature = 69 # type: ignore
"""
: CPUID.80000001H:ECX.LWP[bit 15]
"""
LZCNT: CpuidFeature = 70 # type: ignore
"""
: CPUID.80000001H:ECX.LZCNT[bit 5]
"""
MCOMMIT: CpuidFeature = 71 # type: ignore
"""
: CPUID.80000008H:EBX.MCOMMIT[bit 8]
"""
MMX: CpuidFeature = 72 # type: ignore
"""
: CPUID.01H:EDX.MMX[bit 23]
"""
MONITOR: CpuidFeature = 73 # type: ignore
"""
: CPUID.01H:ECX.MONITOR[bit 3]
"""
MONITORX: CpuidFeature = 74 # type: ignore
"""
: CPUID.80000001H:ECX.MONITORX[bit 29]
"""
MOVBE: CpuidFeature = 75 # type: ignore
"""
: CPUID.01H:ECX.MOVBE[bit 22]
"""
MOVDIR64B: CpuidFeature = 76 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.MOVDIR64B[bit 28]
"""
MOVDIRI: CpuidFeature = 77 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.MOVDIRI[bit 27]
"""
MPX: CpuidFeature = 78 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.MPX[bit 14]
"""
MSR: CpuidFeature = 79 # type: ignore
"""
: CPUID.01H:EDX.MSR[bit 5]
"""
MULTIBYTENOP: CpuidFeature = 80 # type: ignore
"""
: Multi-byte nops (``0F1F /0``): CPUID.01H.EAX[Bits 11:8] = 0110B or 1111B
"""
PADLOCK_ACE: CpuidFeature = 81 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.ACE[Bits 7:6] = 11B ([6] = exists, [7] = enabled)
"""
PADLOCK_PHE: CpuidFeature = 82 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.PHE[Bits 11:10] = 11B ([10] = exists, [11] = enabled)
"""
PADLOCK_PMM: CpuidFeature = 83 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.PMM[Bits 13:12] = 11B ([12] = exists, [13] = enabled)
"""
PADLOCK_RNG: CpuidFeature = 84 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.RNG[Bits 3:2] = 11B ([2] = exists, [3] = enabled)
"""
PAUSE: CpuidFeature = 85 # type: ignore
"""
``PAUSE`` instruction (Pentium 4 or later)
"""
PCLMULQDQ: CpuidFeature = 86 # type: ignore
"""
: CPUID.01H:ECX.PCLMULQDQ[bit 1]
"""
PCOMMIT: CpuidFeature = 87 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.PCOMMIT[bit 22]
"""
PCONFIG: CpuidFeature = 88 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.PCONFIG[bit 18]
"""
PKU: CpuidFeature = 89 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.PKU[bit 3]
"""
POPCNT: CpuidFeature = 90 # type: ignore
"""
: CPUID.01H:ECX.POPCNT[bit 23]
"""
PREFETCHW: CpuidFeature = 91 # type: ignore
"""
: CPUID.80000001H:ECX.PREFETCHW[bit 8]
"""
PREFETCHWT1: CpuidFeature = 92 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.PREFETCHWT1[bit 0]
"""
PTWRITE: CpuidFeature = 93 # type: ignore
"""
: CPUID.(EAX=14H, ECX=0H):EBX.PTWRITE[bit 4]
"""
RDPID: CpuidFeature = 94 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.RDPID[bit 22]
"""
RDPMC: CpuidFeature = 95 # type: ignore
"""
``RDPMC`` instruction (Pentium MMX or later, or Pentium Pro or later)
"""
RDPRU: CpuidFeature = 96 # type: ignore
"""
: CPUID.80000008H:EBX.RDPRU[bit 4]
"""
RDRAND: CpuidFeature = 97 # type: ignore
"""
: CPUID.01H:ECX.RDRAND[bit 30]
"""
RDSEED: CpuidFeature = 98 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.RDSEED[bit 18]
"""
RDTSCP: CpuidFeature = 99 # type: ignore
"""
: CPUID.80000001H:EDX.RDTSCP[bit 27]
"""
RTM: CpuidFeature = 100 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.RTM[bit 11]
"""
SEP: CpuidFeature = 101 # type: ignore
"""
: CPUID.01H:EDX.SEP[bit 11]
"""
SGX1: CpuidFeature = 102 # type: ignore
"""
: CPUID.(EAX=12H, ECX=0H):EAX.SGX1[bit 0]
"""
SHA: CpuidFeature = 103 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.SHA[bit 29]
"""
SKINIT: CpuidFeature = 104 # type: ignore
"""
: CPUID.80000001H:ECX.SKINIT[bit 12]
"""
SKINIT_OR_SVM: CpuidFeature = 105 # type: ignore
"""
:class:`SKINIT` or :class:`SVM`
"""
SMAP: CpuidFeature = 106 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EBX.SMAP[bit 20]
"""
SMX: CpuidFeature = 107 # type: ignore
"""
: CPUID.01H:ECX.SMX[bit 6]
"""
SSE: CpuidFeature = 108 # type: ignore
"""
: CPUID.01H:EDX.SSE[bit 25]
"""
SSE2: CpuidFeature = 109 # type: ignore
"""
: CPUID.01H:EDX.SSE2[bit 26]
"""
SSE3: CpuidFeature = 110 # type: ignore
"""
: CPUID.01H:ECX.SSE3[bit 0]
"""
SSE4_1: CpuidFeature = 111 # type: ignore
"""
: CPUID.01H:ECX.SSE4_1[bit 19]
"""
SSE4_2: CpuidFeature = 112 # type: ignore
"""
: CPUID.01H:ECX.SSE4_2[bit 20]
"""
SSE4A: CpuidFeature = 113 # type: ignore
"""
: CPUID.80000001H:ECX.SSE4A[bit 6]
"""
SSSE3: CpuidFeature = 114 # type: ignore
"""
: CPUID.01H:ECX.SSSE3[bit 9]
"""
SVM: CpuidFeature = 115 # type: ignore
"""
: CPUID.80000001H:ECX.SVM[bit 2]
"""
SEV_ES: CpuidFeature = 116 # type: ignore
"""
: CPUID.8000001FH:EAX.SEV-ES[bit 3]
"""
SYSCALL: CpuidFeature = 117 # type: ignore
"""
: CPUID.80000001H:EDX.SYSCALL[bit 11]
"""
TBM: CpuidFeature = 118 # type: ignore
"""
: CPUID.80000001H:ECX.TBM[bit 21]
"""
TSC: CpuidFeature = 119 # type: ignore
"""
: CPUID.01H:EDX.TSC[bit 4]
"""
VAES: CpuidFeature = 120 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.VAES[bit 9]
"""
VMX: CpuidFeature = 121 # type: ignore
"""
: CPUID.01H:ECX.VMX[bit 5]
"""
VPCLMULQDQ: CpuidFeature = 122 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.VPCLMULQDQ[bit 10]
"""
WAITPKG: CpuidFeature = 123 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.WAITPKG[bit 5]
"""
WBNOINVD: CpuidFeature = 124 # type: ignore
"""
: CPUID.(EAX=80000008H, ECX=0H):EBX.WBNOINVD[bit 9]
"""
XOP: CpuidFeature = 125 # type: ignore
"""
: CPUID.80000001H:ECX.XOP[bit 11]
"""
XSAVE: CpuidFeature = 126 # type: ignore
"""
: CPUID.01H:ECX.XSAVE[bit 26]
"""
XSAVEC: CpuidFeature = 127 # type: ignore
"""
: CPUID.(EAX=0DH, ECX=1H):EAX.XSAVEC[bit 1]
"""
XSAVEOPT: CpuidFeature = 128 # type: ignore
"""
: CPUID.(EAX=0DH, ECX=1H):EAX.XSAVEOPT[bit 0]
"""
XSAVES: CpuidFeature = 129 # type: ignore
"""
: CPUID.(EAX=0DH, ECX=1H):EAX.XSAVES[bit 3]
"""
SEV_SNP: CpuidFeature = 130 # type: ignore
"""
: CPUID.8000001FH:EAX.SEV-SNP[bit 4]
"""
SERIALIZE: CpuidFeature = 131 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.SERIALIZE[bit 14]
"""
TSXLDTRK: CpuidFeature = 132 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.TSXLDTRK[bit 16]
"""
INVLPGB: CpuidFeature = 133 # type: ignore
"""
: CPUID.80000008H:EBX.INVLPGB[bit 3]
"""
AMX_BF16: CpuidFeature = 134 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AMX-BF16[bit 22]
"""
AMX_TILE: CpuidFeature = 135 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AMX-TILE[bit 24]
"""
AMX_INT8: CpuidFeature = 136 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AMX-INT8[bit 25]
"""
CYRIX_FPU: CpuidFeature = 137 # type: ignore
"""
Cyrix FPU instructions (Cyrix, AMD Geode GX/LX)
"""
CYRIX_SMM: CpuidFeature = 138 # type: ignore
"""
: Cyrix SMM instructions: ``SVDC``, ``RSDC``, ``SVLDT``, ``RSLDT``, ``SVTS``, ``RSTS`` (Cyrix, AMD Geode GX/LX)
"""
CYRIX_SMINT: CpuidFeature = 139 # type: ignore
"""
Cyrix ``SMINT 0F38`` (6x86MX and later, AMD Geode GX/LX)
"""
CYRIX_SMINT_0F7E: CpuidFeature = 140 # type: ignore
"""
Cyrix ``SMINT 0F7E`` (6x86 or earlier)
"""
CYRIX_SHR: CpuidFeature = 141 # type: ignore
"""
: Cyrix SMM instructions: ``RDSHR``, ``WRSHR`` (6x86MX, M II, Cyrix III)
"""
CYRIX_DDI: CpuidFeature = 142 # type: ignore
"""
: Cyrix DDI instructions: ``BB0_Reset``, ``BB1_Reset``, ``CPU_READ``, ``CPU_WRITE`` (MediaGX, GXm, GXLV, GX1)
"""
CYRIX_EMMI: CpuidFeature = 143 # type: ignore
"""
: Cyrix AND CPUID.80000001H:EDX.EMMI[bit 24]
"""
CYRIX_DMI: CpuidFeature = 144 # type: ignore
"""
: Cyrix DMI instructions: ``DMINT``, ``RDM`` (AMD Geode GX/LX)
"""
CENTAUR_AIS: CpuidFeature = 145 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.AIS[Bits 1:0] = 11B ([0] = exists, [1] = enabled)
"""
MOV_TR: CpuidFeature = 146 # type: ignore
"""
MOV to/from TR (80386, Intel486, Cyrix, Geode)
"""
SMM: CpuidFeature = 147 # type: ignore
"""
``RSM`` instruction (some 386s, some 486s, Pentium and later)
"""
TDX: CpuidFeature = 148 # type: ignore
"""
: CPUID.(EAX=??H, ECX=?H):???.????[bit ??]
"""
KL: CpuidFeature = 149 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):ECX.KL[bit 23]
"""
AESKLE: CpuidFeature = 150 # type: ignore
"""
: CPUID.19H:EBX.AESKLE[bit 0]
"""
WIDE_KL: CpuidFeature = 151 # type: ignore
"""
: CPUID.19H:EBX.WIDE_KL[bit 2]
"""
UINTR: CpuidFeature = 152 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.UINTR[bit 5]
"""
HRESET: CpuidFeature = 153 # type: ignore
"""
: CPUID.(EAX=07H, ECX=01H):EAX.HRESET[bit 22]
"""
AVX_VNNI: CpuidFeature = 154 # type: ignore
"""
: CPUID.(EAX=07H, ECX=01H):EAX.AVX-VNNI[bit 4]
"""
PADLOCK_GMI: CpuidFeature = 155 # type: ignore
"""
: CPUID.0C0000000H:EAX >= 0C0000001H AND CPUID.0C0000001H:EDX.GMI[Bits 5:4] = 11B ([4] = exists, [5] = enabled)
"""
FRED: CpuidFeature = 156 # type: ignore
"""
: CPUID.(EAX=07H, ECX=01H):EAX.FRED[bit 17]
"""
LKGS: CpuidFeature = 157 # type: ignore
"""
: CPUID.(EAX=07H, ECX=01H):EAX.LKGS[bit 18]
"""
AVX512_FP16: CpuidFeature = 158 # type: ignore
"""
: CPUID.(EAX=07H, ECX=0H):EDX.AVX512-FP16[bit 23]
"""
UDBG: CpuidFeature = 159 # type: ignore
"""
Undocumented Intel ``RDUDBG`` and ``WRUDBG`` instructions
"""
KNC: CpuidFeature = 160 # type: ignore
"""
Intel Knights Corner
"""
PADLOCK_UNDOC: CpuidFeature = 161 # type: ignore
"""
Undocumented instruction
"""
