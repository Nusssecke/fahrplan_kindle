# https://github.com/NiLuJe/FBInk/blob/master/fbink.h
# Better wrapper UNFINISHED!!!

import platform
from enum import Enum

if platform.release() == '5.19.0-76051900-generic':
    from bin.fbink import FBInk_old
else:
    # Load the wrapper module, it's linked against FBInk, so the dynamic loader will take care of pulling in the actual FBInk library
    from _fbink import ffi, lib as FBInk

# Magic number for automatic fbfd handling
FBFD_AUTO = -1
# As 0 is an invalid marker value, we can coopt it to try to retrieve our own last sent marker
LAST_MARKER = 0


# List of available fonts
class FONT_INDEX(Enum):
    IBM = 0  # font8x8
    UNSCII = 1  # unscii-8
    UNSCII_ALT = 2  # unscii-8-alt
    UNSCII_THIN = 3  # unscii-8-thin
    UNSCII_FANTASY = 4  # unscii-8-fantasy
    UNSCII_MCR = 5  # unscii-8-mcr
    UNSCII_TALL = 6  # unscii-16
    BLOCK = 7  # block
    LEGGIE = 8  # leggie (regular)
    VEGGIE = 9  # leggie EGA/VGA/FB
    KATES = 10  # kates (nexus)
    FKP = 11  # fkp
    CTRLD = 12  # ctrld
    ORP = 13  # orp (regular)
    ORPB = 14  # orp (bold)
    ORPI = 15  # orp (italic)
    SCIENTIFICA = 16  # scientifica (regular)
    SCIENTIFICAB = 17  # scientifica (bold)
    SCIENTIFICAI = 18  # scientifica (italic)
    TERMINUS = 19  # terminus (regular)
    TERMINUSB = 20  # terminus (bold)
    FATTY = 21  # fatty
    SPLEEN = 22  # spleen
    TEWI = 23  # tewi (medium)
    TEWIB = 24  # tewi (bold)
    TOPAZ = 25  # Topaz+ A1200
    MICROKNIGHT = 26  # MicroKnight+
    VGA = 27  # IBM VGA 8x16
    UNIFONT = 28  # Unifont (single-wide glyphs only)
    UNIFONTDW = 29  # Unifont (double-wide glyphs only)
    COZETTE = 30  # Cozette
    FONT_MAX = 255


# List of supported font styles
class FONT_STYLE(Enum):
    FNT_REGULAR = 0
    FNT_ITALIC = 1
    FNT_BOLD = 2
    FNT_BOLD_ITALIC = 3


# List of available halign/valign values
class ALIGN_INDEX(Enum):
    NONE = 0
    CENTER = 1
    EDGE = 2
    ALIGN_MAX = 255


# List of available padding values
class PADDING_INDEX(Enum):
    NO_PADDING = 0
    HORI_PADDING = 1
    VERT_PADDING = 2
    FULL_PADDING = 3
    MAX_PADDING = 255


# List of available colors in the eInk color map
# NOTE: This is split in FG & BG to ensure that the default values lead to a sane result (i.e., black on white)
class FG_COLOR_INDEX(Enum):
    FG_BLACK = 0  # 0x00
    FG_GRAY1 = 1  # 0x11
    FG_GRAY2 = 2  # 0x22
    FG_GRAY3 = 3  # 0x33
    FG_GRAY4 = 4  # 0x44
    FG_GRAY5 = 5  # 0x55
    FG_GRAY6 = 6  # 0x66
    FG_GRAY7 = 7  # 0x77
    FG_GRAY8 = 8  # 0x88
    FG_GRAY9 = 9  # 0x99
    FG_GRAYA = 10  # 0xAA
    FG_GRAYB = 11  # 0xBB
    FG_GRAYC = 12  # 0xCC
    FG_GRAYD = 13  # 0xDD
    FG_GRAYE = 14  # 0xEE
    FG_WHITE = 15  # 0xFF
    FG_MAX = 255


class BG_COLOR_INDEX(Enum):
    BG_WHITE = 0
    BG_GRAY1 = 1
    BG_GRAY2 = 2
    BG_GRAY3 = 3
    BG_GRAY4 = 4
    BG_GRAY5 = 5
    BG_GRAY6 = 6
    BG_GRAY7 = 7
    BG_GRAY8 = 8
    BG_GRAY9 = 9
    BG_GRAYA = 10
    BG_GRAYB = 11
    BG_GRAYC = 12
    BG_GRAYD = 13
    BG_GRAYE = 14
    BG_BLACK = 15
    BG_MAX = 255


# List of Cervantes device IDs (HWConfig PCB index)
class CERVANTES_DEVICE_ID(Enum):
    DEVICE_CERVANTES_TOUCH = 22
    DEVICE_CERVANTES_TOUCHLIGHT = 23
    DEVICE_CERVANTES_2013 = 33
    DEVICE_CERVANTES_3 = 51
    DEVICE_CERVANTES_4 = 68
    DEVICE_CERVANTES_MAX = 65535


# List of Kobo device IDs
class KOBO_DEVICE_ID(Enum):
    DEVICE_KOBO_TOUCH_AB = 310
    DEVICE_KOBO_TOUCH_C = 320
    DEVICE_KOBO_MINI = 340
    DEVICE_KOBO_GLO = 330
    DEVICE_KOBO_GLO_HD = 371
    DEVICE_KOBO_TOUCH_2 = 372
    DEVICE_KOBO_AURA = 360
    DEVICE_KOBO_AURA_HD = 350
    DEVICE_KOBO_AURA_H2O = 370
    DEVICE_KOBO_AURA_H2O_2 = 374
    DEVICE_KOBO_AURA_H2O_2_R2 = 378
    DEVICE_KOBO_AURA_ONE = 373
    DEVICE_KOBO_AURA_ONE_LE = 381
    DEVICE_KOBO_AURA_SE = 375
    DEVICE_KOBO_AURA_SE_R2 = 379
    DEVICE_KOBO_CLARA_HD = 376
    DEVICE_KOBO_FORMA = 377
    DEVICE_KOBO_FORMA_32GB = 380
    DEVICE_KOBO_LIBRA_H2O = 384
    DEVICE_KOBO_NIA = 382
    DEVICE_KOBO_ELIPSA = 387
    DEVICE_KOBO_LIBRA_2 = 388
    DEVICE_KOBO_SAGE = 383
    DEVICE_KOBO_CLARA_2E = 386
    DEVICE_KOBO_MAX = 65535


"""# List of device IDs for mainline kernels
# c.f., https://github.com/NiLuJe/FBInk/issues/70#issuecomment-1242274710 for Tolinos
class MAINLINE_DEVICE_ID(Enum):
    DEVICE_MAINLINE_TOLINO_SHINE_2HD = ('T' << 8) | ('o' << 8) | ('l' << 8) | KOBO_DEVICE_ID.DEVICE_KOBO_GLO_HD,
    DEVICE_MAINLINE_TOLINO_SHINE_3 = ('T' << 8) | ('o' << 8) | ('l' << 8) | KOBO_DEVICE_ID.DEVICE_KOBO_CLARA_HD,
    DEVICE_MAINLINE_TOLINO_VISION_5 = ('T' << 8) | ('o' << 8) | ('l' << 8) | KOBO_DEVICE_ID.DEVICE_KOBO_LIBRA_H2O,
    DEVICE_MAINLINE_GENERIC_IMX5 = ('i' << 8) | ('.' << 8) | 'M' | 'X' | '5',
    DEVICE_MAINLINE_GENERIC_IMX6 = ('i' << 8) | ('.' << 8) | 'M' | 'X' | '6',
    DEVICE_MAINLINE_GENERIC_SUNXI_B300 = ('A' << 8) | ('W' << 8) | 'B' | '3' | '0' | '0',
    DEVICE_MAINLINE_MAX = 65535"""


class REMARKABLE_DEVICE_ID(Enum):
    DEVICE_REMARKABLE_1 = 1
    DEVICE_REMARKABLE_2 = 2
    DEVICE_REMARKABLE_MAX = 65535


# List of PocketBook device IDs
class POCKETBOOK_DEVICE_ID(Enum):
    DEVICE_POCKETBOOK_MINI = 515
    DEVICE_POCKETBOOK_606 = 606
    DEVICE_POCKETBOOK_611 = 611
    DEVICE_POCKETBOOK_613 = 613
    DEVICE_POCKETBOOK_614 = 614
    DEVICE_POCKETBOOK_615 = 615
    DEVICE_POCKETBOOK_616 = 616
    DEVICE_POCKETBOOK_617 = 617
    DEVICE_POCKETBOOK_TOUCH = 622
    DEVICE_POCKETBOOK_LUX = 623
    DEVICE_POCKETBOOK_BASIC_TOUCH = 624
    DEVICE_POCKETBOOK_BASIC_TOUCH_2 = 625
    DEVICE_POCKETBOOK_LUX_3 = 626
    DEVICE_POCKETBOOK_LUX_4 = 627
    DEVICE_POCKETBOOK_LUX_5 = 628
    DEVICE_POCKETBOOK_SENSE = 630
    DEVICE_POCKETBOOK_TOUCH_HD = 631
    DEVICE_POCKETBOOK_TOUCH_HD_PLUS = 632
    DEVICE_POCKETBOOK_COLOR = 633
    DEVICE_POCKETBOOK_AQUA = 640
    DEVICE_POCKETBOOK_AQUA2 = 641
    DEVICE_POCKETBOOK_ULTRA = 650
    DEVICE_POCKETBOOK_INKPAD_3 = 740
    DEVICE_POCKETBOOK_INKPAD_3_PRO = 742
    DEVICE_POCKETBOOK_INKPAD_COLOR = 741
    DEVICE_POCKETBOOK_INKPAD = 840
    DEVICE_POCKETBOOK_INKPAD_X = 1040
    # DEVICE_POCKETBOOK_COLOR_LUX = ('C' << 8) | ('o' << 8) | ('l' << 8) | ('o' << 8) | ('r' << 8) | 'L' | 'u' | 'x'
    DEVICE_POCKETBOOK_INKPAD_LITE = 970
    DEVICE_POCKETBOOK_MAX = 65535


# If device detection failed...
DEVICE_UNKNOWN = 0

# NOTE: There's no enum for Kindles, because there are an insane number of device IDs per model,
#       so it doesn't really fit into this model. Use the deviceName instead.
DEVICE_ID = int


# List of *potentially* available waveform modes.
# NOTE: On EPDC v1 (as well as all Kindle) devices, REAGL & REAGLD generally expect to *always* be flashing.
#       This is currently left at your own discretion, though.
#       c.f., https://github.com/NiLuJe/FBInk/commit/32acece78f7cc92b06faa4a668feead260b8ce24
# NOTE: On very old devices (e.g., Kobo Mk. 3 & 4; possibly early PB), only AUTO, DU & GC16 may be relied on.
#       GC4 will probably behave, but A2 & GL16 are not a given at all:
#       e.g., GL16 is actively broken on Kobo <= Mk. 4: c.f.,
#       https://github.com/baskerville/plato/issues/158#issuecomment-787520759.
#       If a waveform mode produces unexpected/broken results,
#       and/or if you start to hit unexpected EPDC timeouts (or even an OOPS),
#       that's usually a strong hint that you're trying to use something you shouldn't ;).
# NOTE: See the various mxcfb headers in the eink folder for more details about what's available on your platform.
class WFM_MODE_INDEX(Enum):
    WFM_AUTO = 0  # Let the EPDC choose, via histogram analysis of the refresh region.
    #                   May *not* always (or ever) opt to use REAGL on devices where it is otherwise available.
    #                   This is the default.
    #                   If you request a flashing update w/ AUTO, FBInk automatically uses GC16 instead.
    #                   NOTE: On sunxi SoCs, this analysis is done on CPU, instead of by the PxP.
    #                         As such, it's going to be slower. Prefer explicitly choosing a mode instead.
    #                         (When in doubt, GL16 is usually a good middle ground).
    # Common
    WFM_DU = 1  # From any to B&W, fast (~260ms), some light ghosting.
    #            On-screen pixels will be left as-is for new content that is *not* B&W.
    #            Great for UI highlights, or tracing touch/pen input.
    #            Will never flash.
    #            DU stands for "Direct Update".
    WFM_GC16 = 2  # From any to any, ~450ms, high fidelity (i.e., lowest risk of ghosting).
    #              Ideal for image content.
    #              If flashing, will flash and update the full region.
    #              If not, only changed pixels will update.
    #              GC stands for "Grayscale Clearing"
    WFM_GC4 = 3  # From any to B/W/GRAYA/GRAY5, (~290ms), some ghosting. (may be implemented as DU4 on some devices).
    #             Will *probably* never flash, especially if the device doesn't implement any other 4 color modes.
    #             Limited use-cases in practice.
    WFM_A2 = 4  # From B&W to B&W, fast (~120ms), some ghosting.
    #            On-screen pixels will be left as-is for new content that is *not* B&W.
    #            FBInk will ask the EPDC to enforce quantization to B&W to honor the "to" requirement,
    #            (via EPDC_FLAG_FORCE_MONOCHROME).
    #            Will never flash.
    #            Consider bracketing a series of A2 refreshes between white screens to transition in and out of A2,
    #            so as to honor the "from" requirement,
    #            (especially given that FORCE_MONOCHROME may not be reliably able to do so, c.f., refresh_kobo_mk7):
    #            non-flashing GC16 for the in transition, A2 or GC16 for the out transition.
    #            A stands for "Animation"
    WFM_GL16 = 5  # From white to any, ~450ms, some ghosting.
    #              Typically optimized for text on a white background.
    # Newer generation devices only
    WFM_REAGL = 6  # From white to any, ~450ms, with ghosting and flashing reduction.
    #               When available, best option for text (in place of GL16).
    #               May enforce timing constraints if in collision with another waveform mode, e.g.,
    #               it may, to some extent, wait for completion of previous updates to have access to HW resources.
    #               Marketing term for the feature is "Regal". Technically called 5-bit waveform modes.
    WFM_REAGLD = 7  # From white to any, ~450ms, with more ghosting reduction, but less flashing reduction.
    #                Should only be used when flashing, which should yield a less noticeable flash than GC16.
    #                Rarely used in practice, because still optimized for text or lightly mixed content,
    #                not pure image content.
    # (Mostly) Kindle only
    WFM_GC16_FAST = 8  # Better latency at the expense of lower fidelity than GC16.
    WFM_GL16_FAST = 9  # Better latency at the expense of lower fidelity than GL16.
    WFM_DU4 = 10  # From any to B/W/GRAYA/GRAY5. (e.g., GC4. Will never flash. Also available on Kobo Mk. 9).
    WFM_GL4 = 11  # From white to B/W/GRAYA/GRAY5.
    WFM_GL16_INV = 12  # From black to any. Optimized for text on a black background (e.g., nightmode).
    # "Nightmode" waveform modes (dubbed "eclipse" in Kobo-land).
    # Only available on some devices (Zelda on Kindle, Mk. 8+ on Kobo).
    # If you need to check at runtime whether it's actually supported, on an i.MX board,
    # check if /sys/class/graphics/fb0/waveform_mode_gck16 exists ;).
    # Otherwise, refer to the hasEclipseWfm deviceQuirks.
    WFM_GCK16 = 13  # From black to any. Goes hand-in-hand with GLKW16, should only be used when flashing.
    WFM_GLKW16 = 14  # From black to any. Newer variant of GL16_INV. (On Kobo, Mk. 9 only. It's GLK16 on sunxi).
    # For documentation purposes
    WFM_INIT = 15  # May flash several times to end up with a white screen, slow (~2000ms).
    WFM_UNKNOWN = 16
    # reMarkable only
    WFM_INIT2 = 17
    # PocketBook only
    WFM_A2IN = 18
    WFM_A2OUT = 19
    WFM_GC16HQ = 20  # Only available on i.MX SoCs. Alias for REAGL, or REAGLD when flashing.
    WFM_GS16 = 21  # Only available on B288 SoCs. Fidelity supposedly somewhere between GL16 and GC16.
    # Kobo Sunxi only
    WFM_GU16 = 22  # GL16, but honoring the in-kernel DISP_EINK_SET_GC_CNT
    # WFM_GCK16,    # GC16, but for white - on - black.
    WFM_GLK16 = 23  # GL16, but for white-on-black.
    WFM_CLEAR = 24  # GC16 local (NOTE: Appears to crash the EPDC... [Elipsa on FW 4.28.17826])
    WFM_GC4L = 25  # GC4 local (NOTE: Appears to crash the EPDC... [Elipsa on FW 4.28.17826])
    WFM_GCC16 = 26  # GCC16
    WFM_MAX = 255


# List of *potentially* available HW dithering modes
class HW_DITHER_INDEX(Enum):
    HWD_PASSTHROUGH = 0
    HWD_FLOYD_STEINBERG = 1
    HWD_ATKINSON = 2
    HWD_ORDERED = 3  # Generally the only supported HW variant on EPDC v2
    HWD_QUANT_ONLY = 4
    HWD_LEGACY = 255  # Use legacy EPDC v1 dithering instead (if available).
    #                        Note that it is *not* offloaded to the PxP, it's purely software, in-kernel.
    #                        Usually based on Atkinson's algo. The most useful one being the Y8->Y1 one,
    #                        which we request with A2/DU refreshes.


# List of NTX rotation quirk types (c.f., mxc_epdc_fb_check_var @ drivers/video/fbdev/mxc/mxc_epdc_v2_fb.c)...
class NTX_ROTA_INDEX(Enum):
    NTX_ROTA_STRAIGHT = 0  # No shenanigans (at least as far as ioctls are concerned)
    NTX_ROTA_ALL_INVERTED = 1  # Every rotation is inverted by the kernel
    NTX_ROTA_ODD_INVERTED = 2  # Only Landscape (odd) rotations are inverted by the kernel
    NTX_ROTA_SANE = 3  # NTX_ROTA_STRAIGHT, and ntxBootRota is the native Portrait orientation.
    #                            Optionally, bonus points if that's actually UR, and the panel is natively mounted UR,
    #                            like on the Kobo Libra.
    #                            Triple whammy if the touch layer rotation matches!
    NTX_ROTA_SUNXI = 4  # The rotate flag is technically meaningless, but *may* be set by third-party code (we don't).
    NTX_ROTA_CW_TOUCH = 5  # No kernel shenanigans, and Touch panel mounted in the invert of the usual rotation.
    NTX_ROTA_MAX = 255


# Available states for fbink_sunxi_ntx_enforce_rota
class SUNXI_FORCE_ROTA_INDEX(Enum):
    FORCE_ROTA_NOTSUP = -128  # For FBInkState on non-sunxi platforms
    FORCE_ROTA_CURRENT_ROTA = -5  # Honor the gyro if it matches the working buffer's rotation; match the wb otherwise (NOTE: Requires fbdamage)
    FORCE_ROTA_CURRENT_LAYOUT = -4  # Honor the gyro if it matches the working buffer's layout; match the wb otherwise (NOTE: Requires fbdamage)
    FORCE_ROTA_PORTRAIT = -3  # Honor the gyro if it matches a Portrait layout
    FORCE_ROTA_LANDSCAPE = -2  # Honor the gyro if it matches a Landscape layout
    FORCE_ROTA_GYRO = -1  # Honor the gyro (NOTE: default)
    FORCE_ROTA_UR = 0  # FB_ROTATE_UR
    FORCE_ROTA_CW = 1  # FB_ROTATE_CW
    FORCE_ROTA_UD = 2  # FB_ROTATE_UD
    FORCE_ROTA_CCW = 3  # FB_ROTATE_CCW
    FORCE_ROTA_WORKBUF = 4  # Match the working buffer's rotation (NOTE: Requires fbdamage)
    FORCE_ROTA_MAX = 127


# List of swipe directions for fbink_mtk_set_swipe_data
class MTK_SWIPE_DIRECTION_INDEX(Enum):
    MTK_SWIPE_DIR_DOWN = 0
    MTK_SWIPE_DIR_UP = 1
    MTK_SWIPE_DIR_LEFT = 2
    MTK_SWIPE_DIR_RIGHT = 3
    MTK_SWIPE_DIR_MAX = 255


# List of halftone pattern modes for fbink_mtk_set_halftone
class MTK_HALFTONE_MODE_INDEX(Enum):
    MTK_HALFTONE_DISABLED = 0
    MTK_HALFTONE_DEFAULT_CHECKER_SIZE = 1
    MTK_HALFTONE_MAX_CHECKER_SIZE = 2147483647


# A struct to dump FBInk's internal state into, like fbink_state_dump() would, but in C ;)
class FBInkState:
    user_hz: int  # USER_HZ (should pretty much always be 100)
    font_name: str  # fbink_cfg->fontname (c.f., fontname_to_string())
    view_width: int  # viewWidth (MAY be different than screen_width on devices with a viewport)
    view_height: int  # viewHeight (ditto)
    screen_width: int  # screenWidth (Effective width, c.f., is_ntx_quirky_landscape & initialize_fbink())
    screen_height: int  # screenHeight (ditto)
    scanline_stride: int  # fInfo.line_length (scanline length in bytes, padding included)
    bpp: int  # vInfo.bits_per_pixel
    inverted_grayscale: bool  # true if vInfo.grayscale is set to GRAYSCALE_8BIT_INVERTED (@ 8bpp)
    device_name: str  # deviceQuirks.deviceName (short common name, no brand)
    device_codename: str  # deviceQuirks.deviceCodename
    device_platform: str  # deviceQuirks.devicePlatform (often a codename, too)
    device_id: DEVICE_ID  # deviceQuirks.deviceId (decimal value, c.f., identify_device() on Kindle!)
    pen_fg_color: int  # penFGColor (Actual grayscale value, not FG_COLOR_INDEX_E)
    pen_bg_color: int  # penBGColor (ditto)
    screen_dpi: int  # deviceQuirks.screenDPI
    font_w: int  # FONTW (effective width of a glyph cell, i.e. scaled)
    font_h: int  # FONTH (effective height of a glyph cell, i.e. scaled)
    max_cols: int  # MAXCOLS (at current cell size)
    max_rows: int  # MAXROWS (ditto)
    view_hori_origin: int  # viewHoriOrigin (would be non-zero on devices with a horizontal viewport)
    view_vert_origin: int  # viewVertOrigin (origin in px of row 0, includes viewport + viewVertOffset)
    view_vert_offset: int  # viewVertOffset (shift in px needed to vertically balance rows over viewHeight)
    fontsize_mult: int  # FONTSIZE_MULT (current cell scaling multiplier)
    glyph_width: int  # glyphWidth (native width of a glyph cell, i.e. unscaled)
    glyph_height: int  # glyphHeight (native height of a glyph cell, i.e. unscaled)
    is_perfect_fit: bool  # deviceQuirks.isPerfectFit (horizontal column balance is perfect over viewWidth)
    is_sunxi: bool  # deviceQuirks.isSunxi (device is running on an AllWinner SoC)
    sunxi_has_fbdamage: bool  # sunxiCtx.has_fbdamage (true when fbdamage module is loaded)
    sunxi_force_rota: SUNXI_FORCE_ROTA_INDEX  # sunxiCtx.force_rota (current effective value)
    is_kindle_legacy: bool  # deviceQuirks.isKindleLegacy (device is a Kindle using the original einkfb EPDC API)
    is_kindle_mtk: bool  # deviceQuirks.isKindleMTK (device is a Kindle running on a MediatTek SoC)
    is_kobo_non_mt: bool  # deviceQuirks.isKoboNonMT (device is a Kobo with no MultiTouch input support)
    ntx_boot_rota: int  # deviceQuirks.ntxBootRota (Native rotation at boot)
    ntx_rota_quirk: NTX_ROTA_INDEX  # deviceQuirks.ntxRotaQuirk (c.f., utils/dump.c)
    is_ntx_quirky_landscape: bool  # deviceQuirks.isNTX16bLandscape (rotation compensation is in effect)
    current_rota: int  # vInfo.rotate (current native rotation, c.f., <linux/fb.h>)
    can_rotate: bool  # deviceQuirks.canRotate (device has a gyro)
    can_hw_invert: bool  # deviceQuirks.canHWInvert (device can use EPDC inversion)
    has_eclipse_wfm: bool  # deviceQuirks.hasEclipseWfm (device can use nightmode waveform modes)


# What a FBInk config should look like. Perfectly sane when fully zero-initialized.
class FBInkConfig:

    def __init__(self):
        self._fbink_cfg = ffi.new("FBInkConfig *")

    @property
    def row(self) -> int:
        """ :return: y axis (i.e. line), counts down from the bottom of the screen if negative"""
        return self._fbink_cfg.row

    @row.setter
    def row(self, value: int):
        """:param value: y axis (i.e. line), counts down from the bottom of the screen if negative"""
        print("setter of x called")
        self._fbink_cfg.row = value

    col: int  # x axis (i.e., column), counts down from the right edge of the screen if negative
    fontmult: int  # Font scaling multiplier (i.e., 4 -> x4), 0 means automatic.
    fontname: FONT_INDEX  # Request a specific bundled font
    is_inverted: bool  # Invert colors.
    #               This is *NOT* mutually exclusive with is_nightmode, and is *always* supported.
    is_flashing: bool  # Request a black flash on refresh (e.g., UPDATE_MODE_FULL instead of PARTIAL)
    is_cleared: bool  # Clear the full screen beforehand (honors bg_color & is_inverted)
    is_centered: bool  # Center the text (horizontally)
    hoffset: int  # Horizontal offset (in pixels) for text position
    voffset: int  # Vertical offset (in pixels) for text position
    is_halfway: bool  # Vertically center the text, honoring row offsets
    is_padded: bool  # Pad the text with blanks (on the left, or on both sides if is_centered)
    is_rpadded: bool  # Right pad the text with blanks
    fg_color: FG_COLOR_INDEX  # Requested foreground color for text (palette index)
    bg_color: BG_COLOR_INDEX  # Requested background color for text (palette index)
    is_overlay: bool  # Don't draw bg and use inverse of fb's underlying pixel as pen fg color
    is_bgless: bool  # Don't draw bg (mutually exclusive with is_overlay, which will take precedence)
    is_fgless: bool  # Don't draw fg (takes precendence over is_overlay/is_bgless)
    no_viewport: bool  # Ignore viewport corrections, whether hardware-related on Kobo, or to center rows
    is_verbose: bool  # Print verbose diagnostic informations on stdout
    is_quiet: bool  # Hide fbink_init()'s hardware setup info (sent to stderr)
    ignore_alpha: bool  # Ignore any potential alpha channel in source image (i.e., flatten the image)
    halign: ALIGN_INDEX  # Horizontal alignment of images/dumps
    valign: ALIGN_INDEX  # Vertical alignment of images/dumps
    scaled_width: int  # Output width of images/dumps (0 for no scaling, -1 for viewport width)
    scaled_height: int  # Output height of images/dumps (0 for no scaling, -1 for viewport height)
    #                   If only *one* of them is left at 0, the image's aspect ratio will be honored.
    #                   If *either* of them is set to < -1, fit to screen while respecting AR.
    #                   NOTE: Scaling is inherently costly. I highly recommend not relying on it,
    #                         preferring instead proper preprocessing of your input images,
    #                         c.f., https:#www.mobileread.com/forums/showpost.php?p=3728291&postcount=17
    wfm_mode: WFM_MODE_INDEX  # Request a specific waveform mode (defaults to AUTO)
    dithering_mode: HW_DITHER_INDEX  # Request a specific dithering mode (defaults to PASSTHROUGH)
    sw_dithering: bool  # Request (ordered) *software* dithering when printing an image.
    #                                      This is *NOT* mutually exclusive with dithering_mode!
    is_nightmode: bool  # Request hardware inversion (via EPDC_FLAG_ENABLE_INVERSION, if supported/safe).
    #            This is *NOT* mutually exclusive with is_inverted!
    #            NOTE: If the HW doesn't support inversion, a warning is printed during init.
    #                   If you're convinced this is in error (i.e., up to date kernel),
    #                   you can bypass that check by setting FBINK_ALLOW_HW_INVERT in your env.
    no_refresh: bool  # Skip actually refreshing the eInk screen (useful when drawing in batches)
    no_merge: bool  # Set the EINK_NO_MERGE flag (Kobo sunxi only)
    is_animated: bool  # Enable refresh animation, following fbink_mtk_set_swipe_data (Kindle MTK only)
    to_syslog: bool  # Send messages & errors to the syslog instead of stdout/stderr

    def to_c(self):
        fbink_cfg = ffi.new("FBInkConfig *")
        print(fbink_cfg.row)
        return fbink_cfg

# Same, but for OT/TTF specific stuff. MUST be zero-initialized.
class FBInkOTConfig:
    """TODO void* font    # NOTE: This is essentially a pointer to a local FBInkOTFonts instance,
    #                      in order to use a set of fonts specific to an FBInkOTConfig,
    #                      via fbink_add_ot_font_v2() & fbink_free_ot_fonts_v2().
    #                      Consider it *private*: it needs to be NULL on init to be sane, but after that,
    #                      it's only used & memory managed by FBInk itself (via the aforemented _v2 API), not the user.
    struct
    {
        short int top;       # Top margin in pixels (if negative, counts backwards from the bottom edge)
        short int bottom;    # Bottom margin in pixels (supports negative values, too)
        short int left;      # Left margin in pixels (if negative, counts backwards from the right edge)
        short int right;     # Right margin in pixels (supports negative values, too)
    } margins """
    style: FONT_STYLE  # Default font style to use when !is_formatted (defaults to Regular)
    size_pt: float  # Size of text in points. If not set (0.0f), defaults to 12pt
    size_px: int  # Size of text in pixels. Optional, but takes precedence over size_pt.
    is_centered: bool  # Horizontal centering
    padding: PADDING_INDEX  # Pad the drawing area (i.e., paint it in the background color).
    #                                    Unlike in the fixed-cell codepath, this always applies to both sides (L&R/T&B),
    #                                    no matter the chosen axis.
    #                                    e.g., HORI_PADDING is useful to prevent overlaps when drawing
    #                                    consecutive strings on the same line(s).
    is_formatted: bool  # Is string "formatted"? Bold/Italic support only, markdown like syntax
    compute_only: bool  # Abort early after the line-break computation pass (no actual rendering).
    #                       NOTE: This is early enough that it will *NOT* be able to predict *every*
    #                             potential case of truncation.
    #                             In particular, broken metrics may yield a late truncation at rendering time.
    no_truncation: bool  # Abort as early as possible (but not necessarily before the rendering pass),
    # if the string cannot fit in the available area at the current font size.


# Optionally used with fbink_print_ot, if you need more details about the line-breaking computations,
# for instance if you want to dynamically compute a best-fit font size for n lines in a specific area.
class FBInkOTFit:
    computed_lines: int  # Expected amount of lines needed, according to font metrics.
    rendered_lines: int  # Actually rendered amount of lines.
    #                                       Will stay 0 in case of an early abort (or a compute_only run),
    #                                       or < computed_lines in case of an unexpected truncation due to broken metrics.
    truncated: bool  # true if the string was truncated (at computation or rendering time).


# This maps to an mxcfb rectangle, used for fbink_get_last_rect, as well as in FBInkDump
# NOTE: Unlike an mxcfb rectangle, left (x) comes *before* top (y)!
class FBInkRect:
    left: int  # x
    top: int  # y
    width: int
    height: int


# For use with fbink_dump & fbink_restore
class FBInkDump:
    data: str
    stride: int
    size: int
    area: FBInkRect
    clip: FBInkRect  # Only restore this rectangular area of the screen (has to intersect w/ the dump's area)
    rota: int
    bpp: int
    is_full: bool


def fbink_version() -> str:
    return ffi.string(FBInk.fbink_version()).decode("ascii")


def fbink_open() -> int:
    """
    Open the framebuffer character device, and returns the newly opened file descriptor.
    @return: file_descriptor
    """
    return FBInk.fbink_open()


def fbink_close(fbfd: int) -> int:
    """
    Unmap the framebuffer (if need be) and close its file descriptor,
    (c.f., the recap at the bottom if you're concerned about mmap handling).
    NOTE: This is safe to call if fbfd is FBFD_AUTO (i.e., -1, which means this is also safe to call after an fbink_open failure).
    @param fbfd: Open file descriptor to the framebuffer character device, as returned by fbink_open()
    @return:
    """
    return FBInk.fbink_close(fbfd)


def fbink_init(fbfd: int, fbink_cfg: FBInkConfig) -> int:
    """
    Initialize internal variables keeping track of the framebuffer's configuration and state, as well as the device's hardware.
    MUST be called at least *once* before any fbink_print*, fbink_dump/restore, fbink_cls or fbink_grid* functions.
    CAN safely be called multiple times,
    but doing so is only necessary if the framebuffer's state has changed (although fbink_reinit is preferred in this case),
    or if you modified one of the FBInkConfig fields that affects its results (listed below).

    Returns -(ENOSYS) if the device is unsupported (NOTE: Only on reMarkable!)
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct.
                        If you wish to customize them, the fields:
                        is_centered, fontmult, fontname, fg_color, bg_color,
                        no_viewport, is_verbose, is_quiet & to_syslog
                        MUST be set beforehand.
                        This means you MUST call fbink_init() again when you update them, too!
                        (This also means the effects from those fields "stick" across the lifetime of your application,
                        or until a subsequent fbink_init() (or effective fbink_reinit()) call gets fed different values).
                        NOTE: For fg_color & bg_color, see fbink_update_pen_colors().
                        NOTE: For is_verbose, is_quiet & to_syslog, see fbink_update_verbosity().

    NOTE: By virtue of, well, setting global variables, do NOT consider this thread-safe.
        The rest of the API should be, though, so make sure you init in your main thread *before* threading begins...
    NOTE: If you just need to make sure the framebuffer state is still up to date before an fbink_* call,
        (e.g., because you're running on a Kobo, which may switch from 16bpp to 32bpp, or simply change orientation),
        prefer using fbink_reinit instead of calling fbink_init *again*, as it's tailored for this use case.
        c.f., KFMon for an example of this use case in the wild.
    NOTE: You can perfectly well keep a few different FBInkConfig structs around, instead of modifying the same one over and over.
        Just remember that some fields *require* an fbink_init() call to be taken into account (see above),
        but if the only fields that differ don't fall into that category, you do *NOT* need an fbink_init() per FBInkConfig...
    """
    return FBInk.fbink_init(fbfd, fbink_cfg.to_c())


def fbink_state_dump(fbink_cfg: FBInkConfig):
    """
    Dump a few of our internal state variables to stdout, in a format easily consumable by a shell (i.e., eval).
    """
    FBInk.fbink_state_dump(fbink_cfg)


def fbink_get_state(fbink_cfg: FBInkConfig, fbink_state: FBInkState):
    """
    Dump a few of our internal state variables to the FBInkState struct pointed to by fbink_state.
    NOTE: This includes quite a few useful things related to device identification, c.f., the FBInkState struct ;).
        You can also peek at the output of fbink -e to get a hint of what the data actually looks like.
    """
    FBInk.fbink_get_state(fbink_cfg, fbink_state)


def fbink_print(fbfd: int, string: str, fbink_cfg: FBInkConfig) -> int:
    """
    Print a string on screen.
    NOTE: The string is expected to be encoded in valid UTF-8:
            * Invalid UTF-8 sequences will be *rejected* and the call will abort early with -(EILSEQ)
            * We assume a single multibyte sequence will occupy a maximum of 4 bytes.
            c.f., my rant about Kobo's broken libc in fbink_internal.h for more details behind this choice.
            Since any decent system built in the last decade should default to UTF-8, that should be pretty much transparent...
    Returns the amount of lines printed on success (helpful when you keep track of which row you're printing to).
    Returns -(EINVAL) if string is empty.
    Returns -(EILSEQ) if string is not a valid UTF-8 sequence.
    Returns -(ENOSYS) when fixed-cell font support is disabled (MINIMAL build w/o BITMAP).
    @param fbfd:	    Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param string:	    UTF-8 encoded string to print.
    @param fbink_cfg:	Pointer to an FBInkConfig struct.
                        Honors every field not specifically related to image/dump support.
    """
    return FBInk.fbink_print(fbfd, bytes(string), fbink_cfg)


def fbink_add_ot_font(filename: str, style: FONT_STYLE) -> int:
    """
    Add an OpenType font to FBInk.
    NOTE: At least one font must be added in order to use fbink_print_ot().
    @param filename:		Path to the font file. This should be a valid *.otf or *.ttf font.
    @param style:		Defines the specific style of the specified font (FNT_REGULAR, FNT_ITALIC, FNT_BOLD or FNT_BOLD_ITALIC).
    NOTE: You MUST free the fonts loaded when you are done with all of them by calling fbink_free_ot_fonts().
    NOTE: You MAY replace a font without first calling fbink_free_ot_fonts().
    NOTE: Default fonts are secreted away in /usr/java/lib/fonts on Kindle,
        and in /usr/local/Trolltech/QtEmbedded-4.6.2-arm/lib/fonts on Kobo,
        but you can't use the Kobo ones because they're obfuscated...
        Which leads me to a final, critical warning:
    NOTE: Don't try to pass non-font files or encrypted/obfuscated font files, because it *will* horribly segfault!
    """
    return FBInk.fbink_add_ot_font(bytes(filename), style)


# style type is (FONT_STYLE_T), cfg type is (FBInkOTConfig)
def fbink_add_ot_font_v2(filename: str, style: FONT_STYLE, cfg: FBInkOTConfig) -> int:
    """
    Same API and behavior, except that the set of fonts being loaded is tied to this specific FBInkOTConfig instance,
    instead of being global.
    In which case, resources MUST be released via fbink_free_ot_fonts_v2()!
    NOTE: You can mix & match the v2 and legacy API, but for every fbink_add_ot_font() there must be an fbink_free_ot_fonts(),
        and for every fbink_add_ot_font_v2(), there must be an fbink_free_ot_fonts_v2()
        (for each matching FBInkOTConfig instance).
    """
    return FBInk.fbink_add_ot_font_v2(bytes(filename), style, cfg)


def fbink_free_ot_fonts() -> int:
    """
    Free all loaded OpenType fonts. You MUST call this when you have finished all OT printing.
    NOTE: Safe to call even if no fonts were actually loaded.
    @return: ?
    """
    return FBInk.fbink_free_ot_fonts()


def fbink_free_ot_fonts_v2(cfg: FBInkOTConfig) -> int:
    """
    Same, but for a specific FBInkOTConfig instance if fbink_add_ot_font_v2 was used.
    NOTE: Safe to call even if no fonts were actually loaded, in which case it'll return -(EINVAL)!
    """
    return FBInk.fbink_free_ot_fonts_v2(cfg)


def fbink_print_ot(fbfd: int, string: str, cfg: FBInkOTConfig, fbink_cfg: FBInkConfig, fit: FBInkOTFit) -> int:
    """
    Print a string using an OpenType font.
    NOTE: The caller MUST have loaded at least one font via fbink_add_ot_font() FIRST.
    This function uses margins (in pixels) instead of rows/columns for positioning and setting the printable area.
    Returns a new top margin for use in subsequent calls, if the return value is positive.
    NOTE: A zero return value indicates there is no room left to print another row of text at the current margins or font size.
    Returns -(ERANGE) if the provided margins are out of range, or sum to < view height or width.
    Returns -(ENOSYS) when OT support is disabled (MINIMAL build w/o OPENTYPE).
    Returns -(ENODATA) if fbink_add_ot_font() hasn't been called yet.
    Returns -(EINVAL) if string is empty.
    Returns -(EILSEQ) if string is not a valid UTF-8 sequence.
    Returns -(ENOSPC) if no_truncation is true, and string needs to be truncated to fit in the available draw area.
            NOTE: This *cannot* prevent *drawing* truncated content on screen in *every* case,
            because broken metrics may skew our initial computations.
            As such, if the intent is to compute a "best fit" font size,
            no_truncation ought to be combined with no_refresh on eInk,
            (as we otherwise do *NOT* inhibit the refresh, in order to preserve get_last_rect's accuracy).
            You'll also probably want to do a cheaper compute_only pass first,
            to catch more obviously predictable truncations.
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param string:      UTF-8 encoded string to print.
    @param cfg:			Pointer to an FBInkOTConfig struct.
    @param fbink_cfg:	Optional pointer to an FBInkConfig struct. If set, the fields
                        is_inverted, is_flashing, is_cleared, is_centered, is_halfway,
                        is_overlay, is_fgless, is_bgless, fg_color, bg_color, valign, halign,
                        wfm_mode, dithering_mode, is_nightmode, no_refresh will be honored.
                        Pass a NULL pointer if unneeded.
    @param fit:			Optional pointer to an FBInkOTFit struct.
                        If set, it will be used to return information about the amount of lines needed to render
                        the string at the requested font size, and whether it was truncated or not.
                        Pass a NULL pointer if unneeded.
    NOTE: Alignment is relative to the printable area, as defined by the margins.
        As such, it only makes sense in the context of a single, specific print call.
    """
    return FBInk.fbink_print_ot(fbfd, bytes(string), cfg, fbink_cfg, fit)


def fbink_printf(fbfd: int, cfg: FBInkOTConfig, fbink_cfg: FBInkConfig, fmt: str, *args) -> int:
    """
    Brings printf formatting to fbink_print and fbink_print_ot ;).
    @param fbfd:	Open file descriptor to the framebuffer character device,
                    if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param cfg:			Optional pointer to an FBInkOTConfig struct.
    @param fbink_cfg:		Optional pointer to an FBInkConfig struct.
    NOTE:   If cfg is NULL, will call fbink_print, otherwise, fbink_print_ot!
            If cfg is valid, fbink_cfg MAY be NULL (same behavior as fbink_print_ot).
            If cfg is NULL, fbink_cfg MUST be valid.
    NOTE: Meaning at least one of those two pointers MUST be valid!
    """
    return FBInk.fbink_printf(fbfd, cfg, fbink_cfg, bytes(fmt))


def fbink_refresh(fbfd: int, region_top: int, region_left: int, region_width: int, region_height: int,
                  fbink_cfg) -> int:
    """
    A simple wrapper around the internal screen refresh handling, without requiring you to include einkfb/mxcfb headers.
    NOTE: Unlike FBInkRect, we *do* honor the original mxcfb rect order here (top before left).
    Returns -(ENOSYS) on non-eInk devices (i.e., pure Linux builds)
    @param  fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param region_top:		top (y) field of an mxcfb rectangle.
    @param region_left:		left (x) field of an mxcfb rectangle.
    @param region_width:	width field of an mxcfb rectangle.
    @param region_height:	height field of an mxcfb rectangle.
    @param fbink_cfg:		Pointer to an FBInkConfig struct. Honors wfm_mode, dithering_mode, is_nightmode, is_flashing.
    NOTE:   If you request an empty region (0x0 @ (0, 0), a full-screen refresh will be performed!
    NOTE:   This *ignores* no_refresh ;).
    NOTE:   As far as dithering is concerned, c.f., HW_DITHER_INDEX_E enum.
            True HW dithering is only supported on devices with a recent EPDC (>= v2)!
            On Kindle, that's everything since the KOA2 (KOA2, PW4, KT4, KOA3),
            On Kobo, that's everything since Mk.7.
    NOTE:   Even then, your device may not actually support anything other than PASSTHROUGH & ORDERED!
            On slightly older devices, the EPDC may support some sort of in-kernel software dithering, hence HWD_LEGACY.
    NOTE:   If you do NOT want to request any dithering, set FBInkConfig's dithering_mode field to HWD_PASSTHROUGH (i.e., 0).
            This is also the fallback value.
    NOTE:   On Kobo devices with a sunxi SoC, you will not be able to refresh content that you haven't drawn yourself first.
            (There's no "shared" framebuffer, each process gets its own private, zero-initialized (i.e., solid black) buffer).
    NOTE:   In case of ioctl failure, errno *should* be preserved,
            allowing the caller to possibly handle some very specific edge-cases.
    """
    return FBInk.fbink_refresh(fbfd, region_top, region_left, region_width, region_height, fbink_cfg)


def fbink_wait_for_submission(fbfd: int, marker: int) -> int:
    """
    A simple wrapper around the MXCFB_WAIT_FOR_UPDATE_SUBMISSION ioctl, without requiring you to include mxcfb headers.
    Returns -(EINVAL) when the update marker is invalid.
    Returns -(ENOSYS) on devices where this ioctl is unsupported.
    NOTE: It is only implemented by Kindle kernels (K5+)!
    @param: fbfd:   Open file descriptor to the framebuffer character device,
                    if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param: marker: The update marker you want to wait for.
    NOTE:   If marker is set to LAST_MARKER (0U), the one from the last update sent by this FBInk session will be used instead.
            If there aren't any, the call will fail and return -(EINVAL)!
    NOTE: Waiting for a random marker *should* simply return early.
    """
    return FBInk.fbink_wait_for_submission(fbfd, marker)


def fbink_wait_for_complete(fbfd: int, marker: int) -> int:
    """
    A simple wrapper around the MXCFB_WAIT_FOR_UPDATE_COMPLETE ioctl, without requiring you to include mxcfb headers.
    Returns -(EINVAL) when the update marker is invalid.
    Returns -(ENOSYS) on non-eInk devices (i.e., pure Linux builds).
    @param fbfd:	Open file descriptor to the framebuffer character device,
                    if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param marker:	The update marker you want to wait for.
    NOTE:   If marker is set to LAST_MARKER (0U), the one from the last update sent by this FBInk session will be used instead.
            If there aren't any, the call will fail and return -(EINVAL)!
    NOTE:   Waiting for a random marker *should* simply return early.
    """
    return FBInk.fbink_wait_for_complete


def fbink_get_last_marker() -> int:
    """
    Return the update marker from the last *refresh* (explicit or implicit) done in this FBInk session.
    NOTE: Returns LAST_MARKER (0U) if there wasn't any, or on non-eInk devices (i.e., pure Linux builds).
    NOTE: Mainly useful if you want to do fairly fancy stuff with wait_for_complete/wait_for_submission,
    otherwise, simply passing LAST_MARKER to 'em should do the trick.
    """
    return FBInk.fbink_get_last_marker()


# We'll need those for fbink_reinit (start > 256 to stay clear of errno values)
OK_BPP_CHANGE: int = 512
OK_ROTA_CHANGE: int = 1024
OK_LAYOUT_CHANGE: int = 2048


def fbink_reinit(fbfd: int, fbink_cfg: FBInkConfig) -> int:
    """
    Attempt to detect changes in framebuffer states (between this call and the last time fbink_init/fbink_reinit was called),
    doing a reinit (i.e., calling fbink_init again) if needed, while doing the least amount of work possible in the process.
    NOTE: The intended use-case is for long running apps which may trigger prints across different framebuffer states,
        to allow them to ensure they'll be using up-to-date init data at key points in their lifecycle
        (without needing to bruteforce a full reinit on every print).
        This is of interest on a few devices, where trying to print based on a "stale" init state would at worst fail,
        at best produce unwanted results (e.g., after a bitdepth change or a hw rotation).
    NOTE: This obviously supercedes fbink_is_fb_quirky, because it should be smarter,
        by catching more scenarios where a reinit would be useful,
        and it can avoid running the same ioctl twice when an ioctl already done by init is needed to detect a state change.
    NOTE: Using fbink_reinit does NOT lift the requirement of having to run fbink_init at least ONCE,
        i.e., you cannot replace the initial fbink_init call by fbink_reinit!
    If reinitialization was *successful*, returns a bitmask with one or more of these flags set:
    bit OK_BPP_CHANGE is set if there was a bitdepth change.
    bit OK_ROTA_CHANGE is set if there was a rotation change.
    bit OK_LAYOUT_CHANGE is set if a rotation change caused a layout change (i.e., an orientation swap, Portrait <-> Landscape),
        this obviously implies OK_ROTA_CHANGE.
        If *only* OK_ROTA_CHANGE is set, it means the rotation change was a simple inversion of the current orientation,
        (i.e., Portrait <-> Inverted Portrait or Landscape <-> Inverted Landscape).
    bit OK_GRAYSCALE_CHANGE is set if there was a grayscale flag change.
        This is only set if the current & last known bitdepth is 8bpp.
        On mxcfb-like platforms, this flag is used by the epdc driver to toggle global HW inversion (a.k.a., night mode).
    NOTE: This means that it may return a *positive* non-zero value on *success*.
        This is helpful for callers that need to track FBInk's internal state via fbink_get_state or fbink_get_fb_pointer,
        because a reinit *might* affect the screen layout, signaling that their current state copy *may* be stale.
        TL;DR: Assume that *any* OK_*_CHANGE return value means that you need to refresh your state tracking.
    NOTE: You'll probably want to take action (changing pen colors or enabling inversion) after an OK_GRAYSCALE_CHANGE,
        especially if it's unexpected.
    NOTE: In turn, this means that a simple EXIT_SUCCESS means that no reinitialization was needed.
    NOTE: On Kobo devices with a sunxi SoC, OK_BPP_CHANGE will *never* happen,
        as the state of the actual framebuffer device is (unfortunately) meaningless there.
    @param fbfd:    Open file descriptor to the framebuffer character device,
				    if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param fbink_cfg:   Pointer to an FBInkConfig struct.
    """
    return FBInk.fbink_reinit(fbfd, fbink_cfg)


def fbink_update_verbosity(fbink_cfg: FBInkConfig):
    """
    Update FBInk's internal verbosity flags
    As mentioned in fbink_init(), the is_verbose, is_quiet & to_syslog fields in an FBInkConfig
    are only processed at initialization time.
    This function allows doing *just* that, without having to go through a more costly full (re)-init.
    @param fbink_cfg:		Pointer to an FBInkConfig struct (is_verbose, is_quiet & to_syslog).
    """
    return FBInk.fbink_update_verbosity(fbink_cfg)


def fbink_update_pen_colors(fbink_cfg: FBInkConfig) -> int:
    """
    Update FBInk's internal representation of pen colors
    As mentioned in fbink_init(), the fg_color & bg_color fields in an FBInkConfig are only processed at initialization time.
    This is because they're not used as-is (because they're not actually colors, just a custom palette index),
    they're just used to pack the matching palette color value into the right pixel format for the target framebuffer.
    This function allows doing *just* that, without having to go through a more costly full (re)-init.
    Returns -(ENOSYS) when drawing primitives are disabled (MINIMAL build w/o DRAW).
    @param fbink_cfg:		Pointer to an FBInkConfig struct (honors fg_color & bg_color).
    """
    return FBInk.fbink_update_pen_colors(fbink_cfg)


# We'll need those for fbink_set_*_pen_* (start > 256 to stay clear of errno values)
OK_ALREADY_SAME = 512


def fbink_set_fg_pen_gray(y: int, quantize: bool, update: bool) -> int:
    """
    Alternatively, you can choose to set the pen colors *directly*, without relying on FBInk's eInk palette handling.
    This is mostly of interest if you want to use color values you're getting from somewhere outside FBInk.
    You will *NOT* have to call fbink_update_pen_colors() when using these, they'll take care of updating the internal state.
    NOTE: The *optional* quantization pass *should* match what the EPDC itself will do anyway (i.e., it's redundant).
    Returns -(ENOSYS) when drawing primitives are disabled (MINIMAL build w/o DRAW).
    @param y:			8-bit luminance value
    @param quantize:	If true, round to the nearest eInk palette color.
    @param update:		If true, abort early and return OK_ALREADY_SAME if that's already the current color.
    """
    return FBInk.fbink_set_fg_pen_gray(y, quantize, update)


def fbink_set_bg_pen_gray(y: int, quantize: bool, update: bool) -> int:
    """
    Alternatively, you can choose to set the pen colors *directly*, without relying on FBInk's eInk palette handling.
    This is mostly of interest if you want to use color values you're getting from somewhere outside FBInk.
    You will *NOT* have to call fbink_update_pen_colors() when using these, they'll take care of updating the internal state.
    NOTE: The *optional* quantization pass *should* match what the EPDC itself will do anyway (i.e., it's redundant).
    Returns -(ENOSYS) when drawing primitives are disabled (MINIMAL build w/o DRAW).
    @param y:			8-bit luminance value
    @param quantize:	If true, round to the nearest eInk palette color.
    @param update:		If true, abort early and return OK_ALREADY_SAME if that's already the current color.
    """
    return FBInk.fbink_set_bg_pen_gray(y, quantize, update)


def fbink_set_fg_pen_rgba(r: int, g: int, b: int, a: int, quantize: bool, update: bool) -> int:
    """
    @param r:			8-bit red component value
    @param g:			8-bit green component value
    @param b:			8-bit blue component value
    @param a:          8-bit alpha component value (opaque is 0xFFu).
    @param quantize:	If true, round to the nearest eInk palette color. This implies a grayscaling pass!
    @param update:		If true, abort early and return OK_ALREADY_SAME if that's already the current color.
                Keep in mind that the comparison is done *after* grayscaling, even without quantize set.
    """
    return FBInk.fbink_set_fg_pen_rgba(r, g, b, a, quantize, update)


def fbink_set_bg_pen_rgba(r: int, g: int, b: int, a: int, quantize: bool, update: bool) -> int:
    """
    @param r:			8-bit red component value
    @param g:			8-bit green component value
    @param b:			8-bit blue component value
    @param a:          8-bit alpha component value (opaque is 0xFFu).
    @param quantize:	If true, round to the nearest eInk palette color. This implies a grayscaling pass!
    @param update:		If true, abort early and return OK_ALREADY_SAME if that's already the current color.
                Keep in mind that the comparison is done *after* grayscaling, even without quantize set.
    """
    return FBInk.fbink_set_bg_pen_rgba(r, g, b, a, quantize, update)


def fbink_print_progress_bar(fbfd: int, percentage: int, fbink_cfg: FBInkConfig) -> int:
    """
    Print a full-width progress bar on screen.
    Returns -(ENOSYS) when fixed-cell font support is disabled (MINIMAL build w/o BITMAP).
    @param fbfd:		    Open file descriptor to the framebuffer character device,
                            if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param percentage:		0-100 value to set the progress bar's progression.
    @param fbink_cfg:		Pointer to an FBInkConfig struct (ignores is_overlay, col & hoffset;
                            as well as is_centered & is_padded).
    """
    return FBInk.fbink_print_progress_bar(fbfd, percentage, fbink_cfg)


def fbink_print_activity_bar(fbfd: int, progress: int, fbink_cfg: FBInkConfig) -> int:
    """
    Print a full-width activity bar on screen (i.e., an infinite progress bar).
    Returns -(ENOSYS) when fixed-cell font support is disabled (MINIMAL build w/o BITMAP).
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param progress:	0-16 value to set the progress thumb's position in the bar.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (ignores is_overlay, is_fgless, col & hoffset;
                        as well as is_centered & is_padded).
    """
    return FBInk.fbink_print_activity_bar(fbfd, progress, fbink_cfg)


def fbink_print_image(fbfd: int, filename: str, x_off: int, y_off: int, fbink_cfg: FBInkConfig) -> int:
    """
    Print an image on screen.
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    @param fbfd:	    Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param filename:    Path to the image file (Supported formats: JPEG, PNG, TGA, BMP, GIF & PNM).
                        If set to "-" and stdin is not attached to a terminal,
                        will attempt to read image data from stdin.
    @param x_off:	    Target coordinates, x (honors negative offsets).
    @param y_off:	    Target coordinates, y (honors negative offsets).
    @param fbink_cfg:   Pointer to an FBInkConfig struct.
                        Where positioning is concerned, honors any combination of halign/valign, row/col & x_off/y_off;
                        otherwise, honors pretty much every other field not specifically concerned with text rendering.
    NOTE: Much like fbink_print_raw_data, for best performance,
        an image that decodes in a pixel format close to the one used by the target device fb is best.
        Generally, that'd be a Grayscale (color-type 0) PNG, ideally dithered down to the eInk palette
        (c.f., https://www.mobileread.com/forums/showpost.php?p=3728291&postcount=17).
        If you can't pre-process your images, dithering can be handled by the hardware on recent devices (c.f. dithering_mode),
        or by FBInk itself (c.f., sw_dithering), but the pixel format still matters:
        On a 32bpp fb, Gray will still be faster than RGB.
        On a 8bpp fb, try to only use Gray for the best performance possible,
        as an RGB input will need to be grayscaled, making it slower than if it were rendered on a 32bpp fb!
        Try to avoid using a 16bpp fb, as conversion to/from RGB565 will generally slow things down.
        If you know you won't need to handle an alpha channel, don't forget ignore_alpha, too ;).
        As expected, the fastest codepath is Gray on an 8bpp fb ;).
    NOTE: There's a direct copy fast path in the very specific case of printing a Grayscale image *without* alpha,
        inversion or dithering on an 8bpp fb.
    NOTE: No such luck on 32bpp, because of a mandatory RGB <-> BGR conversion ;).
    """
    return FBInk.fbink_print_image(fbfd, bytes(filename), x_off, y_off, fbink_cfg)


def fbink_print_raw_data(fbfd: int, data: str, w: int, h: int, len, x_off: int, y_off: int,
                         fbink_cfg: FBInkConfig) -> int:
    """
    Print raw scanlines on screen (packed pixels).
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param data:		Pointer to a buffer holding the image data (Supported pixel formats: Y/YA/RGB/RGBA,
                        8-bit components, the first pixel should be the top-left of the image).
    @param w:			Width (in pixels) of a single scanline of the input image data.
    @param h:			Height (in pixels) of the full image data (i.e., amount of scanlines).
    @param len:			*Exact* size of the input buffer.
                        Input pixel format is simply computed as len / h / w, so this *needs* to be exact,
                        do not pass a padded length (or pad the data itself in any way)!
    @param x_off:		Target coordinates, x (honors negative offsets).
    @param y_off:		Target coordinates, y (honors negative offsets).
    @param fbink_cfg:	Pointer to an FBInkConfig struct.
                        Where positioning is concerned, honors any combination of halign/valign, row/col & x_off/y_off;
                        otherwise, honors pretty much every other field not specifically concerned with text rendering.
    NOTE:   While we do accept a various range of input formats (as far as component interleaving is concerned),
            our display code only handles a few specific combinations, depending on the target hardware.
            To make everyone happy, this will transparently handle the pixel format conversion *as needed*,
            a process which incurs a single copy of the input buffer (same behavior as in the non-raw image codepath).
            If this is a concern to you, make sure your input buffer is formatted in a manner adapted to your output device:
            Generally, that'd be RGBA (32bpp) on Kobo (or RGB (24bpp) with ignore_alpha),
            and YA (grayscale + alpha) on Kindle (or Y (8bpp) with ignore_alpha).
    """
    return FBInk.fbink_print_raw_data(fbfd, bytes(data), w, h, len, x_off, y_off, fbink_cfg)


def fbink_cls(fbfd: int, fbink_cfg: FBInkConfig, rect: FBInkRect, no_rota: bool) -> int:
    """
    Just clear the screen (or a region of it), eInk refresh included (or not ;)).
    Returns -(ENOSYS) when drawing primitives are disabled (MINIMAL build w/o DRAW).
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (honors is_inverted, wfm_mode, dithering_mode, is_nightmode, is_flashing,
                        as well as no_refresh & bg_color).
    @param rect:		Optional pointer to an FBInkRect rectangle (as, say, returned by fbink_get_last_rect),
                        describing the specific region of screen to clear (in absolute coordinates).
                        If the rectangle is empty (i.e., width or height is zero) or the pointer is NULL,
                        the full screen will be cleared.
    @param no_rota:	    Optional, and only useful in very limited cases. When in doubt, set to false.
                        When passing a rect, this requests *not* applying any further rotation hacks,
                        (e.g., isNTX16bLandscape).
                        This is mildly useful if you got a *rotated* rect out of fbink_get_last_rect
                        on such a quirky framebuffer state,
                        and just want to re-use it as-is without mangling the rotation again.
    """
    return FBInk.fbink_cls(fbfd, fbink_cfg.to_c(), rect, no_rota)


def fbink_grid_clear(fbfd: int, cols: int, rows: int, fbink_cfg: FBInkConfig) -> int:
    """
    Like fbink_cls, but instead of absolute coordinates, rely on grid coordinates like fbink_print.
    Honors all the same positioning trickery than fbink_print (i.e., row/col mixed w/ hoffset/voffset).
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (honors col, row, is_halfway, is_centered, is_padded, is_rpadded,
                        voffset, hoffset, is_overlay, is_bgless,
                        wfm_mode, dithering_mode, is_nightmode, is_flashing, no_refresh).
    @param cols:	    Amount of columns to clear (i.e., width).
    @param rows:		Amount of rows to clear (i.e., height).
    """
    return FBInk.fbink_grid_clear(fbfd, cols, rows, fbink_cfg)


def fbink_grid_refresh(fbfd: int, cols: int, rows: int, fbink_cfg: FBInkConfig) -> int:
    """
    Like fbink_refresh, but instead of absolute coordinates, rely on grid coordinates like fbink_print.
    Honors all the same positioning trickery than fbink_print (i.e., row/col mixed w/ hoffset/voffset).
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (honors col, row, is_halfway, is_centered, is_padded, is_rpadded,
                        voffset, hoffset, is_overlay, is_bgless,
                        wfm_mode, dithering_mode, is_nightmode, is_flashing).
    @param cols:		Amount of columns to refresh (i.e., width).
    @param rows:		Amount of rows to refresh (i.e., height).
    NOTE: This *ignores* no_refresh ;).
    """
    return FBInk.fbink_grid_refresh(fbfd, cols, rows, fbink_cfg)


def fbink_dump(fbfd: int, dump: FBInkDump) -> int:
    """
    Dump the full screen.
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    @param fbfd:	Open file descriptor to the framebuffer character device,
                    if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param dump:	Pointer to an FBInkDump struct (will be recycled if already used).
    NOTE:   As with all FBInk structs, FBInkDump *must* be zero-initialized.
            Storage for the dump will be allocated on the heap by FBInk,
            but releasing that memory (i.e., free(dump.data);) is the caller's burden.
            Care should be taken not to leave that pointer dangling (i.e., dump.data = NULL;),
            as a subsequent call to fbink_*_dump with that same struct would otherwise trip the recycling check,
            causing a double free!
            You can use the fbink_free_dump_data() helper function to do just that.
            There are no error codepaths after storage allocation (i.e., you are assured that it has NOT been allocated on error).
            Note that a recycling *will* clear the clip FBInkRect!
    NOTE:   On *most* devices (the exceptions being 4bpp & 16bpp fbs),
            the data being dumped is perfectly valid input for fbink_print_raw_data,
            in case you'd ever want to do some more exotic things with it...
    NOTE:   On Kobo devices with a sunxi SoC, you will not be able to capture content that you haven't drawn yourself first.
            (There's no "shared" framebuffer, each process gets its own private, zero-initialized (i.e., solid black) buffer).
    """
    return FBInk.fbink_dump(fbfd, dump)


def fbink_region_dump(fbfd: int, x_off: int, y_off: int, w: int, h: int, fbink_cfg: FBInkConfig,
                      dump: FBInkDump) -> int:
    """
    Dump a specific region of the screen.
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    Returns -(EINVAL) when trying to dump an empty region.
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param x_off:		Dump coordinates, x (honors negative offsets).
    @param y_off:		Dump coordinates, y (honors negative offsets).
    @param w:			Width of the region to dump.
    @param h:			Height of the region to dump.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (honors any combination of halign/valign, row/col & x_off/y_off).
    @param dump:		Pointer to an FBInkDump struct (will be recycled if already used).
    NOTE: The same considerations as in fbink_dump should be taken regarding the handling of FBInkDump structs.
    """
    return FBInk.fbink_region_dump(fbfd, x_off, y_off, w, h, fbink_cfg, dump)


def fbink_rect_dump(fbfd: int, rect: FBInkRect, dump: FBInkDump) -> int:
    """
    Like fbink_region_dump, but takes an FBInkRect as input, and uses it *as is* (i.e., no rotation/positioning tricks).
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    Returns -(EINVAL) when trying to dump an OOB region.
    The intended use case is being able to use a rect returned by fbink_get_last_rect
    without having to think about the potential fallout from positioning or rotation hacks.
    (c.f., also the "no_rota" flag for fbink_cls).
    NOTE: If NULL or an empty rect is passed, a full dump will be made instead.
    NOTE: The same considerations as in fbink_dump should be taken regarding the handling of FBInkDump structs.
    """
    return FBInk.fbink_rect_dump(fbfd, rect, dump)


def fbink_restore(fbfd: int, fbink_cfg: FBInkConfig, dump: FBInkDump) -> int:
    """
    Restore a framebuffer dump made by fbink_dump/fbink_region_dump/fbink_rect_dump.
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    Otherwise, returns a few different things on failure:
        -(ENOTSUP)	when the dump cannot be restored because it wasn't taken at the current bitdepth and/or rotation,
                    or because it's wider/taller/larger than the current framebuffer, or if the crop is invalid (OOB).
        -(EINVAL)	when there's no data to restore.
    @param fbfd:	    Open file descriptor to the framebuffer character device,
                        set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct (honors wfm_mode, dithering_mode, is_nightmode,
                        is_flashing & no_refresh).
    @param dump:		Pointer to an FBInkDump struct, as setup by fbink_dump or fbink_region_dump.
    NOTE:   In case the dump was regional, it will be restored in the exact same coordinates it was taken from,
            no actual positioning is needed/supported at restore time.
    NOTE:   This does not support any kind of software processing, at all!
            If you somehow need inversion or dithering, it has to be supported at the hardware level at refresh time by your device,
            (i.e., dithering_mode vs. sw_dithering, and is_nightmode vs. is_inverted).
            At most common bitdepths, you can somewhat work around these restrictions, obviously at a performance premium,
            by using fbink_print_raw_data instead (see the relevant notes for fbink_dump), with a few quirky caveats...
            c.f., the last few tests in utils/dump.c for highly convoluted examples that I don't recommend replicating in production.
    NOTE:   "current" actually means "at last init/reinit time".
            Call fbink_reinit first if you really want to make sure bitdepth/rotation still match.
    NOTE:   If you need to restore only part of a dump, you can do so via the clip field of the FBInkDump struct.
            This FBInkRect is the only field you should ever modify yourself.
            This clip rectangle is relative to the *screen*, not the dump's area (i.e., these are absolute screen coordinates).
            As such, it has to intersect with the dump's area, or the call will fail.
            And while it can safely completely overlap the dump's area, it still needs to be constrained to the screen's dimension.
            Of course, only the intersection of this rectangle with the dump's area will be restored.
            Be aware that you'll also need to flip the is_full field yourself first if you ever need to crop a full dump.
    NOTE:   This does *NOT* free data.dump!
    """
    return FBInk.fbink_restore(fbfd, fbink_cfg, dump)


def fbink_free_dump_data(dump: FBInkDump) -> int:
    """
    Free the data allocated by a previous fbink_dump() or fbink_region_dump() call.
    Returns -(ENOSYS) when image support is disabled (MINIMAL build w/o IMAGE).
    Otherwise, returns a few different things on failure:
        -(EINVAL)	when the dump has already been freed.
    @param dump:		    Pointer to an FBInkDump struct.
    NOTE: You MUST call this when you have no further use for this specific data.
    NOTE: But, you MAY re-use a single FBInkDump struct across different dump() calls *without* calling this in between,
          as dump() will implicitly free a dirty struct in order to recycle it.
    """
    return FBInk.fbink_free_dump_data(dump)


def fbink_get_last_rect(rotated: bool) -> FBInkRect:
    """
    Return the coordinates & dimensions of the last thing that was *drawn*.
    Returns an empty (i.e., {0, 0, 0, 0}) rectangle if nothing was drawn.
    @param rotated:		Returns rotated coordinates if applicable.
    NOTE: These are unfiltered *framebuffer* coordinates.
          If your goal is to use that for input detection, mapping that to input coordinates is your responsibility.
          On Kobo, fbink_get_state should contain enough data to help you figure out what kinds of quirks you need to account for.
    NOTE: While this *generally* maps to the refresh region, this does not always hold true:
          this will get updated regardless of no_refresh,
          and will ignore what is_flashing might do to make the refresh region fullscreen.
          i.e., it corresponds to what's drawn to the fb, not necessarily to what's refreshed on screen.
    NOTE: On devices where we may fudge the coordinates to account for broken rotation (i.e., most Kobos @ 16bpp),
          these are, by default, the *unrotated* coordinates!
          i.e., they will *NOT* match with what we actually send to mxcfb (and where we actually drew on the fb)!
          Nothing in our public API actually expects any other kind of coordinates,
          so having this return the rotated coordinates would be confusing...
          If, for some reason (e.g., comparing against actual ioctl values),
          you *do* need the rotated variant, set rotated to true.
    """
    return FBInk.fbink_get_last_rect(rotated)


def fbink_button_scan(fbfd: int, press_button: bool, nosleep: bool) -> int:
    """
    Scan the screen for Kobo's "Connect" button in the "USB plugged in" popup,
    and optionally generate an input event to press that button.
    KOBO i.MX Only! Returns -(ENOSYS) when disabled (!KOBO, or Kobo on a sunxi SoC, as well as MINIMAL builds w/o BUTTON_SCAN).
    Otherwise, returns a few different things on failure:
        -(EXIT_FAILURE)	when the button was not found.
        With press_button:
        -(ENODEV)	when we couldn't generate a touch event at all (unlikely to ever happen on current HW).
        -(ENOTSUP)	when the generated touch event appeared to have failed to actually tap the button.
                Emphasis on "appeared to", it's tricky to be perfectly sure the right thing happened...
                CANNOT happen when nosleep is true (because it skips this very codepath).
    NOTE: For the duration of this call, screen updates should be kept to a minimum: in particular,
          we of course expect to be able to see the "Connect" button,
          but we also expect the middle section of the final line to be untouched!
    @param fbfd:	Open file descriptor to the framebuffer character device,
                    if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param press_button:	Generate an input event to press the button if true,
                            MAY sleep up to 5s to confirm that input was successful! (unless nosleep is true).
    @param nosleep:		If true, don't try to confirm that press_button's input event was successful,
                        avoiding the nanosleep() calls that would incur...
    NOTE: Thread-safety obviously goes out the window with press_button enabled,
          since you can then only reasonably expect to be able to concurrently run a single instance of that function ;).
    """
    return FBInk.fbink_button_scan(fbfd, press_button, nosleep)


def fbink_wait_for_usbms_processing(fbfd: int, force_unpulug: bool) -> int:
    """
    Wait for the end of a Kobo USBMS session, trying to detect a successful content import in the process.
    NOTE:   Expects to be called while in the "Connected" state (like after a successful fbink_button_scan() call w/ press_buton)!
            It will abort early if that's not the case.
    NOTE:   For the duration of this call (which is obviously blocking!), screen updates should be kept to a minimum:
            in particular, we expect the middle section of the final line to be untouched!
    KOBO i.MX Only! Returns -(ENOSYS) when disabled (!KOBO, or Kobo on a sunxi SoC, as well as MINIMAL builds w/o BUTTON_SCAN).
    Otherwise, returns a few different things on failure:
        -(EXIT_FAILURE)	when the expected chain of events fails to be detected properly.
        -(ENODATA)	when there was no new content to import at the end of the USBMS session.
        -(ETIME)	when we failed to detect the end of the import session itself, because it ran longer than 5 minutes.
    @param fbfd:		Open file descriptor to the framebuffer character device,
                if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param force_unplug:	After having made sure to be in USBMS mode, generate a fake USB unplug event to force Nickel to wake up.
                This makes sense if you want to do stuff behind Nickel's back during the USBMS session,
                instead of simply monitoring it, especially with fake USBMS sessions ;).
                NOTE: Obviously, if this was a real USBMS session, and not an entirely faked one,
                        if you force an unplug while onboard is still mounted on the connected to machine,
                        shit will go horribly wrong!
    NOTE:   Thread-safety obviously goes out the window with force_unplug enabled,
            since you can then only reasonably expect to be able to concurrently run a single instance of that function ;).
    """
    return FBInk.fbink_wait_for_usbms_processing(fbfd, force_unpulug)


def fbink_invert_screen(fbfd: int, fbink_cfg: FBInkConfig) -> int:
    """
    Inverts the *existing* content of the *full* screen.
    This is mildly useful on devices with no HW inversion support,
    to trigger a full "nightmode" swap, without actually having to redraw anything.
    @param fbfd:		Open file descriptor to the framebuffer character device,
                        if set to FBFD_AUTO, the fb is opened & mmap'ed for the duration of this call.
    @param fbink_cfg:	Pointer to an FBInkConfig struct.
    NOTE: On Kobo devices with a sunxi SoC, you will not be able to affect content that you haven't drawn yourself first.
    """
    return FBInk.fbink_invert_screen(fbfd, fbink_cfg)


def fbink_get_fb_pointer(fbfd: int, buffer_size) -> bytes:
    """
    The functions below are much lower level than the rest of the API:
    outside of GUI toolkit implementations and very specific workflows, you shouldn't need to rely on them.

    Grants direct access to the backing buffer's base pointer, as well as its size (in bytes; e.g., smem_len).
    MUST NOT be called before fbink_init
    MUST NOT be called with an FBFD_AUTO fbfd
    MAY be called before before any fbink_print*, fbink_dump/restore, fbink_cls or fbink_grid* functions.
    (i.e., it'll implicitly setup the backing buffer if necessary).
    Returns NULL on failure (in which case, *buffer_size is set to 0).
    NOTE: This *may* need to be refreshed after a framebuffer state change, c.f., fbink_reinit!
        (In practice, though, the pointer itself is stable;
        only the buffer/mapping size may change on some quirky platforms (usually, PB)).
    @param fbfd:	    Open file descriptor to the framebuffer character device,
                        cannot be set to FBFD_AUTO!
    @param buffer_size:	Out parameter. On success, will be set to the buffer's size, in bytes.
    """


def fbink_get_fb_info(var_info, fix_info):
    """
    For when you *really* need a mostly untouched copy of the full linuxfb structs...
    NOTE: Prefer fbink_get_state, unless you *really* have no other choices...
    """


# Magic constants for fbink_set_fb_info (> INT8_MAX to steer clear of legitimate values)
KEEP_CURRENT_ROTATE = 128
KEEP_CURRENT_BITDEPTH = 128
KEEP_CURRENT_GRAYSCALE = 128
TOGGLE_GRAYSCALE = 64


def fbink_set_fb_info(fbdf: int, rota: int, bpp: int, grayscale: int, fbink_cfg) -> int:
    """
    Sets the framebuffer's bitdepth and/or native rotation.
    MUST NOT be called before fbink_init
    Only tested on Kobo & Kindle, here be dragons on other platforms!
    Returns a few different things on failure:
        -(ENODEV)	if called before fbink_init
        -(EINVAL)	when one of rota/bpp/grayscale is invalid
        -(ECANCELED)	if an ioctl failed, meaning the fb state may be left in an undefined state.
            This is *highly* unlikely, but, if it happens,
            checking the sanity of the fb state is the caller's responsibilty!
            (i.e., you'll have to *at least* run fbink_reinit yourself).
    NOTE: On sunxi, only the rotation can be controlled: i.e., this will simply invoke fbink_sunxi_ntx_enforce_rota,
       except we only accept values matching linuxfb rotation constants.
       Prefer using fbink_sunxi_ntx_enforce_rota directly yourself.
    NOTE: On success, this will reinit the state *now* (returning the exact same values as fbink_reinit).
       In particular, if you're using fbink_get_state and/or fbink_get_fb_pointer,
       check and handle that return value properly (as you would an actual fbink_reinit call),
       or you may be left with stale state data if you don't refresh it when necessary :).
    @param fbfd:	    Open file descriptor to the framebuffer character device.
                        if set to FBFD_AUTO, the fb is opened for the duration of this call.
    @param rota:	    *native* linuxfb rotation value (c.f., fbink_rota_canonical_to_native).
                        Untouched if set to KEEP_CURRENT_ROTATE
    @param bpp:		    bitdepth value (in bits).
                        Supported values: 4, 8, 16, 32
                        Untouched if set to KEEP_CURRENT_BITDEPTH
    @param grayscale:	grayscale value.
                            (enforced to 0 if bpp != 8).
                            If bpp == 8, only meaningful on mxcfb:
                            Generally set to GRAYSCALE_8BIT (1),
                            setting it to GRAYSCALE_8BIT_INVERTED (2)
                            will automagically enforce HW inversion via EPDC_FLAG_ENABLE_INVERSION
                            Untouched if set to KEEP_CURRENT_GRAYSCALE
                            If set to TOGGLE_GRAYSCALE, will toggle between INVERTED & not @ 8bpp
    @param fbink_cfg:		Pointer to an FBInkConfig struct.
    """


def fbink_toggle_sunxi_ntx_pen_mode(fbfd: int, toggle: bool) -> int:
    pass


def fbink_sunxi_ntx_enforce_rota(fbfd: int, mode, fbink_cfg) -> int:
    pass
