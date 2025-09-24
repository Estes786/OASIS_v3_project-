#!/usr/bin/env python3
"""
OASIS 2.0 Basic Usage Examples
Ultra-lightweight AI demonstrations for mobile environments
Copy and run these examples to get started!
"""

import os
import sys
from datetime import datetime

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.oasis_controller import OASISController
from core.hf_integration import HuggingFaceAPI
from business.revenue_engine import RevenueEngine


def example_1_basic_content_generation():
    """Example 1: Basic AI content generation"""
    
    print("🎯 Example 1: Basic Content Generation")
    print("====================================")
    
    try:
        # Initialize OASIS controller
        oasis = OASISController()
        
        # Generate content
        result = oasis.generate_content(
            prompt="Write a brief introduction about mobile AI revolution",
            max_tokens=100
        )
        
        if result['success']:
            print(f"✅ Generated content:")
            print(f"📝 {result['content']}")
            print(f"⏱️  Processing time: {result['processing_time']:.2f}s")
            print(f"🔢 API calls made: {result['api_calls']}")
        else:
            print(f"❌ Error: {result['error']}")
    
    except Exception as e:
        print(f"❌ Example failed: {e}")
        print("💡 Make sure to configure HF_TOKEN in .env file")


def example_2_revenue_generation():
    """Example 2: Revenue generation demonstration"""
    
    print("\\n💰 Example 2: Revenue Generation")
    print("===============================")
    
    try:
        # Initialize revenue engine
        revenue_engine = RevenueEngine()
        
        # Generate content for client (simulated)
        content_result = revenue_engine.generate_content_service(
            content_type='blog_post',
            parameters={
                'topic': 'Benefits of AI automation for small businesses',
                'audience': 'business owners',
                'tone': 'professional',
                'length': '600'
            },
            pricing_tier='premium'
        )
        
        if content_result['success']:
            print(f"✅ Content service completed:")
            print(f"💵 Revenue generated: ${content_result['pricing']['amount']}")
            print(f"📄 Content preview: {content_result['content'][:150]}...")
            print(f"📊 Word count: {content_result['metadata']['word_count']}")
        else:
            print(f"❌ Revenue generation failed: {content_result['error']}")
    
    except Exception as e:
        print(f"❌ Revenue example failed: {e}")


def example_3_api_automation():
    """Example 3: API service automation"""
    
    print("\\n🔌 Example 3: API Service Automation")
    print("===================================")
    
    try:
        revenue_engine = RevenueEngine()
        
        # Automate API services for client
        api_result = revenue_engine.automate_api_service(
            api_calls=25,
            service_type='standard',
            bulk_discount=False
        )
        
        if api_result['success']:
            print(f"✅ API automation completed:")
            print(f"🔢 API calls processed: {api_result['api_calls_processed']}")
            print(f"💵 Total revenue: ${api_result['pricing']['total_cost']:.2f}")
            print(f"⚡ Processing speed: {api_result['performance']['throughput']:.2f} calls/second")
            print(f"💡 Profit margin: {api_result['business_metrics']['profit_margin']*100}%")
        
    except Exception as e:
        print(f"❌ API automation example failed: {e}")


def example_4_hmaqca_orchestration():
    """Example 4: HMAQCA multi-agent orchestration"""
    
    print("\\n🎯 Example 4: HMAQCA Orchestration")
    print("=================================")
    
    try:
        oasis = OASISController()
        
        # Run HMAQCA orchestration
        orchestration = oasis.hmaqca_orchestration(
            task="Create a mobile app marketing strategy",
            context={
                "target_market": "young professionals",
                "budget": "low-cost",
                "timeline": "2 weeks"
            }
        )
        
        if orchestration['success']:
            print(f"✅ HMAQCA orchestration completed:")
            print(f"🧠 Models used: {len(orchestration['models_used'])}")
            print(f"⏱️  Total processing: {orchestration['processing_time']:.2f}s")
            print(f"📋 Final synthesis: {orchestration['final_synthesis']['content'][:200]}...")
        
    except Exception as e:
        print(f"❌ HMAQCA example failed: {e}")


def example_5_custom_solution_proposal():
    """Example 5: Custom solution proposal generation"""
    
    print("\\n🏢 Example 5: Custom Solution Proposal")
    print("====================================")
    
    try:
        revenue_engine = RevenueEngine()
        
        # Create custom solution proposal
        solution = revenue_engine.create_custom_solution(
            solution_type='implementation',
            requirements={
                'industry': 'e-commerce',
                'integration_count': 3,
                'mobile_app': True,
                'api_integration': True,
                'enterprise_scale': False
            },
            timeline='3-4 weeks'
        )
        
        if solution['success']:
            print(f"✅ Custom solution proposal created:")
            print(f"💵 Project value: ${solution['pricing']['final_price']:.2f}")
            print(f"📈 Complexity multiplier: {solution['pricing']['complexity_multiplier']:.1f}x")
            print(f"📋 Proposal preview: {solution['proposal'][:200]}...")
            print(f"🎯 Deliverables: {len(solution['deliverables'])} items")
        
    except Exception as e:
        print(f"❌ Custom solution example failed: {e}")


def example_6_huggingface_direct():
    """Example 6: Direct Hugging Face API usage"""
    
    print("\\n🤗 Example 6: Direct Hugging Face API")
    print("===================================")
    
    try:
        # Get HF token from environment
        from dotenv import load_dotenv
        load_dotenv()
        hf_token = os.getenv('HF_TOKEN')
        
        if not hf_token or hf_token == 'your_hugging_face_token_here':
            print("⚠️  Please configure HF_TOKEN in .env file first")
            return
        
        # Initialize HF API
        hf_api = HuggingFaceAPI(hf_token)
        
        # Text generation
        text_result = hf_api.generate_text(
            model='gpt2',
            prompt='The future of mobile AI is',
            max_tokens=50
        )
        
        if text_result['success']:
            print(f"✅ Text generation:")
            print(f"📝 Generated: {text_result['text']}")
        
        # Text classification
        classify_result = hf_api.classify_text(
            model='cardiffnlp/twitter-roberta-base-sentiment-latest',
            text='OASIS 2.0 is revolutionizing mobile AI development!'
        )
        
        if classify_result['success']:
            print(f"\\n✅ Sentiment analysis:")
            classifications = classify_result['classifications']
            if isinstance(classifications, list) and len(classifications) > 0:
                top_class = classifications[0]
                print(f"😊 Sentiment: {top_class.get('label', 'unknown')}")
        
        # Show API stats
        stats = hf_api.get_stats()
        print(f"\\n📊 API Statistics:")
        print(f"🔢 Requests made: {stats['requests_made']}")
        print(f"⏱️  Average time: {stats['average_processing_time']}")
        
    except Exception as e:
        print(f"❌ Hugging Face API example failed: {e}")


def example_7_mobile_optimization():
    """Example 7: Mobile performance optimization"""
    
    print("\\n📱 Example 7: Mobile Optimization")
    print("===============================")
    
    try:
        oasis = OASISController()
        
        # Test mobile optimization features
        optimization = oasis.mobile_optimize(
            operation='batch_processing',
            data=['task1', 'task2', 'task3'] * 5  # Simulate large batch
        )
        
        print(f"✅ Mobile optimization applied:")
        print(f"🔋 Battery impact: {optimization['optimizations_applied']['battery_impact']}")
        print(f"💾 Memory efficiency: {optimization['mobile_performance']['memory_efficient']}")
        print(f"📶 Network minimal: {optimization['mobile_performance']['network_minimal']}")
        print(f"💽 Storage usage: Zero local models")
        
    except Exception as e:
        print(f"❌ Mobile optimization example failed: {e}")


def example_8_session_analytics():
    """Example 8: Session analytics and monitoring"""
    
    print("\\n📊 Example 8: Session Analytics")
    print("==============================")
    
    try:
        # OASIS controller stats
        oasis = OASISController()
        stats = oasis.get_session_stats()
        
        print(f"✅ OASIS Session Stats:")
        for key, value in stats.items():
            if key not in ['startup_time']:  # Skip complex objects
                print(f"  {key}: {value}")
        
        # Revenue engine stats (if available)
        try:
            revenue_engine = RevenueEngine()
            revenue_stats = revenue_engine.get_revenue_stats()
            
            print(f"\\n💰 Revenue Analytics:")
            session_summary = revenue_stats['session_summary']
            print(f"  Total revenue: ${session_summary['total_revenue']:.2f}")
            print(f"  Transactions: {session_summary['transaction_count']}")
            print(f"  Session duration: {session_summary['session_duration_hours']:.2f}h")
            
        except Exception:
            print("\\n💰 Revenue stats: Not available (no transactions yet)")
        
    except Exception as e:
        print(f"❌ Analytics example failed: {e}")


def run_all_examples():
    """Run all examples in sequence"""
    
    print("🚀 OASIS 2.0 Ultra-Lightweight Examples")
    print("======================================")
    print("Mobile AI Revolution • Zero Dependencies • Instant Revenue")
    print()
    
    # Check environment first
    print("🔍 Environment Check:")
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        hf_token = os.getenv('HF_TOKEN')
        if not hf_token or hf_token == 'your_hugging_face_token_here':
            print("⚠️  HF_TOKEN not configured!")
            print("📝 Steps to configure:")
            print("  1. Get token: https://huggingface.co/settings/tokens")
            print("  2. Edit .env file: nano .env")
            print("  3. Replace 'your_hugging_face_token_here' with your token")
            print("\\n🎯 Running examples with limited functionality...")
        else:
            print("✅ HF_TOKEN configured")
        
        print(f"🐍 Python: {sys.version.split()[0]}")
        print(f"📁 Working dir: {os.getcwd()}")
        print()
        
    except Exception as e:
        print(f"⚠️  Environment check failed: {e}")
        print()
    
    # List of examples to run
    examples = [
        ("Basic Content Generation", example_1_basic_content_generation),
        ("Revenue Generation", example_2_revenue_generation),
        ("API Automation", example_3_api_automation),
        ("HMAQCA Orchestration", example_4_hmaqca_orchestration),
        ("Custom Solution Proposal", example_5_custom_solution_proposal),
        ("Direct Hugging Face API", example_6_huggingface_direct),
        ("Mobile Optimization", example_7_mobile_optimization),
        ("Session Analytics", example_8_session_analytics)
    ]
    
    # Run examples
    for i, (name, func) in enumerate(examples, 1):
        try:
            print(f"\\n{'='*60}")
            print(f"🎯 Running Example {i}: {name}")
            print(f"{'='*60}")
            
            func()
            
            print(f"\\n✅ Example {i} completed successfully!")
            
        except KeyboardInterrupt:
            print(f"\\n⚠️  Examples interrupted by user")
            break
        except Exception as e:
            print(f"\\n❌ Example {i} failed: {e}")
            print("Continuing with next example...")
        
        # Small delay between examples
        import time
        time.sleep(1)
    
    print(f"\\n{'='*60}")
    print("🎉 All OASIS 2.0 examples completed!")
    print("💡 Ready to start your AI revolution!")
    print(f"{'='*60}")


def main():
    """Main entry point for examples"""
    
    import argparse
    
    parser = argparse.ArgumentParser(description='OASIS 2.0 Usage Examples')
    parser.add_argument('--example', type=int, choices=range(1, 9),
                       help='Run specific example (1-8)')
    parser.add_argument('--all', action='store_true',
                       help='Run all examples')
    
    args = parser.parse_args()
    
    if args.example:
        # Run specific example
        examples = {
            1: ("Basic Content Generation", example_1_basic_content_generation),
            2: ("Revenue Generation", example_2_revenue_generation),
            3: ("API Automation", example_3_api_automation),
            4: ("HMAQCA Orchestration", example_4_hmaqca_orchestration),
            5: ("Custom Solution Proposal", example_5_custom_solution_proposal),
            6: ("Direct Hugging Face API", example_6_huggingface_direct),
            7: ("Mobile Optimization", example_7_mobile_optimization),
            8: ("Session Analytics", example_8_session_analytics)
        }
        
        name, func = examples[args.example]
        print(f"🎯 Running Example {args.example}: {name}")
        func()
        
    elif args.all:
        # Run all examples
        run_all_examples()
        
    else:
        # Interactive mode
        print("🚀 OASIS 2.0 Examples - Interactive Mode")
        print("=======================================")
        print()
        print("Available examples:")
        print("  1. Basic Content Generation")
        print("  2. Revenue Generation")
        print("  3. API Automation")
        print("  4. HMAQCA Orchestration")
        print("  5. Custom Solution Proposal")
        print("  6. Direct Hugging Face API")
        print("  7. Mobile Optimization")
        print("  8. Session Analytics")
        print("  9. Run ALL examples")
        print()
        
        try:
            choice = input("Select example (1-9): ").strip()
            
            if choice == '9':
                run_all_examples()
            elif choice.isdigit() and 1 <= int(choice) <= 8:
                examples = [
                    example_1_basic_content_generation,
                    example_2_revenue_generation,
                    example_3_api_automation,
                    example_4_hmaqca_orchestration,
                    example_5_custom_solution_proposal,
                    example_6_huggingface_direct,
                    example_7_mobile_optimization,
                    example_8_session_analytics
                ]
                examples[int(choice) - 1]()
            else:
                print("❌ Invalid choice")
                
        except KeyboardInterrupt:
            print("\\n👋 Goodbye!")


if __name__ == "__main__":
    main()