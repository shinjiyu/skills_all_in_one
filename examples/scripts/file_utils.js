/**
 * 文件工具脚本
 * 提供文件操作相关功能
 */

const fs = require('fs');
const path = require('path');

/**
 * 读取文件内容
 * @param {string} filePath - 文件路径
 * @returns {string} 文件内容
 */
function readFile(filePath) {
    try {
        return fs.readFileSync(filePath, 'utf-8');
    } catch (error) {
        throw new Error(`读取文件失败: ${error.message}`);
    }
}

/**
 * 写入文件
 * @param {string} filePath - 文件路径
 * @param {string} content - 文件内容
 * @param {boolean} append - 是否追加模式
 */
function writeFile(filePath, content, append = false) {
    try {
        const dir = path.dirname(filePath);
        if (!fs.existsSync(dir)) {
            fs.mkdirSync(dir, { recursive: true });
        }
        
        if (append) {
            fs.appendFileSync(filePath, content, 'utf-8');
        } else {
            fs.writeFileSync(filePath, content, 'utf-8');
        }
    } catch (error) {
        throw new Error(`写入文件失败: ${error.message}`);
    }
}

/**
 * 获取文件信息
 * @param {string} filePath - 文件路径
 * @returns {object} 文件信息
 */
function getFileInfo(filePath) {
    try {
        const stats = fs.statSync(filePath);
        return {
            exists: true,
            size: stats.size,
            created: stats.birthtime,
            modified: stats.mtime,
            isFile: stats.isFile(),
            isDirectory: stats.isDirectory()
        };
    } catch (error) {
        return {
            exists: false,
            error: error.message
        };
    }
}

/**
 * 列出目录内容
 * @param {string} dirPath - 目录路径
 * @returns {array} 文件列表
 */
function listDirectory(dirPath) {
    try {
        const items = fs.readdirSync(dirPath);
        return items.map(item => {
            const itemPath = path.join(dirPath, item);
            const info = getFileInfo(itemPath);
            return {
                name: item,
                path: itemPath,
                ...info
            };
        });
    } catch (error) {
        throw new Error(`读取目录失败: ${error.message}`);
    }
}

/**
 * 搜索文件
 * @param {string} dirPath - 搜索目录
 * @param {string} pattern - 文件名模式（支持通配符）
 * @returns {array} 匹配的文件列表
 */
function searchFiles(dirPath, pattern) {
    const results = [];
    const regex = new RegExp(pattern.replace(/\*/g, '.*'));
    
    function searchRecursive(currentPath) {
        try {
            const items = fs.readdirSync(currentPath);
            
            for (const item of items) {
                const itemPath = path.join(currentPath, item);
                const info = getFileInfo(itemPath);
                
                if (info.isDirectory) {
                    searchRecursive(itemPath);
                } else if (regex.test(item)) {
                    results.push({
                        name: item,
                        path: itemPath,
                        size: info.size
                    });
                }
            }
        } catch (error) {
            // 忽略权限错误等
        }
    }
    
    searchRecursive(dirPath);
    return results;
}

// 命令行接口
if (require.main === module) {
    const args = process.argv.slice(2);
    
    if (args.length < 2) {
        console.error('用法: node file_utils.js <command> <path> [options]');
        console.error('命令: read, write, info, list, search');
        process.exit(1);
    }
    
    const command = args[0];
    const filePath = args[1];
    
    try {
        switch (command) {
            case 'read':
                const content = readFile(filePath);
                console.log(content);
                break;
            
            case 'write':
                const writeContent = args[2] || '';
                writeFile(filePath, writeContent);
                console.log('文件写入成功');
                break;
            
            case 'info':
                const info = getFileInfo(filePath);
                console.log(JSON.stringify(info, null, 2));
                break;
            
            case 'list':
                const items = listDirectory(filePath);
                console.log(JSON.stringify(items, null, 2));
                break;
            
            case 'search':
                const pattern = args[2] || '*';
                const files = searchFiles(filePath, pattern);
                console.log(JSON.stringify(files, null, 2));
                break;
            
            default:
                console.error(`未知命令: ${command}`);
                process.exit(1);
        }
    } catch (error) {
        console.error('错误:', error.message);
        process.exit(1);
    }
}

module.exports = {
    readFile,
    writeFile,
    getFileInfo,
    listDirectory,
    searchFiles
};


