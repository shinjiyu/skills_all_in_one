/**
 * 文本处理脚本
 * 提供各种文本处理功能
 */

const fs = require('fs');
const path = require('path');

/**
 * 统计文本信息
 * @param {string} text - 要统计的文本
 * @returns {object} 统计结果
 */
function countTextStats(text) {
    const words = text.trim().split(/\s+/).filter(word => word.length > 0);
    const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
    const paragraphs = text.split(/\n\s*\n/).filter(p => p.trim().length > 0);
    
    return {
        characters: text.length,
        charactersNoSpaces: text.replace(/\s/g, '').length,
        words: words.length,
        sentences: sentences.length,
        paragraphs: paragraphs.length
    };
}

/**
 * 提取关键词（简单实现）
 * @param {string} text - 文本内容
 * @param {number} topN - 返回前 N 个关键词
 * @returns {array} 关键词列表
 */
function extractKeywords(text, topN = 10) {
    const words = text.toLowerCase()
        .replace(/[^\w\s]/g, '')
        .split(/\s+/)
        .filter(word => word.length > 3);
    
    const wordCount = {};
    words.forEach(word => {
        wordCount[word] = (wordCount[word] || 0) + 1;
    });
    
    return Object.entries(wordCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, topN)
        .map(([word, count]) => ({ word, count }));
}

/**
 * 格式化文本
 * @param {string} text - 原始文本
 * @param {string} format - 格式类型：'uppercase', 'lowercase', 'title', 'sentence'
 * @returns {string} 格式化后的文本
 */
function formatText(text, format) {
    switch (format) {
        case 'uppercase':
            return text.toUpperCase();
        case 'lowercase':
            return text.toLowerCase();
        case 'title':
            return text.split(' ').map(word => 
                word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
            ).join(' ');
        case 'sentence':
            return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
        default:
            return text;
    }
}

// 命令行接口
if (require.main === module) {
    const args = process.argv.slice(2);
    
    if (args.length < 2) {
        console.error('用法: node text_processor.js <command> <input> [options]');
        console.error('命令: count, keywords, format');
        process.exit(1);
    }
    
    const command = args[0];
    const input = args[1];
    
    // 从文件读取或直接使用输入
    let text;
    if (fs.existsSync(input)) {
        text = fs.readFileSync(input, 'utf-8');
    } else {
        text = input;
    }
    
    switch (command) {
        case 'count':
            const stats = countTextStats(text);
            console.log(JSON.stringify(stats, null, 2));
            break;
        
        case 'keywords':
            const topN = parseInt(args[2]) || 10;
            const keywords = extractKeywords(text, topN);
            console.log(JSON.stringify(keywords, null, 2));
            break;
        
        case 'format':
            const format = args[2] || 'sentence';
            const formatted = formatText(text, format);
            console.log(formatted);
            break;
        
        default:
            console.error(`未知命令: ${command}`);
            process.exit(1);
    }
}

module.exports = {
    countTextStats,
    extractKeywords,
    formatText
};


