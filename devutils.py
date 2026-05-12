#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevUtils-CLI 🛠️
A lightweight, zero-dependency Python CLI toolbox for developers.

Author: DevUtils Team
License: MIT
Version: 1.0.0
"""

import argparse
import base64
import hashlib
import json
import os
import random
import re
import string
import sys
import time
import urllib.parse
import uuid
from datetime import datetime, timezone
from typing import Optional

__version__ = "1.0.0"
__author__ = "DevUtils Team"

# ============================================================================
# Utility Functions
# ============================================================================

def print_header(title: str):
    """Print formatted header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def print_success(message: str):
    """Print success message"""
    print(f"✅ {message}")

def print_error(message: str):
    """Print error message"""
    print(f"❌ {message}", file=sys.stderr)

def print_info(message: str):
    """Print info message"""
    print(f"ℹ️  {message}")

# ============================================================================
# Tool: JSON Formatter
# ============================================================================

def json_tool(args):
    """JSON formatting and validation tool"""
    print_header("🔧 JSON Formatter & Validator")
    
    if args.input:
        try:
            data = json.loads(args.input)
            if args.minify:
                result = json.dumps(data, separators=(',', ':'))
            else:
                result = json.dumps(data, indent=args.indent, ensure_ascii=False)
            print(result)
            print_success("JSON formatted successfully!")
        except json.JSONDecodeError as e:
            print_error(f"Invalid JSON: {e}")
    else:
        # Interactive mode
        print_info("Enter JSON (press Ctrl+D or type 'END' on new line to finish):")
        lines = []
        try:
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                lines.append(line)
        except EOFError:
            pass
        
        if lines:
            try:
                data = json.loads('\n'.join(lines))
                print("\n" + "="*60)
                print(json.dumps(data, indent=2, ensure_ascii=False))
                print("="*60)
                print_success("JSON is valid!")
            except json.JSONDecodeError as e:
                print_error(f"Invalid JSON: {e}")

# ============================================================================
# Tool: Base64 Encoder/Decoder
# ============================================================================

def base64_tool(args):
    """Base64 encoding and decoding tool"""
    print_header("🔐 Base64 Encoder/Decoder")
    
    if args.decode:
        try:
            decoded = base64.b64decode(args.input).decode('utf-8')
            print(f"Decoded:\n{decoded}")
        except Exception as e:
            print_error(f"Decoding failed: {e}")
    else:
        encoded = base64.b64encode(args.input.encode()).decode('utf-8')
        print(f"Encoded:\n{encoded}")

# ============================================================================
# Tool: Password Generator
# ============================================================================

def password_tool(args):
    """Secure password generator"""
    print_header("🔑 Password Generator")
    
    length = args.length or 16
    chars = string.ascii_letters + string.digits
    
    if args.symbols:
        chars += string.punctuation
    
    if args.no_upper:
        chars = chars.lower() + string.digits
    
    if args.no_digits:
        chars = ''.join(c for c in chars if not c.isdigit())
    
    password = ''.join(random.SystemRandom().choice(chars) for _ in range(length))
    
    print(f"Generated Password: {password}")
    print_info(f"Length: {len(password)} characters")
    
    # Strength indicator
    strength = "Weak" if length < 8 else "Medium" if length < 12 else "Strong"
    print_info(f"Strength: {strength}")

# ============================================================================
# Tool: UUID Generator
# ============================================================================

def uuid_tool(args):
    """UUID generator"""
    print_header("🆔 UUID Generator")
    
    count = args.count or 1
    version = args.version or 4
    
    for i in range(count):
        if version == 1:
            uid = uuid.uuid1()
        elif version == 3:
            uid = uuid.uuid3(uuid.NAMESPACE_DNS, args.name or 'example.com')
        elif version == 4:
            uid = uuid.uuid4()
        elif version == 5:
            uid = uuid.uuid5(uuid.NAMESPACE_DNS, args.name or 'example.com')
        else:
            uid = uuid.uuid4()
        
        output = str(uid)
        if args.uppercase:
            output = output.upper()
        print(f"{i+1}. {output}")

# ============================================================================
# Tool: Hash Generator
# ============================================================================

def hash_tool(args):
    """Hash generator (MD5, SHA1, SHA256, SHA512)"""
    print_header("#️⃣  Hash Generator")
    
    if not args.input:
        print_error("No input provided")
        return
    
    data = args.input.encode('utf-8')
    
    algorithms = ['md5', 'sha1', 'sha256', 'sha512'] if args.all else [args.algorithm or 'sha256']
    
    for algo in algorithms:
        hasher = hashlib.new(algo)
        hasher.update(data)
        print(f"{algo.upper()}: {hasher.hexdigest()}")

# ============================================================================
# Tool: Timestamp Converter
# ============================================================================

def timestamp_tool(args):
    """Timestamp and date converter"""
    print_header("⏰ Timestamp Converter")
    
    if args.to_date:
        # Unix timestamp to date
        try:
            ts = float(args.input)
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            print(f"UTC: {dt.strftime('%Y-%m-%d %H:%M:%S')} UTC")
            dt_local = datetime.fromtimestamp(ts)
            print(f"Local: {dt_local.strftime('%Y-%m-%d %H:%M:%S')}")
        except ValueError as e:
            print_error(f"Invalid timestamp: {e}")
    elif args.to_timestamp:
        # Date to unix timestamp
        try:
            dt = datetime.strptime(args.input, '%Y-%m-%d %H:%M:%S')
            ts = dt.timestamp()
            print(f"Unix Timestamp: {int(ts)}")
            print(f"Milliseconds: {int(ts * 1000)}")
        except ValueError:
            print_error("Invalid date format. Use: YYYY-MM-DD HH:MM:SS")
    else:
        # Show current time
        now = datetime.now()
        utc_now = datetime.now(timezone.utc)
        print(f"Current Local Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Current UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')} UTC")
        print(f"Unix Timestamp: {int(now.timestamp())}")
        print(f"ISO 8601: {now.isoformat()}")

# ============================================================================
# Tool: URL Encoder/Decoder
# ============================================================================

def url_tool(args):
    """URL encoding and decoding tool"""
    print_header("🔗 URL Encoder/Decoder")
    
    if args.decode:
        try:
            decoded = urllib.parse.unquote(args.input)
            print(f"Decoded:\n{decoded}")
        except Exception as e:
            print_error(f"Decoding failed: {e}")
    else:
        encoded = urllib.parse.quote(args.input, safe='')
        print(f"Encoded:\n{encoded}")

# ============================================================================
# Tool: Text Case Converter
# ============================================================================

def case_tool(args):
    """Text case converter"""
    print_header("📝 Text Case Converter")
    
    text = args.input
    
    if args.camel:
        # Convert to camelCase
        words = re.split(r'[\s_-]+', text)
        result = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        print(f"camelCase: {result}")
    
    if args.pascal:
        # Convert to PascalCase
        words = re.split(r'[\s_-]+', text)
        result = ''.join(word.capitalize() for word in words)
        print(f"PascalCase: {result}")
    
    if args.snake:
        # Convert to snake_case
        result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower().replace(' ', '_').replace('-', '_')
        print(f"snake_case: {result}")
    
    if args.kebab:
        # Convert to kebab-case
        result = re.sub(r'(?<!^)(?=[A-Z])', '-', text).lower().replace(' ', '-').replace('_', '-')
        print(f"kebab-case: {result}")
    
    if not any([args.camel, args.pascal, args.snake, args.kebab]):
        # Show all conversions
        words = re.split(r'[\s_-]+', text)
        print(f"Original: {text}")
        print(f"UPPERCASE: {text.upper()}")
        print(f"lowercase: {text.lower()}")
        print(f"Title Case: {text.title()}")
        print(f"camelCase: {words[0].lower() + ''.join(word.capitalize() for word in words[1:])}")
        print(f"PascalCase: {''.join(word.capitalize() for word in words)}")
        print(f"snake_case: {re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower().replace(' ', '_').replace('-', '_')}")
        print(f"kebab-case: {re.sub(r'(?<!^)(?=[A-Z])', '-', text).lower().replace(' ', '-').replace('_', '-')}")

# ============================================================================
# Tool: Lorem Ipsum Generator
# ============================================================================

def lorem_tool(args):
    """Lorem ipsum text generator"""
    print_header("📄 Lorem Ipsum Generator")
    
    words = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
        "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
        "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
        "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
        "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id", "est", "laborum"
    ]
    
    paragraphs = args.paragraphs or 1
    
    for p in range(paragraphs):
        # Generate random paragraph
        para_length = random.randint(50, 100)
        para_words = [random.choice(words) for _ in range(para_length)]
        para_words[0] = para_words[0].capitalize()
        paragraph = ' '.join(para_words) + '.'
        print(f"\nParagraph {p+1}:\n{paragraph}")

# ============================================================================
# Tool: QR Code Generator (ASCII)
# ============================================================================

def qr_tool(args):
    """Simple ASCII QR code representation"""
    print_header("📱 QR Code Generator (ASCII)")
    
    text = args.input
    print_info("Generating ASCII representation...")
    print()
    
    # Create a simple ASCII art representation
    hash_val = hashlib.md5(text.encode()).hexdigest()
    size = 10
    
    print("╔" + "═" * (size * 2 + 2) + "╗")
    for i in range(size):
        row = "║ "
        for j in range(size):
            idx = (i * size + j) % len(hash_val)
            if int(hash_val[idx], 16) > 8:
                row += "██"
            else:
                row += "  "
        row += " ║"
        print(row)
    print("╚" + "═" * (size * 2 + 2) + "╝")
    print()
    print_info("Note: This is a visual representation. Use 'qrcode' library for real QR codes.")

# ============================================================================
# Main CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        prog='devutils',
        description='🛠️ DevUtils-CLI - A lightweight toolbox for developers',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  devutils json --input '{"name":"test"}'
  devutils password --length 20 --symbols
  devutils uuid --count 5
  devutils hash --input "hello world" --algorithm sha256
  devutils timestamp
  devutils base64 --input "Hello World"
  devutils url --input "hello world"
  devutils case --input "hello world" --camel
  devutils lorem --paragraphs 3
  devutils qr --input "https://example.com"
        """
    )
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    subparsers = parser.add_subparsers(dest='command', help='Available tools')
    
    # JSON tool
    json_parser = subparsers.add_parser('json', help='JSON formatter and validator')
    json_parser.add_argument('--input', '-i', help='JSON string to format')
    json_parser.add_argument('--indent', type=int, default=2, help='Indentation spaces (default: 2)')
    json_parser.add_argument('--minify', action='store_true', help='Minify JSON output')
    
    # Base64 tool
    base64_parser = subparsers.add_parser('base64', help='Base64 encoder/decoder')
    base64_parser.add_argument('--input', '-i', required=True, help='Text to encode/decode')
    base64_parser.add_argument('--decode', '-d', action='store_true', help='Decode mode')
    
    # Password tool
    password_parser = subparsers.add_parser('password', help='Secure password generator')
    password_parser.add_argument('--length', '-l', type=int, help='Password length (default: 16)')
    password_parser.add_argument('--symbols', '-s', action='store_true', help='Include symbols')
    password_parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    password_parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    
    # UUID tool
    uuid_parser = subparsers.add_parser('uuid', help='UUID generator')
    uuid_parser.add_argument('--count', '-c', type=int, help='Number of UUIDs to generate (default: 1)')
    uuid_parser.add_argument('--version', '-v', type=int, choices=[1, 3, 4, 5], help='UUID version (default: 4)')
    uuid_parser.add_argument('--name', '-n', help='Name for UUID v3/v5')
    uuid_parser.add_argument('--uppercase', '-u', action='store_true', help='Output uppercase')
    
    # Hash tool
    hash_parser = subparsers.add_parser('hash', help='Hash generator (MD5, SHA1, SHA256, SHA512)')
    hash_parser.add_argument('--input', '-i', required=True, help='Text to hash')
    hash_parser.add_argument('--algorithm', '-a', choices=['md5', 'sha1', 'sha256', 'sha512'], help='Hash algorithm')
    hash_parser.add_argument('--all', action='store_true', help='Generate all hash types')
    
    # Timestamp tool
    timestamp_parser = subparsers.add_parser('timestamp', help='Timestamp converter')
    timestamp_parser.add_argument('--input', '-i', help='Input value')
    timestamp_parser.add_argument('--to-date', action='store_true', help='Convert timestamp to date')
    timestamp_parser.add_argument('--to-timestamp', action='store_true', help='Convert date to timestamp')
    
    # URL tool
    url_parser = subparsers.add_parser('url', help='URL encoder/decoder')
    url_parser.add_argument('--input', '-i', required=True, help='Text to encode/decode')
    url_parser.add_argument('--decode', '-d', action='store_true', help='Decode mode')
    
    # Case tool
    case_parser = subparsers.add_parser('case', help='Text case converter')
    case_parser.add_argument('--input', '-i', required=True, help='Text to convert')
    case_parser.add_argument('--camel', action='store_true', help='Convert to camelCase')
    case_parser.add_argument('--pascal', action='store_true', help='Convert to PascalCase')
    case_parser.add_argument('--snake', action='store_true', help='Convert to snake_case')
    case_parser.add_argument('--kebab', action='store_true', help='Convert to kebab-case')
    
    # Lorem tool
    lorem_parser = subparsers.add_parser('lorem', help='Lorem ipsum generator')
    lorem_parser.add_argument('--paragraphs', '-p', type=int, help='Number of paragraphs (default: 1)')
    
    # QR tool
    qr_parser = subparsers.add_parser('qr', help='QR code generator (ASCII)')
    qr_parser.add_argument('--input', '-i', required=True, help='Text to encode')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
    
    # Route to appropriate tool
    commands = {
        'json': json_tool,
        'base64': base64_tool,
        'password': password_tool,
        'uuid': uuid_tool,
        'hash': hash_tool,
        'timestamp': timestamp_tool,
        'url': url_tool,
        'case': case_tool,
        'lorem': lorem_tool,
        'qr': qr_tool,
    }
    
    if args.command in commands:
        try:
            commands[args.command](args)
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            sys.exit(0)
        except Exception as e:
            print_error(f"Error: {e}")
            sys.exit(1)
    else:
        print_error(f"Unknown command: {args.command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
